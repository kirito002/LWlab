#!/usr/bin/env python3
"""将 website-content.json 同步到静态 HTML。仅使用 Python 标准库；--check 检查是否同步。"""
import hashlib
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'website-content.json'


def esc(value):
    return html.escape(str(value), quote=True)


def rich(text):
    """内容只支持 **加粗**；HTML 按普通文字转义。"""
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', esc(text))


def paragraphs(items):
    return '\n'.join('<p>' + rich(x) + '</p>' for x in items)


def photo(path, name, cls='photo'):
    return (f'<div class="{cls}"><span class="photo-fallback" aria-hidden="true">{esc(name[0])}</span>'
            f'<img src="{esc(path)}" alt="{esc(name)}" loading="lazy" onerror="this.style.display=\'none\'"></div>')


def section(key, title, english, body, alternate=False):
    return (f'<section class="section{" section-alt" if alternate else ""}" id="{key}">\n'
            f'  <div class="container">\n<h2 class="section-title">{title} '
            f'<span class="section-title-en">{english}</span></h2>\n{body}\n  </div>\n</section>')


def replace_once(text, pattern, replacement):
    result, count = re.subn(pattern, lambda _: replacement, text, flags=re.S)
    if count != 1:
        raise ValueError(f'预期一个页面区域，实际 {count} 个：{pattern}')
    return result


def faculty_card(person):
    facts = [('研究方向', person['field']), ('实验室位置', person['office'])]
    body = '\n'.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in facts)
    body += (f'<div><dt>Email</dt><dd><a class="link" href="mailto:{esc(person["email"])}">'
             f'{esc(person["email"])}</a></dd></div>')
    groups = []
    for group in person['sections']:
        items = ''.join(f'<li>{rich(x)}</li>' for x in group['items'])
        groups.append(f'<div class="faculty-block"><h4>{esc(group["title"])}</h4><ul>{items}</ul></div>')
    return (f'<article class="faculty-profile faculty-{esc(person["theme"])}" id="{esc(person["id"])}" '
            f'tabindex="0" aria-labelledby="{esc(person["id"])}-name">\n'
            f'<div class="faculty-head">{photo(person["photo"], person["name"], "faculty-photo")}'
            f'<div class="faculty-meta"><p class="faculty-role">Principal Investigator</p>'
            f'<h3 class="faculty-name" id="{esc(person["id"])}-name">{esc(person["name"])}</h3>'
            f'<p class="faculty-en">{esc(person["english"])} · {esc(person["title"])}</p></div></div>'
            f'<ul class="faculty-affiliations">' + ''.join(f'<li>{esc(x)}</li>' for x in person['affiliations']) + '</ul>'
            f'<dl class="faculty-facts">{body}</dl><p class="faculty-summary">{esc(person["summary"])}</p>'
            f'<div class="faculty-body">{"".join(groups)}</div>'
            '<p class="faculty-publications"><a class="link" href="publication.html">发表论文 →</a></p></article>')


