"""챕터별 표 점유율 측정 + 표 종류 4분류.

각 쪽에서 세로 괘선이 덮는 세로 범위를 쪽 높이로 나눠 '표 점유율'을 재고,
표 영역을 네 종류로 분류한다:
  data(데이터표)   : 세로 4열↑ & 가로 8줄↑ 조밀 격자 — 엑셀 처리 가능
  form(양식형)     : 라벨·값·중첩형(세로 3열, 또는 데이터 기준 미달)
  callout(콜아웃)  : 작은 박스(세로 ≤2열, 점유율 <35%) — 1×1 강조 등
  block(구획)      : 큰 박스로 감싼 본문·목차(세로 ≤2열, 점유율 ≥35%)
그림·사진은 괘선이 없으면 0. 대상 PDF는 ScienceON에서 받은 KISTI 2024/2025 연차보고서 원문.
의존: poppler(pdftoppm, pdftotext), Pillow
"""
import subprocess, glob, os, json, tempfile
from PIL import Image

def render(pdf, outdir, dpi=70):
    os.makedirs(outdir, exist_ok=True)
    subprocess.run(['pdftoppm','-png','-r',str(dpi),pdf,f'{outdir}/p'], check=True)
    return sorted(glob.glob(f'{outdir}/*.png'))

def analyze(path, dark=150):
    im = Image.open(path).convert('L'); W,H = im.size
    t = im.transpose(Image.TRANSPOSE); Wt,Ht = t.size; dv = t.tobytes()
    needv = int(0.15*Wt); vtop=[]; vbot=[]; nv=0
    for r in range(Ht):
        row = dv[r*Wt:(r+1)*Wt]; best=cur=0; s=0; bs=-1
        for i,v in enumerate(row):
            if v<dark:
                if cur==0: s=i
                cur+=1
                if cur>best: best=cur; bs=s
            else: cur=0
        if best>=needv: vtop.append(bs); vbot.append(bs+best); nv+=1
    if nv<2: return (0.0,0,0,'none')
    top,bot = min(vtop),max(vbot); cov=(bot-top)/Wt
    dh = im.tobytes(); needh=int(0.45*W); hc=0; prev=-5
    for y in range(max(0,top),min(H,bot)):
        row=dh[y*W:(y+1)*W]; best=cur=0
        for v in row:
            if v<dark:
                cur+=1
                if cur>best: best=cur
            else: cur=0
        if best>=needh:
            if y-prev>3: hc+=1
            prev=y
    if nv>=4 and hc>=8: cat='data'                 # 데이터표 (초록)
    elif nv<=2:        cat='block' if cov>=0.35 else 'callout'  # 구획(빨강)/콜아웃(주황)
    else:              cat='form'                  # 양식형(파랑)
    return (round(cov,3), nv, hc, cat)

def measure(pdf,label):
    with tempfile.TemporaryDirectory() as d:
        files=render(pdf,d)
        res={i+1:analyze(f) for i,f in enumerate(files)}
    print(f"{label}: {len(res)} pages"); return res

RANGES={
 '2024':[('1.개요',27,40,0),('2.수행 과정·내용',41,124,0),('3.가 정성적 성과',125,177,0),
   ('3.나 정량적 성과',178,184,1),('3.다 계획외·기여',185,194,0),('4.기여 정도',195,197,0),
   ('5.관리·활용',198,199,0),('6.참고문헌',200,202,0)],
 '2025':[('1.개요',24,42,0),('2.수행 과정·내용',43,134,0),('3.가 정량적 성과',135,168,1),
   ('3.나 계획외·기여',169,177,0),('4.활용 계획',178,185,0),('5.참고문헌',186,187,0),('부록',188,260,1)],
}
res={'2024':measure('/tmp/kisti.pdf','2024'),'2025':measure('/tmp/kisti2025.pdf','2025')}
json.dump({y:{str(p):v for p,v in d.items()} for y,d in res.items()}, open('/tmp/tablecov2.json','w'))

CATS=['data','form','callout','block']  # 녹 파 주 빨
def agg(y):
    print(f"\n===== {y} — 표 점유율 분해 (데이터/양식/콜아웃/구획) =====")
    print(f"{'챕터':20s}{'쪽':>4s}{'전체':>6s}{'🟢데이터':>8s}{'🔵양식':>7s}{'🟠콜아웃':>8s}{'🔴구획':>7s}")
    na=[]
    for name,a,b,flag in RANGES[y]:
        ps=[res[y][p] for p in range(a,b+1) if p in res[y]]
        if not ps: continue
        n=len(ps)
        def c(cat): return sum(p[0] for p in ps if p[3]==cat)/n*100
        tot=sum(p[0] for p in ps)/n*100
        print(f"{name+('*' if flag else ' '):20s}{n:>4d}{tot:>5.0f}%{c('data'):>7.0f}%{c('form'):>6.0f}%{c('callout'):>7.0f}%{c('block'):>6.0f}%")
        if not flag and '참고문헌' not in name: na+=ps
    n=len(na)
    def c(cat): return sum(p[0] for p in na if p[3]==cat)/n*100
    tot=sum(p[0] for p in na)/n*100
    print(f"{'→ 서술챕터(정량성과·부록 제외)':24s}{n:>4d}{tot:>5.0f}%{c('data'):>7.0f}%{c('form'):>6.0f}%{c('callout'):>7.0f}%{c('block'):>6.0f}%")
agg('2024'); agg('2025')
print("\n🟢데이터=nv≥4&가로괘선≥8(엑셀OK) 🔵양식=라벨·값·중첩 🟠콜아웃=작은박스(≤2열,점유<35%) 🔴구획=큰박스로감싼본문·목차(≤2열,점유≥35%)")
