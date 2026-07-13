"""
chunk_prefilter.py — Drop parser-artifact chunks before Stage 2 QA generation.

Surveyed across all four manuals (HP, Canon, Cisco, Samsung). Three artifact
types produce broken QA and are dropped here:

  1. numeric_header_table — Docling/pdfplumber mis-parses a table-of-contents,
     index, or layout fragment as a table whose headers are just numeric
     placeholders: ["0"], ["0","1"], ["0","1","2"], ... The rows are usually
     bare page numbers or scattered cells. Found in ALL four manuals.
     (Canon "0 / 1", Cisco/Samsung "0 / 1 / 2", HP "0" and "0 / 1".)

  2. index_dump — raw back-of-book index chunks: page-number salad like
     "margins, small ... jams 156 ... Tray 2 155". Heading is "Index" and the
     body is mostly words-followed-by-page-numbers with almost no sentences.
     (HP index pages.)

  3. image_only — chunk is essentially just ![alt](images/...) refs with almost
     no prose; the LLM fabricates steps. Found in all manuals.

These are Stage-1 parsing artifacts, not real content. Excluding them is data
hygiene; report the dropped count as a quality gate.

USAGE (in stage2_pipeline.py, right after chunk_all):
    from chunk_prefilter import filter_chunks
    chunks, dropped = filter_chunks(chunks)
"""
import re

_IMG_RE = re.compile(r'!\[.*?\]\(.*?\)')
# headers array that is ENTIRELY numeric placeholders: "0", "1", "2", ...
_NUMERIC_HEADERS_RE = re.compile(r'"headers"\s*:\s*\[\s*(?:"\d+"\s*,\s*)*"\d+"\s*\]')


def _text_of(chunk):
    return chunk if isinstance(chunk, str) else getattr(chunk, "text", "") or ""


def _real_text_words(text: str) -> int:
    t = _IMG_RE.sub('', text)
    t = re.sub(r'\*\*|\#|`', '', t)
    return len(re.findall(r'[A-Za-z]{2,}', t))


def is_numeric_header_table(text: str) -> bool:
    """
    True when a table's headers are purely numeric placeholders (0/1/2...),
    which is Docling's signature for a mis-parsed TOC/index/layout fragment.
    """
    if 'table_index' not in text and 'Table data' not in text:
        return False
    return bool(_NUMERIC_HEADERS_RE.search(text))


def is_index_dump(text: str, heading: str = "") -> bool:
    """
    True for back-of-book index chunks: heading 'Index' (or the body is
    dominated by 'word ... number' index entries) with almost no sentences.
    """
    head = (heading or "").strip().lower()
    body = _IMG_RE.sub('', text)
    # count index-style "term <pagenum>" hits
    page_refs = re.findall(r'[A-Za-z][A-Za-z ,]{2,}\s\d{1,3}\b', body)
    # sentences (end punctuation) — real prose has these; index dumps don't
    sentences = re.findall(r'[a-z]{3,}[.!?]', body)
    if head == "index" and len(page_refs) >= 5 and len(sentences) <= 2:
        return True
    # heading-agnostic: very dense page-ref salad with no sentences
    if len(page_refs) >= 12 and len(sentences) == 0:
        return True
    return False


def is_image_only(text: str, min_words: int = 6) -> bool:
    imgs = len(_IMG_RE.findall(text))
    return imgs >= 1 and _real_text_words(text) <= min_words


def classify(text: str, heading: str = "") -> str | None:
    """Return the drop-reason for a chunk, or None to keep it."""
    if is_numeric_header_table(text):
        return "numeric_header_table"
    if is_index_dump(text, heading):
        return "index_dump"
    if is_image_only(text):
        return "image_only"
    return None


def filter_chunks(chunks):
    """Split chunks into (kept, dropped). dropped = list of (chunk, reason)."""
    kept, dropped = [], []
    for c in chunks:
        text = _text_of(c)
        heading = c if isinstance(c, str) else (getattr(c, "heading", "") or "")
        reason = classify(text, heading)
        if reason:
            dropped.append((c, reason))
        else:
            kept.append(c)
    return kept, dropped


if __name__ == "__main__":
    tests = [
        # numeric-header tables — all variants seen across manuals
        ('Section: 0 / 1\nTable data: {"headers": ["0", "1"], "rows":[{"1":"2"}]}', "", "numeric_header_table"),
        ('Section: 0 / 1 / 2\nTable data:\n{"headers":["0","1","2"],"rows":[]}', "", "numeric_header_table"),
        ('Section: 0\nTable data: {"headers": ["0"], "rows":[{"0":"x"}]}', "", "numeric_header_table"),
        # real tables — keep
        ('Table data: {"headers": ["Paper Type","Paper Weight"], "rows":[]}', "", None),
        ('Table data: {"headers": ["Item","Specification"], "rows":[]}', "", None),
        ('Table data: {"headers": ["LED","Status","Description"], "rows":[]}', "", None),
        # index dumps — drop
        ('margins, small. HP Customer Care 142, 188, 204 520-sheet Tray 2 155 locating 2 jams 156 subnet mask 136', "Index", "index_dump"),
        # real prose — keep
        ('Connect a USB cable when connecting the machine and a computer.', "USB port", None),
        ('This chapter describes basic operations, such as how to use the control panel.', "Basic Operations", None),
        # image-only — drop
        ('![1 Open the platen cover](images/image_p23_01.png)', "", "image_only"),
    ]
    ok = True
    for text, head, expect in tests:
        got = classify(text, head)
        mark = "OK" if got == expect else "FAIL"
        if got != expect: ok = False
        print(f"  [{mark}] {str(got):22s} exp {str(expect):22s} :: {text[:45].replace(chr(10),' ')}")
    print("\nALL PASS" if ok else "\nFAILURES")
