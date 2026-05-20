import fitz, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
doc = fitz.open(r"d:\COLLEGE\MDes Thesis\Drishti_Thesis_Template\draft2_ai_review.pdf")

# Method 1: colored spans
print("=== COLORED TEXT SPANS ===")
found = False
for i, page in enumerate(doc):
    blocks = page.get_text("dict")["blocks"]
    for b in blocks:
        if b.get("type") == 0:
            for line in b.get("lines", []):
                for span in line.get("spans", []):
                    color = span.get("color", 0)
                    if color != 0:
                        found = True
                        txt = span["text"][:150]
                        print(f"Page {i+1} | color={hex(color)} | {txt}")
if not found:
    print("No colored text spans found.")

# Method 2: drawings/rectangles with fill color (highlight backgrounds)
print("\n=== HIGHLIGHT RECTANGLES (drawings) ===")
for i, page in enumerate(doc):
    paths = page.get_drawings()
    for path in paths:
        if path.get("fill") and path["fill"] != (1,1,1) and path["fill"] != (0,0,0):
            fill = path["fill"]
            rect = path["rect"]
            # Get text inside this rect
            clip_text = page.get_text("text", clip=rect).strip().replace("\n", " ")
            if clip_text:
                print(f"Page {i+1} | fill={fill} | rect={rect} | text: {clip_text[:200]}")

print("\n=== DONE ===")
