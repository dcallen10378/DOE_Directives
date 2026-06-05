#!/usr/bin/env python3
"""Extract the DOE 413 source PDFs to page-tagged Markdown via OCR.

These PDFs carry a text layer with no usable ToUnicode mapping, so direct text
extraction yields glyph codes. We render each page and OCR it instead. Every
page is delimited with a `[p. N]` marker so the chatbot can cite page numbers,
and section numbers/headings survive in-line in the OCR text for "§X" citations.
"""
import io
import os
import sys
import glob
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

SRC = "docs/source-pdfs"
OUT = "docs"

# filename -> metadata used for the markdown header
META = {
    "413.3B-Order-Chg7.pdf": dict(
        number="DOE O 413.3B Chg 7",
        title="Program and Project Management for the Acquisition of Capital Assets",
        cite="DOE O 413.3B",
        kind="Order (requirements)",
        url="https://www.directives.doe.gov/directives-documents/400-series/0413.3-BOrder-B-chg7-ltdchg",
        dpi=250,
    ),
    "413.3-5A-PerformanceBaseline-Chg1.pdf": dict(
        number="DOE G 413.3-5A Chg 1",
        title="Performance Baseline Guide",
        cite="the Performance Baseline Guide (DOE G 413.3-5A)",
        kind="Guide (non-mandatory)",
        url="https://www.directives.doe.gov/directives-documents/400-series/0413.3-EGuide-05a",
        dpi=250,
    ),
    "413.3-7A-RiskManagement-Chg2.pdf": dict(
        number="DOE G 413.3-7A Chg 2",
        title="Risk Management Guide",
        cite="the Risk Management Guide (DOE G 413.3-7A)",
        kind="Guide (non-mandatory)",
        url="https://www.directives.doe.gov/directives-documents/400-series/0413.3-EGuide-07a-chg2-ltdchg",
        dpi=250,
    ),
    "413.3-20-ChangeControl-Chg1.pdf": dict(
        number="DOE G 413.3-20 Chg 1 (Admin Chg)",
        title="Change Control Management Guide",
        cite="the Change Control Management Guide (DOE G 413.3-20)",
        kind="Guide (non-mandatory)",
        url="https://www.directives.doe.gov/directives-documents/400-series/0413.3-EGuide-20-admchg1",
        dpi=250,
    ),
    "413.3-21A-CostEstimating.pdf": dict(
        number="DOE G 413.3-21A",
        title="Cost Estimating Guide",
        cite="the Cost Estimating Guide (DOE G 413.3-21A)",
        kind="Guide (non-mandatory)",
        url="https://www.directives.doe.gov/directives-documents/400-series/0413.3-EGuide-21A",
        dpi=200,
    ),
    "EVMS-GoldCard.pdf": dict(
        number="DOE EVMS Gold Card",
        title="Earned Value Management System (EVMS) Gold Card",
        cite="the DOE EVMS Gold Card",
        kind="Quick-reference card",
        url="https://www.energy.gov/projectmanagement/articles/earned-value-management-system-evms-gold-card",
        dpi=300,
    ),
}


def ocr_page(page, dpi):
    pix = page.get_pixmap(dpi=dpi)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    return pytesseract.image_to_string(img)


def build(fname, meta):
    path = os.path.join(SRC, fname)
    doc = fitz.open(path)
    n = doc.page_count
    out_path = os.path.join(OUT, os.path.splitext(fname)[0] + ".md")
    with open(out_path, "w") as f:
        f.write(f"# {meta['number']} — {meta['title']}\n\n")
        f.write(f"- **Document:** {meta['number']}\n")
        f.write(f"- **Type:** {meta['kind']}\n")
        f.write(f"- **Cite as:** {meta['cite']}\n")
        f.write(f"- **Official source:** {meta['url']}\n")
        f.write(f"- **Pages:** {n}  •  **Extraction:** OCR (page text below; "
                f"`[p. N]` marks the PDF page).\n\n---\n")
        for i, page in enumerate(doc, start=1):
            text = ocr_page(page, meta["dpi"]).strip()
            # collapse runs of blank lines
            lines = [ln.rstrip() for ln in text.splitlines()]
            cleaned, blank = [], 0
            for ln in lines:
                if ln.strip() == "":
                    blank += 1
                    if blank <= 1:
                        cleaned.append("")
                else:
                    blank = 0
                    cleaned.append(ln)
            f.write(f"\n[p. {i}]\n\n")
            f.write("\n".join(cleaned).strip() + "\n")
            print(f"  {fname}: page {i}/{n}", flush=True)
    doc.close()
    print(f"WROTE {out_path}", flush=True)


def main():
    for fname, meta in META.items():
        if not os.path.exists(os.path.join(SRC, fname)):
            print(f"SKIP (missing): {fname}", flush=True)
            continue
        print(f"=== {fname} ===", flush=True)
        build(fname, meta)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
