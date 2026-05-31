const state = {
  astrology: null,
  astrologyError: "",
  hoveredAstro: null,
  pinnedAstro: null,
  chartQuery: null,
  history: [],
  displayFilter: {
    aspectLines: true,
    hiddenAspectTypes: [],
    hiddenAspectBodies: [],
    hiddenBodies: []
  }
};
const assetVersion = "v34";
const historyStorageKey = "occult-atlas-chart-history";
const sidebarStorageKey = "occult-atlas-sidebar-collapsed";
const displayFilterStorageKey = "occult-atlas-display-filter";
const apiBaseStorageKey = "occult-atlas-api-base";
const apiBaseUrl = normalizeApiBaseUrl(
  globalThis.OCCULT_ATLAS_API_BASE || localStorage.getItem(apiBaseStorageKey) || ""
);
const appBaseUrl = normalizeAppBaseUrl(globalThis.OCCULT_ATLAS_APP_BASE || ".");
const defaultHiddenAstroBodies = ["chiron", "north-node", "south-node"];
const defaultLocation = {
  label: "",
  lat: 31.2304,
  lon: 121.4737
};

const elements = {
  astroChart: document.getElementById("astroChart"),
  astroStatus: document.getElementById("astroStatus"),
  astroPlanetTable: document.getElementById("astroPlanetTable"),
  astroAspectList: document.getElementById("astroAspectList"),
  refreshAstroButton: document.getElementById("refreshAstroButton"),
  exportChartButton: document.getElementById("exportChartButton"),
  resetToNowButton: document.getElementById("resetToNowButton"),
  chartQueryForm: document.getElementById("chartQueryForm"),
  chartDateTime: document.getElementById("chartDateTime"),
  chartLocationLabel: document.getElementById("chartLocationLabel"),
  chartLatitude: document.getElementById("chartLatitude"),
  chartLongitude: document.getElementById("chartLongitude"),
  chartHistoryList: document.getElementById("chartHistoryList"),
  astroInsight: document.getElementById("astroInsight"),
  planetCount: document.getElementById("planetCount"),
  aspectCount: document.getElementById("aspectCount"),
  chartTitle: document.getElementById("chartTitle"),
  sidebarToggle: document.getElementById("sidebarToggle"),
  chartControlToggle: document.getElementById("chartControlToggle"),
  chartControlPanel: document.getElementById("chartControlPanel"),
  aspectDisplayPanel: document.getElementById("aspectDisplayPanel"),
  aspectLinesToggle: document.getElementById("aspectLinesToggle"),
  aspectTypeFilterList: document.getElementById("aspectTypeFilterList"),
  bodyVisibilityFilterList: document.getElementById("bodyVisibilityFilterList"),
  aspectBodyFilterList: document.getElementById("aspectBodyFilterList")
};

const zodiacIcons = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"];
const zodiacEnglishNames = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"];
const zodiacInfo = [
  { name: "白羊座", element: "火元素", modality: "基本宫", line: "启动、直接、开路和主动表达。", icon: "aries" },
  { name: "金牛座", element: "土元素", modality: "固定宫", line: "稳定、积累、感官和价值维护。", icon: "taurus" },
  { name: "双子座", element: "风元素", modality: "变动宫", line: "信息、语言、连接和快速转换。", icon: "gemini" },
  { name: "巨蟹座", element: "水元素", modality: "基本宫", line: "照护、记忆、情绪边界和归属感。", icon: "cancer" },
  { name: "狮子座", element: "火元素", modality: "固定宫", line: "创造、自我呈现、热情和心的主权。", icon: "leo" },
  { name: "处女座", element: "土元素", modality: "变动宫", line: "分析、修整、服务和具体技艺。", icon: "virgo" },
  { name: "天秤座", element: "风元素", modality: "基本宫", line: "关系、判断、比例和协商。", icon: "libra" },
  { name: "天蝎座", element: "水元素", modality: "固定宫", line: "深度、欲望、危机和转化。", icon: "scorpio" },
  { name: "射手座", element: "火元素", modality: "变动宫", line: "远方、信念、探索和意义扩张。", icon: "sagittarius" },
  { name: "摩羯座", element: "土元素", modality: "基本宫", line: "结构、责任、目标和现实秩序。", icon: "capricorn" },
  { name: "水瓶座", element: "风元素", modality: "固定宫", line: "系统、社群、异端视角和未来感。", icon: "aquarius" },
  { name: "双鱼座", element: "水元素", modality: "变动宫", line: "想象、共感、溶解和灵性渗透。", icon: "pisces" }
];
const houseInfo = [
  "第一宫：自我、身体、气质、外显风格与人生进入世界的方式。",
  "第二宫：资源、金钱、所有物、身体安全感与个人价值。",
  "第三宫：学习、语言、手足邻里、短途移动与日常信息交换。",
  "第四宫：家庭、根源、内在基地、私人生活与情绪安全。",
  "第五宫：创造、恋爱、娱乐、子女、舞台感与生命喜悦。",
  "第六宫：工作流程、健康、习惯、服务、修复与日常秩序。",
  "第七宫：伴侣、合作、公开关系、契约与投射出的他者。",
  "第八宫：共享资源、亲密、债务、危机、死亡与深层转化。",
  "第九宫：高等学习、远行、哲学、出版、信仰与世界观。",
  "第十宫：事业、名声、社会角色、目标、成就与公共责任。",
  "第十一宫：朋友、团体、社群、愿景、网络与共同未来。",
  "第十二宫：潜意识、隐退、梦、灵性、隔离、消融与幕后之事。"
];
const angleInfo = {
  asc: { name: "上升点", line: "东方地平线，描述人格入口、身体显现和他人第一眼感到的气质。" },
  mc: { name: "中天", line: "天顶方向，描述公共身份、事业目标、可见成就和社会召唤。" },
  dsc: { name: "下降点", line: "西方地平线，描述亲密关系、合作对象和被投射到他者身上的主题。" },
  ic: { name: "天底", line: "地下天顶，描述根源、家庭、私密基地和内在安全感。" }
};
const planetIconIds = {
  sun: "sun",
  moon: "moon",
  mercury: "mercury",
  venus: "venus",
  mars: "mars",
  jupiter: "jupiter",
  saturn: "saturn",
  uranus: "uranus",
  neptune: "neptune",
  pluto: "pluto",
  chiron: "chiron",
  "north-node": "north-node",
  "south-node": "north-node"
};
const aspectIconIds = {
  conjunction: "conjunction",
  opposition: "opposition",
  square: "square",
  trine: "trine",
  sextile: "sextile"
};
const aspectMeaning = {
  conjunction: "合相强调两股力量合并、放大或互相覆盖。",
  opposition: "冲相强调两端拉扯、镜像、对立与需要被看见的张力。",
  square: "刑相强调摩擦、压力、行动阻碍和必须调整的结构。",
  trine: "拱相强调顺流、支持、自然流动和较容易被调动的资源。",
  sextile: "六合强调机会、协作、可练习的能力和温和的联结。"
};
const planetMeaning = {
  sun: "太阳代表中心意识、生命力、意志和当下最需要被照亮的主题。",
  moon: "月亮代表情绪、身体节律、习惯反应和即时感受。",
  mercury: "水星代表语言、思考、学习、传递和信息处理。",
  venus: "金星代表关系、吸引、价值、审美和愉悦感。",
  mars: "火星代表行动、欲望、冲突、切入点和主动性。",
  jupiter: "木星代表扩张、信念、机会、意义和远景。",
  saturn: "土星代表边界、责任、时间、限制和结构化。",
  uranus: "天王星代表突变、解放、断裂、创新和电性的觉醒。",
  neptune: "海王星代表想象、迷雾、溶解、灵感和无边界感。",
  pluto: "冥王星代表深层转化、权力、阴影、清除和不可逆的再生。",
  chiron: "凯龙星代表伤口、疗愈、导师经验，以及把脆弱转化为技艺的路径。",
  "north-node": "北交点代表灵魂发展方向、陌生但需要练习的经验，以及未来牵引力。",
  "south-node": "南交点代表熟悉的惯性、旧经验、天赋存量，以及需要松动的舒适区。"
};
const planetPlacementThemes = {
  sun: "核心意识、生命力和自我表达",
  moon: "情绪反应、安全感和身体节律",
  mercury: "思考方式、语言、学习和信息处理",
  venus: "关系模式、审美、吸引力和价值感",
  mars: "行动方式、欲望、竞争和切入点",
  jupiter: "扩张方式、信念、机会和意义感",
  saturn: "责任、边界、限制和结构化方式",
  uranus: "突破、独立、变化和非传统反应",
  neptune: "想象、灵感、迷雾、共感和溶解感",
  pluto: "深层转化、权力议题、阴影和再生",
  chiron: "伤口、疗愈经验和把脆弱转成技艺的方式",
  "north-node": "成长方向、未来牵引和需要练习的经验",
  "south-node": "熟悉惯性、旧有天赋和需要松动的舒适区"
};
const chartRadius = {
  viewBox: "-360 -350 720 700",
  sign: 294,
  tickOuterMajor: 286,
  tickOuter: 280,
  tickInnerMajor: 252,
  tickInnerMedium: 264,
  tickInner: 272,
  houseInner: 118,
  houseOuter: 242,
  houseLabel: 140,
  angleInner: 78,
  angleOuter: 312,
  angleLabel: 330,
  planet: 206,
  outer: 316,
  zodiac: 266,
  middle: 214,
  inner: 116
};

