"""
markdown_parser.py — Parse Stage 1 Markdown into structured content blocks.

CHANGES (vs previous):
  - Fix #3: heading_path (unchanged from your version).
  - Fix #6 (PAGE OFFSET): a block is now stamped with the page that was
    active when its FIRST content line was added (block_start_page), not the
    live cur_page at flush time. Previously, a block whose body spanned one
    or more <!-- page: N --> markers was stamped with the LATER page, causing
    a negative page offset (cited = actual + k) that grew through front-matter.
  - Also: the image-filename page override no longer clobbers cur_page for
    text blocks; it only informs the page of the image line itself. This
    removes a second source of page drift.
"""
import re, json, os
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ContentBlock:
    heading: str
    body: str
    block_type: str = "text"
    images: List[str] = field(default_factory=list)
    table_data: Optional[dict] = None
    page_hint: Optional[int] = None
    source_file: str = ""
    heading_path: str = ""


def _table_heading(td: dict, fallback: str) -> str:
    if isinstance(td, dict):
        headers = td.get("headers", [])
        if headers and len(headers) >= 2:
            return " / ".join(str(h) for h in headers[:3])
        rows = td.get("rows", [])
        if rows and isinstance(rows[0], dict):
            return " / ".join(list(rows[0].keys())[:3])
    if fallback and fallback != "Untitled":
        return fallback
    return "Untitled"


