/* LW Lab · 交互脚本（无外部依赖）
   1. 移动端导航开合
   2. 合照轮播：自动滚动 + 手动切换
   3. Hero 徽标粒子动画：鼠标靠近粒子散开，移开后复原（参考 deepseek harness 鲸鱼效果）
*/
(function () {
  'use strict';

  /* ================= 移动端导航 ================= */

  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('siteNav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ================= 合照轮播 ================= */

  (function () {
    var gallery = document.getElementById('gallery');
    var track = document.getElementById('galleryTrack');
    if (!gallery || !track) return;

    var slides = track.querySelectorAll('img');
    var total = slides.length;
    if (!total) return;

    var dotsWrap = document.getElementById('galleryDots');
    var dots = [];
    for (var i = 0; i < total; i++) {
      var d = document.createElement('button');
      d.type = 'button';
      d.className = 'gallery-dot';
      d.setAttribute('aria-label', '切换到第 ' + (i + 1) + ' 张合影');
      dotsWrap.appendChild(d);
      dots.push(d);
      (function (idx) {
        d.addEventListener('click', function () { goTo(idx); poke(); });
      })(i);
    }

    var current = 0;
    var hovering = false;
    var lastInteract = 0;

    function updateDots() {
      for (var i = 0; i < total; i++) {
        dots[i].classList.toggle('active', i === current);
      }
    }

    function goTo(i) {
      current = (i % total + total) % total;
      track.scrollTo({ left: current * track.clientWidth, behavior: 'smooth' });
      updateDots();
    }

    // 手动操作后暂停自动播放 8 秒
    function poke() { lastInteract = Date.now(); }

    document.getElementById('galleryPrev').addEventListener('click', function () { goTo(current - 1); poke(); });
    document.getElementById('galleryNext').addEventListener('click', function () { goTo(current + 1); poke(); });

    gallery.addEventListener('pointerenter', function () { hovering = true; });
    gallery.addEventListener('pointerleave', function () { hovering = false; poke(); });
    track.addEventListener('touchstart', poke, { passive: true });
    track.addEventListener('scroll', function () {
      var idx = Math.round(track.scrollLeft / track.clientWidth);
      if (idx !== current && idx >= 0 && idx < total) {
        current = idx;
        updateDots();
      }
    }, { passive: true });

    updateDots();

    // 每隔几秒自动滚动到下一张
    setInterval(function () {
      if (hovering || document.hidden) return;
      if (Date.now() - lastInteract < 8000) return;
      goTo(current + 1);
    }, 4500);
  })();

  /* ================= Hero 徽标粒子动画 ================= */

  (function () {
    var hero = document.getElementById('home');
    var canvas = document.getElementById('heroCanvas');
    if (!hero || !canvas || !canvas.getContext) return;
    var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var lettering = document.getElementById('logoLettering');

    var ctx = canvas.getContext('2d');

    // 徽标以 data URI 内联：保证 file:// 打开时画布读取像素不被跨源污染
    var logo = new Image();
    var ready = false;
    logo.onload = function () { ready = true; rebuild(); };
    logo.src = 'data:image/jpeg;base64,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';

    var particles = [];
    var W = 0, H = 0, dpr = 1;
    var mouse = { x: -9999, y: -9999 };
    var RADIUS = 10, R2 = RADIUS * RADIUS, POWER = 6, SPRING = 0.02, FRICTION = 0.9;
    var raf = null;
    var visible = true;
    var t = 0;

    function resize() {
      // 画布只覆盖 Hero 左栏（粒子 + 文字所在区域）
      W = canvas.clientWidth || canvas.parentElement.clientWidth;
      H = canvas.clientHeight || canvas.parentElement.clientHeight;
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.round(W * dpr);
      canvas.height = Math.round(H * dpr);
      rebuild();
    }

    function rebuild() {
      if (!ready || !W || !H) return;
      particles = [];

      // 徽标显示尺寸：宽 ≤ 92% 左栏宽，高 ≤ 48% 左栏高（上限 460px），水平居中、中心位于 40% 高度处（下方留文字）
      var maxW = W * 0.92;
      var maxH = Math.min(H * 0.48, 460);
      var scale = Math.min(maxW / logo.width, maxH / logo.height);
      var w = logo.width * scale;
      var h = logo.height * scale;
      var ox = (W - w) / 2;
      var oy = H * 0.40 - h / 2;
      if (lettering) {
        lettering.style.left = ox + 'px';
        lettering.style.top = oy + 'px';
        lettering.style.width = w + 'px';
        lettering.style.fontSize = Math.max(21, Math.min(32, w / 8.5)) + 'px';
      }

      // 降采样读取像素：非白色的像素生成一个粒子
      var sw = Math.min(200, Math.max(40, Math.round(w)));
      var sh = Math.max(1, Math.round(sw * logo.height / logo.width));
      var off = document.createElement('canvas');
      off.width = sw;
      off.height = sh;
      var octx = off.getContext('2d');
      octx.drawImage(logo, 0, 0, sw, sh);
      var data;
      try {
        data = octx.getImageData(0, 0, sw, sh).data;
      } catch (e) {
        return; // 画布被污染时放弃动画，Hero 保持静态
      }

      var step = Math.max(2, Math.round(sw / 105));
      var size = Math.max(2, w / sw * step * 0.92);

      for (var y = 0; y < sh; y += step) {
        for (var x = 0; x < sw; x += step) {
          // 仅移除源徽标上方两行文字，保留原有图形、配色和粒子物理。
          var sourceX = x / sw * logo.width;
          var sourceY = y / sh * logo.height;
          if (sourceY < 32 || (sourceY < 58 && sourceX > 74 && sourceX < 128)) continue;
          var i = (y * sw + x) * 4;
          var r = data[i], g = data[i + 1], b = data[i + 2];
          if (0.299 * r + 0.587 * g + 0.114 * b > 232) continue; // 白底跳过
          particles.push({
            hx: ox + (x + step / 2) / sw * w + (Math.random() - 0.5) * 1.5,
            hy: oy + (y + step / 2) / sh * h + (Math.random() - 0.5) * 1.5,
            x: ox + (Math.random() - 0.5) * W * 0.8,
            y: oy + (Math.random() - 0.5) * H * 0.8,
            vx: 0, vy: 0,
            c: 'rgb(' + r + ',' + g + ',' + b + ')',
            ph: Math.random() * Math.PI * 2,
            s: size
          });
        }
      }
      if (reducedMotion) frame();
    }

    function frame() {
      if (!reducedMotion) raf = requestAnimationFrame(frame);
      if (!visible || document.hidden) return;
      t += 0.016;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < particles.length; i++) {
        var p = particles[i];
        if (reducedMotion) {
          ctx.fillStyle = p.c;
          ctx.fillRect(p.hx, p.hy, p.s, p.s);
          continue;
        }

        // 鼠标斥力：靠近则被推开
        var dx = p.x - mouse.x;
        var dy = p.y - mouse.y;
        var d2 = dx * dx + dy * dy;
        if (d2 < R2) {
          var d = Math.sqrt(d2) || 1;
          var f = (RADIUS - d) / RADIUS * POWER;
          p.vx += dx / d * f;
          p.vy += dy / d * f;
        }

        // 弹簧拉回平衡点（平衡点带缓慢浮动，保持呼吸感）
        var tx = p.hx + Math.sin(t * 0.8 + p.ph) * 1.5;
        var ty = p.hy + Math.cos(t * 0.6 + p.ph) * 1.5;
        p.vx += (tx - p.x) * SPRING;
        p.vy += (ty - p.y) * SPRING;
        p.vx *= FRICTION;
        p.vy *= FRICTION;
        p.x += p.vx;
        p.y += p.vy;

        ctx.fillStyle = p.c;
        ctx.fillRect(p.x, p.y, p.s, p.s);
      }
    }

    canvas.addEventListener('pointermove', function (e) {
      var rect = canvas.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
    });

    canvas.addEventListener('pointerleave', function () {
      mouse.x = -9999;
      mouse.y = -9999;
    });

    var resizeTimer;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(resize, 180);
    });

    // Hero 滚出视口时暂停绘制，节省 CPU
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        if (reducedMotion && visible) frame();
      }, { threshold: 0.02 }).observe(hero);
    }

    resize();
    if (!raf && !reducedMotion) raf = requestAnimationFrame(frame);
  })();

  /* ================= 首页"最新论文"展示卡 ================= */
  /* paper-card 内放多个 <article class="paper-slide"> 时自动轮播（7 秒/张）；
     只有一篇时保持静态。新文章按 index.html 中注释的指引添加。 */

  (function () {
    var card = document.getElementById('paperCard');
    if (!card) return;

    var slides = card.querySelectorAll('.paper-slide');
    if (slides.length < 2) return;

    var idx = 0;
    setInterval(function () {
      if (document.hidden) return;
      slides[idx].classList.remove('active');
      idx = (idx + 1) % slides.length;
      slides[idx].classList.add('active');
    }, 7000);
  })();

  /* ================= 导师柔光与清晰的徽标文字 ================= */
  (function () {
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var lettering = document.getElementById('logoLettering');
    if (!lettering || reduced) return;
    var letters = Array.prototype.slice.call(lettering.querySelectorAll('.logo-letter'));
    var colors = ['#e63946', '#ff7b00', '#f4c20d', '#2a9d3f', '#0089ff', '#8437e8', '#d81b8c'];
    var inView = true;
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        inView = entries[0].isIntersecting;
      }).observe(lettering);
    }
    function recolor(letter) {
      letter.style.color = colors[Math.floor(Math.random() * colors.length)];
    }
    // 只动鼠标所在的字母：无邻居水纹、无节流
    letters.forEach(function (letter) {
      letter.addEventListener('pointerenter', function () {
        if (!inView) return;
        recolor(letter);
        letter.getAnimations().forEach(function (animation) { animation.cancel(); });
        letter.animate([
          { transform: 'translate(0,0) rotate(0)' },
          { transform: 'translate(-4px,-8px) rotate(-18deg)', offset: 0.25 },
          { transform: 'translate(4px,3px) rotate(14deg)', offset: 0.55 },
          { transform: 'translate(0,0) rotate(0)' }
        ], { duration: 440, easing: 'ease-out' });
      });
    });
    setInterval(function () {
      if (document.hidden || !inView) return;
      recolor(letters[Math.floor(Math.random() * letters.length)]);
    }, 850);
  })();

})();
