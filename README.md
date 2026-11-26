# 해외 R&D 보고 체계와 기계가독성 조사

**성과를 어떤 필드로 받고, 보고서를 어떻게 만들고, 공개 DB로 어떻게 다시 보여주는가**

- 작성일: 2026.11.
- 작성자: 장민석 (msjang@kisti.re.kr)

> [!WARNING]
> 본 문서는 작성자 개인의 조사 결과이며 소속 기관의 공식 입장이 아닙니다. 각국 제도의 해석에 오류가 있을 수 있으니 인용 전 원문을 확인하시기 바랍니다.
>
> 이 저장소의 문서는 Claude(Anthropic)를 자료 수집·판독 도구로 사용해 작성했습니다. 검수를 하였지만 실수가 있을 수 있습니다. 수정이 필요한 경우 레포의 [Issue](https://github.com/msjang/machine-ready-report-survey/issues)에 남겨주세요.
>
> 인용한 각국 서식·시스템 화면·공개 페이지의 보존 사본은 [`sources/`](sources/)에, 비교 데이터는 [`data/`](data/)에 두어 원문이 사라져도 추적할 수 있게 했습니다.

## 웹에서 읽으세요

문서가 길고 표가 많습니다. 목차와 문서 간 이동이 붙은 웹 페이지가 훨씬 읽기 편합니다.

**→ [msjang.github.io/machine-ready-report-survey](https://msjang.github.io/machine-ready-report-survey/)**

저장소에는 마크다운 원본과 보존 사본·데이터만 둡니다. HTML은 GitHub Pages가 만듭니다.

## 무엇을 조사했나

KISTI는 대한민국 연구보고서가 모이는 종착지이지만, 보고서가 모이는 형식은 여전히 기계가 구조를 읽기 어려운 HWP·PDF에 머물러 있습니다. 새 표준 양식을 세우기에 앞서, 우리와 비슷한 임무를 수행하는 해외 선진 연구기관이 성과보고를 어떻게 받고 어떻게 다시 보여주는지 벤치마킹했습니다.

한국 연구보고서의 병합 표가 담는 정보를 일본·중국·미국·EU·영국이 어떻게 다루는지, 국가마다 세 층(입력 필드 · 연구보고서 · 공개 재표현)으로 비교했습니다.

## 핵심 관찰

- 한국 연구보고서는 과제 메타데이터와 성과를 양식형 병합 표에 다시 입력하게 하고, 그 보고서를 다시 시스템에 복사해 붙입니다. 같은 정보가 여러 번 입력되고 구조는 사라집니다.
- 일본·중국·미국·EU·영국은 같은 정보를 시스템 필드로 한 번 받고, 보고서와 공개 페이지를 그 필드에서 자동으로 만듭니다.
- 제안: 메타데이터는 시스템 필드로, 과제번호는 영구 주소이자 공개 API로, 보고서 본체는 구조화 소스에서 HWPX·PDF·웹으로 렌더링, 표는 데이터일 때만.

## 문서

| 문서 | 내용 |
|---|---|
| [핵심 리포트](index.md) | 문제·해외 비교·모범·제안·시점을 짧게 정리 |
| [별첨](appendix.md) | A 국가별 상세 · B 미국 DoE · C 중국 GB/T · D 초록·요약문 · E 표 사용 · F 아카이브·연구지원 · G 현장의 목소리 · H 방법·남은 질문 |
| [출처](sources.md) | 인용 원문의 URL·수집일·보존 사본 경로 |
| [작성 규칙](PROCESS.md) | 수집·정정·커밋 규칙 |

## 관련 자료

- AAiCON 2026 발제 (한국 공문서 양식 개혁) — <https://msjang.github.io/aaicon26-kgovdoc-reform/>
- KrIGF 2026 세션 (사전 법적 확신 메커니즘) — <https://msjang.github.io/krigf26-no-action-letter/>
- 폰트 EULA 조항 조사 — <https://msjang.github.io/krigf26-font-eula-survey/>
- pypandoc-hwpx — <https://github.com/msjang/pypandoc-hwpx>

## 라이선스

조사 문서는 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ko). 인용한 각국 서식·문언의 권리는 각 권리자에게 있습니다.
