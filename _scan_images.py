import re
from pathlib import Path

root = Path(r"E:\pack\solana\sim")
htmls = [p for p in root.rglob("*.html") if "wp-content" not in str(p) and "wp-includes" not in str(p)]
print("HTML count", len(htmls))
pat = re.compile(r"""(?:src|content)=["']([^"']+\.(?:png|jpe?g|webp|svg|gif))""", re.I)
for h in htmls:
    text = h.read_text(encoding="utf-8", errors="ignore")
    imgs = pat.findall(text)
    uniq = []
    for i in imgs:
        i = i.split()[0]
        if i.startswith("http") or i.startswith("data:"):
            continue
        if i not in uniq:
            uniq.append(i)
    print("\n===", h.relative_to(root), "imgs", len(uniq))
    for i in uniq:
        print(i)
