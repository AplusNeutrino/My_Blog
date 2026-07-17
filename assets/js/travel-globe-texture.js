((scope) => {
  'use strict';

  const AREA_TYPES = new Set(['Polygon', 'MultiPolygon']);
  const LINE_TYPES = new Set(['LineString', 'MultiLineString']);
  const DISPLAY_SUPERSAMPLE = 1.5;
  const HAINAN_CODE = '460000';
  const featureCollection = (features) => ({ type: 'FeatureCollection', features });
  const isAreaFeature = (feature) => AREA_TYPES.has(feature?.geometry?.type);
  const isLineFeature = (feature) => LINE_TYPES.has(feature?.geometry?.type);

  const isSouthChinaSeaBoundary = (d3, feature) => {
    if (!isLineFeature(feature)) {
      return false;
    }

    const [[west, south], [east, north]] = d3.geoBounds(feature);
    return west > 100 && east < 130 && south < 10 && north < 26 && east - west > 8;
  };

  const featureCode = (feature, source) => {
    const property = source.code_property;
    return property ? String(feature?.properties?.[property] ?? '') : '';
  };

  const sourceFeatures = (layer) => {
    const features = Array.isArray(layer?.geojson?.features) ? layer.geojson.features : [];
    const source = layer.source || {};
    const included = new Set((source.include_codes || []).map(String));
    const excluded = new Set((source.exclude_codes || []).map(String));

    return features.filter((feature) => {
      const code = featureCode(feature, source);
      if (code && excluded.has(code)) {
        return false;
      }
      return !included.size || included.has(code);
    });
  };

  const visualAreaFeature = (d3, feature, source) => {
    if (featureCode(feature, source) !== HAINAN_CODE || feature?.geometry?.type !== 'MultiPolygon') {
      return feature;
    }

    let mainIsland = null;
    let mainIslandArea = -Infinity;
    feature.geometry.coordinates.forEach((polygon) => {
      const polygonArea = d3.geoArea({ type: 'Polygon', coordinates: polygon });
      if (polygonArea > mainIslandArea) {
        mainIsland = polygon;
        mainIslandArea = polygonArea;
      }
    });

    return {
      ...feature,
      geometry: {
        type: 'Polygon',
        coordinates: mainIsland
      }
    };
  };

  const samePoint = (left, right) =>
    Array.isArray(left) &&
    Array.isArray(right) &&
    left[0] === right[0] &&
    left[1] === right[1];

  const stitchLineSegments = (segments) => {
    const paths = [];
    let activePath = [];

    segments.forEach((segment) => {
      if (!Array.isArray(segment) || segment.length < 2) {
        return;
      }
      if (!activePath.length) {
        activePath = segment.slice();
        return;
      }

      const activeEnd = activePath[activePath.length - 1];
      if (samePoint(activeEnd, segment[0])) {
        activePath.push(...segment.slice(1));
        return;
      }
      if (samePoint(activeEnd, segment[segment.length - 1])) {
        activePath.push(...segment.slice(0, -1).reverse());
        return;
      }

      paths.push(activePath);
      activePath = segment.slice();
    });

    if (activePath.length) {
      paths.push(activePath);
    }
    return paths;
  };

  const visualNationalOutlineFeature = (feature) => {
    if (feature?.geometry?.type !== 'MultiLineString') {
      return feature;
    }

    const visibleSegments = feature.geometry.coordinates.filter((line) => {
      let west = Infinity;
      let south = Infinity;
      let east = -Infinity;
      let north = -Infinity;
      line.forEach(([longitude, latitude]) => {
        west = Math.min(west, longitude);
        south = Math.min(south, latitude);
        east = Math.max(east, longitude);
        north = Math.max(north, latitude);
      });
      const isHainanMainIsland = west >= 108.4 && east <= 111.2 && south >= 18 && north <= 20.3;
      return north >= 20.18 || isHainanMainIsland;
    });
    const coordinates = stitchLineSegments(visibleSegments);

    return {
      ...feature,
      geometry: {
        type: 'MultiLineString',
        coordinates
      }
    };
  };

  const createProjection = (d3, mode, width, height) => {
    if (mode === 'orthographic') {
      return d3
        .geoOrthographic()
        .rotate([-105, -24, 0])
        .translate([width / 2, height / 2])
        .scale(Math.min(width, height) * 0.43)
        .clipAngle(90)
        .precision(0.3);
    }

    return d3
      .geoEquirectangular()
      .translate([width / 2, height / 2])
      .scale(width / (2 * Math.PI))
      .clipExtent([
        [0, 0],
        [width, height]
      ])
      .precision(0.2);
  };

  const createCanvas = (factory, width, height) => {
    const canvas = factory(width, height);
    canvas.width = width;
    canvas.height = height;
    return canvas;
  };

  const pathFill = (context, path, features, fillStyle) => {
    if (!features.length) {
      return;
    }
    context.beginPath();
    path(featureCollection(features));
    context.fillStyle = fillStyle;
    context.fill('evenodd');
  };

  const pathStroke = (context, path, features, strokeStyle, lineWidth, lineDash = []) => {
    if (!features.length) {
      return;
    }
    context.beginPath();
    path(featureCollection(features));
    context.strokeStyle = strokeStyle;
    context.lineWidth = lineWidth;
    context.lineJoin = 'round';
    context.lineCap = 'round';
    context.setLineDash(lineDash);
    context.stroke();
    context.setLineDash([]);
  };

  const idColor = (id) => `rgb(${id & 255}, ${(id >> 8) & 255}, ${(id >> 16) & 255})`;

  // Spread pick IDs across all RGB channels so antialiased edge colors cannot mimic another region.
  const pickIdForIndex = (index) => {
    let value = index + 1;
    value = Math.imul(value ^ (value >>> 16), 0x7feb352d);
    value = Math.imul(value ^ (value >>> 15), 0x846ca68b);
    value = (value ^ (value >>> 16)) >>> 0;
    return (value & 0xffffff) || 0x010101;
  };

  const render = ({ d3, layers, regions, palette, width, height, mode = 'equirectangular', canvasFactory }) => {
    if (!d3 || typeof d3.geoPath !== 'function') {
      throw new Error('D3 geographic renderer is unavailable');
    }

    const colors = palette || {};
    const safeWidth = Math.max(320, Math.round(width));
    const safeHeight = Math.max(180, Math.round(height));
    const displayWidth = Math.round(safeWidth * DISPLAY_SUPERSAMPLE);
    const displayHeight = Math.round(safeHeight * DISPLAY_SUPERSAMPLE);
    const displayCanvas = createCanvas(canvasFactory, safeWidth, safeHeight);
    const renderCanvas = createCanvas(canvasFactory, displayWidth, displayHeight);
    const pickCanvas = createCanvas(canvasFactory, safeWidth, safeHeight);
    const display = renderCanvas.getContext('2d', { alpha: false });
    const output = displayCanvas.getContext('2d', { alpha: false });
    const pick = pickCanvas.getContext('2d', { willReadFrequently: true });
    const displayProjection = createProjection(d3, mode, displayWidth, displayHeight);
    const pickProjection = createProjection(d3, mode, safeWidth, safeHeight);
    const displayPath = d3.geoPath(displayProjection, display);
    const pickPath = d3.geoPath(pickProjection, pick);
    const resolution = Math.max(0.55, safeWidth / 2048);
    const requestedLineScale = Number.parseFloat(colors.lineScale);
    const lineScale = Number.isFinite(requestedLineScale)
      ? Math.min(2, Math.max(0.75, requestedLineScale))
      : 1;
    const strokeWidth = (preferred, minimum) =>
      Math.max(minimum, preferred * resolution) * DISPLAY_SUPERSAMPLE * lineScale;
    const normalizedLayers = (layers || []).map((layer) => ({
      ...layer,
      features: sourceFeatures(layer)
    }));
    const areaLayers = normalizedLayers.filter((layer) => layer.source?.boundary_kind !== 'national-outline');
    const regionLookup = new Map((regions || []).map((region) => [`${region.source}:${String(region.code)}`, region]));
    const visitedFeatures = [];

    display.fillStyle = colors.base;
    display.fillRect(0, 0, displayWidth, displayHeight);
    pick.fillStyle = '#000000';
    pick.fillRect(0, 0, safeWidth, safeHeight);

    if (mode === 'orthographic') {
      display.beginPath();
      displayPath({ type: 'Sphere' });
      display.fillStyle = colors.base;
      display.fill();
    }

    display.beginPath();
    displayPath(d3.geoGraticule10());
    display.strokeStyle = colors.grid;
    display.lineWidth = strokeWidth(0.65, 0.45);
    display.stroke();

    areaLayers.forEach((layer) => {
      const areas = layer.features
        .filter(isAreaFeature)
        .map((feature) => visualAreaFeature(d3, feature, layer.source));
      pathFill(display, displayPath, areas, colors.land);

      areas.forEach((feature) => {
        const code = featureCode(feature, layer.source);
        const region = regionLookup.get(`${layer.source.id}:${code}`);
        if (!region || region.visited !== true) {
          return;
        }
        visitedFeatures.push({ feature, source: layer.source, region, code });
        pathFill(display, displayPath, [feature], colors.visitedFill);
      });
    });

    normalizedLayers.forEach((layer) => {
      const kind = layer.source?.boundary_kind;
      if (kind === 'country') {
        pathStroke(display, displayPath, layer.features, colors.worldBorder, strokeWidth(0.65, 0.45));
      } else if (kind === 'province') {
        const provinceFeatures = layer.features
          .filter((feature) => !isSouthChinaSeaBoundary(d3, feature))
          .map((feature) => (isAreaFeature(feature) ? visualAreaFeature(d3, feature, layer.source) : feature));
        pathStroke(display, displayPath, provinceFeatures, colors.provinceBorder, strokeWidth(0.8, 0.55));
      }
    });

    const maritimeBoundaryFeatures = normalizedLayers
      .filter((layer) => layer.source?.boundary_kind === 'province')
      .flatMap((layer) => layer.features.filter((feature) => isSouthChinaSeaBoundary(d3, feature)));
    pathStroke(
      display,
      displayPath,
      maritimeBoundaryFeatures,
      colors.maritimeBorder,
      strokeWidth(2.1, 1.35),
      [7 * DISPLAY_SUPERSAMPLE, 5 * DISPLAY_SUPERSAMPLE]
    );

    normalizedLayers
      .filter((layer) => layer.source?.boundary_kind === 'national-outline')
      .forEach((layer) => {
        const nationalFeatures = layer.features.map(visualNationalOutlineFeature);
        pathStroke(display, displayPath, nationalFeatures, colors.nationalBorder, strokeWidth(1.55, 1));
      });

    if (mode === 'orthographic') {
      display.beginPath();
      displayPath({ type: 'Sphere' });
      display.strokeStyle = colors.sphereBorder;
      display.lineWidth = strokeWidth(1.1, 0.8);
      display.stroke();
    }

    const manifest = visitedFeatures.map(({ feature, source, region, code }, index) => {
      const id = pickIdForIndex(index);
      pathFill(pick, pickPath, [feature], idColor(id));
      return {
        id,
        source: source.id,
        code,
        label: region.label,
        group: region.group,
        status: '已到访',
        visitedOn: Array.isArray(region.visitedOn) ? region.visitedOn : [],
        places: Array.isArray(region.places) ? region.places : [],
        note: region.note || ''
      };
    });
    output.imageSmoothingEnabled = true;
    output.imageSmoothingQuality = 'medium';
    output.drawImage(renderCanvas, 0, 0, safeWidth, safeHeight);

    return { displayCanvas, pickCanvas, manifest };
  };

  scope.TravelGlobeTexture = { render };
})(globalThis);