def render(data, home, pubs):
    site = data['site']
    hero = ('<div class="hero-text">' + f'<h1 class="hero-title">{esc(site["name"])}</h1>'
            f'<p class="hero-sub">{esc(site["subtitle"])}</p><p class="hero-intro">{esc(site["intro"])}</p></div>')
    home = replace_once(home, r'<div class="hero-text">.*?</div>', hero)
    words = ''.join('<span class="logo-word">' + ''.join(f'<span class="logo-letter" aria-hidden="true">{esc(c)}</span>' for c in word) + '</span>' for word in site['logo_text'].split())
    lettering = f'<div class="logo-lettering" id="logoLettering" role="img" aria-label="{esc(site["logo_text"])}">{words}</div>'
    if 'id="logoLettering"' in home:
        home = replace_once(home, r'<div class="logo-lettering".*?</div>', lettering)
    else:
        home = home.replace('</canvas>', '</canvas>\n' + lettering, 1)
    papers = []
    for i, paper in enumerate(data['latest_publications']):
        papers.append(f'<article class="paper-slide{" active" if i == 0 else ""}">'
                      f'<a class="paper-fig" href="publication.html" aria-label="查看论文列表"><img src="{esc(paper["image"])}" alt="{esc(paper["alt"])}"></a>'
                      f'<div class="paper-info"><p class="paper-title">{esc(paper["title"])}</p>'
                      f'<p class="paper-meta">{rich(paper["meta"])}</p></div></article>')
    home = replace_once(home, r'<aside class="hero-right">.*?</aside>', '<aside class="hero-right"><p class="hero-paper-label">Latest Publication · 最新发表</p><div class="paper-card" id="paperCard">' + ''.join(papers) + '</div></aside>')
    gallery = ('<h3 class="people-group-title">实验室合影 Group Photos</h3><div class="gallery" id="gallery">'
               '<div class="gallery-track" id="galleryTrack">' + ''.join(f'<img src="{esc(p["image"])}" alt="{esc(p["alt"])}" draggable="false">' for p in data['group_photos']) + '</div>'
               '<button class="gallery-btn gallery-prev" id="galleryPrev" aria-label="上一张">‹</button>'
               '<button class="gallery-btn gallery-next" id="galleryNext" aria-label="下一张">›</button>'
               '<div class="gallery-dots" id="galleryDots" role="group" aria-label="合影切换"></div></div>')
    research = '<div class="research-grid">' + ''.join(f'<article class="research-card"><h3><img src="{esc(r["icon"])}" alt="" aria-hidden="true">{esc(r["title"])}</h3><p>{esc(r["text"])}</p></article>' for r in data['research']) + '</div>'
    people = '<h3 class="people-group-title">导师 Faculty</h3><div class="faculty-grid">' + ''.join(faculty_card(p) for p in data['faculty']) + '</div>'
    for group in data['people']:
        people += f'<h3 class="people-group-title">{esc(group["title"])}</h3><div class="people-grid">'
        for p in group['members']:
            people += '<div class="person">' + photo(p['photo'], p['name']) + f'<p class="person-name">{esc(p["name"])}</p><p class="person-sub">{esc(p["english"])} · {esc(group["role"])}</p></div>'
        people += '</div>'
    news = '<ul class="news-list">'
    for n in sorted(data['news'], key=lambda x: x['date'], reverse=True):
        detail = rich(n.get('detail', ''))
        if n.get('url'):
            if not n['url'].startswith('https://'):
                raise ValueError('新闻链接必须使用 https://')
            detail += f' <a class="link" href="{esc(n["url"])}" target="_blank" rel="noopener">{esc(n["link_label"])}</a>'
        figure = ''
        if n.get('image'):
            caption = n.get('image_caption', '')
            alt = n.get('image_alt') or caption or '新闻配图'
            figure = ('<figure class="news-figure"><button class="news-thumb" type="button" '
                      f'data-lightbox-src="{esc(n["image"])}" aria-label="放大查看配图">'
                      f'<img src="{esc(n["image"])}" alt="{esc(alt)}" loading="lazy"></button>'
                      + (f'<figcaption>{esc(caption)}</figcaption>' if caption else '') + '</figure>')
        news += (f'<li class="news-item"><time class="news-date" datetime="{esc(n["date"])}">{esc(n["date"])}</time>'
                 f'<div class="news-text"><p class="news-title">{rich(n["title"])}</p>'
                 + (f'<p class="news-detail">{detail}</p>' if detail else '') + figure + '</div></li>')
    news += '</ul><p class="news-more"><a class="link" href="publication.html">查看实验室全部发表论文 →</a></p>'
    join = '<div class="section-body">' + paragraphs(data['join']['paragraphs']) + f'<p>联系邮箱：<a class="link" href="mailto:{esc(data["join"]["email"])}">{esc(data["join"]["email"])}</a><br>实验室位置：{esc(data["join"]["address"])}</p></div>'
    sections = {
        'about': section('about', '关于', 'About', '<div class="section-body">' + paragraphs(data['about']) + '</div>' + gallery),
        'research': section('research', '研究', 'Research', research, True),
        'people': section('people', '团队', 'People', people),
        'news': section('news', '新闻', 'News', news, True),
        'join': section('join', '加入我们', 'Join Us', join),
    }
    for key, value in sections.items():
        home = replace_once(home, rf'<section\b[^>]*\bid="{key}"[^>]*>.*?</section>', value)
    bibliography = '<h2 class="section-title">发表论文 <span class="section-title-en">Publications</span></h2>'
    bibliography += f'<p class="pub-note">{esc(data["publication_note"])}</p>'
    for group in sorted(data['publications'], key=lambda x: x['year'], reverse=True):
        bibliography += f'<h3 class="pub-year">{group["year"]}</h3><ol class="pub-list">' + ''.join(f'<li>{rich(t)}</li>' for t in group['entries']) + '</ol>'
    pubs = replace_once(pubs, r'<section class="pub-page">.*?</section>', '<section class="pub-page"><div class="container">' + bibliography + '</div></section>')
    footer = f'<footer class="site-footer"><div class="container"><p>{esc(site["footer"])}</p></div></footer>'
    return [replace_once(page, r'<footer class="site-footer">.*?</footer>', footer) for page in (home, pubs)]


def main():
    data = json.loads(SOURCE.read_text(encoding='utf-8'))
    paths = [ROOT / 'index.html', ROOT / 'publication.html']
    original = [p.read_text(encoding='utf-8') for p in paths]
    pages = render(data, *original)
    # 根据内容、脚本、样式和图片自动生成缓存版本，无需手动维护日期。
    digest = hashlib.sha256(SOURCE.read_bytes())
    assets = ([ROOT / 'css/style.css', ROOT / 'js/main.js']
               + sorted((ROOT / 'assets/photos').rglob('*'))
               + sorted((ROOT / 'assets/other').rglob('*'))
               + sorted((ROOT / 'assets/icons').rglob('*')))
    for p in assets:
        if p.is_file() and p.suffix.lower() in {'.css', '.js', '.jpg', '.jpeg', '.png', '.svg'}:
            digest.update(p.relative_to(ROOT).as_posix().encode())
            digest.update(p.read_bytes())
    version = digest.hexdigest()[:12]
    def versioned(match):
        prefix, path, suffix = match.groups()
        if not path.startswith(('assets/', 'css/', 'js/')):
            return match.group(0)
        return prefix + path + '?v=' + version + suffix
    pages = [re.sub(r'((?:src|href)=")([^"?]+)(?:\?v=[^"]*)?(")', versioned, page) for page in pages]
    changed = [p.name for p, old, new in zip(paths, original, pages) if old != new]
    if '--check' in sys.argv:
        print('需同步：' + ', '.join(changed) if changed else '内容与页面一致。')
        return bool(changed)
    for path, old, new in zip(paths, original, pages):
        if old != new:
            path.write_text(new, encoding='utf-8')
    print('已同步：' + (', '.join(changed) or '无需修改'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
