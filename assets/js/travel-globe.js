(() => {
  const roots = document.querySelectorAll('[data-travel-globe-root]');

  if (!roots.length) {
    return;
  }

  const toNumber = (value) => Number.parseFloat(value) || 0;
  const normalizeName = (value) => String(value || '').trim().toLowerCase();
  const clamp = (value, min, max) => Math.min(max, Math.max(min, value));

  roots.forEach((root) => {
    const canvas = root.querySelector('[data-travel-globe-canvas]');
    const dataNode = root.querySelector('[data-travel-globe-data]');
    const sourceNode = root.querySelector('[data-travel-boundary-sources]');
    const tooltip = root.querySelector('[data-travel-globe-tooltip]');
    const statusNode = root.querySelector('[data-travel-boundary-status]');

    if (!canvas || !dataNode || !sourceNode || !tooltip) {
      return;
    }

    let places = [];
    let sources = [];

    try {
      places = JSON.parse(dataNode.textContent || '[]')
        .map((place, index) => ({
          ...place,
          id: `${normalizeName(place.group)}-${normalizeName(place.name)}-${index}`,
          lat: toNumber(place.lat),
          lon: toNumber(place.lon),
          label: place.label || place.name,
          visited: place.visited === true
        }))
        .filter((place) => place.visited && Number.isFinite(place.lat) && Number.isFinite(place.lon));
      sources = JSON.parse(sourceNode.textContent || '[]');
    } catch (error) {
      console.warn('[travel-globe] invalid JSON data', error);
      return;
    }

    const ctx = canvas.getContext('2d');
    const media = window.matchMedia('(prefers-reduced-motion: reduce)');
    const state = {
      width: 0,
      height: 0,
      dpr: 1,
      radius: 0,
      cx: 0,
      cy: 0,
      centerLon: 105,
      centerLat: 24,
      lastTime: 0,
      pointerInside: false,
      dragging: false,
      dragStartX: 0,
      dragStartY: 0,
      dragStartLon: 0,
      dragStartLat: 0,
      highlightedBoundaryName: null,
      highlightedPlaceId: null,
      boundaries: [],
      projectedBoundaries: [],
      projectedPlaces: []
    };

    const getVar = (name, fallback) => {
      const value = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
      return value || fallback;
    };

    const colors = () => ({
      text: getVar('--heading-color', '#d8dee9'),
      muted: getVar('--text-muted-color', '#8f9baa'),
      border: getVar('--main-border-color', 'rgba(255,255,255,.14)'),
      accent: getVar('--link-color', '#58a6ff')
    });

    const resize = () => {
      const rect = canvas.getBoundingClientRect();
      state.dpr = Math.min(window.devicePixelRatio || 1, 2);
      state.width = Math.max(1, rect.width);
      state.height = Math.max(1, rect.height);
      canvas.width = Math.round(state.width * state.dpr);
      canvas.height = Math.round(state.height * state.dpr);
      ctx.setTransform(state.dpr, 0, 0, state.dpr, 0, 0);
      state.radius = Math.max(130, Math.min(state.width, state.height) * 0.47);
      state.cx = state.width * 0.5;
      state.cy = state.height * 0.5;
    };

    const project = (lat, lon) => {
      const phi = (lat * Math.PI) / 180;
      const lambda = ((lon - state.centerLon) * Math.PI) / 180;
      const pitch = (state.centerLat * Math.PI) / 180;
      const cosPhi = Math.cos(phi);
      const x = cosPhi * Math.sin(lambda);
      const y = Math.sin(phi);
      const z = cosPhi * Math.cos(lambda);
      const y2 = y * Math.cos(pitch) - z * Math.sin(pitch);
      const z2 = y * Math.sin(pitch) + z * Math.cos(pitch);

      return {
        x: state.cx + x * state.radius,
        y: state.cy - y2 * state.radius,
        z: z2,
        visible: z2 > -0.04
      };
    };

    const drawSegmentedLine = (points, color, alpha, width) => {
      ctx.save();
      ctx.strokeStyle = color;
      ctx.globalAlpha = alpha;
      ctx.lineWidth = width;
      ctx.lineJoin = 'round';
      ctx.lineCap = 'round';
      ctx.beginPath();

      let drawing = false;

      points.forEach((point) => {
        if (!point.visible) {
          drawing = false;
          return;
        }

        if (!drawing) {
          ctx.moveTo(point.x, point.y);
          drawing = true;
          return;
        }

        ctx.lineTo(point.x, point.y);
      });

      ctx.stroke();
      ctx.restore();
    };

    const drawGrid = (palette) => {
      for (let lat = -60; lat <= 60; lat += 30) {
        const points = [];

        for (let lon = -180; lon <= 180; lon += 4) {
          points.push(project(lat, lon));
        }

        drawSegmentedLine(points, palette.border, lat === 0 ? 0.24 : 0.12, lat === 0 ? 1 : 0.75);
      }

      for (let lon = -180; lon < 180; lon += 30) {
        const points = [];

        for (let lat = -84; lat <= 84; lat += 4) {
          points.push(project(lat, lon));
        }

        drawSegmentedLine(points, palette.border, 0.11, 0.75);
      }
    };

    const coordinatesToRings = (geometry) => {
      if (!geometry) {
        return [];
      }

      if (geometry.type === 'Polygon') {
        return geometry.coordinates;
      }

      if (geometry.type === 'MultiPolygon') {
        return geometry.coordinates.flat();
      }

      if (geometry.type === 'LineString') {
        return [geometry.coordinates];
      }

      if (geometry.type === 'MultiLineString') {
        return geometry.coordinates;
      }

      return [];
    };

    const shouldUseFeature = (feature, source) => {
      const properties = feature.properties || {};
      const codeProperty = source.code_property;
      const includeCodes = Array.isArray(source.include_codes) ? source.include_codes.map(String) : [];
      const excludeCodes = Array.isArray(source.exclude_codes) ? source.exclude_codes.map(String) : [];
      const code = codeProperty ? String(properties[codeProperty] || '') : '';

      if (codeProperty && excludeCodes.includes(code)) {
        return false;
      }

      if (!codeProperty || !includeCodes.length) {
        return true;
      }

      return includeCodes.includes(code);
    };

    const normalizeFeature = (feature, source) => {
      const properties = feature.properties || {};
      const code = source.code_property ? String(properties[source.code_property] || '') : '';
      const overrides = source.name_overrides || {};
      const name =
        overrides[code] ||
        properties[source.name_property] ||
        properties.NAME ||
        properties.name ||
        properties.NL_NAME_1 ||
        properties.CNTR_NAME ||
        properties.GEOID ||
        source.name;

      return {
        id: `${source.id}-${properties.GEOID || properties.STUSAB || code || normalizeName(name)}`,
        name,
        normalizedName: normalizeName(name),
        region: source.region || source.name,
        sourceName: source.source_name || source.name,
        sourceUrl: source.source_url || '',
        official: source.official === true,
        rings: coordinatesToRings(feature.geometry).map((ring) =>
          ring
            .map(([lon, lat]) => [toNumber(lon), toNumber(lat)])
            .filter(([lon, lat]) => Number.isFinite(lon) && Number.isFinite(lat))
        )
      };
    };

    const loadBoundarySources = async () => {
      const enabledSources = sources.filter((source) => source.enabled && source.data_url);
      const loaded = [];
      const loadedSummaries = [];

      if (statusNode) {
        statusNode.textContent = enabledSources.length
          ? `边界层加载中：${enabledSources.map((source) => source.name).join(' / ')}`
          : '暂无启用边界层';
      }

      for (const source of enabledSources) {
        try {
          const response = await fetch(source.data_url, { mode: 'cors' });

          if (!response.ok) {
            throw new Error(`${response.status} ${response.statusText}`);
          }

          const geojson = await response.json();
          const features = Array.isArray(geojson.features) ? geojson.features : [];
          const sourceBoundaries = features
            .filter((feature) => shouldUseFeature(feature, source))
            .map((feature) => normalizeFeature(feature, source))
            .filter((boundary) => boundary.rings.some((ring) => ring.length > 1));

          loaded.push(...sourceBoundaries);
          loadedSummaries.push(`${source.region || source.name}: ${sourceBoundaries.length}`);
        } catch (error) {
          console.warn(`[travel-globe] boundary source failed: ${source.name}`, error);
        }
      }

      state.boundaries = loaded;

      if (statusNode) {
        statusNode.textContent = state.boundaries.length
          ? `${state.boundaries.length} 条国界轮廓已接入（${loadedSummaries.join(' / ')}）；点位 ${places.length}`
          : '边界层未加载成功';
      }
    };

    const projectBoundary = (boundary) => ({
      boundary,
      rings: boundary.rings.map((ring) =>
        ring.map(([lon, lat], index) => {
          const previous = index > 0 ? ring[index - 1] : null;
          const split = previous ? Math.abs(lon - previous[0]) > 120 : false;
          return { ...project(lat, lon), lon, lat, split };
        })
      )
    });

    const projectPlaces = () =>
      places.map((place) => ({
        ...place,
        ...project(place.lat, place.lon)
      }));

    const drawBoundary = (projected, palette) => {
      const { boundary, rings } = projected;
      const isHighlighted = boundary.normalizedName === state.highlightedBoundaryName;
      const alpha = isHighlighted ? 0.82 : 0.36;
      const width = isHighlighted ? 1.8 : 0.85;

      rings.forEach((ring) => {
        const segments = [];
        let current = [];

        ring.forEach((point) => {
          if (point.split) {
            if (current.length > 1) {
              segments.push(current);
            }
            current = [];
          }
          current.push(point);
        });

        if (current.length > 1) {
          segments.push(current);
        }

        segments.forEach((segment) => drawSegmentedLine(segment, palette.muted, alpha, width));
      });
    };

    const drawPlace = (place, palette) => {
      if (!place.visible) {
        return;
      }

      const active = place.id === state.highlightedPlaceId;
      const size = active ? 3.2 : 2.15;

      ctx.save();
      const glow = ctx.createRadialGradient(place.x, place.y, 0, place.x, place.y, active ? 9 : 6);
      glow.addColorStop(0, 'rgba(88, 166, 255, 0.78)');
      glow.addColorStop(0.42, 'rgba(88, 166, 255, 0.24)');
      glow.addColorStop(1, 'rgba(88, 166, 255, 0)');
      ctx.fillStyle = glow;
      ctx.fillRect(place.x - 9, place.y - 9, 18, 18);

      ctx.beginPath();
      ctx.arc(place.x, place.y, size, 0, Math.PI * 2);
      ctx.fillStyle = palette.accent;
      ctx.globalAlpha = active ? 0.98 : 0.76;
      ctx.fill();
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.78)';
      ctx.globalAlpha = active ? 0.84 : 0.38;
      ctx.lineWidth = 0.75;
      ctx.stroke();
      ctx.restore();
    };

    const draw = (time = 0) => {
      const palette = colors();

      if (!state.pointerInside && !state.dragging && !media.matches && state.lastTime) {
        state.centerLon = (state.centerLon + (time - state.lastTime) * 0.0045) % 360;
      }

      state.lastTime = time;
      ctx.clearRect(0, 0, state.width, state.height);

      const glow = ctx.createRadialGradient(state.cx, state.cy, state.radius * 0.12, state.cx, state.cy, state.radius * 1.12);
      glow.addColorStop(0, 'rgba(88, 166, 255, 0.13)');
      glow.addColorStop(0.56, 'rgba(88, 166, 255, 0.038)');
      glow.addColorStop(1, 'rgba(88, 166, 255, 0)');
      ctx.fillStyle = glow;
      ctx.fillRect(0, 0, state.width, state.height);

      ctx.save();
      ctx.beginPath();
      ctx.arc(state.cx, state.cy, state.radius, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(255, 255, 255, 0.022)';
      ctx.fill();
      ctx.strokeStyle = palette.border;
      ctx.globalAlpha = 0.78;
      ctx.lineWidth = 1;
      ctx.stroke();
      ctx.restore();

      drawGrid(palette);

      state.projectedBoundaries = state.boundaries.map(projectBoundary);
      state.projectedPlaces = projectPlaces();
      state.projectedBoundaries.forEach((projected) => drawBoundary(projected, palette));
      state.projectedPlaces.forEach((place) => drawPlace(place, palette));

      requestAnimationFrame(draw);
    };

    const setTooltip = (item, clientX, clientY) => {
      if (!item) {
        tooltip.hidden = true;
        return;
      }

      const rect = root.getBoundingClientRect();
      const x = Math.min(rect.width - 210, Math.max(12, clientX - rect.left + 14));
      const y = Math.min(rect.height - 104, Math.max(12, clientY - rect.top + 14));

      tooltip.style.setProperty('--travel-tooltip-x', `${x}px`);
      tooltip.style.setProperty('--travel-tooltip-y', `${y}px`);
      tooltip.querySelector('[data-travel-tooltip-name]').textContent = item.title;
      tooltip.querySelector('[data-travel-tooltip-region]').textContent = item.region;
      tooltip.querySelector('[data-travel-tooltip-status]').textContent = item.status;
      tooltip.querySelector('[data-travel-tooltip-coords]').textContent = item.meta;
      tooltip.hidden = false;
    };

    const highlight = ({ boundaryName = null, placeId = null } = {}) => {
      state.highlightedBoundaryName = boundaryName;
      state.highlightedPlaceId = placeId;
    };

    const nearestPlace = (event) => {
      const rect = canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      let nearest = null;

      state.projectedPlaces.forEach((place) => {
        if (!place.visible) {
          return;
        }

        const dx = place.x - x;
        const dy = place.y - y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance <= 9 && (!nearest || distance < nearest.distance)) {
          nearest = { place, distance };
        }
      });

      return nearest;
    };

    const nearestBoundary = (event) => {
      const rect = canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      let nearest = null;

      state.projectedBoundaries.forEach(({ boundary, rings }) => {
        rings.forEach((ring) => {
          ring.forEach((point) => {
            if (!point.visible) {
              return;
            }

            const dx = point.x - x;
            const dy = point.y - y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance <= 7 && (!nearest || distance < nearest.distance)) {
              nearest = { boundary, distance };
            }
          });
        });
      });

      return nearest;
    };

    canvas.addEventListener('pointerdown', (event) => {
      state.pointerInside = true;
      state.dragging = true;
      state.dragStartX = event.clientX;
      state.dragStartY = event.clientY;
      state.dragStartLon = state.centerLon;
      state.dragStartLat = state.centerLat;
      canvas.classList.add('is-dragging');
      canvas.setPointerCapture?.(event.pointerId);
      tooltip.hidden = true;
      event.preventDefault();
    });

    canvas.addEventListener('pointermove', (event) => {
      if (!state.dragging) {
        return;
      }

      const dx = event.clientX - state.dragStartX;
      const dy = event.clientY - state.dragStartY;
      state.centerLon = state.dragStartLon - dx * 0.34;
      state.centerLat = clamp(state.dragStartLat + dy * 0.24, -68, 68);
      highlight();
      tooltip.hidden = true;
    });

    const stopDragging = (event) => {
      if (!state.dragging) {
        return;
      }

      state.dragging = false;
      canvas.classList.remove('is-dragging');
      canvas.releasePointerCapture?.(event.pointerId);
    };

    canvas.addEventListener('pointerup', stopDragging);
    canvas.addEventListener('pointercancel', stopDragging);

    canvas.addEventListener('mousemove', (event) => {
      if (state.dragging) {
        return;
      }

      state.pointerInside = true;
      const point = nearestPlace(event);

      if (point) {
        highlight({ placeId: point.place.id });
        setTooltip(
          {
            title: point.place.label,
            region: `${point.place.group} / ${point.place.name}`,
            status: '已去过',
            meta: `${point.place.lat.toFixed(4)}, ${point.place.lon.toFixed(4)}`
          },
          event.clientX,
          event.clientY
        );
        return;
      }

      const nearest = nearestBoundary(event);

      if (!nearest) {
        highlight();
        tooltip.hidden = true;
        return;
      }

      highlight({ boundaryName: nearest.boundary.normalizedName });
      setTooltip(
        {
          title: nearest.boundary.name,
          region: nearest.boundary.region,
          status: nearest.boundary.official ? '边界层 / 已标注来源' : '边界层',
          meta: nearest.boundary.sourceName
        },
        event.clientX,
        event.clientY
      );
    });

    canvas.addEventListener('mouseleave', () => {
      state.pointerInside = false;
      state.dragging = false;
      canvas.classList.remove('is-dragging');
      highlight();
      tooltip.hidden = true;
    });

    new ResizeObserver(() => {
      resize();
    }).observe(canvas);

    resize();
    loadBoundarySources();
    requestAnimationFrame(draw);
  });
})();
