---
version: 1.0
name: QuokkaGround-landing-design
description: "A warm-neutral, light-canvas freelance dev-studio landing built around layered near-white surfaces (#ffffff → #f0f1f2), a deep ink ramp (#14161a → #878d96), and the QuokkaGround brand green (#4a9e00) used as the single chromatic accent — tuned for AA contrast on white and applied only to CTAs, focus rings, eyebrow markers, and selection. The system reads as Linear-discipline calm with a sage tint (#f1f5ec) hero band and a fine fixed dot-grid atmosphere that fades out after 720px. Display type is Plus Jakarta Sans 600–800 with tight negative tracking over Noto Sans KR body; monospace details use the system mono stack. Cards are white panels with hairline borders, crisp small shadows, and 12px radius. Four muted signal colours (blue/green/amber/purple) categorise tech tags. No gradients as decoration, no dark mode — one intentional light theme."

colors:
  accent: "#4a9e00"
  accent-hover: "#5fb800"
  accent-text: "#3d8300"          # AA-safe green for text on white
  accent-wash: "rgba(74,158,0,.06)"
  accent-line: "rgba(74,158,0,.22)"
  accent-glow: "rgba(74,158,0,.16)"
  ink: "#14161a"
  ink-secondary: "#565b63"
  ink-tertiary: "#878d96"
  canvas: "#ffffff"
  surface-subtle: "#fafafa"
  surface-panel: "#f6f7f7"
  surface-panel-2: "#f0f1f2"
  surface-sage: "#f1f5ec"          # hero band tint
  hairline: "rgba(17,18,20,.08)"
  hairline-soft: "rgba(17,18,20,.05)"
  hairline-strong: "rgba(17,18,20,.16)"
  signal-mobile: "#1f74c4"         # tech-tag category: mobile/frontend
  signal-backend: "#3d8300"        # tech-tag category: backend
  signal-infra: "#b07400"          # tech-tag category: infra/devops
  signal-tool: "#7a37c9"           # tech-tag category: tools

typography:
  display:
    fontFamily: Plus Jakarta Sans, Noto Sans KR
    fontWeight: 700–800
    letterSpacing: -0.02em … -0.04em
    usage: h1 hero, h2 section heads — always tight, never all-caps
  body:
    fontFamily: Noto Sans KR
    fontWeight: 300–500
    lineHeight: 1.65
    usage: paragraphs, form labels, card descriptions
  mono:
    fontFamily: ui-monospace, SF Mono, Cascadia Mono, Roboto Mono, Menlo
    usage: eyebrows, stat labels, tech tags, terminal-card rows — small sizes (.72–.86rem) only
  rules:
    - Max two loaded font families (Jakarta Sans + Noto Sans KR); mono is system stack.
    - English micro-labels (YEARS EXP., APPS LIVE) are mono uppercase; Korean copy is never uppercase.

rounded:
  sm: 8px
  md: 12px      # default card radius
  lg: 16px
  pill: 999px   # filter chips, nav CTA

elevation:
  sm: "0 1px 2px rgba(17,18,20,.04)"          # resting cards
  md: "0 8px 30px -12px rgba(17,18,20,.16)"
  lg: "0 24px 60px -20px rgba(17,18,20,.22)"  # card hover
  rules:
    - Shadows are crisp and downward, never blurry halos.
    - Hover = translateY(-6px) + shadow-lg + accent-line border, 300ms ease-out-expo.

atmosphere:
  - Fixed dot-grid (radial-gradient 1px dots, 26px cell, 3.5% ink) masked to fade out by 720px scroll.
  - Sage band behind hero only; all other sections alternate white / surface-subtle with hairline top borders.
  - No decorative gradients, no glassmorphism, no dark sections.

components:
  nav: "Fixed top bar, hairline bottom border on scroll; brand dot + wordmark left, links centre, pill CTA right."
  hero: "Centered column — ringed mascot image (aspect 4/3, webp, preloaded), mono eyebrow with accent tick, display h1 with accent em, sub, two buttons (solid accent / ghost), 3-stat strip over hairline."
  section-head: "Mono eyebrow label (.sl) → display h2 → one-line sub (.ss); centered in most sections."
  portfolio-card: "White panel, square 480×480 webp cover full-bleed on top (object-fit cover, 1.03 scale on hover), 20px padded body: bold title, 2-line desc, mono tech tags in signal colours."
  portfolio-filter: "Pill chips above grid; active chip = solid accent with white text + aria-pressed; counts in mono."
  metric-tile: "4-up bordered grid row; huge display number with accent-tinted unit span, mono label, small desc."
  terminal-card: "About-side profile card styled as a terminal window — dots bar, mono `// key` labels, right-aligned values."
  testimonial-card: "Star row (accent), quote, emoji avatar + anonymised client role. No client names, no platform ratings."
  form: "Two-col name/email, textarea, honeypot (.hp-field, off-screen), consent checkbox (accent), solid accent submit. Submits to Make webhook."

motion:
  - IntersectionObserver .reveal fade-up, 90ms sibling stagger, one-shot.
  - Compositor-friendly properties only (transform, opacity); no auto-playing marquees.
  - Full prefers-reduced-motion override: animations/transitions collapse to ~0ms, reveals forced visible.

voice:
  - Korean first-person studio voice: "대표 개발자가 직접" — concrete deliverables over adjectives.
  - Numbers only when factual (years, shipped apps, SDKs, award); no vanity metrics.
  - Project copy states exact scope honestly (e.g. "결제·보안 모듈 담당", not "앱 전체 개발").
