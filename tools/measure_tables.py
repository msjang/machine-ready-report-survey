"""챕터별 표 점유율 측정 — 쪽에서 세로 괘선이 덮는 세로 범위 ÷ 쪽 높이.

세로 괘선 >=2개일 때만 셈(그림·사진은 괘선 없으면 0). 박스로 감싼 본문·목차도
표로 집계됨(의도된 것). 대상 PDF는 ScienceON에서 받은 KISTI 2024/2025 연차보고서 원문.
의존: poppler(pdftoppm, pdftotext), Pillow
"""
import subprocess, glob, os, json, tempfile
from PIL import Image

def render(pdf, outdir, dpi=70):
    os.makedirs(outdir, exist_ok=True)
    subprocess.run(['pdftoppm','-png','-r',str(dpi),pdf,f'{outdir}/p'], check=True)
    return sorted(glob.glob(f'{outdir}/*.png'))

def page_table_coverage(path, dark=150, minfrac=0.15):
    """세로 괘선이 덮는 세로 범위의 비율(0~1). 세로 괘선 >=2개일 때만."""
    im = Image.open(path).convert('L')
    W, H = im.size
    t = im.transpose(Image.TRANSPOSE)          # 행=원래 열
    Wt, Ht = t.size                            # Wt=H, Ht=W
    data = t.tobytes()
    need = int(minfrac * Wt)                   # 긴 세로 run 기준(원래 H의 15%)
    vtop, vbot, nv = [], [], 0
    for r in range(Ht):                        # r = 원래 열 x
        row = data[r*Wt:(r+1)*Wt]
        best = cur = 0; bs = bstart = -1; s = 0
        for i, v in enumerate(row):
            if v < dark:
                if cur == 0: s = i
                cur += 1
                if cur > best: best, bstart = cur, s
            else:
                cur = 0
        if best >= need:
            vtop.append(bstart); vbot.append(bstart+best); nv += 1
    if nv < 2:
        return 0.0
    top, bot = min(vtop), max(vbot)
    return max(0.0, (bot - top) / Wt)

def measure(pdf, label, dpi=70):
    with tempfile.TemporaryDirectory() as d:
        files = render(pdf, d, dpi)
        cov = {i+1: round(page_table_coverage(f), 3) for i, f in enumerate(files)}
    print(f"{label}: {len(cov)} pages measured")
    return cov

RANGES = {
 '2024': {
   'front(표지~목차)': (1,26),
   '1.개요': (27,40),
   '2.수행 과정·내용': (41,124),
   '3.가 정성적 성과': (125,177),
   '3.나 정량적 성과*': (178,194),
   '4.기여 정도': (195,197),
   '5.관리·활용': (198,199),
   '6.참고문헌': (200,202),
 },
 '2025': {
   'front(표지~목차)': (1,23),
   '1.개요': (24,42),
   '2.수행 과정·내용': (43,134),
   '3.가 정량적 성과*': (135,168),
   '3.나 계획외·기여': (169,177),
   '4.활용 계획': (178,185),
   '5.참고문헌': (186,187),
   '부록*': (188,260),
 },
}

cov = {'2024': measure('/tmp/kisti.pdf','2024'),
       '2025': measure('/tmp/kisti2025.pdf','2025')}
json.dump(cov, open('/tmp/tablecov.json','w'))

def agg(year):
    print(f"\n===== KISTI {year} — 챕터별 표 점유율 =====")
    print(f"{'챕터':22s} {'쪽수':>4s} {'평균표%':>7s} {'표쪽비율':>7s}")
    for name,(a,b) in RANGES[year].items():
        vals=[cov[year][p] for p in range(a,b+1) if p in cov[year]]
        if not vals: continue
        avg=sum(vals)/len(vals)
        tablepg=sum(1 for v in vals if v>=0.4)/len(vals)
        print(f"{name:22s} {len(vals):>4d} {avg*100:>6.1f}% {tablepg*100:>6.1f}%")
agg('2024'); agg('2025')
print("\n* = 정량적 성과/부록 (본래 표 중심, 참고용)")
print("평균표% = 쪽당 세로괘선 점유율 평균, 표쪽비율 = 점유율 40%↑ 쪽의 비율")