bindEvents();
initializeChartControls();
initializeSidebar();
initializeDisplayFilter();
loadAstrologySnapshot();
registerServiceWorker();

function bindEvents() {
  elements.sidebarToggle.addEventListener("click", () => {
    setSidebarCollapsed(!document.body.classList.contains("sidebar-collapsed"));
  });

  elements.chartControlToggle.addEventListener("click", () => {
    setChartControlOpen(elements.chartControlPanel.hidden);
  });

  document.addEventListener("click", (event) => {
    if (elements.chartControlPanel.hidden) return;
    if (event.target.closest(".chart-control-menu")) return;
    setChartControlOpen(false);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      setChartControlOpen(false);
    }
  });

  elements.refreshAstroButton.addEventListener("click", () => {
    loadAstrologySnapshot(state.chartQuery);
  });

  elements.exportChartButton.addEventListener("click", () => {
    exportCurrentChart().catch((error) => {
      elements.astroStatus.textContent = `导出失败：${error instanceof Error ? error.message : String(error)}`;
    });
  });

  elements.resetToNowButton.addEventListener("click", () => {
    setDefaultQueryValues(new Date());
    state.chartQuery = null;
    loadAstrologySnapshot();
  });

  elements.chartQueryForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const query = readChartQueryFromForm();
    state.chartQuery = query;
    addChartHistory(query);
    loadAstrologySnapshot(query);
  });

  elements.chartHistoryList.addEventListener("click", (event) => {
    const deleteButton = event.target.closest("[data-history-delete]");
    if (deleteButton) {
      event.stopPropagation();
      deleteChartHistory(deleteButton.dataset.historyDelete);
      return;
    }
    const row = event.target.closest("[data-history-id]");
    if (!row) return;
    const item = state.history.find((entry) => entry.id === row.dataset.historyId);
    if (!item) return;
    state.chartQuery = item.query;
    applyQueryToForm(item.query);
    loadAstrologySnapshot(item.query);
  });

  elements.chartHistoryList.addEventListener("keydown", (event) => {
    if (event.key !== "Enter" && event.key !== " ") return;
    const deleteButton = event.target.closest("[data-history-delete]");
    if (!deleteButton) return;
    event.preventDefault();
    deleteChartHistory(deleteButton.dataset.historyDelete);
  });

  elements.aspectDisplayPanel.addEventListener("change", (event) => {
    const control = event.target;
    if (!(control instanceof HTMLInputElement)) return;
    if (control.id === "aspectLinesToggle") {
      state.displayFilter.aspectLines = control.checked;
    } else if (control.dataset.filterAspect) {
      toggleFilterValue("hiddenAspectTypes", control.dataset.filterAspect, !control.checked);
    } else if (control.dataset.filterBodyVisibility) {
      toggleFilterValue("hiddenBodies", control.dataset.filterBodyVisibility, !control.checked);
    } else if (control.dataset.filterBody) {
      toggleFilterValue("hiddenAspectBodies", control.dataset.filterBody, !control.checked);
    }
    saveDisplayFilter();
    if (state.astrology) {
      renderAstrology();
    }
  });

  elements.astroPlanetTable.addEventListener("mouseover", (event) => {
    const row = event.target.closest("[data-astro-id]");
    if (!row) return;
    setHover("planet", row.dataset.astroId);
  });

  elements.astroPlanetTable.addEventListener("click", (event) => {
    const row = event.target.closest("[data-astro-id]");
    if (!row) return;
    togglePin("planet", row.dataset.astroId);
  });

  elements.astroAspectList.addEventListener("mouseover", (event) => {
    const row = event.target.closest("[data-astro-id]");
    if (!row) return;
    setHover("aspect", row.dataset.astroId);
  });

  elements.astroAspectList.addEventListener("click", (event) => {
    const row = event.target.closest("[data-astro-id]");
    if (!row) return;
    togglePin("aspect", row.dataset.astroId);
  });

  document.querySelector(".sky-sidebar").addEventListener("mouseleave", () => {
    clearHover();
  });

  elements.astroChart.addEventListener("mousemove", (event) => {
    const target = resolveChartTarget(event);
    if (target) {
      setHover(target.type, target.id);
    } else {
      clearHover();
    }
  });

  elements.astroChart.addEventListener("click", (event) => {
    const target = resolveChartTarget(event);
    if (!target) return;
    togglePin(target.type, target.id);
  });

  elements.astroChart.addEventListener("mouseleave", () => {
    clearHover();
  });

  elements.astroInsight.addEventListener("click", (event) => {
    const link = event.target.closest("[data-focus-type][data-focus-id]");
    if (!link) return;
    togglePin(link.dataset.focusType, link.dataset.focusId);
  });
}

async function exportCurrentChart() {
  if (!state.astrology) {
    throw new Error("暂无可导出的星盘数据");
  }
  const sourceSvg = elements.astroChart.querySelector("svg");
  if (!sourceSvg) {
    throw new Error("星盘尚未渲染完成");
  }

  const cleanSvg = sourceSvg.cloneNode(true);
  cleanSvg.querySelectorAll(".active,.dim").forEach((node) => {
    node.classList.remove("active", "dim");
  });
  localizeChartSvgForExport(cleanSvg, state.astrology);
  await inlineSvgImages(cleanSvg);

  const exportSvg = buildPrintableChartSvg(cleanSvg, state.astrology);
  const blob = new Blob([exportSvg], { type: "image/svg+xml;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `${buildExportFilename(state.astrology)}.svg`;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

async function inlineSvgImages(svg) {
  const images = Array.from(svg.querySelectorAll("image"));
  await Promise.all(images.map(async (image) => {
    const href = image.getAttribute("href") || image.getAttribute("xlink:href");
    if (!href || href.startsWith("data:")) return;
    const response = await fetch(href);
    if (!response.ok) return;
    const blob = await response.blob();
    const dataUrl = await blobToDataUrl(blob);
    image.setAttribute("href", dataUrl);
    image.removeAttribute("xlink:href");
  }));
}

function blobToDataUrl(blob) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result);
    reader.onerror = reject;
    reader.readAsDataURL(blob);
  });
}

function localizeChartSvgForExport(svg, snapshot) {
  const angleLabels = Array.from(svg.querySelectorAll(".angle-label"));
  angleLabels.forEach((label, index) => {
    const angle = snapshot.angles?.[index];
    if (!angle) return;
    const degreeLabel = label.querySelector(".angle-degree");
    if (degreeLabel) {
      degreeLabel.textContent = `${englishSignName(angle.signIndex)} ${formatDegree(angle.signDegree)}`;
    }
  });

  const centerLabel = svg.querySelector(".astro-center:not(.sub)");
  if (centerLabel && snapshot.moonPhase) {
    centerLabel.textContent = englishMoonPhase(snapshot.moonPhase);
  }
}

