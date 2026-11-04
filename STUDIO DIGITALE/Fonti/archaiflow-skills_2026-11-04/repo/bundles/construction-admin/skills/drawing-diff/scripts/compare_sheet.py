#!/usr/bin/env python3
"""Compare one sheet against its other revision, two ways.

Text extraction catches dimension, note, tag and title-block edits and reports
exact values. An aligned raster overlay catches linework that moved when no text
changed. Neither sees what the other sees, so both run and the output records
which one was skipped.

Writes <sheet>.json plus a before/after PNG pair for every changed region.
"""
import argparse
import json
import re
import sys
from collections import deque
from pathlib import Path

try:
    import pymupdf
except ImportError:  # PyMuPDF < 1.24 only exposes `fitz`
    try:
        import fitz as pymupdf
    except ImportError:
        sys.exit(
            "ERROR: PyMuPDF is not installed.\n"
            "Install with:  pip install PyMuPDF"
        )


# --- text engine ------------------------------------------------------------

def lines_of(page):
    """[(text, x, y)]. Lines, not words, because a word-level diff splits
    '2 HR RATED' into three findings."""
    out = []
    data = page.get_text("dict")
    for block in data.get("blocks", []):
        for line in block.get("lines", []):
            text = "".join(span.get("text", "") for span in line.get("spans", []))
            text = re.sub(r"\s+", " ", text).strip()
            if not text:
                continue
            x0, y0, _, _ = line["bbox"]
            out.append((text, x0, y0))
    return out


def key_lines(lines, tol, scale=1.0, shift=(0.0, 0.0)):
    """Bucket lines by position so the diff compares like with like. Two lines
    can round onto one key on a dense sheet, so a key holds a list.

    Scale and shift normalise the new sheet onto the old one for keying only.
    The position stored against each line stays the real one on its own sheet."""
    out = {}
    for text, x, y in lines:
        key = (round((x * scale - shift[0]) / tol), round((y * scale - shift[1]) / tol))
        out.setdefault(key, []).append((text, [round(x, 1), round(y, 1)]))
    return out


def uniform_scale(old_rect, new_rect, tol=0.01):
    """Ratio between two page sizes when one is a clean re-scale of the other,
    else None. A half-size print is the same sheet and compares fine once the
    ratio is out; a different aspect ratio is a different sheet."""
    rw = old_rect.width / new_rect.width
    rh = old_rect.height / new_rect.height
    if abs(rw - rh) / max(rw, 1e-9) > tol:
        return None
    return rw


def global_text_shift(old_lines, new_lines, scale):
    """The offset a re-plot applied to the whole sheet, from the lines that read
    the same on both sides. Without removing it every note reads as moved and a
    dimension change scatters into one addition plus one removal instead of
    landing in `edited`, which is the finding worth having."""
    counts = {}
    for text, x, y in old_lines:
        counts.setdefault(text, [[], []])[0].append((x, y))
    for text, x, y in new_lines:
        counts.setdefault(text, [[], []])[1].append((x * scale, y * scale))

    deltas = {}
    for o, n in counts.values():
        # Only lines that appear exactly once on each side vote.
        if len(o) != 1 or len(n) != 1:
            continue
        d = (round(n[0][0] - o[0][0]), round(n[0][1] - o[0][1]))
        deltas[d] = deltas.get(d, 0) + 1

    if not deltas:
        return 0.0, 0.0
    (dx, dy), hits = max(deltas.items(), key=lambda kv: kv[1])
    total = sum(deltas.values())
    # Trust it only when most of the sheet agrees, so a couple of moved notes
    # never drag every other line out of place.
    if (dx, dy) == (0, 0) or hits < max(3, total * 0.6):
        return 0.0, 0.0
    return float(dx), float(dy)


