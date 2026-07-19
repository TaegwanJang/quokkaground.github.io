#!/usr/bin/env python3
"""work/<slug>/index.html 생성기.

소스: ../포트폴리오/<프로젝트>/2026-*.md (이 저장소 밖, 지원서 작성 워크스페이스).
확정 텍스트(복붙용 블록)만 사용하고 [확인 필요]/[추정] 표기 항목은 제외한다.
실행: LangdingPage 루트에서 `python3 tools/build-work-pages.py`
"""
import html
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent          # LangdingPage/
PORTF = ROOT.parent / '포트폴리오'
SITE = 'https://quokkaground.com'

# 랜딩 카드 순서와 동일. (slug, 포트폴리오 폴더, 카드 제목, 카테고리 라벨, 슬라이드 수)
PROJECTS = [
    ('emember', '이멤버', '이멤버 — 이랜드 통합 멤버십', '앱 개발', 2),
    ('yeoun', '여운', '여운 — 사주명리 AI 소개팅', '풀스택', 3),
    ('everyreels', 'Everyreels', 'Everyreels — 숏드라마 스트리밍', '앱 개발', 2),
    ('jieum', '지음', '지음 — 법률 기반 소개팅 풀스택', '풀스택', 2),
    ('saucesdk', 'SauceSDK', 'Sauce Live·Clip — 커머스 SDK', 'SDK·플러그인', 1),
    ('stipop', 'Stipop', 'Stipop — 스티커 Flutter SDK', 'SDK·플러그인', 2),
    ('momscode', 'MomsCode', 'MomsCode — 헬스케어 (캐나다 출시)', '앱 개발', 1),
    ('saucestudio', 'SauceStudio', 'SauceStudio — Native→Flutter 전환', '유지보수·전환', 2),
    ('isacfood', 'IsacFood', 'IsacFood — 구내식당 예약·평가', '앱 개발', 2),
    ('waterfarmers', 'WaterFarmers', 'WaterFarmers — 생태체험 교육 앱', '앱 개발', 3),
    ('vine', '바인', '바인 — 크리스천 데이팅', '풀스택', 2),
    ('sauceclip', 'SauceClip영상편집', 'SauceClip — 숏폼 영상 편집앱', '앱 개발', 2),
    ('langdy', 'Langdy', '랭디 — 1:1 매칭 교육 앱', '앱 개발', 2),
    ('cabinet', 'Cabinet', 'Cabinet — 소셜 지도 앱', '앱 개발', 5),
    ('minusplus', '마이너스플러스', '마이너스플러스 — 체성분 관리', '앱 개발', 1),
    ('smartbible', '성경과찬송가', '스마트 성경과찬송가 — 음원 구독', '유지보수·전환', 3),
    ('photomon', '포토몬', '포토몬 — Target SDK 정책 대응', '유지보수·전환', 2),
    ('myhealthnote', '마이헬스노트', '마이헬스노트 — 당뇨 관리 iOS', '유지보수·전환', 1),
]

URL_ALLOW = ('apps.apple.com', 'play.google.com', 'pub.dev', 'github.com')
URL_LABEL = {
    'apps.apple.com': 'App Store에서 보기',
    'play.google.com': 'Google Play에서 보기',
    'pub.dev': 'pub.dev 패키지 보기',
    'github.com': 'GitHub 저장소 보기',
}


def nfc(s):
    return unicodedata.normalize('NFC', s)


def find_md(folder_name):
    for d in PORTF.iterdir():
        if nfc(d.name) == folder_name:
            for f in sorted(d.iterdir()):
                if nfc(f.name).startswith('2026-') and f.suffix == '.md':
                    return f.read_text()
    raise FileNotFoundError(folder_name)


def fenced_after(text, heading_pat):
    """heading_pat(정규식)에 매치되는 줄 이후 첫 ``` 블록 내용."""
    m = re.search(heading_pat, text, re.M)
    if not m:
        return ''
    rest = text[m.end():]
    fm = re.search(r'```\n(.*?)```', rest, re.S)
    return fm.group(1).strip() if fm else ''


