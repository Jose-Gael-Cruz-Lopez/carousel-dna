#!/usr/bin/env python3
"""
fetch-carousel.py — fetch the slides of an Instagram carousel via gallery-dl.

This wraps `gallery-dl` so the carousel-design-analysis skill can pull a creator's
carousel slides from a public IG URL instead of requiring manual screenshots.

Usage:
    python3 fetch-carousel.py <instagram-url> [--out DIR] [--cookies-from-browser BROWSER]

Examples:
    python3 fetch-carousel.py https://www.instagram.com/p/ABC123/
    python3 fetch-carousel.py https://www.instagram.com/p/ABC123/ --cookies-from-browser firefox
    python3 fetch-carousel.py https://www.instagram.com/p/ABC123/ --out /tmp/cd-fetch

Prerequisites:
    pip install gallery-dl
    (or: pipx install gallery-dl, brew install gallery-dl)

Cookies:
    Most IG carousels now require auth. Pass `--cookies-from-browser firefox` (or chrome,
    safari, edge) to reuse your logged-in session. Read-only — gallery-dl extracts cookies,
    it does not modify the browser profile.

Output:
    Slides land in <out>/<creator>/<shortcode>/ as 1.jpg, 2.jpg, ... in carousel order.
    The script prints the absolute output path on success and exits 0.
    On failure, prints a diagnostic to stderr and exits non-zero.

Honesty note:
    Instagram's terms restrict automated access. This wrapper is intended for personal
    research on public posts. Don't run it at scale or against accounts you don't have
    permission to view.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


SHORTCODE_RE = re.compile(r"instagram\.com/(?:p|reel|reels)/([A-Za-z0-9_-]+)")


def die(msg: str, code: int = 1) -> None:
    print(f"fetch-carousel: {msg}", file=sys.stderr)
    sys.exit(code)


def parse_shortcode(url: str) -> str:
    m = SHORTCODE_RE.search(url)
    if not m:
        die(f"could not extract IG shortcode from URL: {url!r}")
    return m.group(1)


def check_gallery_dl() -> str:
    path = shutil.which("gallery-dl")
    if not path:
        die(
            "gallery-dl is not installed. Install with one of:\n"
            "  pip install gallery-dl\n"
            "  pipx install gallery-dl\n"
            "  brew install gallery-dl"
        )
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch IG carousel slides via gallery-dl.")
    parser.add_argument("url", help="Instagram post URL (e.g. https://www.instagram.com/p/ABC123/)")
    parser.add_argument(
        "--out",
        default=None,
        help="Output directory. Defaults to <skill>/assets/fetched/<shortcode>.",
    )
    parser.add_argument(
        "--cookies-from-browser",
        default=None,
        help="Browser to extract cookies from (firefox, chrome, safari, edge, brave).",
    )
    parser.add_argument(
        "--cookies",
        default=None,
        help="Path to a Netscape-format cookies.txt file (alternative to --cookies-from-browser).",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress gallery-dl progress output (errors still print).",
    )
    args = parser.parse_args()

    check_gallery_dl()
    shortcode = parse_shortcode(args.url)

    skill_root = Path(__file__).resolve().parent.parent
    out_dir = Path(args.out).resolve() if args.out else skill_root / "assets" / "fetched" / shortcode
    out_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "gallery-dl",
        "--directory", str(out_dir),
        "--filename", "{num}.{extension}",
        "--option", "extractor.instagram.include=posts",
        "--write-metadata",
    ]
    if args.cookies_from_browser:
        cmd += ["--cookies-from-browser", args.cookies_from_browser]
    elif args.cookies:
        cmd += ["--cookies", args.cookies]
    if args.quiet:
        cmd.append("--quiet")
    cmd.append(args.url)

    try:
        result = subprocess.run(cmd, check=False)
    except FileNotFoundError:
        die("gallery-dl invocation failed (is it on PATH?).")
        return 1

    if result.returncode != 0:
        die(
            f"gallery-dl exited with code {result.returncode}. "
            "Common causes: login required (use --cookies-from-browser), "
            "post is private or deleted, rate-limited (try again later)."
        )

    images = sorted(p for p in out_dir.glob("*.jpg")) + sorted(p for p in out_dir.glob("*.png"))
    if not images:
        die(
            f"No images downloaded into {out_dir}. "
            "The post may not be a carousel, or auth may be required."
        )

    creator = None
    for meta in out_dir.glob("*.json"):
        try:
            data = json.loads(meta.read_text())
            creator = data.get("username") or data.get("owner_username") or creator
        except (OSError, json.JSONDecodeError):
            continue

    summary = {
        "shortcode": shortcode,
        "creator": f"@{creator}" if creator else None,
        "slide_count": len(images),
        "out_dir": str(out_dir),
        "slides": [str(p) for p in images],
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
