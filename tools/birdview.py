#!/usr/bin/env python3
"""보고서 PDF 전 쪽을 저해상 썸네일 격자(버드뷰)로 만든다.

표가 어디에 몰려 있는지, 보고서 전체가 표인지 서술인지를 한 화면에서 본다.

사용:
    python3 tools/birdview.py <report.pdf> <out.jpg> [--cols 15] [--dpi 28] [--title "..."]

의존: poppler(pdftoppm), Pillow
"""
import argparse, glob, math, os, subprocess, tempfile
from PIL import Image, ImageDraw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("out")
    ap.add_argument("--cols", type=int, default=15)
    ap.add_argument("--dpi", type=int, default=28)
    ap.add_argument("--thumb-width", type=int, default=150)
    ap.add_argument("--title", default="")
    a = ap.parse_args()

    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-png", "-r", str(a.dpi), a.pdf, f"{tmp}/p"],
                       check=True)
        files = sorted(glob.glob(f"{tmp}/*.png"))
        if not files:
            raise SystemExit("no pages rendered")
        n = len(files)
        tw = a.thumb_width
        im0 = Image.open(files[0])
        th = int(im0.height * tw / im0.width)
        rows = math.ceil(n / a.cols)
        g, top = 3, 40
        W = a.cols * tw + g * (a.cols + 1)
        H = top + rows * th + g * (rows + 1)
        sheet = Image.new("RGB", (W, H), "white")
        ImageDraw.Draw(sheet).text((g + 4, 12),
                                   f"{a.title or os.path.basename(a.pdf)} — {n} pages",
                                   fill="black")
        for i, f in enumerate(files):
            im = Image.open(f).convert("RGB").resize((tw, th))
            r, c = divmod(i, a.cols)
            sheet.paste(im, (g + c * (tw + g), top + g + r * (th + g)))
        if a.out.lower().endswith((".jpg", ".jpeg")):
            sheet.save(a.out, quality=82, optimize=True)
        else:
            sheet.save(a.out)
        print(f"{a.out}: {n} pages, {sheet.size[0]}x{sheet.size[1]}")


if __name__ == "__main__":
    main()
