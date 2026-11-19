#!/usr/bin/env python3
"""Search the original English sources (video/earnings-call transcripts and Musk's X posts) for passages.

Only the Python standard library is used. Paths are resolved relative to this script, so it works from any directory.

Examples:
  python3 scripts/search.py "hire" "attitude" --person elon
  python3 scripts/search.py "first principles" --person elon --years 2013-2016
  python3 scripts/search.py "speed of light" --person jensen --source transcripts --limit 15
  python3 scripts/search.py "delete" "requirement" --source x
  python3 scripts/search.py --regex "limiting factor|bottleneck" --person elon
  python3 scripts/search.py "focus" "saying no" --person jobs

Matching: every term must appear in the same passage (case-insensitive). Use --regex for one regular expression instead.
Output: one block per hit with date, title/type, the passage (plus neighbouring lines with --context), and a source link.
YouTube links include &t=<seconds>s so they open at the moment the passage starts.
"""
import argparse
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "references" / "sources"
TS = re.compile(r"^\[(\d+):(\d\d):(\d\d)\]\s*(.*)$")


def secs(h, m, s):
    return int(h) * 3600 + int(m) * 60 + int(s)


def years_ok(date, yr):
    if not yr:
        return True
    m = re.match(r"(\d{4})", date or "")
    return bool(m) and yr[0] <= int(m.group(1)) <= yr[1]


def matcher(a):
    if a.regex:
        rx = re.compile(a.regex, re.I)
        return lambda t: bool(rx.search(t))
    terms = [t.lower() for t in a.terms]
    return lambda t: all(x in t.lower() for x in terms)


def trim(passage, a):
    """Some transcripts have very long paragraphs; keep about a.width characters around the first match."""
    if len(passage) <= a.width * 2:
        return passage
    if a.regex:
        m = re.search(a.regex, passage, re.I)
        pos = m.start() if m else 0
    else:
        pos = passage.lower().find(a.terms[0].lower())
    lo, hi = max(0, pos - a.width), min(len(passage), pos + a.width)
    return ("... " if lo else "") + passage[lo:hi] + (" ..." if hi < len(passage) else "")


def transcripts(a, hit):
    people = ["elon", "jensen", "jobs"] if a.person == "all" else [a.person]
    for who in people:
        for f in sorted((SRC / "transcripts" / who).glob("*.md")):
            text = f.read_text(encoding="utf-8", errors="ignore")
            head, _, body = text.partition("\n---\n")
            if "\n- 重复: " in head and not a.include_duplicates:
                continue
            meta = dict(re.findall(r"^- (日期|链接|分类|频道): (.*)$", head, re.M))
            if not years_ok(meta.get("日期"), a.years):
                continue
            title = head.split("\n", 1)[0].lstrip("# ").strip()
            url = meta.get("链接", "")
            lines = [l for l in body.split("\n") if l.strip()]
            for i, line in enumerate(lines):
                m = TS.match(line)
                content = m.group(4) if m else line
                if not hit(content):
                    continue
                lo, hi = max(0, i - a.context), min(len(lines), i + a.context + 1)
                passage = trim(" ".join(TS.sub(r"\4", l) for l in lines[lo:hi]), a)
                link = url
                if m and "youtube.com/watch" in url:
                    link = "%s&t=%ds" % (url, secs(*m.groups()[:3]))
                when = "[%s:%s:%s] " % m.groups()[:3] if m else ""
                yield (meta.get("日期", ""), f"{who} | {title} ({meta.get('分类', '')}) | {when}{f.stem}", passage, link)


def tweets(a, hit):
    if a.person not in ("all", "elon"):  # 只有马斯克有推文
        return
    line_rx = re.compile(r"^- (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) · (.*) \((https://x\.com/\S+)\)$")
    for name, kind in (("elon-musk-x-posts.md", "post"), ("elon-musk-x-replies.md", "reply")):
        f = SRC / "x" / name
        if not f.exists():
            continue
        for line in f.read_text(encoding="utf-8").split("\n"):
            m = line_rx.match(line)
            if m and years_ok(m.group(1), a.years) and hit(m.group(3)):
                yield (m.group(1), f"elon | X {kind}", m.group(3), m.group(4))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("terms", nargs="*", help="words that must all appear (case-insensitive)")
    ap.add_argument("--regex", help="use one regular expression instead of terms")
    ap.add_argument("--person", choices=["elon", "jensen", "jobs", "all"], default="all")
    ap.add_argument("--source", choices=["transcripts", "x", "all"], default="all")
    ap.add_argument("--years", help="e.g. 2018-2022 or 2024")
    ap.add_argument("--context", type=int, default=1, help="neighbouring transcript lines to include (default 1)")
    ap.add_argument("--width", type=int, default=500, help="characters kept on each side of a match in long paragraphs (default 500)")
    ap.add_argument("--include-duplicates", action="store_true", help="also search re-uploads of the same event (skipped by default)")
    ap.add_argument("--limit", type=int, default=30, help="max hits to print (default 30)")
    a = ap.parse_args()
    if not a.terms and not a.regex:
        ap.error("give search terms or --regex")
    if a.years:
        p = a.years.split("-")
        a.years = (int(p[0]), int(p[-1]))
    hit = matcher(a)
    results = []
    if a.source in ("transcripts", "all"):
        results += list(transcripts(a, hit))
    if a.source in ("x", "all"):
        results += list(tweets(a, hit))
    results.sort(key=lambda r: r[0])
    print(f"{len(results)} hits" + (f", showing first {a.limit}" if len(results) > a.limit else ""))
    for date, where, passage, link in results[: a.limit]:
        print(f"\n## {date} | {where}\n{passage}\n{link}")
    if not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
