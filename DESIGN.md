---
version: 3.1
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
  ink-tertiary: "#6f757e"          # 3.1: #878d96 은 대비 3.2:1 로 AA 미달 — 글자에는 쓰지 않는다
  hairline-ink: "#878d96"          # 구분선·장식 전용 (텍스트 금지)
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
  family: Pretendard Variable (dynamic subset via jsdelivr, weights 400/500/700 in use) — the only loaded family. Chosen for Korean body readability (wide hangul counters, balanced weight); replaced IBM Plex Sans KR which read thin/loose at body sizes.
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
    - Weights in use: 400/500/700 (variable font offers 45–920; stay at 700 for display).

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

page-order: hero → proof (지표 밴드) → portfolio → process → about → stack → testimonials → contact.
  3.1: 히어로 스탯과 프로세스 하단 met-row 가 같은 증거를 두 번 말하던 중복을 #proof 하나로 통합.
  Single contact CTA — no duplicate CTA band. 페이지의 주요 액션은 "프로젝트 문의" 하나(nav CTA·히어로 solid 버튼 동일).

readability:
  - Body 17px / 1.75 line-height; paragraphs capped at 62ch.
  - Containers cap at 1180px (1380px ≥1800px viewports, body 18px there).

atmosphere:
  - Fixed dot-grid (1px ink dots at 3.5%, 26px cell) masked to fade out by 720px scroll.
  - Hero band sits on the sage tint; sections alternate canvas / surface-subtle with hairline top borders.
  - The neon quokka mascot is framed with soft accent rings on the sage band.
  - Icons are inline stroke SVG only (20px grid, 1.6 weight, currentColor). 이모지 금지 — OS마다 렌더가 달라지고 색·크기를 맞출 수 없다.
  - No gradients as decoration, no glassmorphism beyond the translucent white nav blur.

components:
  nav: "Fixed top bar on rgba(255,255,255,.72) blur; hairline bottom on scroll; brand dot + wordmark, links centre, solid green CTA (3.1: wash pill → solid, 페이지 단일 주요 액션)."
  hero: "Two-column on desktop — left: mono eyebrow with blinking '_' caret, left-aligned display h1 (accent em), sub, solid CTA(문의)/ghost(포트폴리오), 응답 시간 한 줄(.hero-note), 출시작 커버 4장 가로 줄(.hero-proof, 165px — 커버는 글자가 그려진 480 정사각이라 그보다 작게 쓰면 읽히지 않는다); right: ringed neon mascot (clamp 250–440px).
    Collapses to LEFT-ALIGNED single column under 1000px, 마스코트는 제목 아래(3.1: order:-1 제거 — 첫 화면 맨 위는 제안이 차지). 600px 이하 버튼 전폭."
  section-head: "Mono eyebrow (.sl) → display h2 → one-line sub; centered."
  portfolio-card: "Charcoal panel, square 480px WebP cover full-bleed (1.03 scale on hover), body: 담당 범위 한 줄(.prole, KR sans — 한글이라 mono 금지), bold title as crawlable link, 2-line desc, signal-coloured tags, '상세 보기 →' affordance.
    카드 크기는 전부 동일 — 커버가 글자까지 그려진 정사각 이미지라 칸을 넓히면 그 글자가 잘린다. 대표작 확대·featured 배치 금지."
  portfolio-filter: "유형 = 칩 행(active = solid green). 분야 = 테두리 없는 글자 행(.pf-filter--dom, active = accent + underline) — 3.1: 칩 10개의 상단 크롬을 절반으로. counts in mono."
  project-modal: "Centered dialog (860px, full-screen mobile) over rgba(17,18,20,.55) blur: title bar + circular close, on-demand 1080px slides, page-link + contact CTA footer. Deep link #p=<slug>."
  process-step: "5-up grid of subtle panels — mono accent number, bold title, 한 문장 desc; hover = accent wash.
    섹션 헤드는 좌측 2단(.proc-head: 제목 / 리드) — 전 섹션이 가운데 정렬이라 리듬이 없던 문제. 통계는 가운데 박스가 아니라 accent 좌측 보더 각주 한 개(.proc-stat)."
  metric-tile: "4-up bordered row in #proof, 히어로 바로 아래 (2-col tablet, 1-col mobile); huge 700-weight number with accent unit span, mono label, factual desc.
    3.1: PROJECT RANGE(금액대) 제외 — 범위의 아래쪽이 기준점이 된다. GRAND PRIZE(2016) 제외 후 자기소개 배지로 이동 — 출시 지표와 같은 줄에 두면 나머지까지 옛날 실적으로 읽힌다.
    Numbers must be verifiable or owner-stated facts — never borrowed prestige."
  terminal-card: "Profile card as terminal window — dots bar on panel-2, mono `// key` labels, right-aligned values; the page's deliberate dark-identity moment."
  testimonial-card: "요약 한 줄(.tpull, 인용문에서 뽑은 구절 — 본문은 원문 유지), quote, SVG avatar + anonymised role.
    3.1: ★★★★★ 제거 — 4개가 모두 동일해 정보량이 0. 대표 후기 1개는 전폭(.tc-lead) + 3개. No client names, no platform ratings."
  form: "Subtle-surface inputs, green focus ring, honeypot (.hp-field), 동의는 한 줄 + <details> 전문(.consent-full) — 3.1: 보내기 직전 3줄 법률 문단이 가장 무겁던 문제. solid green submit."

motion:
  - IntersectionObserver .reveal fade-up, 90ms sibling stagger, one-shot.
  - Hero caret blink is the only looping animation besides the mascot rings.
  - Compositor-friendly properties only; full prefers-reduced-motion collapse.

voice:
  - Korean first-person studio voice — 대표 개발자가 직접 만들고, 함께해 온 팀이 받친다 (no conditional clauses about team availability, no headcount).
  - Numbers only when verifiable against the resume (apps shipped, 3 SDKs, typical launch window, grand prize).
  - Project copy states exact scope honestly (e.g. "결제·보안 모듈 담당", never "앱 전체 개발").