function buildPrintableChartSvg(chartSvg, snapshot) {
  const serializer = new XMLSerializer();
  const chartMarkup = serializer.serializeToString(chartSvg);
  const chartDate = formatEnglishDateTime(snapshot.calculatedAt);
  const coords = snapshot.location ? formatEnglishCoordinates(snapshot.location.lat, snapshot.location.lon) : "";
  const locationName = snapshot.location?.label || "Custom coordinates";
  const title = state.chartQuery ? "Historical Astrology Chart" : "Current Sky Chart";
  const chartMode = state.chartQuery ? "Historical query" : "Current moment";
  const houseSystem = snapshot.houseSystem || "Placidus";
  const zodiac = snapshot.zodiac === "tropical" ? "Tropical zodiac" : `${snapshot.zodiac || "Zodiac"}`;
  const engine = snapshot.engine || "Swiss Ephemeris";

  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1600" viewBox="0 0 1200 1600">
  <defs>
    <radialGradient id="paperGlow" cx="50%" cy="38%" r="58%">
      <stop offset="0%" stop-color="#283632"/>
      <stop offset="58%" stop-color="#17191d"/>
      <stop offset="100%" stop-color="#0f1115"/>
    </radialGradient>
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="18" stdDeviation="24" flood-color="#000000" flood-opacity="0.34"/>
    </filter>
  </defs>
  <style>
    .poster-title { fill: #f7f1e7; font-family: "Segoe UI", "Microsoft YaHei", Arial, sans-serif; font-size: 58px; font-weight: 800; text-anchor: middle; }
    .poster-subtitle { fill: #aeb9b6; font-family: "Segoe UI", "Microsoft YaHei", Arial, sans-serif; font-size: 22px; font-weight: 600; text-anchor: middle; }
    .poster-label { fill: #79d6ca; font-family: "Segoe UI", "Microsoft YaHei", Arial, sans-serif; font-size: 18px; font-weight: 800; letter-spacing: 2px; text-anchor: middle; }
    .meta-label { fill: #79d6ca; font-family: "Segoe UI", Arial, sans-serif; font-size: 15px; font-weight: 800; letter-spacing: 1px; }
    .meta-value { fill: #e7eee9; font-family: "Segoe UI", Arial, sans-serif; font-size: 23px; font-weight: 650; }
    .poster-footer { fill: #7f8987; font-family: "Segoe UI", "Microsoft YaHei", Arial, sans-serif; font-size: 18px; text-anchor: middle; }
    .astro-ring { fill: none; stroke: rgba(220,226,231,0.2); }
    .astro-ring.outer { stroke-width: 1.5; }
    .astro-ring.zodiac { stroke-width: 1.2; }
    .astro-ring.middle { stroke-width: 1; stroke-dasharray: 2 8; }
    .astro-ring.inner { stroke-width: 1; }
    .zodiac-tick,.house-line { stroke: rgba(220,226,231,0.18); stroke-width: 1; }
    .zodiac-tick.major { stroke: rgba(220,226,231,0.42); stroke-width: 1.6; }
    .house-label,.angle-label { dominant-baseline: middle; fill: #c1c8c7; font-family: "Segoe UI", Arial, sans-serif; font-size: 11px; font-weight: 700; text-anchor: middle; }
    .angle-degree { fill: #d1c7b6; font-size: 9px; font-weight: 600; }
    .angle-line { stroke: rgba(240,242,244,0.68); stroke-width: 1.5; }
    .aspect-line { stroke-width: 1.4; opacity: 0.62; stroke-linecap: round; }
    .aspect-line.active { stroke-width: 1.4; opacity: 0.62; }
    .aspect-line.conjunction { stroke: #c89c44; }
    .aspect-line.opposition,.aspect-line.square { stroke: #ba6a77; }
    .aspect-line.trine,.aspect-line.sextile { stroke: #6ca79d; }
    .planet-node circle { fill: #e9f4ef; stroke: #2d6b63; stroke-width: 2; }
    .astro-center { fill: #f0f2f4; font-family: "Segoe UI", "Microsoft YaHei", Arial, sans-serif; font-size: 18px; font-weight: 800; text-anchor: middle; }
    .astro-center.sub { fill: #aeb9b6; font-size: 11px; font-weight: 600; }
    .time-dial,.magic-layer { opacity: 0.32; }
    .time-dial line,.time-dial circle,.magic-layer circle,.magic-layer polygon,.magic-layer line { fill: none; stroke: rgba(143,209,200,0.22); stroke-width: 1; }
    .time-dial .time-pointer { stroke: rgba(244,201,93,0.62); stroke-width: 1.8; stroke-linecap: round; }
    .magic-layer-runes text { dominant-baseline: middle; fill: rgba(244,201,93,0.34); font-size: 13px; font-weight: 700; text-anchor: middle; }
  </style>
  <rect width="1200" height="1600" fill="url(#paperGlow)"/>
  <circle cx="600" cy="790" r="458" fill="none" stroke="#31413d" stroke-width="1"/>
  <circle cx="600" cy="790" r="424" fill="none" stroke="#202a28" stroke-width="1"/>
  <text class="poster-label" x="600" y="132">OCCULT ATLAS</text>
  <text class="poster-title" x="600" y="210">${escapeSvg(title)}</text>
  <text class="poster-subtitle" x="600" y="254">${escapeSvg(chartMode)} · ${escapeSvg(houseSystem)} · ${escapeSvg(zodiac)}</text>
  <g transform="translate(170 304)">
    <text class="meta-label" x="0" y="0">TIME</text>
    <text class="meta-value" x="0" y="34">${escapeSvg(chartDate)}</text>
    <text class="meta-label" x="0" y="84">LOCATION</text>
    <text class="meta-value" x="0" y="118">${escapeSvg(locationName)}</text>
  </g>
  <g transform="translate(740 304)">
    <text class="meta-label" x="0" y="0">COORDINATES</text>
    <text class="meta-value" x="0" y="34">${escapeSvg(coords)}</text>
    <text class="meta-label" x="0" y="84">ENGINE</text>
    <text class="meta-value" x="0" y="118">${escapeSvg(engine)}</text>
  </g>
  <g filter="url(#softShadow)" transform="translate(100 320)">
    <svg x="0" y="0" width="1000" height="1000" viewBox="-360 -350 720 700">
      ${chartMarkup.replace(/^<svg[^>]*>|<\/svg>$/g, "")}
    </svg>
  </g>
  <text class="poster-footer" x="600" y="1460">Generated for reflection and study · Not a deterministic prediction</text>
</svg>`;
}

function buildExportFilename(snapshot) {
  const compactDate = new Date(snapshot.calculatedAt).toISOString().slice(0, 16).replace(/[-:T]/g, "");
  return `occult-atlas-chart-${compactDate}`;
}

function initializeChartControls() {
  state.history = loadChartHistory();
  setDefaultQueryValues(new Date());
  renderChartHistory();
}

function initializeSidebar() {
  const collapsed = localStorage.getItem(sidebarStorageKey) === "true";
  setSidebarCollapsed(collapsed);
}

function initializeDisplayFilter() {
  try {
    const raw = localStorage.getItem(displayFilterStorageKey);
    const saved = raw ? JSON.parse(raw) : null;
    state.displayFilter = {
      aspectLines: saved?.aspectLines !== false,
      hiddenAspectTypes: Array.isArray(saved?.hiddenAspectTypes) ? saved.hiddenAspectTypes : [],
      hiddenAspectBodies: Array.isArray(saved?.hiddenAspectBodies) ? saved.hiddenAspectBodies : [...defaultHiddenAstroBodies],
      hiddenBodies: Array.isArray(saved?.hiddenBodies) ? saved.hiddenBodies : [...defaultHiddenAstroBodies]
    };
  } catch {
    state.displayFilter = {
      aspectLines: true,
      hiddenAspectTypes: [],
      hiddenAspectBodies: [...defaultHiddenAstroBodies],
      hiddenBodies: [...defaultHiddenAstroBodies]
    };
  }
}

function saveDisplayFilter() {
  localStorage.setItem(displayFilterStorageKey, JSON.stringify(state.displayFilter));
}

function toggleFilterValue(key, value, hidden) {
  const values = new Set(state.displayFilter[key]);
  if (hidden) {
    values.add(value);
  } else {
    values.delete(value);
  }
  state.displayFilter[key] = Array.from(values);
}

function setSidebarCollapsed(collapsed) {
  document.body.classList.toggle("sidebar-collapsed", collapsed);
  localStorage.setItem(sidebarStorageKey, String(collapsed));
  elements.sidebarToggle.setAttribute("aria-expanded", String(!collapsed));
  elements.sidebarToggle.setAttribute("aria-label", collapsed ? "展开左侧星盘菜单" : "收起左侧星盘菜单");
  elements.sidebarToggle.querySelector("span").textContent = collapsed ? "›" : "‹";
  if (collapsed) {
    setChartControlOpen(false);
  }
}

function setChartControlOpen(open) {
  elements.chartControlPanel.hidden = !open;
  elements.chartControlToggle.setAttribute("aria-expanded", String(open));
  document.body.classList.toggle("control-menu-open", open);
}

async function loadAstrologySnapshot(query = null) {
  try {
    elements.astroStatus.textContent = query ? "读取历史星盘..." : "读取实时星盘...";
    const response = await fetch(buildAstrologyUrl(query), { cache: "no-store" });
    if (!response.ok) {
      const payload = await safeJson(response);
      throw new Error(payload?.message || `Astrology API returned ${response.status}`);
    }
    state.astrology = await response.json();
    state.astrologyError = "";
    state.hoveredAstro = null;
    state.pinnedAstro = null;
  } catch (error) {
    state.astrology = null;
    state.astrologyError = error instanceof Error ? error.message : String(error);
  }

  renderAstrology();
}

function buildAstrologyUrl(query) {
  const endpoint = buildApiUrl("/api/astrology/now");
  if (!query) return endpoint;
  const params = new URLSearchParams();
  params.set("datetime", query.datetime);
  params.set("lat", String(query.lat));
  params.set("lon", String(query.lon));
  if (query.label) params.set("label", query.label);
  return `${endpoint}?${params.toString()}`;
}

function buildApiUrl(path) {
  return apiBaseUrl ? `${apiBaseUrl}${path}` : `.${path}`;
}

function normalizeApiBaseUrl(value) {
  return String(value || "").trim().replace(/\/+$/, "");
}

function setDefaultQueryValues(date) {
  elements.chartDateTime.value = toDateTimeLocalValue(date);
  elements.chartLocationLabel.value = defaultLocation.label;
  elements.chartLatitude.value = String(defaultLocation.lat);
  elements.chartLongitude.value = String(defaultLocation.lon);
}

function readChartQueryFromForm() {
  const dateValue = elements.chartDateTime.value;
  const date = dateValue ? new Date(dateValue) : new Date();
  const lat = Number.parseFloat(elements.chartLatitude.value || String(defaultLocation.lat));
  const lon = Number.parseFloat(elements.chartLongitude.value || String(defaultLocation.lon));
  return {
    id: crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random()}`,
    datetime: date.toISOString(),
    label: elements.chartLocationLabel.value.trim(),
    lat: Number.isFinite(lat) ? lat : defaultLocation.lat,
    lon: Number.isFinite(lon) ? lon : defaultLocation.lon
  };
}

function applyQueryToForm(query) {
  elements.chartDateTime.value = toDateTimeLocalValue(new Date(query.datetime));
  elements.chartLocationLabel.value = query.label || "";
  elements.chartLatitude.value = String(query.lat);
  elements.chartLongitude.value = String(query.lon);
}

function setHover(type, id) {
  if (state.hoveredAstro?.type === type && state.hoveredAstro?.id === id) return;
  state.hoveredAstro = { type, id };
  updateAstrologyFocus();
}

function clearHover() {
  if (!state.hoveredAstro) return;
  state.hoveredAstro = null;
  updateAstrologyFocus();
}

function resolveChartTarget(event) {
  if (!state.astrology) return null;
  const svg = elements.astroChart.querySelector("svg");
  if (!svg) return null;
  const point = svg.createSVGPoint();
  point.x = event.clientX;
  point.y = event.clientY;
  const local = point.matrixTransform(svg.getScreenCTM().inverse());
  return resolveAstroPoint(local.x, local.y, state.astrology);
}

function resolveAstroPoint(x, y, snapshot) {
  const radius = Math.hypot(x, y);
  const longitude = normalizeChartLongitude(Math.atan2(y, x) * 180 / Math.PI + 90);

  const planetHit = nearestRadialBody(snapshot.bodies, x, y, chartRadius.planet, 25);
  if (planetHit) return { type: "planet", id: planetHit.id };

  const angleHit = nearestAngle(snapshot.angles || [], x, y, radius, 10);
  if (angleHit) return { type: "angle", id: angleHit.id };

  const houseHit = nearestAngle(snapshot.houses || [], x, y, radius, 9);
  if (houseHit) return { type: "house", id: houseHit.id };

  if (radius >= chartRadius.tickInnerMajor - 18 && radius <= chartRadius.outer + 26) {
    return { type: "zodiac", id: String(Math.floor(longitude / 30)) };
  }

  const aspectHit = nearestAspect(snapshot, x, y, 7);
  if (aspectHit) return { type: "aspect", id: aspectHit.id };

  return null;
}

function nearestRadialBody(bodies, x, y, _radius, tolerance) {
  let best = null;
  for (const [index, body] of bodies.entries()) {
    if (!isBodyVisible(body.id)) continue;
    const point = polarPoint(chartRadius.planet, body.longitude);
    const distance = Math.hypot(x - point.x, y - point.y);
    if (distance <= tolerance && (!best || distance < best.distance || (Math.abs(distance - best.distance) < 0.01 && index < best.index))) {
      best = { ...body, distance, index };
    }
  }
  return best;
}

function nearestAngle(items, x, y, radius, tolerance) {
  if (radius < chartRadius.angleInner - 12 || radius > chartRadius.angleOuter + 24) return null;
  let best = null;
  for (const item of items) {
    const distance = distanceToRadialSegment(x, y, item.longitude, chartRadius.angleInner, chartRadius.angleOuter);
    if (distance <= tolerance && (!best || distance < best.distance)) {
      best = { ...item, distance };
    }
  }
  return best;
}

function nearestAspect(snapshot, x, y, tolerance) {
  let best = null;
  for (const aspect of snapshot.aspects) {
    if (!isAspectVisible(aspect)) continue;
    const a = snapshot.bodies.find((body) => body.id === aspect.a);
    const b = snapshot.bodies.find((body) => body.id === aspect.b);
    if (!isBodyVisible(a?.id) || !isBodyVisible(b?.id)) continue;
    if (!a || !b) continue;
    const pa = polarPoint(chartRadius.planet, a.longitude);
    const pb = polarPoint(chartRadius.planet, b.longitude);
    const distance = distanceToSegment(x, y, pa.x, pa.y, pb.x, pb.y);
    if (distance <= tolerance && (!best || distance < best.distance)) {
      best = { ...aspect, distance };
    }
  }
  return best;
}

function togglePin(type, id) {
  if (state.pinnedAstro?.type === type && state.pinnedAstro?.id === id) {
    state.pinnedAstro = null;
  } else {
    state.pinnedAstro = { type, id };
  }
  state.hoveredAstro = null;
  updateAstrologyFocus();
}

function renderAstrology() {
  if (!state.astrology) {
    elements.astroStatus.textContent = state.astrologyError
      ? `实时星盘不可用：${state.astrologyError}`
      : "等待实时星盘数据...";
    elements.astroChart.innerHTML = buildEmptyChart();
    elements.astroPlanetTable.innerHTML = `<div class="astro-empty">启动 <code>python scripts/dev-server.py</code> 后可读取 Swiss Ephemeris 数据。</div>`;
    elements.astroAspectList.innerHTML = "";
    elements.astroInsight.hidden = true;
    return;
  }

  const snapshot = state.astrology;
  const warning = snapshot.warning ? " · fallback" : "";
  const visibleBodies = snapshot.bodies.filter((body) => isBodyVisible(body.id));
  const visibleAspects = snapshot.aspects.filter((aspect) => isAspectVisible(aspect));
  elements.astroStatus.textContent = `${formatDateTime(snapshot.calculatedAt)} · ${snapshot.engine}${warning}`;
  elements.chartTitle.textContent = `${state.chartQuery ? "历史星盘" : "本地实时星盘"} · ${snapshot.houseSystem || "Placidus"}`;
  elements.planetCount.textContent = `${visibleBodies.length + (snapshot.angles?.length || 0)}/${snapshot.bodies.length + (snapshot.angles?.length || 0)}`;
  elements.aspectCount.textContent = `${visibleAspects.length}/${snapshot.aspects.length}`;
  const angleRows = (snapshot.angles || []).map((angle) => `
    <button class="astro-row angle-row" type="button" data-astro-type="angle" data-astro-id="${escapeHtml(angle.id)}">
      <span class="astro-mini-symbol">${escapeHtml(angle.label)}</span>
      <span>${escapeHtml(angleDisplayName(angle.id))}</span>
      <strong>${escapeHtml(angle.sign)} ${formatDegree(angle.signDegree)}</strong>
    </button>
  `).join("");
  elements.astroPlanetTable.innerHTML = visibleBodies.map((body) => `
    <button class="astro-row" type="button" data-astro-type="planet" data-astro-id="${escapeHtml(body.id)}">
      <img src="${iconPath("planet", body.id)}" alt="">
      <span>${escapeHtml(body.name)}</span>
      <strong>${escapeHtml(body.sign)} ${formatDegree(body.signDegree)}${body.retrograde ? " R" : ""}</strong>
    </button>
  `).join("") + angleRows;
  elements.astroAspectList.innerHTML = visibleAspects.length
    ? visibleAspects.slice(0, 14).map((aspect) => `
      <button class="astro-row aspect" type="button" data-astro-type="aspect" data-astro-id="${escapeHtml(aspect.id)}">
        <img src="${iconPath("aspect", aspect.aspect)}" alt="">
        <span>${escapeHtml(aspect.aName)} · ${escapeHtml(aspect.bName)}</span>
        <strong>${escapeHtml(aspect.aspectLabel || aspect.aspect)} ${aspect.orb.toFixed(2)}°</strong>
      </button>
    `).join("")
    : `<div class="astro-empty">当前过滤条件下没有可显示的相位线。</div>`;
  renderDisplayFilters(snapshot);
  elements.astroChart.innerHTML = buildAstroChart(snapshot, !state.chartQuery);
  elements.astroInsight.hidden = false;
  updateAstrologyFocus();
}

function buildEmptyChart() {
  return `
    <svg viewBox="-380 -320 760 640" role="img" aria-label="Astrology chart waiting for live data">
      <circle class="astro-ring outer" r="240"></circle>
      <circle class="astro-ring middle" r="190"></circle>
      <circle class="astro-ring inner" r="116"></circle>
      <text class="astro-center" y="-6">Occult Atlas</text>
      <text class="astro-center sub" y="18">等待实时星盘数据</text>
    </svg>
  `;
}

function renderDisplayFilters(snapshot) {
  elements.aspectLinesToggle.checked = state.displayFilter.aspectLines;
  const aspectTypes = Array.from(new Map(snapshot.aspects.map((aspect) => [
    aspect.aspect,
    aspect.aspectLabel || aspect.aspect
  ])).entries());
  elements.aspectTypeFilterList.innerHTML = aspectTypes.map(([id, label]) => `
    <label class="filter-toggle">
      <input type="checkbox" data-filter-aspect="${escapeHtml(id)}" ${state.displayFilter.hiddenAspectTypes.includes(id) ? "" : "checked"}>
      <span>${escapeHtml(label)}</span>
    </label>
  `).join("");
  elements.bodyVisibilityFilterList.innerHTML = snapshot.bodies.map((body) => `
    <label class="filter-toggle">
      <input type="checkbox" data-filter-body-visibility="${escapeHtml(body.id)}" ${state.displayFilter.hiddenBodies.includes(body.id) ? "" : "checked"}>
      <span>${escapeHtml(body.name)}</span>
    </label>
  `).join("");
  elements.aspectBodyFilterList.innerHTML = snapshot.bodies.map((body) => `
    <label class="filter-toggle">
      <input type="checkbox" data-filter-body="${escapeHtml(body.id)}" ${state.displayFilter.hiddenAspectBodies.includes(body.id) ? "" : "checked"}>
      <span>${escapeHtml(body.name)}</span>
    </label>
  `).join("");
}

function buildAstroChart(snapshot, isLive = true) {
  const signZones = zodiacIcons.map((_icon, index) => {
    const innerStart = polarPoint(chartRadius.tickInnerMajor, index * 30);
    const outerStart = polarPoint(chartRadius.outer, index * 30);
    const outerEnd = polarPoint(chartRadius.outer, index * 30 + 30);
    const innerEnd = polarPoint(chartRadius.tickInnerMajor, index * 30 + 30);
    const largeArc = 0;
    return `<path class="zodiac-zone" data-astro-type="zodiac" data-astro-id="${index}" d="M ${innerStart.x} ${innerStart.y} L ${outerStart.x} ${outerStart.y} A ${chartRadius.outer} ${chartRadius.outer} 0 ${largeArc} 1 ${outerEnd.x} ${outerEnd.y} L ${innerEnd.x} ${innerEnd.y} A ${chartRadius.tickInnerMajor} ${chartRadius.tickInnerMajor} 0 ${largeArc} 0 ${innerStart.x} ${innerStart.y} Z"></path>`;
  }).join("");
  const signLabels = zodiacIcons.map((icon, index) => {
    const point = polarPoint(chartRadius.sign, index * 30 + 15);
    return `
      <image class="zodiac-icon" data-astro-type="zodiac" data-astro-id="${index}" href="${iconPath("zodiac", icon)}" x="${point.x - 17}" y="${point.y - 17}" width="34" height="34"></image>
    `;
  }).join("");
  const zodiacTicks = Array.from({ length: 360 }, (_, index) => {
    const isMajor = index % 30 === 0;
    const isMedium = index % 5 === 0;
    const outer = polarPoint(isMajor ? chartRadius.tickOuterMajor : chartRadius.tickOuter, index);
    const inner = polarPoint(isMajor ? chartRadius.tickInnerMajor : isMedium ? chartRadius.tickInnerMedium : chartRadius.tickInner, index);
    return `<line class="zodiac-tick ${isMajor ? "major" : isMedium ? "medium" : ""}" x1="${outer.x}" y1="${outer.y}" x2="${inner.x}" y2="${inner.y}"></line>`;
  }).join("");
  const timeMotion = buildTimeMotion(isLive);
  const houseLines = (snapshot.houses || []).map((house) => {
    const inner = polarPoint(chartRadius.houseInner, house.longitude);
    const outer = polarPoint(chartRadius.houseOuter, house.longitude);
    const label = polarPoint(chartRadius.houseLabel, house.longitude + 3);
    return `
      <g class="house-node" data-astro-type="house" data-astro-id="${escapeHtml(house.id)}">
        <line class="house-line" x1="${inner.x}" y1="${inner.y}" x2="${outer.x}" y2="${outer.y}"></line>
        <text class="house-label" x="${label.x}" y="${label.y}">${house.number}</text>
      </g>
    `;
  }).join("");
  const angleLines = (snapshot.angles || []).map((angle) => {
    const inner = polarPoint(chartRadius.angleInner, angle.longitude);
    const outer = polarPoint(chartRadius.angleOuter, angle.longitude);
    const label = polarPoint(chartRadius.angleLabel, angle.longitude);
    const angleText = `${angle.sign} ${formatDegree(angle.signDegree)}`;
    return `
      <g class="angle-node" data-astro-type="angle" data-astro-id="${escapeHtml(angle.id)}">
        <line class="angle-line ${angle.id}" x1="${inner.x}" y1="${inner.y}" x2="${outer.x}" y2="${outer.y}"></line>
        <text class="angle-label" x="${label.x}" y="${label.y}">
          <tspan x="${label.x}" dy="-0.35em">${escapeSvg(angle.label)}</tspan>
          <tspan class="angle-degree" x="${label.x}" dy="1.2em">${escapeSvg(angleText)}</tspan>
        </text>
      </g>
    `;
  }).join("");
  const aspectLines = snapshot.aspects.slice(0, 24).map((aspect) => {
    if (!isAspectVisible(aspect)) return "";
    const a = snapshot.bodies.find((body) => body.id === aspect.a);
    const b = snapshot.bodies.find((body) => body.id === aspect.b);
    if (!a || !b) return "";
    const pa = polarPoint(chartRadius.planet, a.longitude);
    const pb = polarPoint(chartRadius.planet, b.longitude);
    return `<line class="aspect-line ${aspect.aspect}" data-astro-type="aspect" data-astro-id="${escapeHtml(aspect.id)}" data-astro-a="${escapeHtml(aspect.a)}" data-astro-b="${escapeHtml(aspect.b)}" x1="${pa.x}" y1="${pa.y}" x2="${pb.x}" y2="${pb.y}"></line>`;
  }).join("");
  const planets = snapshot.bodies.map((body) => {
    if (!isBodyVisible(body.id)) return "";
    const point = polarPoint(chartRadius.planet, body.longitude);
    return `
      <g class="planet-node" data-astro-type="planet" data-astro-id="${escapeHtml(body.id)}">
        <circle cx="${point.x}" cy="${point.y}" r="18"></circle>
        <image href="${iconPath("planet", body.id)}" x="${point.x - 17}" y="${point.y - 17}" width="34" height="34"></image>
      </g>
    `;
  }).join("");

  return `
    <svg viewBox="${chartRadius.viewBox}" role="img" aria-label="Live astrology chart">
      ${timeMotion}
      <circle class="astro-ring outer" r="${chartRadius.outer}"></circle>
      <circle class="astro-ring zodiac" r="${chartRadius.zodiac}"></circle>
      <circle class="astro-ring middle" r="${chartRadius.middle}"></circle>
      <circle class="astro-ring inner" r="${chartRadius.inner}"></circle>
      <g>${signZones}</g>
      <g>${zodiacTicks}</g>
      <g>${houseLines}</g>
      <g>${aspectLines}</g>
      <g>${planets}</g>
      <g>${angleLines}</g>
      <g>${signLabels}</g>
      <text class="astro-center" y="-8">${escapeSvg(snapshot.moonPhase.name)}</text>
      <text class="astro-center sub" y="16">${escapeSvg(snapshot.houseSystem || "Placidus")}</text>
    </svg>
  `;
}

function buildTimeMotion(isLive = true) {
  const forwardTicks = Array.from({ length: 48 }, (_, index) => {
    const longitude = index * 7.5;
    const outer = polarPoint(index % 4 === 0 ? 340 : 334, longitude);
    const inner = polarPoint(index % 4 === 0 ? 324 : 328, longitude);
    return `<line x1="${outer.x}" y1="${outer.y}" x2="${inner.x}" y2="${inner.y}"></line>`;
  }).join("");
  const reverseTicks = Array.from({ length: 24 }, (_, index) => {
    const longitude = index * 15 + 4;
    const outer = polarPoint(index % 3 === 0 ? 300 : 294, longitude);
    const inner = polarPoint(index % 3 === 0 ? 284 : 288, longitude);
    return `<line x1="${outer.x}" y1="${outer.y}" x2="${inner.x}" y2="${inner.y}"></line>`;
  }).join("");
  const runeMarks = Array.from({ length: 24 }, (_, index) => {
    const point = polarPoint(306, index * 15 + 7.5);
    const mark = index % 3 === 0 ? "◇" : index % 3 === 1 ? "△" : "✦";
    return `<text x="${point.x}" y="${point.y}">${mark}</text>`;
  }).join("");
  const sigilLines = Array.from({ length: 6 }, (_, index) => {
    const a = polarPoint(156, index * 60);
    const b = polarPoint(156, index * 60 + 120);
    return `<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}"></line>`;
  }).join("");
  const spokeLines = Array.from({ length: 12 }, (_, index) => {
    const inner = polarPoint(228, index * 30);
    const outer = polarPoint(248, index * 30);
    return `<line x1="${inner.x}" y1="${inner.y}" x2="${outer.x}" y2="${outer.y}"></line>`;
  }).join("");

  const sigilAnimation = isLive ? `<animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="210s" repeatCount="indefinite"></animateTransform>` : "";
  const forwardAnimation = isLive ? `<animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="160s" repeatCount="indefinite"></animateTransform>` : "";
  const reverseAnimation = isLive ? `<animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="240s" repeatCount="indefinite"></animateTransform>` : "";
  const runeAnimation = isLive ? `<animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="300s" repeatCount="indefinite"></animateTransform>` : "";
  const spokeAnimation = isLive ? `<animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="120s" repeatCount="indefinite"></animateTransform>` : "";

  return `
    <g class="magic-layer magic-layer-sigil">
      <circle r="156"></circle>
      <polygon points="${polygonPoints(6, 156, -90)}"></polygon>
      <polygon points="${polygonPoints(6, 156, -60)}"></polygon>
      ${sigilLines}
      ${sigilAnimation}
    </g>
    <g class="time-dial time-dial-forward">
      <circle r="332"></circle>
      ${forwardTicks}
      <line class="time-pointer" x1="0" y1="-306" x2="0" y2="-340"></line>
      ${forwardAnimation}
    </g>
    <g class="time-dial time-dial-reverse">
      <circle r="292"></circle>
      ${reverseTicks}
      <line class="time-pointer faint" x1="0" y1="260" x2="0" y2="300"></line>
      ${reverseAnimation}
    </g>
    <g class="magic-layer magic-layer-runes">
      <circle r="306"></circle>
      ${runeMarks}
      ${runeAnimation}
    </g>
    <g class="magic-layer magic-layer-spokes">
      <circle r="238"></circle>
      ${spokeLines}
      ${spokeAnimation}
    </g>
  `;
}

function updateAstrologyFocus() {
  if (!state.astrology) return;
  const focus = resolveFocusedAstro(state.astrology);
  const activeFocus = state.hoveredAstro || state.pinnedAstro;
  const rows = document.querySelectorAll(".astro-row[data-astro-id]");
  const planets = elements.astroChart.querySelectorAll(".planet-node[data-astro-id]");
  const aspects = elements.astroChart.querySelectorAll(".aspect-line[data-astro-id]");
  const houses = elements.astroChart.querySelectorAll(".house-node[data-astro-id]");
  const angles = elements.astroChart.querySelectorAll(".angle-node[data-astro-id]");
  const zodiacs = elements.astroChart.querySelectorAll("[data-astro-type='zodiac'][data-astro-id]");

  rows.forEach((row) => {
    const active = Boolean(focus) && row.dataset.astroType === activeFocus.type && row.dataset.astroId === activeFocus.id;
    const pinned = Boolean(state.pinnedAstro) && row.dataset.astroType === state.pinnedAstro.type && row.dataset.astroId === state.pinnedAstro.id;
    row.classList.toggle("active", active);
    row.classList.toggle("pinned", pinned);
  });

  if (!focus) {
    planets.forEach((planet) => planet.classList.remove("active", "dim"));
    aspects.forEach((aspect) => aspect.classList.remove("active", "dim"));
    houses.forEach((house) => house.classList.remove("active", "dim"));
    angles.forEach((angle) => angle.classList.remove("active", "dim"));
    zodiacs.forEach((zodiac) => zodiac.classList.remove("active", "dim"));
    renderInsight(null);
    return;
  }

  houses.forEach((house) => {
    const active = focus.type === "house" && house.dataset.astroId === focus.value.id;
    house.classList.toggle("active", active);
    house.classList.toggle("dim", focus.type === "house" && !active);
  });
  angles.forEach((angle) => {
    const active = focus.type === "angle" && angle.dataset.astroId === focus.value.id;
    angle.classList.toggle("active", active);
    angle.classList.toggle("dim", focus.type === "angle" && !active);
  });
  zodiacs.forEach((zodiac) => {
    const active = focus.type === "zodiac" && zodiac.dataset.astroId === String(focus.value.index);
    zodiac.classList.toggle("active", active);
    zodiac.classList.toggle("dim", focus.type === "zodiac" && !active);
  });

  if (focus.type === "planet") {
    planets.forEach((planet) => {
      const active = planet.dataset.astroId === focus.value.id;
      planet.classList.toggle("active", active);
      planet.classList.toggle("dim", !active);
    });
    aspects.forEach((aspect) => {
      const related = aspect.dataset.astroA === focus.value.id || aspect.dataset.astroB === focus.value.id;
      aspect.classList.toggle("active", related);
      aspect.classList.toggle("dim", !related);
    });
  } else if (focus.type === "aspect") {
    planets.forEach((planet) => {
      const active = planet.dataset.astroId === focus.value.a || planet.dataset.astroId === focus.value.b;
      planet.classList.toggle("active", active);
      planet.classList.toggle("dim", !active);
    });
    aspects.forEach((aspect) => {
      const active = aspect.dataset.astroId === focus.value.id;
      aspect.classList.toggle("active", active);
      aspect.classList.toggle("dim", !active);
    });
  } else {
    planets.forEach((planet) => planet.classList.add("dim"));
    aspects.forEach((aspect) => aspect.classList.add("dim"));
  }

  renderInsight(focus);
}

function renderInsight(snapshot) {
  const hovered = snapshot?.note ? snapshot : resolveFocusedAstro(snapshot);
  if (!hovered) {
    elements.astroInsight.classList.remove("has-focus");
    elements.astroInsight.setAttribute("aria-hidden", "true");
    elements.astroInsight.innerHTML = "";
    return;
  }
  elements.astroInsight.classList.add("has-focus");
  elements.astroInsight.setAttribute("aria-hidden", "false");
  const note = hovered.note;
  elements.astroInsight.innerHTML = `
    <div class="insight-header">
      <div>
        <p class="eyebrow">Focus</p>
        <h3>${note.titleHtml || escapeHtml(note.title)}</h3>
      </div>
      <img class="insight-symbol" src="${escapeHtml(note.iconSrc)}" alt="">
    </div>
    <dl>
      <div><dt>当前状态</dt><dd>${escapeHtml(note.line1)}</dd></div>
      <div><dt>${escapeHtml(note.windowLabel || "时间窗口")}</dt><dd>${escapeHtml(note.line2)}</dd></div>
      ${note.extraRows ? note.extraRows.map((row) => `<div><dt>${escapeHtml(row.label)}</dt><dd>${escapeHtml(row.value)}</dd></div>`).join("") : ""}
      ${note.relatedLinks ? `<div><dt>相关相位</dt><dd>${formatRelatedLinks(note.relatedLinks)}</dd></div>` : ""}
      <div><dt>说明</dt><dd>${escapeHtml(note.line3)}</dd></div>
    </dl>
  `;
}

function resolveHoveredAstro(snapshot) {
  return resolveAstroReference(snapshot, state.hoveredAstro);
}

function resolveFocusedAstro(snapshot) {
  return resolveAstroReference(snapshot, state.hoveredAstro || state.pinnedAstro);
}

function resolveAstroReference(snapshot, reference) {
  if (!reference) return null;
  if (reference.type === "planet") {
    const body = snapshot.bodies.find((item) => item.id === reference.id);
    if (!body) return null;
    return {
      type: "planet",
      value: body,
      note: {
        title: body.name,
        iconSrc: iconPath("planet", body.id),
        line1: `${body.sign} ${formatDegree(body.signDegree)}${body.retrograde ? " 逆行" : ""}${body.precision === "approximate" ? " · 近似" : body.precision === "derived" ? " · 推导点" : ""}`,
        windowLabel: "星座停留",
        line2: `${formatRange(body.stateWindow)}`,
        extraRows: [
          {
            label: "落座含义",
            value: describePlanetPlacement(body)
          }
        ],
        line3: planetMeaning[body.id] || "当前行星状态。",
        relatedLinks: getBodyAspects(snapshot, body)
      }
    };
  }
  if (reference.type === "angle") {
    const angle = snapshot.angles?.find((item) => item.id === reference.id);
    if (!angle) return null;
    const info = angleInfo[angle.id] || { name: angle.label, line: "四轴描述星盘与地平线、天顶之间的关键交点。" };
    return {
      type: "angle",
      value: angle,
      note: {
        title: `${angle.label} · ${info.name}`,
        iconSrc: iconPath("zodiac", zodiacIcons[angle.signIndex] || "aries"),
        line1: `${angle.sign} ${formatDegree(angle.signDegree)}`,
        windowLabel: "轴点位置",
        line2: angle.direction || "地平线/子午线交点",
        line3: info.line
      }
    };
  }
  if (reference.type === "house") {
    const house = snapshot.houses?.find((item) => item.id === reference.id);
    if (!house) return null;
    return {
      type: "house",
      value: house,
      note: {
        title: `第 ${house.number} 宫`,
        iconSrc: iconPath("zodiac", zodiacIcons[house.signIndex] || "aries"),
        line1: `${house.sign} ${formatDegree(house.signDegree)}`,
        windowLabel: "宫头位置",
        line2: snapshot.houseSystem || "Placidus",
        line3: houseInfo[house.number - 1] || "宫位描述生命经验发生的领域。"
      }
    };
  }
  if (reference.type === "zodiac") {
    const index = Number(reference.id);
    const info = zodiacInfo[index];
    if (!info) return null;
    return {
      type: "zodiac",
      value: { index, ...info },
      note: {
        title: info.name,
        iconSrc: iconPath("zodiac", info.icon),
        line1: `${info.element} · ${info.modality}`,
        windowLabel: "黄道区间",
        line2: `${index * 30}° - ${(index + 1) * 30}°`,
        line3: info.line
      }
    };
  }
  const aspect = snapshot.aspects.find((item) => item.id === reference.id);
  if (!aspect) return null;
  return {
    type: "aspect",
    value: aspect,
    note: {
      title: `${aspect.aName} ${aspect.aspectLabel || aspect.aspect} ${aspect.bName}`,
      titleHtml: `<button class="inline-focus-link title-link" type="button" data-focus-type="planet" data-focus-id="${escapeHtml(aspect.a)}">${escapeHtml(aspect.aName)}</button><span>${escapeHtml(aspect.aspectLabel || aspect.aspect)}</span><button class="inline-focus-link title-link" type="button" data-focus-type="planet" data-focus-id="${escapeHtml(aspect.b)}">${escapeHtml(aspect.bName)}</button>`,
      iconSrc: iconPath("aspect", aspect.aspect),
      line1: `容许度 ${aspect.orb.toFixed(2)}°`,
      windowLabel: "相位窗口",
      line2: `${formatRange(aspect.window)}`,
      line3: aspectMeaning[aspect.aspect] || "当前相位状态。"
    }
  };
}

function getBodyAspects(snapshot, body) {
  return snapshot.aspects
    .filter((aspect) => isAspectVisible(aspect))
    .filter((aspect) => aspect.a === body.id || aspect.b === body.id)
    .slice(0, 6)
    .map((aspect) => {
      const otherName = aspect.a === body.id ? aspect.bName : aspect.aName;
      return {
        id: aspect.id,
        label: `${otherName} ${aspect.aspectLabel || aspect.aspect} · ${aspect.orb.toFixed(2)}°`
      };
    });
}

function formatRelatedLinks(links) {
  if (!links.length) return "当前主要相位列表中没有紧密连线。";
  return `<ul class="related-link-list">${links.map((link) => `
    <li>
      <button class="inline-focus-link related-link" type="button" data-focus-type="aspect" data-focus-id="${escapeHtml(link.id)}">${escapeHtml(link.label)}</button>
    </li>
  `).join("")}</ul>`;
}

function describePlanetPlacement(body) {
  const sign = zodiacInfo[body.signIndex];
  const planetTheme = planetPlacementThemes[body.id] || "这颗星体的主题";
  if (!sign) {
    return `${body.name}落在${body.sign}。\n星体主题：${planetTheme}。\n综合解读：这些主题会透过这个星座的方式表达。`;
  }
  return `${body.name}落在${sign.name}。\n星体主题：${planetTheme}。\n星座风格：${sign.element}、${sign.modality}。\n综合解读：这些主题会带有${sign.name}的表达方式，重点是${sign.line}`;
}

function angleDisplayName(id) {
  return angleInfo[id]?.name || id.toUpperCase();
}

function isAspectVisible(aspect) {
  return state.displayFilter.aspectLines
    && isBodyVisible(aspect.a)
    && isBodyVisible(aspect.b)
    && !state.displayFilter.hiddenAspectTypes.includes(aspect.aspect)
    && !state.displayFilter.hiddenAspectBodies.includes(aspect.a)
    && !state.displayFilter.hiddenAspectBodies.includes(aspect.b);
}

function isBodyVisible(id) {
  return Boolean(id) && !state.displayFilter.hiddenBodies.includes(id);
}

function loadChartHistory() {
  try {
    const raw = localStorage.getItem(historyStorageKey);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveChartHistory() {
  localStorage.setItem(historyStorageKey, JSON.stringify(state.history.slice(0, 8)));
}

function addChartHistory(query) {
  const entry = {
    id: query.id,
    query,
    savedAt: new Date().toISOString()
  };
  state.history = [entry, ...state.history.filter((item) => !sameChartQuery(item.query, query))].slice(0, 8);
  saveChartHistory();
  renderChartHistory();
}

function deleteChartHistory(id) {
  state.history = state.history.filter((entry) => entry.id !== id);
  if (state.chartQuery && !state.history.some((entry) => sameChartQuery(entry.query, state.chartQuery))) {
    state.chartQuery = null;
  }
  saveChartHistory();
  renderChartHistory();
}

function sameChartQuery(a, b) {
  return a.datetime === b.datetime
    && Number(a.lat).toFixed(4) === Number(b.lat).toFixed(4)
    && Number(a.lon).toFixed(4) === Number(b.lon).toFixed(4);
}

function renderChartHistory() {
  if (!state.history.length) {
    elements.chartHistoryList.innerHTML = `<div class="chart-history-empty">查询后会在这里保留最近记录。</div>`;
    return;
  }
  elements.chartHistoryList.innerHTML = state.history.map((entry) => {
    const query = entry.query;
    return `
      <button class="history-row" type="button" data-history-id="${escapeHtml(entry.id)}">
        <span class="history-title">${escapeHtml(query.label || "未命名地点")}</span>
        <span class="history-delete" role="button" tabindex="0" data-history-delete="${escapeHtml(entry.id)}" aria-label="删除这条历史星盘">×</span>
        <strong>${escapeHtml(formatDateTime(query.datetime))}</strong>
        <small>${escapeHtml(formatCoordinates(query.lat, query.lon))}</small>
      </button>
    `;
  }).join("");
}

function isHovered(type, id) {
  return state.hoveredAstro?.type === type && state.hoveredAstro?.id === id;
}

function iconPath(type, id) {
  if (type === "zodiac") return `${appBaseUrl}/assets/astro-icons/zodiac-${id}.png?${assetVersion}`;
  if (type === "aspect") return `${appBaseUrl}/assets/astro-icons/aspect-${aspectIconIds[id] || id}.png?${assetVersion}`;
  return `${appBaseUrl}/assets/astro-icons/planet-${planetIconIds[id] || id}.png?${assetVersion}`;
}

function polarPoint(radius, longitude) {
  const angle = (longitude - 90) * Math.PI / 180;
  return {
    x: Math.cos(angle) * radius,
    y: Math.sin(angle) * radius
  };
}

function polygonPoints(count, radius, offset = 0) {
  return Array.from({ length: count }, (_, index) => {
    const point = polarPoint(radius, offset + index * (360 / count));
    return `${point.x},${point.y}`;
  }).join(" ");
}

function normalizeChartLongitude(value) {
  return ((value % 360) + 360) % 360;
}

function angularDistance(a, b) {
  const diff = Math.abs(normalizeChartLongitude(a) - normalizeChartLongitude(b));
  return Math.min(diff, 360 - diff);
}

function distanceToRadialSegment(x, y, longitude, innerRadius, outerRadius) {
  const radius = Math.hypot(x, y);
  const pointLongitude = normalizeChartLongitude(Math.atan2(y, x) * 180 / Math.PI + 90);
  const radialDistance = radius < innerRadius ? innerRadius - radius : radius > outerRadius ? radius - outerRadius : 0;
  const arcDistance = Math.sin(angularDistance(pointLongitude, longitude) * Math.PI / 180) * Math.min(Math.max(radius, innerRadius), outerRadius);
  return Math.hypot(radialDistance, arcDistance);
}

function distanceToSegment(px, py, ax, ay, bx, by) {
  const dx = bx - ax;
  const dy = by - ay;
  const lengthSq = dx * dx + dy * dy;
  if (!lengthSq) return Math.hypot(px - ax, py - ay);
  const t = Math.max(0, Math.min(1, ((px - ax) * dx + (py - ay) * dy) / lengthSq));
  return Math.hypot(px - (ax + t * dx), py - (ay + t * dy));
}

function formatDegree(value) {
  const degree = Math.floor(value);
  const minute = Math.round((value - degree) * 60);
  return `${degree}°${String(minute).padStart(2, "0")}′`;
}

function englishSignName(signIndex) {
  return zodiacEnglishNames[Number(signIndex)] || "Zodiac";
}

function englishMoonPhase(phase) {
  const angle = Number(phase.angle);
  if (!Number.isFinite(angle)) return "Moon Phase";
  if (angle < 22.5 || angle >= 337.5) return "New Moon";
  if (angle < 67.5) return "Waxing Crescent";
  if (angle < 112.5) return "First Quarter";
  if (angle < 157.5) return "Waxing Gibbous";
  if (angle < 202.5) return "Full Moon";
  if (angle < 247.5) return "Waning Gibbous";
  if (angle < 292.5) return "Last Quarter";
  return "Waning Crescent";
}

function formatRange(window) {
  if (!window?.startsAt || !window?.endsAt) return "起止时间估算中";
  return `${formatDateTime(window.startsAt)} - ${formatDateTime(window.endsAt)}`;
}

function toDateTimeLocalValue(date) {
  const offsetMs = date.getTimezoneOffset() * 60_000;
  return new Date(date.getTime() - offsetMs).toISOString().slice(0, 16);
}

function formatCoordinates(lat, lon) {
  const latSuffix = lat >= 0 ? "N" : "S";
  const lonSuffix = lon >= 0 ? "E" : "W";
  return `${Math.abs(Number(lat)).toFixed(4)}°${latSuffix}, ${Math.abs(Number(lon)).toFixed(4)}°${lonSuffix}`;
}

function formatEnglishCoordinates(lat, lon) {
  const latSuffix = lat >= 0 ? "N" : "S";
  const lonSuffix = lon >= 0 ? "E" : "W";
  return `${Math.abs(Number(lat)).toFixed(4)}° ${latSuffix}, ${Math.abs(Number(lon)).toFixed(4)}° ${lonSuffix}`;
}

function formatEnglishDateTime(value) {
  return new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "short",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    timeZoneName: "short"
  }).format(new Date(value));
}

function formatDateTime(value) {
  return new Intl.DateTimeFormat("zh-Hans", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  }).format(new Date(value));
}

function formatShortDateTime(value) {
  return new Intl.DateTimeFormat("zh-Hans", {
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  }).format(new Date(value));
}

async function safeJson(response) {
  try {
    return await response.json();
  } catch {
    return null;
  }
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function escapeSvg(value) {
  return escapeHtml(value);
}

function registerServiceWorker() {
  if ("serviceWorker" in navigator && location.protocol !== "file:") {
    navigator.serviceWorker.register(`${appBaseUrl}/sw.js`).catch(() => {});
  }
}

function normalizeAppBaseUrl(value) {
  const base = String(value || ".").trim().replace(/\/+$/, "");
  return base || ".";
}
