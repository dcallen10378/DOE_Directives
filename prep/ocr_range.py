#!/usr/bin/env python3
"""OCR a contiguous page range of one PDF to a partial text file.

Usage: ocr_range.py <pdf> <start_idx> <end_idx_excl> <dpi> <out_partial>
Writes `[p. N]` + page text blocks so partials can be concatenated in order.
"""
import sys, io
import fitz
import pytesseract
from PIL import Image

path, start, end, dpi, out = (
    sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
)
doc = fitz.open(path)
with open(out, "w") as f:
    for i in range(start, end):
        pix = doc[i].get_pixmap(dpi=dpi)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img).strip()
        cleaned, blank = [], 0
        for ln in (l.rstrip() for l in text.splitlines()):
            if ln.strip() == "":
                blank += 1
                if blank <= 1:
                    cleaned.append("")
            else:
                blank = 0
                cleaned.append(ln)
        f.write(f"\n[p. {i+1}]\n\n")
        f.write("\n".join(cleaned).strip() + "\n")
        print(f"range {start}-{end}: page {i+1}", flush=True)
print(f"PART DONE {start}-{end}", flush=True)