def parse_detail(detail):
    """'n) 제목' 단위로 나눠 (제목, [불릿]) 목록. 들여쓴 연속줄은 앞 불릿에 병합."""
    out = []
    cur_title, cur_items = None, []
    for line in detail.splitlines():
        h = re.match(r'^\d\)\s*(.+)$', line)
        if h:
            if cur_title:
                out.append((cur_title, cur_items))
            cur_title, cur_items = h.group(1).strip(), []
        elif line.startswith('- '):
            cur_items.append(line[2:].strip())
        elif line.startswith('  ') and cur_items:
            cur_items[-1] += ' ' + line.strip()
    if cur_title:
        out.append((cur_title, cur_items))
    return out


def parse_achievements(block):
    pairs, name = [], None
    for line in block.splitlines():
        m = re.match(r'^\[성과명\]\s*(.+)$', line)
        d = re.match(r'^\[설명\]\s*(.+)$', line)
        if m:
            name = m.group(1).strip()
        elif d and name:
            if '확인 필요' not in name and '확인 필요' not in d.group(1):
                pairs.append((name, d.group(1).strip()))
            name = None
    return pairs


def parse_period(text):
    m = re.search(r'참여 기간[:：]?\s*\*\*([^*]+)\*\*', text)
    if m and '확인' not in m.group(1):
        return m.group(1).strip()
    return ''


def result_urls(text):
    m = re.search(r'^## 9\..*$', text, re.M)
    if not m:
        return []
    urls, seen = [], set()
    for u in re.findall(r'https://[^\s)»`\'"<>]+', text[m.end():]):
        u = u.rstrip('.,')
        host = u.split('/')[2]
        key = next((a for a in URL_ALLOW if host.endswith(a)), None)
        if key and u not in seen:
            seen.add(u)
            urls.append((URL_LABEL[key], u))
    return urls


def e(s):
    return html.escape(s, quote=True)


CSS = '''*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#fff;--bg-subtle:#fafafa;--ink:#14161a;--ink-2:#565b63;--ink-3:#878d96;
--line:rgba(17,18,20,.08);--line-2:rgba(17,18,20,.05);--acc:#4a9e00;--acc-text:#3d8300;
--acc-wash:rgba(74,158,0,.06);--acc-line:rgba(74,158,0,.22);--r:12px;--r-sm:8px;
--fh:'IBM Plex Sans KR',sans-serif;--fb:'IBM Plex Sans KR',sans-serif;
--fm:ui-monospace,'SF Mono',Menlo,monospace;
--sh-sm:0 1px 2px rgba(17,18,20,.04)}
body{background:var(--bg);color:var(--ink);font-family:var(--fb);line-height:1.7;-webkit-font-smoothing:antialiased;word-break:keep-all;overflow-wrap:break-word}
a{color:var(--acc-text)}
nav{display:flex;justify-content:space-between;align-items:center;padding:16px 24px;border-bottom:1px solid var(--line-2);
position:sticky;top:0;background:rgba(255,255,255,.92);backdrop-filter:blur(8px);z-index:10}
nav .brand{display:flex;align-items:center;gap:8px;font-family:var(--fh);font-weight:700;color:var(--ink);text-decoration:none;font-size:.95rem}
nav .brand i{width:8px;height:8px;border-radius:50%;background:var(--acc)}
nav .cta{font-size:.86rem;font-weight:500;color:#fff;background:var(--acc);padding:8px 16px;border-radius:999px;text-decoration:none}
main{max-width:800px;margin:0 auto;padding:48px 20px 80px}
.crumb{font-size:.8rem;color:var(--ink-3);margin-bottom:20px}
.crumb a{color:var(--ink-3);text-decoration:none}
.crumb a:hover{color:var(--acc-text)}
.eyebrow{font-family:var(--fm);font-size:.74rem;letter-spacing:.12em;color:var(--acc-text);margin-bottom:12px}
h1{font-family:var(--fh);font-size:clamp(1.5rem,3.4vw,2.1rem);letter-spacing:-.02em;line-height:1.3;margin-bottom:14px;text-wrap:balance}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 8px}
.tag{font-family:var(--fm);font-size:.74rem;padding:5px 11px;border-radius:6px;border:1px solid var(--line);color:var(--ink-2);background:var(--bg-subtle)}
.period{font-size:.85rem;color:var(--ink-3);margin-bottom:26px}
.links{display:flex;flex-wrap:wrap;gap:10px;margin:6px 0 30px}
.links a{font-size:.86rem;font-weight:500;border:1px solid var(--acc-line);border-radius:999px;padding:8px 16px;text-decoration:none;background:var(--acc-wash)}
h2{font-family:var(--fh);font-size:1.12rem;letter-spacing:-.01em;margin:38px 0 12px}
ul{padding-left:20px;display:grid;gap:6px;font-size:.94rem;color:var(--ink-2)}
ul li::marker{color:var(--acc)}
figure{margin:16px 0}
figure img{width:100%;height:auto;border:1px solid var(--line-2);border-radius:var(--r);display:block;box-shadow:var(--sh-sm)}
.ach{display:grid;gap:12px;margin-top:6px}
.ach div{background:var(--bg-subtle);border:1px solid var(--line);border-radius:var(--r);padding:16px 18px}
.ach b{display:block;font-size:.94rem;margin-bottom:4px}
.ach p{font-size:.88rem;color:var(--ink-2)}
.cta-box{margin-top:52px;text-align:center;background:var(--acc-wash);border:1px solid var(--acc-line);border-radius:var(--r);padding:34px 20px}
.cta-box p{color:var(--ink-2);font-size:.94rem;margin-bottom:16px}
.cta-box a{display:inline-block;background:var(--acc);color:#fff;font-weight:600;text-decoration:none;padding:12px 26px;border-radius:999px}
.pn-nav{display:flex;justify-content:space-between;gap:12px;margin-top:40px;font-size:.88rem}
.pn-nav a{text-decoration:none;color:var(--ink-2);border:1px solid var(--line);border-radius:var(--r-sm);padding:12px 16px;flex:1;max-width:48%}
.pn-nav a:hover{border-color:var(--acc-line);color:var(--acc-text)}
footer{border-top:1px solid var(--line-2);padding:28px 24px;text-align:center;font-size:.8rem;color:var(--ink-3)}
footer a{color:var(--ink-3)}'''


