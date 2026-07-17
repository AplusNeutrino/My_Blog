import * as THREE from './third-party/travel-globe/three.module.min.js';

const roots = document.querySelectorAll('[data-travel-globe-root]');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const REST_ROTATION_X = THREE.MathUtils.degToRad(-24);
const ORIENTATION_IDLE_DELAY = 2000;
const ORIENTATION_RESET_DURATION = 520;
const clamp = (value, min, max) => Math.min(max, Math.max(min, value));
const normalizeTextArray = (value) =>
  (Array.isArray(value) ? value : [])
    .map((item) => String(item || '').trim())
    .filter(Boolean);

const parseJsonNode = (node, fallback = []) => {
  try {
    return JSON.parse(node?.textContent || JSON.stringify(fallback));
  } catch (error) {
    console.warn('[travel-globe] invalid embedded JSON', error);
    return fallback;
  }
};

const fetchWithTimeout = async (source) => {
  const controller = new AbortController();
  const timer = window.setTimeout(() => controller.abort(), 12000);

  try {
    const response = await fetch(source.data_url, {
      cache: 'default',
      credentials: 'same-origin',
      signal: controller.signal
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const geojson = await response.json();
    if (!geojson || !Array.isArray(geojson.features)) {
      throw new Error('无效 GeoJSON');
    }
    return { source, geojson };
  } finally {
    window.clearTimeout(timer);
  }
};

roots.forEach((root) => {
  let canvas = root.querySelector('[data-travel-globe-canvas]');
  const shell = root.querySelector('.travel-globe-shell');
  const regionNode = root.querySelector('[data-travel-region-data]');
  const sourceNode = root.querySelector('[data-travel-boundary-sources]');
  const dossier = root.querySelector('[data-travel-globe-dossier]');
  const status = root.querySelector('[data-travel-boundary-status]');
  const statusMessage = root.querySelector('[data-travel-boundary-message]');
  const retryButton = root.querySelector('[data-travel-boundary-retry]');
  const dossierMode = root.querySelector('[data-travel-tooltip-mode]');
  const dossierName = root.querySelector('[data-travel-tooltip-name]');
  const dossierRegion = root.querySelector('[data-travel-tooltip-region]');
  const dossierStatus = root.querySelector('[data-travel-tooltip-status]');
  const dossierDatesRow = root.querySelector('[data-travel-tooltip-dates-row]');
  const dossierDates = root.querySelector('[data-travel-tooltip-dates]');
  const dossierPlacesRow = root.querySelector('[data-travel-tooltip-places-row]');
  const dossierPlaces = root.querySelector('[data-travel-tooltip-places]');
  const dossierFields = root.querySelector('[data-travel-dossier-fields]');
  const dossierNote = root.querySelector('[data-travel-tooltip-note]');

  if (
    !canvas ||
    !shell ||
    !dossier ||
    !status ||
    !statusMessage ||
    !retryButton ||
    !dossierMode ||
    !dossierName ||
    !dossierRegion ||
    !dossierStatus ||
    !dossierDatesRow ||
    !dossierDates ||
    !dossierPlacesRow ||
    !dossierPlaces ||
    !dossierFields ||
    !dossierNote ||
    !regionNode ||
    !sourceNode
  ) {
    return;
  }

  const regions = parseJsonNode(regionNode).map((region) => ({
    ...region,
    code: String(region.code || ''),
    visited: region.visited === true,
    visitedOn: normalizeTextArray(region.visited_on),
    places: normalizeTextArray(region.places),
    note: String(region.note || '').trim()
  }));
  const sources = parseJsonNode(sourceNode)
    .filter((source) => source.enabled === true && source.data_url)
    .map((source) => ({
      ...source,
      data_url: new URL(source.data_url, document.baseURI).href
    }));
  const moduleUrl = new URL(import.meta.url);
  const versionedAssetUrl = (path) => {
    const url = new URL(path, moduleUrl);
    url.search = moduleUrl.search;
    return url;
  };
  const d3Url = versionedAssetUrl('./third-party/travel-globe/d3.min.js').href;
  const textureHelperUrl = versionedAssetUrl('./travel-globe-texture.js').href;
  const workerUrl = versionedAssetUrl('./travel-globe-worker.js');
  let textureCanvas = document.createElement('canvas');
  let pickCanvas = document.createElement('canvas');
  let pickContext = pickCanvas.getContext('2d', { willReadFrequently: true });
  const pickManifest = new Map();
  const raycaster = new THREE.Raycaster();
  const pointer = new THREE.Vector2();
  const globeCenter = new THREE.Vector3();
  const cameraPosition = new THREE.Vector3();
  const surfaceNormal = new THREE.Vector3();
  const surfaceToCamera = new THREE.Vector3();

  let worker = null;
  let renderer = null;
  let scene = null;
  let camera = null;
  let globe = null;
  let globeMaterial = null;
  let mapTexture = null;
  let pickTexture = null;
  let highlightUniforms = null;
  let fallbackContext = null;
  let fallbackMode = false;
  let initialized = false;
  let viewportVisible = false;
  let pointerInside = false;
  let pointerDown = false;
  let dragging = false;
  let dragStartX = 0;
  let dragStartY = 0;
  let startRotationX = 0;
  let startRotationY = 0;
  let lastFrame = 0;
  let hoverFrame = 0;
  let statusTimer = 0;
  let mainThreadLayers = [];
  let textureSizeKey = '';
  let hoveredRegion = null;
  let pinnedRegion = null;
  let activeRegion = null;
  let loopRunning = false;
  let interactionAnimating = false;
  let interactionStartedAt = 0;
  let interactionScaleFrom = 1;
  let interactionScaleTo = 1;
  let interactionStrengthFrom = 0;
  let interactionStrengthTo = 0;
  let interactionScale = 1;
  let interactionStrength = 0;
  let orientationTimer = 0;
  let orientationAnimating = false;
  let orientationStartedAt = 0;
  let orientationFromX = REST_ROTATION_X;

  const palette = () => {
    const styles = getComputedStyle(root);
    const read = (name) => styles.getPropertyValue(name).trim();
    return {
      viewport: read('--travel-globe-viewport'),
      base: read('--travel-globe-base'),
      visitedFill: read('--travel-globe-fill'),
      land: read('--travel-globe-land'),
      grid: read('--travel-globe-grid'),
      worldBorder: read('--travel-globe-world-border'),
      provinceBorder: read('--travel-globe-province-border'),
      maritimeBorder: read('--travel-globe-maritime-border'),
      nationalBorder: read('--travel-globe-national-border'),
      sphereBorder: read('--travel-globe-sphere-border'),
      lineScale: read('--travel-globe-line-scale'),
      hoverFill: read('--travel-globe-hover-fill'),
      hoverBorder: read('--travel-globe-hover-border')
    };
  };

  const textureDimensions = () => {
    const rect = shell.getBoundingClientRect();
    if (fallbackMode) {
      const dpr = Math.min(window.devicePixelRatio || 1, 1.5);
      return {
        width: Math.max(480, Math.round(rect.width * dpr)),
        height: Math.max(300, Math.round(rect.height * dpr)),
        key: `fallback-${Math.round(rect.width)}-${Math.round(rect.height)}`
      };
    }
    const mobile = rect.width < 640;
    return mobile
      ? { width: 1280, height: 640, key: 'webgl-1280' }
      : { width: 2560, height: 1280, key: 'webgl-2560' };
  };

  const setStatus = (message, { retry = false, hideAfter = 0 } = {}) => {
    window.clearTimeout(statusTimer);
    status.hidden = false;
    statusMessage.textContent = message;
    retryButton.hidden = !retry;
    if (hideAfter) {
      statusTimer = window.setTimeout(() => {
        status.hidden = true;
      }, hideAfter);
    }
  };

  const sameRegion = (left, right) => Boolean(left && right && left.id === right.id);

  const hideDossier = () => {
    dossierMode.textContent = 'GEO MEMORY RECORD';
    dossierName.textContent = '未选择记录';
    dossierRegion.textContent = '';
    dossierRegion.hidden = true;
    dossierStatus.textContent = '';
    dossierStatus.hidden = true;
    dossierDatesRow.hidden = true;
    dossierDates.textContent = '';
    dossierPlacesRow.hidden = true;
    dossierPlaces.textContent = '';
    dossierFields.hidden = true;
    dossierNote.hidden = true;
    dossierNote.textContent = '';
    dossier.classList.remove('is-pinned', 'has-details');
    dossier.classList.add('is-empty');
  };

  const showDossier = (region, isPinned) => {
    if (!region) {
      hideDossier();
      return;
    }

    dossierMode.textContent = isPinned ? 'PINNED RECORD' : 'GEO MEMORY RECORD';
    dossierName.textContent = region.label;
    dossierRegion.textContent = region.group;
    dossierRegion.hidden = false;
    dossierStatus.textContent = region.status;
    dossierStatus.hidden = false;

    const dates = normalizeTextArray(region.visitedOn);
    dossierDatesRow.hidden = !dates.length;
    dossierDates.textContent = dates.join(' / ');

    const places = normalizeTextArray(region.places);
    dossierPlacesRow.hidden = !places.length;
    dossierPlaces.textContent = places.join(' · ');
    dossierFields.hidden = !dates.length && !places.length;

    const note = String(region.note || '').trim();
    dossierNote.hidden = !note;
    dossierNote.textContent = note;
    dossier.classList.remove('is-empty');
    dossier.classList.toggle('is-pinned', isPinned);
    dossier.classList.toggle('has-details', Boolean(dates.length || places.length || note));
  };

  const setHighlightId = (region) => {
    if (!highlightUniforms || !region) {
      return;
    }
    highlightUniforms.travelPickId.value.set(
      (region.id & 255) / 255,
      ((region.id >> 8) & 255) / 255,
      ((region.id >> 16) & 255) / 255
    );
  };

  const applyInteractionFrame = (time) => {
    if (interactionAnimating) {
      const progress = clamp((time - interactionStartedAt) / 180, 0, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      interactionScale = THREE.MathUtils.lerp(interactionScaleFrom, interactionScaleTo, eased);
      interactionStrength = THREE.MathUtils.lerp(interactionStrengthFrom, interactionStrengthTo, eased);
      interactionAnimating = progress < 1;
    }

    if (globe) {
      globe.scale.setScalar(fallbackMode || reducedMotion.matches ? 1 : interactionScale);
    }
    if (highlightUniforms) {
      highlightUniforms.travelHoverStrength.value = interactionStrength;
    }
  };

  const setInteractionTarget = (hasActiveRegion) => {
    const targetScale = hasActiveRegion ? 1.018 : 1;
    const targetStrength = hasActiveRegion ? 1 : 0;
    const now = performance.now();
    applyInteractionFrame(now);

    if (reducedMotion.matches || fallbackMode) {
      interactionAnimating = false;
      interactionScale = 1;
      interactionStrength = targetStrength;
      applyInteractionFrame(now);
      return;
    }

    interactionScaleFrom = interactionScale;
    interactionScaleTo = targetScale;
    interactionStrengthFrom = interactionStrength;
    interactionStrengthTo = targetStrength;
    interactionStartedAt = now;
    interactionAnimating =
      Math.abs(interactionScaleFrom - interactionScaleTo) > 0.0001 ||
      Math.abs(interactionStrengthFrom - interactionStrengthTo) > 0.0001;
  };

  const updateActiveRegion = () => {
    const nextRegion = hoveredRegion || pinnedRegion;
    const regionChanged = !sameRegion(activeRegion, nextRegion);
    activeRegion = nextRegion;

    shell.classList.toggle('has-active-region', Boolean(activeRegion));
    shell.classList.toggle('has-pinned-region', Boolean(pinnedRegion));
    canvas.classList.toggle('has-region-hover', Boolean(activeRegion));

    if (activeRegion) {
      setHighlightId(activeRegion);
      showDossier(activeRegion, sameRegion(activeRegion, pinnedRegion));
    } else {
      hideDossier();
    }

    if (regionChanged) {
      setInteractionTarget(Boolean(activeRegion));
    }
    syncAnimationLoop();
  };

  const setHoveredRegion = (region) => {
    if (sameRegion(hoveredRegion, region) || (!hoveredRegion && !region)) {
      return;
    }
    hoveredRegion = region;
    updateActiveRegion();
  };

  const togglePinnedRegion = (region) => {
    pinnedRegion = region && !sameRegion(pinnedRegion, region) ? region : null;
    updateActiveRegion();
  };

  const clearRegions = () => {
    hoveredRegion = null;
    pinnedRegion = null;
    updateActiveRegion();
  };

  const renderOnce = () => {
    if (renderer && scene && camera) {
      renderer.render(scene, camera);
    }
  };

  const cancelOrientationReset = () => {
    window.clearTimeout(orientationTimer);
    orientationTimer = 0;
    orientationAnimating = false;
  };

  const applyOrientationFrame = (time) => {
    if (!orientationAnimating || !globe) {
      return;
    }
    const progress = clamp((time - orientationStartedAt) / ORIENTATION_RESET_DURATION, 0, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    globe.rotation.x = THREE.MathUtils.lerp(orientationFromX, REST_ROTATION_X, eased);
    orientationAnimating = progress < 1;
  };

  const scheduleOrientationReset = () => {
    window.clearTimeout(orientationTimer);
    orientationTimer = window.setTimeout(() => {
      orientationTimer = 0;
      if (!globe || fallbackMode || Math.abs(globe.rotation.x - REST_ROTATION_X) < 0.0001) {
        return;
      }
      if (reducedMotion.matches) {
        globe.rotation.x = REST_ROTATION_X;
        renderOnce();
        return;
      }
      orientationFromX = globe.rotation.x;
      orientationStartedAt = performance.now();
      orientationAnimating = true;
      syncAnimationLoop();
    }, ORIENTATION_IDLE_DELAY);
  };

  const shouldAutoRotate = () =>
    viewportVisible &&
    !document.hidden &&
    !reducedMotion.matches &&
    !pointerDown &&
    !dragging &&
    !activeRegion;

  const animate = (time) => {
    applyInteractionFrame(time);
    applyOrientationFrame(time);
    if (lastFrame && shouldAutoRotate()) {
      globe.rotation.y += ((time - lastFrame) * Math.PI * 2) / 55000;
    }
    lastFrame = time;
    renderOnce();

    if (!shouldAutoRotate() && !interactionAnimating && !orientationAnimating) {
      loopRunning = false;
      lastFrame = 0;
      renderer.setAnimationLoop(null);
    }
  };

  const syncAnimationLoop = () => {
    if (!renderer) {
      return;
    }

    const shouldRun =
      viewportVisible &&
      !document.hidden &&
      (shouldAutoRotate() || interactionAnimating || orientationAnimating);
    if (shouldRun && !loopRunning) {
      loopRunning = true;
      lastFrame = 0;
      renderer.setAnimationLoop(animate);
      return;
    }

    if (!shouldRun && loopRunning) {
      loopRunning = false;
      renderer.setAnimationLoop(null);
    }

    applyInteractionFrame(performance.now());
    applyOrientationFrame(performance.now());
    renderOnce();
  };

  const resizeRenderer = () => {
    const rect = shell.getBoundingClientRect();
    if (renderer && camera) {
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
      renderer.setSize(Math.max(1, rect.width), Math.max(1, rect.height), false);
      camera.aspect = Math.max(1, rect.width) / Math.max(1, rect.height);
      camera.position.z = rect.width < 640 ? 3.32 : 3.12;
      camera.updateProjectionMatrix();
      renderOnce();
    } else if (fallbackContext) {
      const dimensions = textureDimensions();
      canvas.width = dimensions.width;
      canvas.height = dimensions.height;
    }
  };

  const updateRendererPalette = (colors = palette()) => {
    renderer?.setClearColor(colors.viewport, 1);
    if (highlightUniforms) {
      highlightUniforms.travelHoverFill.value.set(colors.hoverFill);
      highlightUniforms.travelHoverBorder.value.set(colors.hoverBorder);
    }
  };

  const createMapTexture = (source) => {
    const texture = new THREE.CanvasTexture(source);
    texture.colorSpace = THREE.SRGBColorSpace;
    texture.minFilter = THREE.LinearFilter;
    texture.magFilter = THREE.LinearFilter;
    texture.generateMipmaps = false;
    if (renderer) {
      texture.anisotropy = Math.min(8, renderer.capabilities.getMaxAnisotropy());
    }
    return texture;
  };

  const createPickTexture = (source) => {
    const texture = new THREE.CanvasTexture(source);
    texture.colorSpace = THREE.NoColorSpace;
    texture.minFilter = THREE.NearestFilter;
    texture.magFilter = THREE.NearestFilter;
    texture.generateMipmaps = false;
    return texture;
  };

  const configureHighlightShader = () => {
    globeMaterial.onBeforeCompile = (shader) => {
      shader.uniforms.travelPickMap = { value: pickTexture };
      shader.uniforms.travelPickId = { value: new THREE.Vector3() };
      shader.uniforms.travelPickTexel = {
        value: new THREE.Vector2(1 / Math.max(1, pickCanvas.width), 1 / Math.max(1, pickCanvas.height))
      };
      shader.uniforms.travelHoverFill = { value: new THREE.Color() };
      shader.uniforms.travelHoverBorder = { value: new THREE.Color() };
      shader.uniforms.travelHoverStrength = { value: interactionStrength };

      shader.fragmentShader = shader.fragmentShader
        .replace(
          '#include <map_pars_fragment>',
          `#include <map_pars_fragment>
uniform sampler2D travelPickMap;
uniform vec3 travelPickId;
uniform vec2 travelPickTexel;
uniform vec3 travelHoverFill;
uniform vec3 travelHoverBorder;
uniform float travelHoverStrength;

float travelRegionMatch(vec3 sampleColor) {
  vec3 delta = abs(sampleColor - travelPickId);
  float largestDelta = max(delta.r, max(delta.g, delta.b));
  return 1.0 - step(0.5 / 255.0, largestDelta);
}`
        )
        .replace(
          '#include <map_fragment>',
          `#include <map_fragment>
if (travelHoverStrength > 0.001) {
  float center = travelRegionMatch(texture2D(travelPickMap, vMapUv).rgb);
  vec2 texel = travelPickTexel;
  float east = travelRegionMatch(texture2D(travelPickMap, vMapUv + vec2(texel.x, 0.0)).rgb);
  float west = travelRegionMatch(texture2D(travelPickMap, vMapUv - vec2(texel.x, 0.0)).rgb);
  float north = travelRegionMatch(texture2D(travelPickMap, vMapUv + vec2(0.0, texel.y)).rgb);
  float south = travelRegionMatch(texture2D(travelPickMap, vMapUv - vec2(0.0, texel.y)).rgb);
  float northEast = travelRegionMatch(texture2D(travelPickMap, vMapUv + texel).rgb);
  float northWest = travelRegionMatch(texture2D(travelPickMap, vMapUv + vec2(-texel.x, texel.y)).rgb);
  float southEast = travelRegionMatch(texture2D(travelPickMap, vMapUv + vec2(texel.x, -texel.y)).rgb);
  float southWest = travelRegionMatch(texture2D(travelPickMap, vMapUv - texel).rgb);
  float eastOuter = travelRegionMatch(texture2D(travelPickMap, vMapUv + vec2(texel.x * 2.0, 0.0)).rgb);
  float westOuter = travelRegionMatch(texture2D(travelPickMap, vMapUv - vec2(texel.x * 2.0, 0.0)).rgb);
  float northOuter = travelRegionMatch(texture2D(travelPickMap, vMapUv + vec2(0.0, texel.y * 2.0)).rgb);
  float southOuter = travelRegionMatch(texture2D(travelPickMap, vMapUv - vec2(0.0, texel.y * 2.0)).rgb);
  float coverage = (
    center * 4.0 +
    east + west + north + south +
    (northEast + northWest + southEast + southWest) * 0.75 +
    (eastOuter + westOuter + northOuter + southOuter) * 0.35
  ) / 12.4;
  if (coverage > 0.01) {
    float fillCoverage = smoothstep(0.34, 0.72, coverage);
    float boundary = smoothstep(0.04, 0.42, coverage) * (1.0 - smoothstep(0.58, 0.96, coverage));
    diffuseColor.rgb = mix(diffuseColor.rgb, travelHoverFill, fillCoverage * 0.13 * travelHoverStrength);
    diffuseColor.rgb = mix(diffuseColor.rgb, travelHoverBorder, boundary * 0.68 * travelHoverStrength);
  }
}`
        );

      highlightUniforms = shader.uniforms;
      updateRendererPalette();
      setHighlightId(activeRegion);
      applyInteractionFrame(performance.now());
    };
    globeMaterial.customProgramCacheKey = () => 'travel-region-highlight-v2';
  };

  const setupRenderer = () => {
    try {
      const colors = palette();
      textureCanvas.width = 1;
      textureCanvas.height = 1;
      const textureContext = textureCanvas.getContext('2d', { alpha: false });
      textureContext.fillStyle = colors.base;
      textureContext.fillRect(0, 0, 1, 1);
      pickCanvas.width = 1;
      pickCanvas.height = 1;
      pickContext.fillStyle = '#000000';
      pickContext.fillRect(0, 0, 1, 1);

      mapTexture = createMapTexture(textureCanvas);
      pickTexture = createPickTexture(pickCanvas);

      renderer = new THREE.WebGLRenderer({
        canvas,
        antialias: true,
        alpha: false,
        powerPreference: 'low-power'
      });
      renderer.setClearColor(colors.viewport, 1);
      renderer.outputColorSpace = THREE.SRGBColorSpace;
      mapTexture.anisotropy = Math.min(8, renderer.capabilities.getMaxAnisotropy());
      mapTexture.needsUpdate = true;
      scene = new THREE.Scene();
      camera = new THREE.PerspectiveCamera(40, 1, 0.1, 20);
      globeMaterial = new THREE.MeshBasicMaterial({
        color: 0xffffff,
        map: mapTexture,
        side: THREE.FrontSide,
        depthTest: true,
        depthWrite: true
      });
      configureHighlightShader();
      globe = new THREE.Mesh(new THREE.SphereGeometry(1, 96, 64), globeMaterial);
      globe.rotation.order = 'YXZ';
      globe.rotation.x = REST_ROTATION_X;
      globe.rotation.y = THREE.MathUtils.degToRad(165);
      scene.add(globe);
      resizeRenderer();
      shell.classList.add('is-render-ready');
      renderOnce();
      return;
    } catch (error) {
      console.warn('[travel-globe] WebGL unavailable, using static canvas fallback', error);
    }

    fallbackMode = true;
    const replacement = canvas.cloneNode(false);
    canvas.replaceWith(replacement);
    canvas = replacement;
    fallbackContext = canvas.getContext('2d', { alpha: false });
    resizeRenderer();
  };

  const updatePickCanvas = (source) => {
    const nextCanvas = document.createElement('canvas');
    nextCanvas.width = source.width;
    nextCanvas.height = source.height;
    const nextContext = nextCanvas.getContext('2d', { willReadFrequently: true });
    nextContext.clearRect(0, 0, nextCanvas.width, nextCanvas.height);
    nextContext.drawImage(source, 0, 0);

    pickCanvas = nextCanvas;
    pickContext = nextContext;

    if (!fallbackMode && pickTexture) {
      const previousTexture = pickTexture;
      pickTexture = createPickTexture(pickCanvas);
      if (highlightUniforms) {
        highlightUniforms.travelPickMap.value = pickTexture;
      }
      previousTexture.dispose();
    }
    if (highlightUniforms && pickCanvas.width && pickCanvas.height) {
      highlightUniforms.travelPickTexel.value.set(1 / pickCanvas.width, 1 / pickCanvas.height);
    }
  };

  const applyRenderedCanvases = (displaySource, pickSource, manifest) => {
    pickManifest.clear();
    (manifest || []).forEach((item) => pickManifest.set(item.id, item));
    updatePickCanvas(pickSource);

    if (fallbackMode) {
      canvas.width = displaySource.width;
      canvas.height = displaySource.height;
      fallbackContext.drawImage(displaySource, 0, 0);
    } else {
      const nextCanvas = document.createElement('canvas');
      nextCanvas.width = displaySource.width;
      nextCanvas.height = displaySource.height;
      const context = nextCanvas.getContext('2d', { alpha: false });
      context.drawImage(displaySource, 0, 0);

      const previousTexture = mapTexture;
      textureCanvas = nextCanvas;
      mapTexture = createMapTexture(textureCanvas);
      globeMaterial.map = mapTexture;
      previousTexture.dispose();
      setHighlightId(activeRegion);
      renderOnce();
    }

    shell.classList.add('is-render-ready', 'is-map-ready');
  };

  const applyWorkerTexture = (data) => {
    applyRenderedCanvases(data.displayBitmap, data.pickBitmap, data.manifest);
    data.displayBitmap.close?.();
    data.pickBitmap.close?.();
  };

  const renderOnMainThread = async (layers = mainThreadLayers) => {
    if (!layers.length) {
      return;
    }
    await import(d3Url);
    await import(textureHelperUrl);
    const dimensions = textureDimensions();
    textureSizeKey = dimensions.key;
    const rendered = globalThis.TravelGlobeTexture.render({
      d3: globalThis.d3,
      layers,
      regions,
      palette: palette(),
      width: dimensions.width,
      height: dimensions.height,
      mode: fallbackMode ? 'orthographic' : 'equirectangular',
      canvasFactory: () => document.createElement('canvas')
    });
    applyRenderedCanvases(rendered.displayCanvas, rendered.pickCanvas, rendered.manifest);
  };

  const loadOnMainThread = async () => {
    setStatus(`边界层载入中 0 / ${sources.length}`);
    const settled = await Promise.allSettled(sources.map(fetchWithTimeout));
    mainThreadLayers = settled.filter((result) => result.status === 'fulfilled').map((result) => result.value);
    const failed = settled.length - mainThreadLayers.length;
    await renderOnMainThread();
    if (!mainThreadLayers.length) {
      setStatus('边界层载入失败', { retry: true });
    } else if (failed) {
      setStatus(`${mainThreadLayers.length} / ${sources.length} 边界层已接入，${failed} 层失败`, { retry: true });
    } else {
      setStatus(`${sources.length} / ${sources.length} 边界层已接入`, { hideAfter: 2200 });
    }
  };

  const handleWorkerMessage = (event) => {
    const data = event.data || {};
    if (data.type === 'progress') {
      setStatus(`边界层载入中 ${data.loaded} / ${data.total}`);
    } else if (data.type === 'texture') {
      applyWorkerTexture(data);
    } else if (data.type === 'complete') {
      if (!data.loaded) {
        setStatus('边界层载入失败', { retry: true });
      } else if (data.failed?.length) {
        setStatus(`${data.loaded} / ${data.total} 边界层已接入，${data.failed.length} 层失败`, { retry: true });
      } else {
        setStatus(`${data.total} / ${data.total} 边界层已接入`, { hideAfter: 2200 });
      }
    } else if (data.type === 'fatal') {
      console.warn('[travel-globe] worker failed, falling back to the main thread', data.message);
      worker?.terminate();
      worker = null;
      loadOnMainThread().catch((error) => {
        console.warn('[travel-globe] main-thread fallback failed', error);
        setStatus('地图纹理生成失败', { retry: true });
      });
    }
  };

  const startDataLoad = () => {
    worker?.terminate();
    worker = null;
    mainThreadLayers = [];
    pickManifest.clear();
    clearRegions();
    setStatus(`边界层载入中 0 / ${sources.length}`);
    const dimensions = textureDimensions();
    textureSizeKey = dimensions.key;

    if ('Worker' in window && 'OffscreenCanvas' in window) {
      worker = new Worker(workerUrl);
      worker.addEventListener('message', handleWorkerMessage);
      worker.addEventListener('error', (event) => {
        console.warn('[travel-globe] worker runtime error', event.message);
        worker?.terminate();
        worker = null;
        loadOnMainThread().catch(() => setStatus('地图纹理生成失败', { retry: true }));
      });
      worker.postMessage({
        type: 'load',
        d3Url,
        textureHelperUrl,
        sources,
        regions,
        palette: palette(),
        width: dimensions.width,
        height: dimensions.height,
        mode: fallbackMode ? 'orthographic' : 'equirectangular'
      });
      return;
    }

    loadOnMainThread().catch((error) => {
      console.warn('[travel-globe] boundary load failed', error);
      setStatus('边界层载入失败', { retry: true });
    });
  };

  const updateThemeTexture = () => {
    if (!initialized) {
      return;
    }
    const colors = palette();
    updateRendererPalette(colors);
    const dimensions = textureDimensions();
    if (worker) {
      worker.postMessage({
        type: 'render',
        palette: colors,
        width: dimensions.width,
        height: dimensions.height,
        mode: fallbackMode ? 'orthographic' : 'equirectangular'
      });
    } else if (mainThreadLayers.length) {
      renderOnMainThread().catch((error) => console.warn('[travel-globe] theme texture update failed', error));
    }
  };

  const decodePickId = (x, y) => {
    if (!pickCanvas.width || !pickCanvas.height) {
      return null;
    }
    const px = clamp(Math.floor(x), 0, pickCanvas.width - 1);
    const py = clamp(Math.floor(y), 0, pickCanvas.height - 1);
    const pixel = pickContext.getImageData(px, py, 1, 1).data;
    const id = pixel[0] | (pixel[1] << 8) | (pixel[2] << 16);
    return pickManifest.get(id) || null;
  };

  const regionAtPointer = (clientX, clientY) => {
    const rect = canvas.getBoundingClientRect();
    if (!rect.width || !rect.height) {
      return null;
    }

    if (fallbackMode) {
      return decodePickId(
        ((clientX - rect.left) / rect.width) * pickCanvas.width,
        ((clientY - rect.top) / rect.height) * pickCanvas.height
      );
    }

    pointer.x = ((clientX - rect.left) / rect.width) * 2 - 1;
    pointer.y = -((clientY - rect.top) / rect.height) * 2 + 1;
    return regionAtNdc(pointer.x, pointer.y);
  };

  const regionAtNdc = (x, y) => {
    if (fallbackMode) {
      return decodePickId(((x + 1) / 2) * pickCanvas.width, ((1 - y) / 2) * pickCanvas.height);
    }

    pointer.set(x, y);
    globe.updateMatrixWorld(true);
    camera.updateMatrixWorld(true);
    raycaster.setFromCamera(pointer, camera);
    globe.getWorldPosition(globeCenter);
    camera.getWorldPosition(cameraPosition);
    const hit = raycaster.intersectObject(globe, false).find((candidate) => {
      surfaceNormal.copy(candidate.point).sub(globeCenter).normalize();
      surfaceToCamera.copy(cameraPosition).sub(candidate.point).normalize();
      return surfaceNormal.dot(surfaceToCamera) > 0.02;
    });
    if (!hit?.uv) {
      return null;
    }
    return decodePickId(hit.uv.x * pickCanvas.width, (1 - hit.uv.y) * pickCanvas.height);
  };

  const regionAtCenter = () => regionAtNdc(0, 0);

  const inspectPointer = (event) => {
    setHoveredRegion(regionAtPointer(event.clientX, event.clientY));
  };

  const bindInteraction = () => {
    canvas.addEventListener('pointerenter', () => {
      pointerInside = true;
      syncAnimationLoop();
    });

    canvas.addEventListener('pointerdown', (event) => {
      pointerInside = true;
      pointerDown = true;
      dragging = false;
      cancelOrientationReset();
      dragStartX = event.clientX;
      dragStartY = event.clientY;
      startRotationX = globe?.rotation.x || 0;
      startRotationY = globe?.rotation.y || 0;
      canvas.focus({ preventScroll: true });
      canvas.setPointerCapture?.(event.pointerId);
      syncAnimationLoop();
      event.preventDefault();
    });

    canvas.addEventListener('pointermove', (event) => {
      if (pointerDown && !fallbackMode) {
        const dx = event.clientX - dragStartX;
        const dy = event.clientY - dragStartY;
        if (Math.abs(dx) + Math.abs(dy) > 3) {
          dragging = true;
          canvas.classList.add('is-dragging');
          setHoveredRegion(null);
        }
        globe.rotation.y = startRotationY + dx * 0.005;
        globe.rotation.x = clamp(startRotationX - dy * 0.0035, -1.1, 1.1);
        renderOnce();
        return;
      }

      if (event.pointerType === 'mouse') {
        window.cancelAnimationFrame(hoverFrame);
        hoverFrame = window.requestAnimationFrame(() => inspectPointer(event));
      }
    });

    const finishPointer = (event, allowSelection = true) => {
      if (!pointerDown) {
        return;
      }
      const moved = Math.abs(event.clientX - dragStartX) + Math.abs(event.clientY - dragStartY);
      const wasDragging = dragging;
      pointerDown = false;
      dragging = false;
      canvas.classList.remove('is-dragging');
      canvas.releasePointerCapture?.(event.pointerId);
      if (allowSelection && moved <= 6) {
        const region = regionAtPointer(event.clientX, event.clientY);
        hoveredRegion = event.pointerType === 'mouse' ? region : null;
        togglePinnedRegion(region);
      }
      if (wasDragging || Math.abs((globe?.rotation.x || 0) - REST_ROTATION_X) >= 0.0001) {
        scheduleOrientationReset();
      }
      syncAnimationLoop();
    };

    canvas.addEventListener('pointerup', finishPointer);
    canvas.addEventListener('pointercancel', (event) => finishPointer(event, false));
    canvas.addEventListener('pointerleave', () => {
      pointerInside = false;
      pointerDown = false;
      dragging = false;
      canvas.classList.remove('is-dragging');
      setHoveredRegion(null);
      if (Math.abs((globe?.rotation.x || 0) - REST_ROTATION_X) >= 0.0001) {
        scheduleOrientationReset();
      }
      syncAnimationLoop();
    });

    canvas.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        event.preventDefault();
        clearRegions();
        return;
      }

      if (event.key === 'Enter') {
        event.preventDefault();
        const region = regionAtCenter();
        hoveredRegion = region;
        togglePinnedRegion(region);
        return;
      }

      if (fallbackMode || !['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(event.key)) {
        return;
      }
      event.preventDefault();
      cancelOrientationReset();
      const step = THREE.MathUtils.degToRad(8);
      if (event.key === 'ArrowLeft') globe.rotation.y -= step;
      if (event.key === 'ArrowRight') globe.rotation.y += step;
      if (event.key === 'ArrowUp') globe.rotation.x = clamp(globe.rotation.x + step, -1.1, 1.1);
      if (event.key === 'ArrowDown') globe.rotation.x = clamp(globe.rotation.x - step, -1.1, 1.1);
      setHoveredRegion(regionAtCenter());
      scheduleOrientationReset();
      renderOnce();
    });

    canvas.addEventListener('blur', () => {
      if (!pointerInside) {
        setHoveredRegion(null);
      }
    });
  };

  const initialize = () => {
    if (initialized) {
      return;
    }
    initialized = true;
    setupRenderer();
    bindInteraction();
    startDataLoad();
  };

  retryButton.addEventListener('click', startDataLoad);

  const preloadObserver = new IntersectionObserver(
    (entries) => {
      if (entries.some((entry) => entry.isIntersecting)) {
        initialize();
        preloadObserver.disconnect();
      }
    },
    { rootMargin: '700px 0px' }
  );
  preloadObserver.observe(root);

  const visibilityObserver = new IntersectionObserver((entries) => {
    viewportVisible = entries.some((entry) => entry.isIntersecting);
    syncAnimationLoop();
  });
  visibilityObserver.observe(root);

  let resizeTimer = 0;
  new ResizeObserver(() => {
    window.clearTimeout(resizeTimer);
    resizeTimer = window.setTimeout(() => {
      resizeRenderer();
      if (!initialized) {
        return;
      }
      const dimensions = textureDimensions();
      if (dimensions.key !== textureSizeKey) {
        textureSizeKey = dimensions.key;
        updateThemeTexture();
      }
    }, 120);
  }).observe(shell);

  document.addEventListener('visibilitychange', syncAnimationLoop);
  reducedMotion.addEventListener?.('change', () => {
    if (reducedMotion.matches && globe) {
      cancelOrientationReset();
      globe.rotation.x = REST_ROTATION_X;
    }
    setInteractionTarget(Boolean(activeRegion));
    syncAnimationLoop();
  });

  let themeFrame = 0;
  new MutationObserver(() => {
    window.cancelAnimationFrame(themeFrame);
    themeFrame = window.requestAnimationFrame(updateThemeTexture);
  }).observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-mode', 'data-bs-theme']
  });

  window.addEventListener('pagehide', (event) => {
    window.clearTimeout(orientationTimer);
    renderer?.setAnimationLoop(null);
    if (!event.persisted) {
      worker?.terminate();
      mapTexture?.dispose();
      pickTexture?.dispose();
      globe?.geometry?.dispose();
      globeMaterial?.dispose();
      renderer?.dispose();
    }
  });
});