def text_diff(old_page, new_page, tol, scale):
    old_lines, new_lines = lines_of(old_page), lines_of(new_page)
    shift = global_text_shift(old_lines, new_lines, scale)
    old = key_lines(old_lines, tol)
    new = key_lines(new_lines, tol, scale=scale, shift=shift)
    added, removed, edited = [], [], []

    for key in set(old) | set(new):
        o = list(old.get(key, []))
        n = list(new.get(key, []))

        # Drop the lines that read the same on both sides at this spot.
        for entry in list(o):
            match = next((e for e in n if e[0] == entry[0]), None)
            if match:
                o.remove(entry)
                n.remove(match)

        # What is left at the same spot on both sides is an edit in place. This
        # is where a dimension change or a rating change lands.
        for (was, at), (now, _) in zip(o, n):
            edited.append({"was": was, "now": now, "at": at})
        for text, at in o[len(n):]:
            removed.append({"text": text, "at": at})
        for text, at in n[len(o):]:
            added.append({"text": text, "at": at})

    # A note that only moved is not a content change. Pull those out of the two
    # lists so the report does not read as two findings.
    moved = []
    for a in list(added):
        hit = next((r for r in removed if r["text"] == a["text"]), None)
        if hit:
            moved.append({"text": a["text"], "was_at": hit["at"], "now_at": a["at"]})
            added.remove(a)
            removed.remove(hit)

    return {
        "sheet_shift_pt": list(shift),
        "sheet_scale": round(scale, 4),
        "added": sorted(added, key=lambda d: (d["at"][1], d["at"][0])),
        "removed": sorted(removed, key=lambda d: (d["at"][1], d["at"][0])),
        "edited": sorted(edited, key=lambda d: (d["at"][1], d["at"][0])),
        "moved": moved,
    }


# --- raster engine ----------------------------------------------------------

def band(samples, stride, y0, y1, x0, x1, step=1):
    return b"".join(samples[y * stride + x0:y * stride + x1]
                    for y in range(y0, y1, step))


def diff_px(a, b):
    """Differing bytes between two equal-length buffers, at C speed."""
    if a == b:
        return 0
    x = int.from_bytes(a, "big") ^ int.from_bytes(b, "big")
    return len(a) - x.to_bytes(len(a), "big").count(0)


def find_offset(old, new, w, h, max_shift, step):
    """Whole-sheet pixel offset from a re-plot. Without removing it, every line
    on the sheet reads as changed."""
    x0, y0 = max_shift, max_shift
    x1, y1 = w - max_shift, h - max_shift
    fixed = band(old.samples, old.stride, y0, y1, x0, x1, step)

    best = (None, None, len(fixed) + 1)
    for dy in range(-max_shift, max_shift + 1):
        for dx in range(-max_shift, max_shift + 1):
            cand = band(new.samples, new.stride, y0 + dy, y1 + dy, x0 + dx, x1 + dx, step)
            d = diff_px(fixed, cand)
            if d < best[2]:
                best = (dx, dy, d)
    dx, dy, d = best
    return dx, dy, round(100 * d / max(len(fixed), 1), 1)


def changed_tiles(old, new, w, h, dx, dy, max_shift, tile, min_frac):
    grid = {}
    for ty, py in enumerate(range(max_shift, h - max_shift - tile, tile)):
        for tx, px in enumerate(range(max_shift, w - max_shift - tile, tile)):
            a = band(old.samples, old.stride, py, py + tile, px, px + tile)
            b = band(new.samples, new.stride, py + dy, py + dy + tile, px + dx, px + dx + tile)
            d = diff_px(a, b)
            if d > tile * tile * min_frac:
                grid[(tx, ty)] = {"px": px, "py": py, "diff": d}
    return grid


def merge_regions(grid, tile):
    """Adjacent changed tiles are one change, not twelve."""
    regions, seen = [], set()
    for start in grid:
        if start in seen:
            continue
        queue, cluster = deque([start]), []
        seen.add(start)
        while queue:
            tx, ty = queue.popleft()
            cluster.append((tx, ty))
            for nb in ((tx + 1, ty), (tx - 1, ty), (tx, ty + 1), (tx, ty - 1)):
                if nb in grid and nb not in seen:
                    seen.add(nb)
                    queue.append(nb)
        xs = [grid[c]["px"] for c in cluster]
        ys = [grid[c]["py"] for c in cluster]
        regions.append({
            "px_rect": [min(xs), min(ys), max(xs) + tile, max(ys) + tile],
            "tiles": len(cluster),
            "diff_px": sum(grid[c]["diff"] for c in cluster),
        })
    regions.sort(key=lambda r: r["tiles"], reverse=True)
    return regions


