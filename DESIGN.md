---
version: 2.0
name: QuokkaGround-landing-design
description: "A software-craft dark studio landing in the Linear × Supabase lineage: a warm, green-tinted near-black canvas (#111310) layered with charcoal panels (#191d16 → #1e231b), hairline borders in warm off-white at 5–18% alpha, and a single chromatic event — the QuokkaGround green (#6fce3c) tuned for dark ground and applied only to CTAs (with near-black text, Supabase-style), the h1 em, focus rings, eyebrow markers, and a blinking terminal caret. Ink is warm off-white (#eceee7 → #767d6d). All type is IBM Plex Sans KR (400/500/700) — one family carrying display and body — with the system mono stack for labels, stats, and terminal details. Portfolio covers (colorful 480px Wishket cards) act as the page's jewelry against the dark panels. Four brightened signal colours (blue/green/amber/purple) categorise tech tags. Deep crisp shadows, a faint off-white dot-grid fading after the hero, no gradients as decoration. Single deliberate dark theme — no light mode."

colors:
  accent: "#6fce3c"
  accent-hover: "#83dc51"
  accent-text: "#8fdf63"           # AA-safe green for small text on dark
  on-accent: "#0d0f0b"             # near-black text on green CTAs (never white)
  accent-wash: "rgba(111,206,60,.09)"
  accent-line: "rgba(111,206,60,.3)"
  accent-glow: "rgba(111,206,60,.22)"
  ink: "#eceee7"
  ink-secondary: "#a8ae9f"
  ink-tertiary: "#767d6d"
  canvas: "#111310"                # warm near-black, green-tinted
  surface-subtle: "#151812"
  surface-panel: "#191d16"
  surface-panel-2: "#1e231b"
  hairline: "rgba(236,238,231,.09)"
  hairline-soft: "rgba(236,238,231,.055)"
  hairline-strong: "rgba(236,238,231,.18)"
  signal-mobile: "#6db3f2"
  signal-backend: "#8fdf63"
  signal-infra: "#e3b45c"
  signal-tool: "#c29bf2"

typography:
  family: IBM Plex Sans KR (400 / 500 / 700) — the only loaded family
  display:
    weight: 700
    letterSpacing: -0.02em … -0.04em
    usage: h1 hero (em in accent green), h2 section heads — tight, never all-caps
  body:
    weight: 400
    lineHeight: 1.65
    wordBreak: keep-all (Korean word-boundary wrapping, sitewide)
  mono:
    fontFamily: ui-monospace, SF Mono, Cascadia Mono, Roboto Mono, Menlo
    usage: eyebrows, stat labels, tech tags, terminal rows — small sizes only
  rules:
    - English micro-labels (YEARS EXP., SDK SHIPPED) are mono uppercase; Korean copy never uppercase.
    - Max weight is 700 (Plex KR has no 800).

rounded:
  sm: 8px
  md: 12px      # default card radius
  lg: 16px
  pill: 999px   # filter chips, nav CTA

elevation:
  sm: "0 1px 2px rgba(0,0,0,.3)"
  md: "0 8px 30px -12px rgba(0,0,0,.5)"
  lg: "0 24px 60px -20px rgba(0,0,0,.65)"   # card hover
  rules:
    - Shadows are deep and downward; glows are reserved for accent CTAs (accent-glow).
    - Hover = translateY(-6px) + shadow-lg + accent-line border, 300ms ease-out-expo.

atmosphere:
  - Fixed dot-grid (1px off-white dots at 5%, 26px cell) masked to fade out by 720px scroll.
  - Hero band sits on a marginally deeper green-tinted surface; sections alternate canvas / surface-subtle with hairline top borders.
  - The neon quokka mascot (green CRT glow) is native to this theme — frame it with soft rings, no border.
  - No gradients as decoration, no glassmorphism beyond the translucent nav blur.

components:
  nav: "Fixed top bar on rgba(17,19,16,.72) blur; hairline bottom on scroll; brand dot + wordmark, links centre, green pill CTA with near-black text."
  hero: "Centered column — ringed neon mascot, mono eyebrow with blinking '_' caret (caretBlink 1.1s steps), display h1 with accent em, sub, solid/ghost buttons, 3-stat strip over hairline."
  section-head: "Mono eyebrow (.sl) → display h2 → one-line sub; centered."
  portfolio-card: "Charcoal panel, square 480px WebP cover full-bleed (1.03 scale on hover), body: bold title as crawlable link, 2-line desc, signal-coloured mono tags, '상세 보기 →' affordance."
  portfolio-filter: "Two labeled chip rows (유형 / 분야); active chip = solid green with near-black text; counts in mono."
  project-modal: "Centered dialog (860px, full-screen mobile) over rgba(0,0,0,.62) blur: title bar + circular close, on-demand 1080px slides, page-link + contact CTA footer. Deep link #p=<slug>."
  process-step: "5-up grid of subtle panels — mono accent number, bold title, small desc; hover = accent wash."
  metric-tile: "4-up bordered row; huge 700-weight number with accent unit span, mono label, factual desc. Numbers must be verifiable — never borrowed prestige."
  terminal-card: "Profile card as terminal window — dots bar on panel-2, mono `// key` labels, right-aligned values; fully native to the dark theme."
  testimonial-card: "Star row (accent), quote, emoji avatar + anonymised role. No client names, no platform ratings."
  form: "Charcoal inputs on subtle surface, green focus ring, honeypot (.hp-field), required privacy consent (1-year retention wording), solid green submit with near-black text."

motion:
  - IntersectionObserver .reveal fade-up, 90ms sibling stagger, one-shot.
  - Hero caret blink is the only looping animation besides the mascot rings.
  - Compositor-friendly properties only; full prefers-reduced-motion collapse.

voice:
  - Korean first-person studio voice — 대표 개발자가 직접 만들고, 함께해 온 팀이 받친다 (no conditional clauses about team availability, no headcount).
  - Numbers only when verifiable against the resume (apps shipped, 3 SDKs, typical launch window, grand prize).
  - Project copy states exact scope honestly (e.g. "결제·보안 모듈 담당", never "앱 전체 개발").
