# Fetcher Protocol

This document covers Branch D of the skill: when the user provides an Instagram URL instead of attached images, fetch the carousel slides locally via `scripts/fetch-carousel.py` (a wrapper around `gallery-dl`), then run the standard deconstruction protocol on the fetched slides.

The fetcher exists to remove the "screenshot 9 slides manually" friction. It is not a scraper for bulk collection — it pulls one post at a time, on demand, against your own logged-in Instagram session.

---

## When to invoke this branch

Trigger Branch D when the user's message contains an Instagram URL matching:

- `https://www.instagram.com/p/<shortcode>/`
- `https://www.instagram.com/reel/<shortcode>/` (single-image, reduced analysis)
- `https://www.instagram.com/reels/<shortcode>/`

If the message has **both** an IG URL and attached images, treat the attachments as canonical and skip fetching — the user already did the work.

If the URL is a profile (`instagram.com/<handle>/`) or a story or a tag page, do NOT fetch — these are not single-post URLs. Ask the user to point at one specific post.

---

## Prerequisites (one-time setup)

The user must install `gallery-dl` once before this branch works. Pick whichever fits their toolchain:

```bash
pip install gallery-dl       # if they have pip
pipx install gallery-dl      # cleaner, isolated
brew install gallery-dl      # macOS Homebrew
```

If the script reports `gallery-dl is not installed`, surface the install command and stop. Do not attempt to install for the user — that needs explicit consent for a system-level package change.

Most Instagram carousels now require an authenticated session. The fetcher reads cookies from the user's browser (read-only — it does not modify the browser profile):

```bash
python3 scripts/fetch-carousel.py <url> --cookies-from-browser firefox
```

Supported browsers: `firefox`, `chrome`, `safari`, `edge`, `brave`. If the user is logged into Instagram in one of these, point at it.

If `--cookies-from-browser` doesn't work (e.g., headless server, cookies locked), the user can export cookies to a Netscape-format file and pass `--cookies path/to/cookies.txt`.

---

## Invocation

The skill calls the script via Bash. From the skill root:

```bash
python3 scripts/fetch-carousel.py "<url>" --cookies-from-browser firefox
```

The script writes slides to `assets/fetched/<shortcode>/` as `1.jpg`, `2.jpg`, … in carousel order, and prints a JSON summary on stdout:

```json
{
  "shortcode": "ABC123",
  "creator": "@moongirlmai",
  "slide_count": 10,
  "out_dir": "/.../assets/fetched/ABC123",
  "slides": [".../1.jpg", ".../2.jpg", ...]
}
```

Capture this JSON. It tells you the creator handle (use it for the entry's filename), the slide count (sanity check before Pass 1), and the absolute paths to feed into the deconstruction.

---

## After fetching

Once slides are on disk, **run the standard deconstruction protocol** (`references/deconstruction-protocol.md`) on them. The fetcher is purely an input shim — it does not change the 5-pass workflow.

The fetcher's downloaded `*.jpg` files are read-only inputs. Do not write Schema A YAML into the `assets/fetched/<shortcode>/` directory. Final entry still goes to `references/style-dna/<creator>/YYYY-MM-DD_<slug>.md`.

If `slide_count == 1`, the post was a single-image (Reel cover, single photo) — apply the partial-data caveats from `deconstruction-protocol.md` §2 (single-image-input handling) and flag the entry's body prose accordingly.

---

## Cleanup

`assets/fetched/` is gitignored by default. Slides accumulate there and can be deleted any time without breaking library entries — the entries reference no fetched files, only the analyzed signal.

Add to `.gitignore` (already present in skill root):

```
assets/fetched/
```

---

## Failure modes and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| `gallery-dl is not installed` | Not in PATH | `pip install gallery-dl` |
| `gallery-dl exited with code 1` and HTML in stderr | IG is showing a login wall | Pass `--cookies-from-browser <browser>` |
| `No images downloaded` | Post is private, deleted, or geo-restricted | Verify URL in browser; if private, user must follow the account |
| `Could not extract IG shortcode from URL` | URL is a profile, story, or malformed | Ask user for a specific post URL |
| Rate-limit / 429 errors | Too many requests in a window | Wait 15-30 minutes; reduce frequency |
| Slides arrive but in wrong order | Rare — gallery-dl's `{num}` is 1-indexed by carousel position | Open an issue against gallery-dl; manually reorder for now |

---

## Honesty rules specific to this branch

- **Always tell the user what URL you fetched and how many slides came back** before starting Pass 1. Wrong post = wasted analysis.
- **If the fetched creator handle disagrees with what the user said** (e.g., user said `@moongirlmai`, fetcher returned `@moongirlmail`), flag the mismatch and confirm before writing the entry. Filenames depend on this.
- **Do not refetch the same post repeatedly.** If slides already exist at `assets/fetched/<shortcode>/`, reuse them and tell the user "already on disk — proceeding to deconstruction."
- **Instagram's TOS restricts automated access.** This branch is for personal research. Don't run it in a loop, don't run it against accounts the user can't view in a browser, don't ship a public service that calls it.

---

## What this branch does NOT do

- It does not fetch a creator's full feed. One post at a time.
- It does not log into Instagram for you. Cookies must already exist from a logged-in browser session.
- It does not bypass private-account protections. If you can't see the post in a browser, the fetcher can't either.
- It does not crawl, paginate, or auto-discover posts. The user always provides the URL.
