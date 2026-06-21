(() => {
  const roots = document.querySelectorAll('[data-travel-globe-root]');

  if (!roots.length) {
    return;
  }

  const toNumber = (value) => Number.parseFloat(value) || 0;

  roots.forEach((root) => {
    const canvas = root.querySelector('[data-travel-globe-canvas]');
    const dataNode = root.querySelector('[data-travel-globe-data]');
    const tooltip = root.querySelector('[data-travel-globe-tooltip]');
    const listItems = Array.from(root.querySelectorAll('[data-travel-place-index]'));

    if (!canvas || !dataNode || !tooltip) {
      return;
    }

    let places = [];

    try {
      places = JSON.parse(dataNode.textContent || '[]').map((place, index) => ({
        ...place,
        index,
        lat: toNumber(place.lat),
        lon: toNumber(place.lon),
        visited: place.visited === true
      }));
    } catch (error) {
      console.warn('[travel-globe] invalid place data', error);
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
      centerLon: 82,
      lastTime: 0,
      pointerInside: false,
      highlightedIndex: null,
      projected: []
    };

    const getVar = (name, fallback) => {
      const value = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
      return value || fallback;
    };

    const colors = () => ({
      text: getVar('--heading-color', '#d8dee9'),
      muted: getVar('--text-muted-color', '#8f9baa'),
      border: getVar('--main-border-color', 'rgba(255,255,255,.14)'),
      accent: getVar('--link-color', '#58a6ff'),
      panel: getVar('--card-bg', '#11151b')
    });

    const resize = () => {
      const rect = canvas.getBoundingClientRect();
      state.dpr = Math.min(window.devicePixelRatio || 1, 2);
      state.width = Math.max(1, rect.width);
      state.height = Math.max(1, rect.height);
      canvas.width = Math.round(state.width * state.dpr);
      canvas.height = Math.round(state.height * state.dpr);
      ctx.setTransform(state.dpr, 0, 0, state.dpr, 0, 0);
      state.radius = Math.max(90, Math.min(state.width, state.height) * 0.39);
      state.cx = state.width * 0.5;
      state.cy = state.height * 0.5;
    };

    const project = (lat, lon) => {
      const phi = (lat * Math.PI) / 180;
      const lambda = ((lon - state.centerLon) * Math.PI) / 180;
      const cosPhi = Math.cos(phi);
      const x = cosPhi * Math.sin(lambda);
      const y = Math.sin(phi);
      const z = cosPhi * Math.cos(lambda);

      return {
        x: state.cx + x * state.radius,
        y: state.cy - y * state.radius,
        z,
        visible: z > -0.04
      };
    };

    const drawSegmentedLine = (points, color, alpha, width) => {
      ctx.save();
      ctx.strokeStyle = color;
      ctx.globalAlpha = alpha;
      ctx.lineWidth = width;
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

        drawSegmentedLine(points, palette.border, lat === 0 ? 0.36 : 0.2, lat === 0 ? 1.2 : 1);
      }

      for (let lon = -180; lon < 180; lon += 30) {
        const points = [];

        for (let lat = -84; lat <= 84; lat += 4) {
          points.push(project(lat, lon));
        }

        drawSegmentedLine(points, palette.border, 0.18, 1);
      }
    };

    const drawPoint = (point, place, palette) => {
      if (!point.visible) {
        return;
      }

      const isHighlighted = place.index === state.highlightedIndex;
      const baseRadius = place.visited ? 3.7 : 2.6;
      const radius = isHighlighted ? baseRadius + 2.4 : baseRadius;
      const color = place.visited ? palette.accent : palette.muted;

      ctx.save();
      ctx.globalAlpha = place.visited ? 0.96 : 0.42;
      ctx.fillStyle = color;
      ctx.shadowColor = color;
      ctx.shadowBlur = place.visited ? 12 : 0;
      ctx.beginPath();
      ctx.arc(point.x, point.y, radius, 0, Math.PI * 2);
      ctx.fill();

      if (place.visited || isHighlighted) {
        ctx.globalAlpha = isHighlighted ? 0.46 : 0.22;
        ctx.shadowBlur = 0;
        ctx.strokeStyle = color;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.arc(point.x, point.y, radius + 5.5, 0, Math.PI * 2);
        ctx.stroke();
      }

      ctx.restore();
    };

    const draw = (time = 0) => {
      const palette = colors();

      if (!state.pointerInside && !media.matches && state.lastTime) {
        state.centerLon = (state.centerLon + (time - state.lastTime) * 0.0045) % 360;
      }

      state.lastTime = time;
      ctx.clearRect(0, 0, state.width, state.height);

      const glow = ctx.createRadialGradient(state.cx, state.cy, state.radius * 0.12, state.cx, state.cy, state.radius * 1.12);
      glow.addColorStop(0, 'rgba(88, 166, 255, 0.12)');
      glow.addColorStop(0.54, 'rgba(88, 166, 255, 0.035)');
      glow.addColorStop(1, 'rgba(88, 166, 255, 0)');
      ctx.fillStyle = glow;
      ctx.fillRect(0, 0, state.width, state.height);

      ctx.save();
      ctx.beginPath();
      ctx.arc(state.cx, state.cy, state.radius, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(255, 255, 255, 0.022)';
      ctx.fill();
      ctx.strokeStyle = palette.border;
      ctx.globalAlpha = 0.74;
      ctx.lineWidth = 1;
      ctx.stroke();
      ctx.restore();

      drawGrid(palette);

      state.projected = places.map((place) => ({
        place,
        point: project(place.lat, place.lon)
      }));

      state.projected
        .slice()
        .sort((a, b) => a.point.z - b.point.z)
        .forEach(({ point, place }) => drawPoint(point, place, palette));

      requestAnimationFrame(draw);
    };

    const setTooltip = (place, point, clientX, clientY) => {
      if (!place || !point || !point.visible) {
        tooltip.hidden = true;
        return;
      }

      const rect = root.getBoundingClientRect();
      const x = Math.min(rect.width - 178, Math.max(12, clientX - rect.left + 14));
      const y = Math.min(rect.height - 86, Math.max(12, clientY - rect.top + 14));

      tooltip.style.setProperty('--travel-tooltip-x', `${x}px`);
      tooltip.style.setProperty('--travel-tooltip-y', `${y}px`);
      tooltip.querySelector('[data-travel-tooltip-name]').textContent = place.name;
      tooltip.querySelector('[data-travel-tooltip-region]').textContent = place.group || '未分组';
      tooltip.querySelector('[data-travel-tooltip-status]').textContent = place.visited ? '已去过' : '未标注';
      tooltip.querySelector('[data-travel-tooltip-coords]').textContent =
        `${Math.abs(place.lat).toFixed(1)}°${place.lat >= 0 ? 'N' : 'S'} / ${Math.abs(place.lon).toFixed(1)}°${place.lon >= 0 ? 'E' : 'W'}`;
      tooltip.hidden = false;
    };

    const clearListHighlight = () => {
      listItems.forEach((item) => item.classList.remove('is-active'));
    };

    const highlight = (index) => {
      state.highlightedIndex = index;
      clearListHighlight();

      if (index !== null) {
        const item = root.querySelector(`[data-travel-place-index="${index}"]`);
        item?.classList.add('is-active');
      }
    };

    const nearestPlace = (event) => {
      const rect = canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      let nearest = null;

      state.projected.forEach(({ place, point }) => {
        if (!point.visible) {
          return;
        }

        const dx = point.x - x;
        const dy = point.y - y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        const limit = place.visited ? 15 : 11;

        if (distance <= limit && (!nearest || distance < nearest.distance)) {
          nearest = { place, point, distance };
        }
      });

      return nearest;
    };

    canvas.addEventListener('mousemove', (event) => {
      state.pointerInside = true;
      const nearest = nearestPlace(event);

      if (!nearest) {
        highlight(null);
        tooltip.hidden = true;
        return;
      }

      highlight(nearest.place.index);
      setTooltip(nearest.place, nearest.point, event.clientX, event.clientY);
    });

    canvas.addEventListener('mouseleave', () => {
      state.pointerInside = false;
      highlight(null);
      tooltip.hidden = true;
    });

    listItems.forEach((item) => {
      const index = Number.parseInt(item.dataset.travelPlaceIndex || '', 10);

      item.addEventListener('mouseenter', () => {
        highlight(index);
      });

      item.addEventListener('mouseleave', () => {
        highlight(null);
      });
    });

    new ResizeObserver(() => {
      resize();
    }).observe(canvas);

    resize();
    requestAnimationFrame(draw);
  });
})();
