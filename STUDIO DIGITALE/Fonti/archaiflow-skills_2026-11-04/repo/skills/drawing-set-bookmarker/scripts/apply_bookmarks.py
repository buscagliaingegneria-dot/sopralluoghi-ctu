#!/usr/bin/env python3
"""Apply a nested bookmark tree to a PDF using pikepdf.

Bookmark tree JSON schema:

    {
      "groups": [
        {
          "label": "Architectural (A)",
          "children": [
            {"label": "A-101 — FIRST FLOOR PLAN", "page": 12},
            {"label": "A-102 — SECOND FLOOR PLAN", "page": 13},
            {
              "label": "A-501 — WALL DETAILS",
              "page": 22,
              "children": [
                {"label": "A-501-1 — Parapet detail", "page": 22}
              ]
            }
          ]
        },
        ...
      ]
    }

- "page" is 1-based PDF page number.
- "children" is optional; supports arbitrary nesting depth.
- Top-level "groups" become the topmost outline items; their "children" are
  the nested sheet bookmarks.
- Top-level groups without an explicit "page" land on the first page of their
  first child.
"""
import argparse
import json
import sys
from pathlib import Path


def _to_outline(pikepdf_mod, items, total_pages):
    """Recursively convert a list of dicts into a list of pikepdf.OutlineItem."""
    outline_items = []
    for entry in items:
        label = entry.get("label", "")
        if not label:
            print(f"WARN: outline entry missing 'label' — skipped: {entry}", file=sys.stderr)
            continue
        children_data = entry.get("children", [])
        # Determine target page: explicit > first descendant > 1
        page = entry.get("page")
        if page is None and children_data:
            page = _first_descendant_page(children_data)
        if page is None:
            page = 1
        if not (1 <= page <= total_pages):
            print(
                f"WARN: page {page} out of range (1..{total_pages}) for '{label}' — clamped",
                file=sys.stderr,
            )
            page = max(1, min(page, total_pages))
        item = pikepdf_mod.OutlineItem(label, destination=page - 1)
        if children_data:
            item.children.extend(_to_outline(pikepdf_mod, children_data, total_pages))
        outline_items.append(item)
    return outline_items


def _first_descendant_page(items):
    for entry in items:
        if "page" in entry:
            return entry["page"]
        if entry.get("children"):
            p = _first_descendant_page(entry["children"])
            if p is not None:
                return p
    return None


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--input", required=True, help="Input PDF path")
    parser.add_argument("--tree", required=True, help="Bookmark tree JSON path")
    parser.add_argument("--output", required=True, help="Output PDF path (bookmarked)")
    args = parser.parse_args()

    try:
        import pikepdf
    except ImportError:
        sys.exit(
            "ERROR: pikepdf not installed. Run scripts/init_workspace.py first or "
            "`pip install pikepdf`."
        )

    input_path = Path(args.input)
    tree_path = Path(args.tree)
    output_path = Path(args.output)

    if not input_path.exists():
        sys.exit(f"Input PDF not found: {input_path}")
    if not tree_path.exists():
        sys.exit(f"Bookmark tree not found: {tree_path}")

    tree = json.loads(tree_path.read_text())
    groups = tree.get("groups")
    if not isinstance(groups, list):
        sys.exit("Bookmark tree JSON must have a top-level 'groups' list.")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with pikepdf.open(input_path) as pdf:
        total_pages = len(pdf.pages)
        with pdf.open_outline() as outline:
            outline.root.clear()
            outline.root.extend(_to_outline(pikepdf, groups, total_pages))
        pdf.save(output_path)

    leaf_count = _count_leaves(groups)
    print(
        f"Wrote {output_path} with {len(groups)} top-level groups "
        f"and {leaf_count} sheet bookmarks ({total_pages} pages)."
    )


def _count_leaves(items):
    count = 0
    for entry in items:
        children = entry.get("children", [])
        if children:
            count += _count_leaves(children)
        else:
            count += 1
    return count


if __name__ == "__main__":
    main()