def crop(page, rect, dpi, path):
    pix = page.get_pixmap(dpi=dpi, clip=rect)
    pix.save(path)


# --- main -------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", required=True)
    parser.add_argument("--new", required=True)
    parser.add_argument("--old-page", required=True, type=int)
    parser.add_argument("--new-page", required=True, type=int)
    parser.add_argument("--sheet", required=True, help="Sheet number, used for filenames")
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--scan-dpi", type=int, default=50, help="Overlay resolution")
    parser.add_argument("--crop-dpi", type=int, default=150, help="Region crop resolution")
    parser.add_argument("--tile", type=int, default=32, help="Overlay tile size in px")
    parser.add_argument("--max-shift", type=int, default=6, help="Re-plot offset search, px")
    parser.add_argument("--min-frac", type=float, default=0.01,
                        help="Fraction of a tile's pixels that must differ")
    parser.add_argument("--max-regions", type=int, default=10)
    parser.add_argument("--text-tol", type=float, default=3.0,
                        help="Points within which two text positions are the same spot")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", args.sheet)

    old_doc, new_doc = pymupdf.open(args.old), pymupdf.open(args.new)
    old_page = old_doc[args.old_page - 1]
    new_page = new_doc[args.new_page - 1]

    result = {
        "sheet": args.sheet,
        "old": {"file": Path(args.old).name, "page": args.old_page},
        "new": {"file": Path(args.new).name, "page": args.new_page},
        "skipped": [],
    }

    # A half-size print is the same sheet at a different paper size, and both
    # engines can still compare it once the ratio is known. A different aspect
    # ratio is a different sheet, and nothing below is meaningful.
    page_scale = uniform_scale(old_page.rect, new_page.rect)

    # Text engine. Both sides have to be machine-readable. Diffing a vector
    # sheet against a scan of it reports every line on the vector side as
    # deleted, which looks like a huge finding and is entirely an artefact.
    has_text = {"old": bool(old_page.get_text("words")),
                "new": bool(new_page.get_text("words"))}
    if not all(has_text.values()):
        result["text"] = None
        result["skipped"].append({
            "engine": "text",
            "reason": "no-text",
            "sides": [side for side, ok in has_text.items() if not ok],
        })
    elif page_scale is None:
        result["text"] = None
        result["skipped"].append({"engine": "text", "reason": "aspect-mismatch"})
    else:
        result["text"] = text_diff(old_page, new_page, args.text_tol, page_scale)

    # Raster engine.
    gray = pymupdf.csGRAY
    zoom_old = args.scan_dpi / 72.0
    zoom_new = zoom_old * (page_scale or 1.0)
    old_pix = old_page.get_pixmap(matrix=pymupdf.Matrix(zoom_old, zoom_old), colorspace=gray)
    new_pix = new_page.get_pixmap(matrix=pymupdf.Matrix(zoom_new, zoom_new), colorspace=gray)

    off_by = (abs(old_pix.width - new_pix.width), abs(old_pix.height - new_pix.height))
    if page_scale is None or max(off_by) > 4:
        result["regions"] = None
        result["alignment"] = None
        result["skipped"].append({
            "engine": "raster",
            "reason": "aspect-mismatch" if page_scale is None else "size-mismatch",
            "old_pt": [round(old_page.rect.width, 1), round(old_page.rect.height, 1)],
            "new_pt": [round(new_page.rect.width, 1), round(new_page.rect.height, 1)],
        })
    else:
        # Rounding can leave the two grids a pixel apart. Compare the overlap.
        w = min(old_pix.width, new_pix.width)
        h = min(old_pix.height, new_pix.height)
        dx, dy, residual = find_offset(old_pix, new_pix, w, h, args.max_shift, step=3)
        result["alignment"] = {
            "dx": dx, "dy": dy, "residual_pct": residual,
            "page_scale": round(page_scale, 4),
        }

        grid = changed_tiles(old_pix, new_pix, w, h, dx, dy, args.max_shift,
                             args.tile, args.min_frac)
        regions = merge_regions(grid, args.tile)
        result["regions_found"] = len(regions)
        result["regions_capped"] = len(regions) > args.max_regions
        regions = regions[:args.max_regions]

        margin = 12.0

        def on_new(v, origin_old, origin_new, off):
            """A coordinate on the old sheet, expressed on the new one: back to
            pixels, apply the alignment offset, then into the new page's own
            points. Handles the paper-size ratio as a side effect of the two
            different zooms."""
            return origin_new + ((v - origin_old) * zoom_old + off) / zoom_new

        for i, r in enumerate(regions, start=1):
            x0, y0, x1, y1 = r["px_rect"]
            rect = pymupdf.Rect(
                old_page.rect.x0 + x0 / zoom_old - margin,
                old_page.rect.y0 + y0 / zoom_old - margin,
                old_page.rect.x0 + x1 / zoom_old + margin,
                old_page.rect.y0 + y1 / zoom_old + margin,
            ) & old_page.rect
            new_rect = pymupdf.Rect(
                on_new(rect.x0, old_page.rect.x0, new_page.rect.x0, dx),
                on_new(rect.y0, old_page.rect.y0, new_page.rect.y0, dy),
                on_new(rect.x1, old_page.rect.x0, new_page.rect.x0, dx),
                on_new(rect.y1, old_page.rect.y0, new_page.rect.y0, dy),
            ) & new_page.rect

            r["rect_pt"] = [round(v, 1) for v in (rect.x0, rect.y0, rect.x1, rect.y1)]
            r["old_crop"] = str(out_dir / f"{safe}-r{i}-old.png")
            r["new_crop"] = str(out_dir / f"{safe}-r{i}-new.png")
            crop(old_page, rect, args.crop_dpi, r["old_crop"])
            crop(new_page, new_rect, args.crop_dpi, r["new_crop"])
            del r["px_rect"]
        result["regions"] = regions

    old_doc.close()
    new_doc.close()

    out = out_dir / f"{safe}.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"Wrote: {out}")
    t = result.get("text")
    if t is None:
        why = next(s for s in result["skipped"] if s["engine"] == "text")
        if why["reason"] == "no-text":
            print(f"  text     skipped: no extractable text on the "
                  f"{' and '.join(why['sides'])} side (a scan)")
        else:
            print("  text     skipped: sheets are different shapes")
    else:
        print(f"  text     {len(t['edited'])} edited, {len(t['added'])} added, "
              f"{len(t['removed'])} removed, {len(t['moved'])} moved")
        if t["sheet_shift_pt"] != [0.0, 0.0]:
            print(f"           whole sheet re-plotted {t['sheet_shift_pt']} pt, "
                  "removed before diffing")
    if result.get("regions") is None:
        why = next(s for s in result["skipped"] if s["engine"] == "raster")
        print(f"  overlay  skipped: {why['reason']} "
              f"({why['old_pt']} pt vs {why['new_pt']} pt)")
    else:
        a = result["alignment"]
        print(f"  overlay  {result['regions_found']} regions, "
              f"offset {a['dx']},{a['dy']} px, residual {a['residual_pct']}%")
        if a["page_scale"] != 1.0:
            print(f"           new sheet is {a['page_scale']}x the old paper size, "
                  "rendered to match")
        if a["residual_pct"] > 40:
            print("  WARNING  sheets did not align. Treat regions as unusable.")
        if result["regions_capped"]:
            print(f"  NOTE     capped at {args.max_regions}; say so in the report.")


if __name__ == "__main__":
    main()
