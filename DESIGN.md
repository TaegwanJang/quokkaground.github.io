---
version: 3.0
name: QuokkaGround-landing-design
description: "A light warm-neutral studio landing (Linear discipline, Wise-calm) on layered near-white surfaces (#ffffff → #f0f1f2) with a sage hero band (#f1f5ec), a deep ink ramp (#14161a → #878d96), and a single chromatic event — the QuokkaGround green (#4a9e00, AA-tuned) on CTAs (white text), the h1 em, focus rings, eyebrow markers, and a blinking terminal caret. All type is IBM Plex Sans KR (400/500/700) with the system mono stack for labels, stats, and terminal details. Body sets at 17px/1.75 with word-break: keep-all; paragraphs cap at 62ch. Desktop hero is two-column (left-aligned copy / ringed neon mascot). Four muted signal colours categorise tech tags. Crisp small shadows, a faint ink dot-grid fading after the hero, no gradients as decoration. Light was chosen over dark deliberately: dense Korean sales copy reads better on light ground — dark identity lives on in the terminal profile card and mono details."

colors:
  accent: "#4a9e00"
  accent-hover: "#5fb800"
  accent-text: "#3d8300"           # AA-safe green for small text on white
  on-accent: "#ffffff"
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
  signal-mobile: "#1f74c4"
  signal-backend: "#3d8300"
  signal-infra: "#b07400"
  signal-tool: "#7a37c9"

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
    usage: Latin/digit-only labels — hero eyebrow, stat labels (YEARS EXP.), stack tags, terminal filename, step numbers, copyright. NEVER on Korean text (no Hangul glyphs → system-font fallback mixes typefaces); Korean labels/chips/buttons/terminal values use the KR sans.
  rules:
    - English micro-labels (YEARS EXP., SDK SHIPPED) are mono uppercase; Korean copy never uppercase.
    - Max weight is 700 (Plex KR has no 800).

rounded:
  sm: 8px
  md: 12px      # default card radius
  lg: 16px
  pill: 999px   # filter chips, nav CTA

elevation:
  sm: "0 1px 2px rgba(17,18,20,.04)"
  md: "0 8px 30px -12px rgba(17,18,20,.16)"
  lg: "0 24px 60px -20px rgba(17,18,20,.22)"   # card hover
  rules:
    - Shadows are crisp and downward, never blurry halos.
    - Hover = translateY(-6px) + shadow-lg + accent-line border, 300ms ease-out-expo.

page-order: hero → portfolio (proof first) → process → about → stack → testimonials → contact. Single contact CTA — no duplicate CTA band.

readability:
  - Body 17px / 1.75 line-height; paragraphs capped at 62ch.
  - Containers cap at 1180px (1380px ≥1800px viewports, body 18px there).

atmosphere:
  - Fixed dot-grid (1px ink dots at 3.5%, 26px cell) masked to fade out by 720px scroll.
  - Hero band sits on the sage tint; sections alternate canvas / surface-subtle with hairline top borders.
  - The neon quokka mascot is framed with soft accent rings on the sage band.
  - No gradients as decoration, no glassmorphism beyond the translucent white nav blur.

components:
  nav: "Fixed top bar on rgba(255,255,255,.72) blur; hairline bottom on scroll; brand dot + wordmark, links centre, green pill CTA."
  hero: "Two-column on desktop — left: mono eyebrow with blinking '_' caret, left-aligned display h1 (accent em), sub (max 36em), solid/ghost buttons, 3-stat strip; right: ringed neon mascot (clamp 250–440px). Collapses to centered single column under 1000px with mascot first."
  section-head: "Mono eyebrow (.sl) → display h2 → one-line sub; centered."
  portfolio-card: "Charcoal panel, square 480px WebP cover full-bleed (1.03 scale on hover), body: bold title as crawlable link, 2-line desc, signal-coloured mono tags, '상세 보기 →' affordance."
  portfolio-filter: "Two labeled chip rows (유형 / 분야); active chip = solid green with white text; counts in mono."
  project-modal: "Centered dialog (860px, full-screen mobile) over rgba(17,18,20,.55) blur: title bar + circular close, on-demand 1080px slides, page-link + contact CTA footer. Deep link #p=<slug>."
  process-step: "5-up grid of subtle panels — mono accent number, bold title, small desc; hover = accent wash."
  metric-tile: "5-up bordered row (2-col tablet, last tile full-width; 1-col mobile); huge 700-weight number with accent unit span, mono label, factual desc. Long ranges (150만~1.2억) use .mn-range at reduced size. Numbers must be verifiable or owner-stated facts — never borrowed prestige."
  terminal-card: "Profile card as terminal window — dots bar on panel-2, mono `// key` labels, right-aligned values; the page's deliberate dark-identity moment."
  testimonial-card: "Star row (accent), quote, emoji avatar + anonymised role. No client names, no platform ratings."
  form: "Subtle-surface inputs, green focus ring, honeypot (.hp-field), required privacy consent (1-year retention wording), solid green submit."

motion:
  - IntersectionObserver .reveal fade-up, 90ms sibling stagger, one-shot.
  - Hero caret blink is the only looping animation besides the mascot rings.
  - Compositor-friendly properties only; full prefers-reduced-motion collapse.

voice:
  - Korean first-person studio voice — 대표 개발자가 직접 만들고, 함께해 온 팀이 받친다 (no conditional clauses about team availability, no headcount).
  - Numbers only when verifiable against the resume (apps shipped, 3 SDKs, typical launch window, grand prize).
  - Project copy states exact scope honestly (e.g. "결제·보안 모듈 담당", never "앱 전체 개발").