def parse_markdown(md_path: str, tables_dir: str = "") -> List[ContentBlock]:
    if not os.path.exists(md_path):
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    blocks: List[ContentBlock] = []
    cur_heading = "Untitled"
    cur_body: List[str] = []
    cur_images: List[str] = []
    cur_page: Optional[int] = None
    # FIX #6: page active when the CURRENT block's first content line was added
    block_start_page: Optional[int] = None
    src = os.path.basename(md_path)

    heading_stack: List[Optional[str]] = [None] * 7
    cur_level: int = 0

    def _heading_path() -> str:
        parts = [h for h in heading_stack[1:] if h]
        return " > ".join(parts)

    heading_re    = re.compile(r"^(#{1,4})\s+(.+)")
    image_re      = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    page_re       = re.compile(r"<!--\s*page[:\s]*(\d+)\s*-->", re.I)
    img_page_re   = re.compile(r"image_p(\d+)")
    json_start_re = re.compile(r"^```json\s*$", re.I)
    json_end_re   = re.compile(r"^```\s*$")
    tbl_ref_re    = re.compile(r"\[Table[:\s]*([^\]]*)\]\(([^)]+\.json)\)")
    json_obj_re   = re.compile(r"^\{")

    in_json = False
    json_buf: List[str] = []
    in_inline_json = False
    inline_json_buf: List[str] = []
    brace_depth = 0

    def _note_content_start():
        """FIX #6: remember the page at the moment this block gets its first content."""
        nonlocal block_start_page
        if block_start_page is None:
            block_start_page = cur_page

    def _flush():
        nonlocal block_start_page
        body = "\n".join(cur_body).strip()
        if body or cur_images:
            blocks.append(ContentBlock(
                cur_heading, body, "text",
                list(cur_images), None,
                block_start_page if block_start_page is not None else cur_page,  # FIX #6
                src, heading_path=_heading_path(),
            ))
        block_start_page = None   # reset for next block

    def _make_table_block(td):
        heading = _table_heading(td, cur_heading)
        path = _heading_path()
        if heading != cur_heading and path:
            path = f"{path} > {heading}"
        elif heading != cur_heading:
            path = heading
        # tables are self-contained: use the page active at the table's location
        blocks.append(ContentBlock(
            heading, f"[Table under: {heading}]",
            "table", [], td, cur_page, src,
            heading_path=path,
        ))

    for raw_line in lines:
        raw = raw_line.rstrip("\n").rstrip("\r")

        pm = page_re.search(raw)
        if pm:
            cur_page = int(pm.group(1))
            continue

        # FIX #6: image-filename page is used ONLY to tag the image line's page,
        # not to overwrite cur_page for the whole text block. We still capture
        # it for image provenance, but do not let it drift text-block pages.
        im_page = img_page_re.search(raw)
        # (intentionally not overwriting cur_page here)

        if json_start_re.match(raw.strip()):
            in_json = True
            json_buf = []
            continue
        if in_json:
            if json_end_re.match(raw.strip()):
                in_json = False
                try:
                    td = json.loads("\n".join(json_buf))
                except Exception:
                    td = {"raw": "\n".join(json_buf)}
                _make_table_block(td)
            else:
                json_buf.append(raw)
            continue

        if not in_inline_json and json_obj_re.match(raw.strip()):
            in_inline_json = True
            inline_json_buf = [raw]
            brace_depth = raw.count("{") - raw.count("}")
            if brace_depth <= 0:
                in_inline_json = False
                try:
                    td = json.loads("\n".join(inline_json_buf))
                    if isinstance(td, dict) and ("table_index" in td or "headers" in td or "rows" in td):
                        _make_table_block(td)
                        continue
                except Exception:
                    pass
                _note_content_start()
                cur_body.append(raw)
            continue
        if in_inline_json:
            inline_json_buf.append(raw)
            brace_depth += raw.count("{") - raw.count("}")
            if brace_depth <= 0:
                in_inline_json = False
                try:
                    td = json.loads("\n".join(inline_json_buf))
                    if isinstance(td, dict) and ("table_index" in td or "headers" in td or "rows" in td):
                        _make_table_block(td)
                    else:
                        _note_content_start()
                        cur_body.extend(inline_json_buf)
                except Exception:
                    _note_content_start()
                    cur_body.extend(inline_json_buf)
            continue

        hm = heading_re.match(raw)
        if hm:
            _flush()
            cur_body = []
            cur_images = []
            cur_heading = hm.group(2).strip()
            # FIX #6: a heading marks the start of a new block; its page is the
            # page active at the heading line.
            block_start_page = cur_page
            level = len(hm.group(1))
            cur_level = level
            heading_stack[level] = cur_heading
            for i in range(level + 1, 7):
                heading_stack[i] = None
            continue

        im = image_re.search(raw)
        if im:
            _note_content_start()
            cur_images.append(im.group(2))
            cur_body.append(raw)
            continue

        tm = tbl_ref_re.search(raw)
        if tm and tables_dir:
            tp = os.path.join(tables_dir, os.path.basename(tm.group(2)))
            if os.path.exists(tp):
                try:
                    with open(tp, "r", encoding="utf-8") as tf:
                        td = json.load(tf)
                        _make_table_block(td)
                    continue
                except Exception:
                    pass
            _note_content_start()
            cur_body.append(raw)
            continue

        # ordinary content line
        if raw.strip():
            _note_content_start()
        cur_body.append(raw)

    _flush()

    # Backfill Untitled headings (unchanged)
    for i in range(len(blocks)):
        if blocks[i].heading != "Untitled":
            continue
        for j in range(i - 1, -1, -1):
            if blocks[j].heading != "Untitled":
                blocks[i].heading = blocks[j].heading
                if not blocks[i].heading_path:
                    blocks[i].heading_path = blocks[j].heading_path
                break
        if blocks[i].heading == "Untitled":
            for j in range(i + 1, len(blocks)):
                if blocks[j].heading != "Untitled":
                    blocks[i].heading = blocks[j].heading
                    if not blocks[i].heading_path:
                        blocks[i].heading_path = blocks[j].heading_path
                    break
        if blocks[i].heading == "Untitled" and blocks[i].body:
            first_line = blocks[i].body.strip().split("\n")[0].strip()
            first_line = re.sub(r"^\*\*(.+?)\*\*", r"\1", first_line)
            first_line = re.sub(r"!\[.*?\]\(.*?\)", "", first_line).strip()
            first_line = re.sub(r"\[Table.*?\]", "", first_line).strip()
            if len(first_line) > 5:
                blocks[i].heading = first_line[:80]
                if not blocks[i].heading_path:
                    blocks[i].heading_path = blocks[i].heading

    return blocks