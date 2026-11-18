#!/usr/bin/env python3
"""Check that English quotes really appear, word for word, in the original sources.

Two ways to use it:
  python3 scripts/verify_quote.py --quote "We had a philosophy of best idea wins" \
      --url "https://www.youtube.com/watch?v=PdQWwsaKhQI&t=1377s"
  python3 scripts/verify_quote.py answer.md      # checks every line that starts with  > "..."

Rules (same as the cards in references/cards/):
  - Case, punctuation, filler words (um, uh) and stuttered repeats ("I I think") are ignored.
  - "..." splits a quote into parts; each part must exist on its own.
  - YouTube link with &t=: the quote must be within 2 minutes of that moment.
  - x.com status link: the quote must be inside that post.
  - Any other link (earnings-call or interview transcript, or a source listed in references/sources/quotes/):
    the quote must be in the transcript with that URL, or be a listed quote with that source.
  - No link: the quote must exist somewhere in that person's sources (pass --person to narrow it down).
In a markdown file, the link is taken from the two lines after the quote.
Exit code 0 = all quotes found, 1 = at least one problem.
"""
import argparse
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "references" / "sources"
YT = re.compile(r"youtube\.com/watch\?v=([\w-]{11})(?:&t=(\d+)s)?")
XL = re.compile(r"(?:x|twitter)\.com/\w+/status/(\d+)")
URL = re.compile(r"https?://[^\s)\]]+")
QUOTE = re.compile(r'^\s*>\s*["\u201c](.+?)["\u201d]\s*$')


def norm(s):
    words = re.sub(r"[^a-z0-9']+", " ", s.lower().replace("’", "'").replace("‘", "'")).replace("'", "").split()
    out = []
    for w in words:
        if w in ("um", "uh", "umm", "uhh", "er", "ah"):
            continue
        if out and out[-1] == w:
            continue
        out.append(w)
    return " ".join(out)


class Corpus:
    def __init__(self):
        self.docs = {}  # (who, id) -> dict(url, paras[(sec|None, norm)], all)
        for who in ("elon", "jensen"):
            for f in (SRC / "transcripts" / who).glob("*.md"):
                text = f.read_text(encoding="utf-8", errors="ignore")
                head = text[:3000]
                m = re.search(r"^- 链接: (\S+)", head, re.M)
                paras = []
                for line in text.split("\n"):
                    t = re.match(r"^\[(\d+):(\d\d):(\d\d)\]\s*(.*)$", line)
                    if t:
                        h, mi, s, body = t.groups()
                        paras.append((int(h) * 3600 + int(mi) * 60 + int(s), norm(body)))
                self.docs[(who, f.stem)] = {"url": m.group(1) if m else "", "paras": paras, "all": norm(text)}
        self.quotes = {}  # person -> [(norm text, source text)] from references/sources/quotes/
        for who in ("elon", "jensen"):
            f = SRC / "quotes" / (who + ".md")
            if f.exists():
                self.quotes[who] = [(norm(m.group(1)), m.group(2)) for m in
                                    re.finditer(r"^- \u201c(.*)\u201d \((.*)\)$", f.read_text(encoding="utf-8"), re.M)]
        self.tweets = {}
        for f in (SRC / "x").glob("*.md"):
            for m in re.finditer(r"^- \S+ \S+ · (.*) \(https://x\.com/\w+/status/(\d+)\)$", f.read_text(encoding="utf-8"), re.M):
                self.tweets[m.group(2)] = norm(m.group(1))

    def check(self, quote, url="", person="all"):
        parts = [norm(p) for p in re.split(r"\.\.\.|…", quote) if norm(p)]
        if not parts:
            return "empty quote"
        found = lambda hay: all(p in hay for p in parts)
        x = XL.search(url or "")
        if x:
            tw = self.tweets.get(x.group(1))
            if tw is None:
                return "post id %s is not in the X data" % x.group(1)
            return None if found(tw) else "not in that X post"
        y = YT.search(url or "")
        if y:
            hits = [(k, d) for k, d in self.docs.items() if k[1] == y.group(1)]
            if not hits:
                return "video %s is not in the sources" % y.group(1)
            d = hits[0][1]
            if y.group(2) and d["paras"]:
                t = int(y.group(2))
                near = " ".join(p for s, p in d["paras"] if t - 120 <= s <= t + 120)
                if found(near):
                    return None
                return "in this video but not near t=%ss" % t if found(d["all"]) else "not in this video"
            return None if found(d["all"]) else "not in this video"
        for who, qs in self.quotes.items():
            if person in ("all", who) and url:
                for qn, src in qs:
                    if url.rstrip("/") in src and found(qn):
                        return None
        if url:
            same = [d for d in self.docs.values() if d["url"] and d["url"].rstrip("/") == url.rstrip("/")]
            if same:
                return None if any(found(d["all"]) for d in same) else "not in the transcript at that URL"
        pool = [d["all"] for k, d in self.docs.items() if person in ("all", k[0])]
        if person in ("all", "elon"):
            pool += list(self.tweets.values())
        pool += [qn for who, qs in self.quotes.items() if person in ("all", who) for qn, _ in qs]
        return None if any(found(h) for h in pool) else "not found anywhere in the sources"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="markdown file whose  > \"...\"  lines should be checked")
    ap.add_argument("--quote")
    ap.add_argument("--url", default="")
    ap.add_argument("--person", choices=["elon", "jensen", "all"], default="all")
    a = ap.parse_args()
    c = Corpus()
    if a.quote:
        err = c.check(a.quote, a.url, a.person)
        print("OK" if not err else "PROBLEM: " + err)
        sys.exit(1 if err else 0)
    if not a.file:
        ap.error("give a markdown file or --quote")
    lines = Path(a.file).read_text(encoding="utf-8").split("\n")
    n = bad = 0
    for i, line in enumerate(lines):
        q = QUOTE.match(line)
        if not q:
            continue
        n += 1
        u = URL.search(" ".join(lines[i + 1:i + 3]))
        err = c.check(q.group(1), u.group(0) if u else "", a.person)
        if err:
            bad += 1
            print("line %d: %s | %s" % (i + 1, err, q.group(1)[:90]))
    print("%d quotes checked, %d problems" % (n, bad))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
