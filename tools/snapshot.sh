#!/usr/bin/env bash
# 원문 스냅샷 보존 도구
# tools/sources.tsv 를 읽어 각 원문을 sources/<country>/ 에 보존한다.
#   html : 텍스트 스냅샷(.md) + (shot=y 면) 스크린샷(.png)
#   pdf  : 원본 PDF 보존(.pdf) + 추출 텍스트 사이드카(.txt)
#   doc  : soffice 로 PDF 변환해 보존 + 추출 텍스트
#   bin  : 내려받아 파일 형식 판별 후 pdf/doc 처리
# 사용: tools/snapshot.sh [country]   (country 생략 시 전부)
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TSV="$ROOT/tools/sources.tsv"
DATE="$(date +%Y-%m-%d)"
UA="Mozilla/5.0 (research snapshot; machine-ready-report-survey; +https://github.com/msjang/machine-ready-report-survey)"
FILTER="${1:-}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

fetch() { # url outfile
  curl -sS -L -A "$UA" --max-time 90 --max-filesize 40000000 \
       --retry 1 -o "$2" -w "%{http_code}" "$1" 2>/dev/null
}

header() { # title url kind > writes to stdout
  printf '# %s\n\n- 출처: %s\n- 수집일: %s\n- 수집 방법: %s\n- 성격: 공개 문서의 보존 사본. 원문 권리는 각 권리자에게 있음\n\n---\n\n' \
    "$1" "$2" "$DATE" "$3"
}

printf '%-28s %-5s %-6s %s\n' SLUG KIND HTTP STATUS
printf '%.0s-' {1..70}; echo

grep -vE '^\s*#|^\s*$' "$TSV" | while IFS=$'\t' read -r country slug kind shot url title; do
  [ -z "$slug" ] && continue
  [ -n "$FILTER" ] && [ "$FILTER" != "$country" ] && continue
  outdir="$ROOT/sources/$country"; mkdir -p "$outdir"
  base="${slug}_${DATE}"
  raw="$TMP/$base.raw"
  code=$(fetch "$url" "$raw")
  status="ok"

  case "$kind" in
    html)
      if [ "$code" = "200" ] && [ -s "$raw" ]; then
        # JS 로 내용을 채우는 페이지가 많아, 렌더링된 DOM 을 Chrome 으로 받아 추출한다.
        dom="$TMP/$base.dom.html"
        timeout 110 google-chrome --headless=new --disable-gpu --no-sandbox \
          --dump-dom --virtual-time-budget=9000 "$url" > "$dom" 2>/dev/null
        [ -s "$dom" ] || cp "$raw" "$dom"
        { header "$title" "$url" "curl + Chrome(렌더 DOM) + pandoc(html→gfm)"; \
          pandoc -f html -t gfm --wrap=none "$dom" 2>/dev/null \
            | sed 's/\\$//' | grep -vE '^\s*(!\[\]\(.*spacer.*\)|<div|</div>|<img)' \
            | cat -s; } > "$outdir/$base.md"
        if [ "$shot" = "y" ]; then
          timeout 110 google-chrome --headless=new --disable-gpu --no-sandbox \
            --hide-scrollbars --force-device-scale-factor=1 --window-size=1280,2400 \
            --virtual-time-budget=8000 --screenshot="$outdir/$base.png" "$url" >/dev/null 2>&1 \
            || status="md ok / shot FAIL"
        fi
      else status="FETCH FAIL"; fi
      ;;
    pdf)
      if [ "$code" = "200" ] && [ -s "$raw" ] && head -c4 "$raw" | grep -q "%PDF"; then
        cp "$raw" "$outdir/$base.pdf"
        { header "$title" "$url" "curl + pdftotext"; echo '```text'; \
          pdftotext -layout "$raw" - 2>/dev/null | head -400; echo '```'; } > "$outdir/$base.txt.md"
      else status="FETCH FAIL (code=$code)"; fi
      ;;
    doc)
      if [ "$code" = "200" ] && [ -s "$raw" ]; then
        cp "$raw" "$TMP/$slug.doc"
        soffice --headless --convert-to pdf --outdir "$TMP" "$TMP/$slug.doc" >/dev/null 2>&1
        if [ -f "$TMP/$slug.pdf" ]; then
          cp "$TMP/$slug.pdf" "$outdir/$base.pdf"
          { header "$title" "$url" "curl + soffice(doc→pdf) + pdftotext"; echo '```text'; \
            pdftotext -layout "$TMP/$slug.pdf" - 2>/dev/null | head -400; echo '```'; } > "$outdir/$base.txt.md"
        else status="DOC CONVERT FAIL"; fi
      else status="FETCH FAIL"; fi
      ;;
    bin)
      if [ "$code" = "200" ] && [ -s "$raw" ]; then
        ft=$(file -b "$raw")
        if head -c4 "$raw" | grep -q "%PDF"; then
          cp "$raw" "$outdir/$base.pdf"
          { header "$title" "$url" "curl + pdftotext"; echo '```text'; \
            pdftotext -layout "$raw" - 2>/dev/null | head -400; echo '```'; } > "$outdir/$base.txt.md"
        else
          cp "$raw" "$TMP/$slug.bin"
          soffice --headless --convert-to pdf --outdir "$TMP" "$TMP/$slug.bin" >/dev/null 2>&1
          if [ -f "$TMP/$slug.pdf" ]; then
            cp "$TMP/$slug.pdf" "$outdir/$base.pdf"
            { header "$title" "$url" "curl + soffice(→pdf) + pdftotext"; echo '```text'; \
              pdftotext -layout "$TMP/$slug.pdf" - 2>/dev/null | head -400; echo '```'; } > "$outdir/$base.txt.md"
          else
            cp "$raw" "$outdir/$base.bin"; status="saved bin ($ft)"
          fi
        fi
      else status="FETCH FAIL"; fi
      ;;
  esac
  printf '%-28s %-5s %-6s %s\n' "$slug" "$kind" "$code" "$status"
done
