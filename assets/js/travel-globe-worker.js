'use strict';

let runtimeReady = false;
let sources = [];
let regions = [];
let palette = {};
let mode = 'equirectangular';
let width = 2048;
let height = 1024;
let loadedLayers = new Map();
let failedLayers = new Map();

const postFailure = (source, error) => {
  const message = error?.name === 'AbortError' ? '请求超时' : error?.message || '载入失败';
  failedLayers.set(source.id, { source, message });
  postMessage({ type: 'layer-error', sourceId: source.id, name: source.name, message });
};

const fetchLayer = async (source) => {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 12000);

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
    clearTimeout(timer);
  }
};

const renderTextures = () => {
  if (!loadedLayers.size) {
    return;
  }

  const rendered = TravelGlobeTexture.render({
    d3: globalThis.d3,
    layers: [...loadedLayers.values()],
    regions,
    palette,
    width,
    height,
    mode,
    canvasFactory: (canvasWidth, canvasHeight) => new OffscreenCanvas(canvasWidth, canvasHeight)
  });
  const displayBitmap = rendered.displayCanvas.transferToImageBitmap();
  const pickBitmap = rendered.pickCanvas.transferToImageBitmap();

  postMessage(
    {
      type: 'texture',
      displayBitmap,
      pickBitmap,
      manifest: rendered.manifest,
      loaded: loadedLayers.size,
      total: sources.length,
      failed: [...failedLayers.values()].map(({ source, message }) => ({ id: source.id, name: source.name, message }))
    },
    [displayBitmap, pickBitmap]
  );
};

const loadAll = async () => {
  loadedLayers = new Map();
  failedLayers = new Map();
  postMessage({ type: 'progress', loaded: 0, total: sources.length });

  await Promise.all(
    sources.map(async (source) => {
      try {
        const layer = await fetchLayer(source);
        loadedLayers.set(source.id, layer);
        failedLayers.delete(source.id);
        postMessage({ type: 'progress', loaded: loadedLayers.size, total: sources.length, name: source.name });
      } catch (error) {
        postFailure(source, error);
      }
    })
  );

  renderTextures();

  postMessage({
    type: 'complete',
    loaded: loadedLayers.size,
    total: sources.length,
    failed: [...failedLayers.values()].map(({ source, message }) => ({ id: source.id, name: source.name, message }))
  });
};

self.addEventListener('message', async (event) => {
  const data = event.data || {};

  if (data.type === 'load') {
    try {
      if (!runtimeReady) {
        importScripts(data.d3Url, data.textureHelperUrl);
        runtimeReady = true;
      }
      sources = data.sources || [];
      regions = data.regions || [];
      palette = data.palette || {};
      mode = data.mode || 'equirectangular';
      width = data.width || width;
      height = data.height || height;
      await loadAll();
    } catch (error) {
      postMessage({ type: 'fatal', message: error?.message || '纹理渲染器初始化失败' });
    }
    return;
  }

  if (data.type === 'render') {
    palette = data.palette || palette;
    mode = data.mode || mode;
    width = data.width || width;
    height = data.height || height;
    try {
      renderTextures();
    } catch (error) {
      postMessage({ type: 'fatal', message: error?.message || '纹理更新失败' });
    }
  }
});