def build_page(idx, slug, folder, card_title, cat, slides):
    text = find_md(folder)
    title = fenced_after(text, r'^## 1\.')
    detail = fenced_after(text, r'^## 5\.')
    background = fenced_after(text, r'^### 6-1\.')
    ach = parse_achievements(fenced_after(text, r'^### 6-2\.'))
    tech = fenced_after(text, r'^## 4\.')
    period = parse_period(text)
    urls = result_urls(text)

    sections = parse_detail(detail)
    desc = ''
    for t, items in sections:
        if items:
            desc = items[0]
            break

    tech_tags = [t.strip() for t in tech.split(',') if t.strip()][:10]

    body_sections = ''.join(
        f'<h2>{e(t)}</h2>\n<ul>' + ''.join(f'<li>{e(i)}</li>' for i in items) + '</ul>\n'
        for t, items in sections if items
    )
    bg_sections = ''.join(
        f'<h2>{e(t)}</h2>\n<ul>' + ''.join(f'<li>{e(i)}</li>' for i in items) + '</ul>\n'
        for t, items in parse_detail(background) if items
    )
    slide_figs = ''.join(
        f'<figure><img src="../../pf/d/{slug}-{i:02d}.webp" alt="{e(card_title)} 상세 이미지 {i}" '
        f'width="1080" loading="lazy" decoding="async" /></figure>\n'
        for i in range(1, slides + 1)
    )
    ach_html = ''
    if ach:
        ach_html = '<h2>프로젝트 성과</h2>\n<div class="ach">' + ''.join(
            f'<div><b>{e(n)}</b><p>{e(d)}</p></div>' for n, d in ach) + '</div>\n'
    links_html = ''
    if urls:
        links_html = '<div class="links">' + ''.join(
            f'<a href="{e(u)}" target="_blank" rel="noopener">{e(l)} ↗</a>' for l, u in urls) + '</div>'

    prev_p = PROJECTS[idx - 1]
    next_p = PROJECTS[(idx + 1) % len(PROJECTS)]
    canonical = f'{SITE}/work/{slug}/'

    jsonld = f'''{{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": {title!r},
  "description": {desc!r},
  "url": "{canonical}",
  "image": "{SITE}/pf/{slug}.webp",
  "inLanguage": "ko",
  "author": {{"@type": "Person", "name": "장태관", "jobTitle": "대표 개발자"}},
  "publisher": {{"@type": "Organization", "name": "QuokkaGround", "url": "{SITE}/"}}
}}'''.replace("'", '"') if False else None
    # json은 수동 구성(따옴표 이슈 회피)
    import json
    jsonld = json.dumps({
        '@context': 'https://schema.org', '@type': 'CreativeWork',
        'name': title, 'description': desc, 'url': canonical,
        'image': f'{SITE}/pf/{slug}.webp', 'inLanguage': 'ko',
        'author': {'@type': 'Person', 'name': '장태관', 'jobTitle': '대표 개발자'},
        'publisher': {'@type': 'Organization', 'name': 'QuokkaGround', 'url': SITE + '/'},
    }, ensure_ascii=False, indent=2)
    breadcrumb = json.dumps({
        '@context': 'https://schema.org', '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'QuokkaGround', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': '포트폴리오', 'item': SITE + '/#portfolio'},
            {'@type': 'ListItem', 'position': 3, 'name': card_title, 'item': canonical},
        ],
    }, ensure_ascii=False, indent=2)

    page = f'''<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1.0" />
  <title>{e(title)} | QuokkaGround</title>
  <meta name="description" content="{e(desc)}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{canonical}" />
  <meta name="theme-color" content="#4a9e00" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:site_name" content="QuokkaGround" />
  <meta property="og:title" content="{e(title)}" />
  <meta property="og:description" content="{e(desc)}" />
  <meta property="og:image" content="{SITE}/pf/{slug}.webp" />
  <meta property="og:locale" content="ko_KR" />
  <meta name="twitter:card" content="summary" />
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="apple-touch-icon" href="/favicon-192x192.png">
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet" />
  <script type="application/ld+json">
{jsonld}
  </script>
  <script type="application/ld+json">
{breadcrumb}
  </script>
  <style>{CSS}</style>
</head>

<body>
  <nav aria-label="주요 메뉴">
    <a href="../../" class="brand"><i aria-hidden="true"></i>QuokkaGround</a>
    <a href="../../#contact" class="cta">프로젝트 문의</a>
  </nav>
  <main>
    <p class="crumb"><a href="../../">홈</a> / <a href="../../#portfolio">포트폴리오</a> / {e(card_title)}</p>
    <p class="eyebrow">{e(cat)}</p>
    <h1>{e(title)}</h1>
    <div class="meta">{''.join(f'<span class="tag">{e(t)}</span>' for t in tech_tags)}</div>
    {f'<p class="period">참여 기간 · {e(period)}</p>' if period else ''}
    {links_html}
    {slide_figs}
    {body_sections}
    {bg_sections}
    {ach_html}
    <div class="cta-box">
      <p>비슷한 프로젝트를 계획 중이신가요? 아이디어 단계여도 괜찮습니다.</p>
      <a href="../../#contact">프로젝트 문의하기 →</a>
    </div>
    <nav class="pn-nav" aria-label="다른 프로젝트">
      <a href="../{prev_p[0]}/" rel="prev">← {e(prev_p[2])}</a>
      <a href="../{next_p[0]}/" rel="next">{e(next_p[2])} →</a>
    </nav>
  </main>
  <footer>
    <a href="../../">QuokkaGround</a> — 모바일 앱·웹·백엔드 풀스택 개발팀 · <a href="../../#portfolio">전체 포트폴리오</a>
  </footer>
</body>

</html>
'''
    out = ROOT / 'work' / slug / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    return title, desc


if __name__ == '__main__':
    for i, (slug, folder, card_title, cat, slides) in enumerate(PROJECTS):
        t, d = build_page(i, slug, folder, card_title, cat, slides)
        print(f'{slug:14s} {t[:46]}')
    print(f'\n{len(PROJECTS)} pages → work/<slug>/index.html')
