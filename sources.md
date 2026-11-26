---
description: "인용한 각국 서식·시스템 화면·공개 페이지의 원문 URL, 수집일, 보존 사본 목록."
---

# 출처 목록

- 수집일: 2026-11-26 (별도 표기 없는 경우)
- 원칙: 인용한 각국 서식·시스템 화면·공개 페이지는 원문 URL·수집일·수집 방법과 함께 보존 사본을 남긴다. 원문 사이트가 개편·삭제되어도 [`sources/`](sources/)의 사본으로 확인할 수 있다.

## 수집·보존 방법

- **HTML 화면**: `curl`로 원본을 받고, 내용을 JavaScript로 채우는 페이지가 많아 Chrome(헤드리스)으로 렌더링된 DOM을 받아 텍스트(`.md`)로 보존한다. 입력 필드 구조가 드러나는 화면은 스크린샷(`.png`)을 함께 둔다.
- **PDF**: 원본을 받아 `pdftotext`로 전체 텍스트(`.txt.md`)를 보존한다. 1MB 이하 원본은 `.pdf`도 함께 두고, 1MB를 넘으면 용량을 줄이려고 전체 텍스트만 남긴다.
- **Word(.doc)**: `soffice`로 PDF 변환 후 텍스트·대표 쪽 이미지를 보존한다.
- 수집에 쓴 도구와 대상 목록은 [`tools/snapshot.sh`](tools/snapshot.sh) · [`tools/sources.tsv`](tools/sources.tsv)에 있다.
- 접속이 되지 않은 원문은 아래 표에 사유를 적고, 대체 가능한 경우 같은 구조의 접속 가능한 사본으로 보존했다.

## 일본 — 科研費(JSPS) · KAKEN

| 문서 | 원문 | 보존 사본 |
|---|---|---|
| JSPS 체험판 — 연구실적 개요 입력 | [원문](https://www-shinsei.jsps.go.jp/kaken/kakenhi_taiken/taiken_free/kofu/shinsei/pages/jissekiH/inputGaiyo.html) | [텍스트](sources/japan/jsps-jisseki-gaiyo_2026-11-26.md) · [화면](sources/japan/jsps-jisseki-gaiyo_2026-11-26.png) |
| JSPS 체험판 — 연구발표 입력 | [원문](https://www-shinsei.jsps.go.jp/kaken/kakenhi_taiken/taiken_free/kofu/shinsei/pages/jissekiH/inputHappyo.html) | [텍스트](sources/japan/jsps-jisseki-happyo_2026-11-26.md) · [화면](sources/japan/jsps-jisseki-happyo_2026-11-26.png) |
| JSPS 체험판 — 산업재산권 입력 | [원문](https://www-shinsei.jsps.go.jp/kaken/kakenhi_taiken/taiken_free/kofu/shinsei/pages/jissekiH/inputZaisanken.html) | [텍스트](sources/japan/jsps-jisseki-zaisanken_2026-11-26.md) · [화면](sources/japan/jsps-jisseki-zaisanken_2026-11-26.png) |
| 様式 F-7-2 실적보고서 기재례 | [원문](https://www.jsps.go.jp/j-grantsinaid/16_rule/data/29_dl/f-07-2_rei_chui.pdf) | [PDF](sources/japan/jsps-yoshiki-f7-2_2026-11-26.pdf) · [텍스트](sources/japan/jsps-yoshiki-f7-2_2026-11-26.txt.md) · [대표 쪽](sources/japan/jsps-yoshiki-f7-2_2026-11-26.png) |
| 様式 C-41 제출 점검표 | [원문](https://www.jsps.go.jp/file/storage/kaken_g_4594/r7jisseki_shourei_checklist_kikan.pdf) | [PDF](sources/japan/jsps-c41-checklist_2026-11-26.pdf) · [텍스트](sources/japan/jsps-c41-checklist_2026-11-26.txt.md) |
| KAKEN 과제 페이지 (18H02839) | [원문](https://kaken.nii.ac.jp/ja/grant/KAKENHI-PROJECT-18H02839/) | [텍스트](sources/japan/kaken-project-18H02839_2026-11-26.md) · [화면](sources/japan/kaken-project-18H02839_2026-11-26.png) |
| KAKEN 첫 화면 | [원문](https://kaken.nii.ac.jp/) | [텍스트](sources/japan/kaken-top_2026-11-26.md) |

## 중국 — 국가과기계획 과기보고 · NSTRS

| 문서 | 원문 | 보존 사본 |
|---|---|---|
| 과학기술상 추천서 경제효익 표 | 원래 인용 [저장성 서식](https://kyc.hznu.edu.cn/upload/Attach/mrbj/302089459.doc) **(404, 삭제됨)** → 동일 구조 [동지대 공개본](https://kyy.tongji.edu.cn/) | [표 이미지·텍스트](sources/china/award-recommendation-economic-benefit_2026-11-26.txt.md) · [표 쪽 화면](sources/china/award-recommendation-economic-benefit_2026-11-26.png) · [PDF](sources/china/award-recommendation_2026-11-26.pdf) |
| GB/T 7713.3-2014 과기보고 작성규칙 | [원문](https://lib.tsinghua.edu.cn/wj/GBT7713_3-2014.pdf) | [PDF](sources/china/gbt-7713-3-2014_2026-11-26.pdf) · [텍스트](sources/china/gbt-7713-3-2014_2026-11-26.txt.md) |
| 과기보고 메타데이터 규범 (GB/T 30535) | [원문](https://most.gov.cn/ztzl/jlkjbg/kjbgxxjl/201409/P020140915541814539196.pdf) | [PDF](sources/china/gbt-30535-metadata_2026-11-26.pdf) · [텍스트](sources/china/gbt-30535-metadata_2026-11-26.txt.md) |
| 중대전항 과기보고 작성 요점 (보고서 번호 형식) | [원문](https://www.most.gov.cn/ztzl/zdzx/tztg/201405/P020140526386090154713.pdf) | [텍스트](sources/china/most-report-number_2026-11-26.txt.md) (원본 1MB 초과, 텍스트만) |
| 国家科技管理信息系统 이용 안내 | [원문](https://service.most.gov.cn/u/cms/static/201806/12145654y1jn.pdf) | [PDF](sources/china/most-nstmis-manual_2026-11-26.pdf) · [텍스트](sources/china/most-nstmis-manual_2026-11-26.txt.md) |
| 과기보고 공개 유예 안내 | [원문](https://kjc.seu.edu.cn/_upload/article/files/0b/26/f18499fc415b8d6b323a58e3d2f0/98a22588-7936-4af0-8027-fbf6e754c561.pdf) | [PDF](sources/china/seu-embargo_2026-11-26.pdf) · [텍스트](sources/china/seu-embargo_2026-11-26.txt.md) |
| 후허하오터시 과제 검수 안내 | [원문](https://lawinsider.com/zh/contracts/fZbOhHhewDc) | [텍스트](sources/china/huhhot-acceptance_2026-11-26.md) |
| 国家科技报告服务系统 첫 화면 | [원문](https://www.nstrs.cn/) | [텍스트](sources/china/nstrs-top_2026-11-26.md) · [화면](sources/china/nstrs-top_2026-11-26.png) |

## 미국 — RPPR · NSF · SBIR · DoE(ESnet)

| 문서 | 원문 | 보존 사본 |
|---|---|---|
| ESnet HEP Network Requirements Review (2024) | [원문 PDF 427쪽](https://www.es.net/assets/Uploads/20251001-HEP-RR-Final.pdf) | [목차 텍스트](sources/usa/esnet-hep-rr-toc_2026-11-26.md) · [목차 쪽](sources/usa/esnet-hep-rr-toc_2026-11-26.png) · [본문 쪽](sources/usa/esnet-hep-rr-body_2026-11-26.png) (전체 21.5MB는 미커밋) |
| eRA Commons RPPR C. Products | [원문](https://www.era.nih.gov/erahelp/commons/Commons/rppr/Forms/C.Products.htm) | [텍스트](sources/usa/era-rppr-c-products_2026-11-26.md) · [화면](sources/usa/era-rppr-c-products_2026-11-26.png) |
| NIH RPPR 질문 목록 | [원문](https://medschool.ucla.edu/sites/g/files/oketem306/files/media/documents/NIH-RPPR-Progress-Report-Questions.pdf) | [PDF](sources/usa/nih-rppr-questions_2026-11-26.pdf) · [텍스트](sources/usa/nih-rppr-questions_2026-11-26.txt.md) |
| SBIR Company Commercialization Report 안내 | [원문](https://www.sbir.gov/sites/default/files/Guide_for_completing_commercialization_Report_SBIR_Gov.pdf) | [텍스트](sources/usa/sbir-commercialization-guide_2026-11-26.txt.md) (원본 1MB 초과, 텍스트만) |
| SBIR 사업화율 벤치마크 | [원문](https://www.sbir.gov/performance-benchmarks) | [텍스트](sources/usa/sbir-performance-benchmarks_2026-11-26.md) · [화면](sources/usa/sbir-performance-benchmarks_2026-11-26.png) |
| NSF SBIR Phase II 보고 서식 (2019년 이전) | [원문](https://seedfund.nsf.gov/assets/files/awardees/Phase_II_Reporting_Pre-2019.pdf) | [PDF](sources/usa/nsf-sbir-phase2-pre2019_2026-11-26.pdf) · [텍스트](sources/usa/nsf-sbir-phase2-pre2019_2026-11-26.txt.md) |
| NSF Project Outcomes Report 안내 | [원문](https://nsf.gov/awards/report-your-outcomes) | [텍스트](sources/usa/nsf-report-your-outcomes_2026-11-26.md) · [화면](sources/usa/nsf-report-your-outcomes_2026-11-26.png) |
| NSF POR 작성 가이드 | [원문](https://resources.research.gov/common/attachment/Desktop/PORPreparingandSubmittingQuickReferenceGuide.pdf) | [텍스트](sources/usa/nsf-por-guide_2026-11-26.txt.md) (원본 1MB 초과, 텍스트만) |
| NSF DCL (인용 정보 자동 첨부) | [원문](https://www.nsf.gov/funding/opportunities/dcl-national-science-foundation-directorate-social-behavioral/nsf16-141) | [텍스트](sources/usa/nsf-dcl-citation_2026-11-26.md) |
| NIH RPPR 작성 안내 (A–I 섹션) | 원 UMD 사본 404 → [eRA: How Do I Fill Out the RPPR Forms](https://www.era.nih.gov/erahelp/commons/Commons/rppr/rppr_fields.htm) · [공식 Instruction Guide](https://grants.nih.gov/grants/rppr/rppr_instruction_guide.pdf) | [eRA 화면 보존](sources/usa/era-rppr-fields_2026-11-26.png) (섹션 A–I 나열) |
| SBIR 사업화 보고 양식 정의 (OMB) | [원문](https://omb.report/icr/202610-3245-001/doc/173864100.pdf) | [PDF](sources/usa/sbir-commercialization-database_2026-11-26.pdf) · [텍스트](sources/usa/sbir-commercialization-database_2026-11-26.txt.md) (수집 시 403, 원문 직접 받아 제공) |

## EU — Horizon Europe · ERC · CORDIS

| 문서 | 원문 | 보존 사본 |
|---|---|---|
| EC Continuous reporting 매뉴얼 | [원문](https://webgate.ec.europa.eu/funding-tenders-opportunities/spaces/OM/pages/1867968/Continuous+reporting+on+milestones+deliverables) | [텍스트](sources/eu/ec-continuous-reporting_2026-11-26.md) |
| Horizon Europe 정기보고 템플릿 | [원문](https://backend.uni-heidelberg.de/de/dokumente/horizon-europe-periodic-report-template/download) | [텍스트](sources/eu/heidelberg-he-periodic-template_2026-11-26.txt.md) (원본 1MB 초과, 텍스트만) |
| ERC 재무보고 안내 (템플릿 자동 채움) | [원문](https://erc.europa.eu/manage-your-project/financial-reporting) | [텍스트](sources/eu/erc-financial-reporting_2026-11-26.md) |
| IHI 과제 문서 (정기보고 기한) | [원문](https://www.ihi.europa.eu/resources-projects/project-documents) | [텍스트](sources/eu/ihi-project-documents_2026-11-26.md) |
| H2020 확산·활용 보고 (Vinnova) | [원문](https://www.vinnova.se/globalassets/mikrosajter/horisont-2020/dokument/h2020_sweden-20112018_disseminationexploitation.pdf) | [텍스트](sources/eu/vinnova-h2020-dissemination_2026-11-26.txt.md) (원본 1MB 초과, 텍스트만) |
| CORDIS 첫 화면 | [원문](https://cordis.europa.eu/) | [텍스트](sources/eu/cordis-top_2026-11-26.md) · [화면](sources/eu/cordis-top_2026-11-26.png) |
| ERC 과학보고 가이드라인 | [원문](https://erc.europa.eu/system/files/2024-04/ERC-Scientific-Reporting-Guidelines.pdf) | **404 — 경로 변경.** ERC 사이트에서 최신본 확인 필요 |
| H2020 확산·활용 보고 (Business Finland) | [원문](https://www.businessfinland.fi/4ab659/globalassets/finnish-customers/horizon-2020/esitysaineistot/dissemination-and-exploitation-under-h2020_rommens.pdf) | **404 — 경로 변경** |

## 영국 — Researchfish · Gateway to Research

| 문서 | 원문 | 보존 사본 |
|---|---|---|
| UKRI 보고 항목 (공통 성과 유형) | [원문](https://www.ukri.org/manage-your-award/reporting-your-projects-outcomes/what-you-need-to-report) | [텍스트](sources/uk/ukri-what-to-report_2026-11-26.md) · [화면](sources/uk/ukri-what-to-report_2026-11-26.png) |
| UKRI 성과보고 안내 | [원문](https://www.ukri.org/manage-your-award/reporting-your-projects-outcomes/) | [텍스트](sources/uk/ukri-reporting_2026-11-26.md) |
| Researchfish Common Question Set (Warwick) | [원문](https://warwick.ac.uk/services/ris/systems/researchfish/research_outcomes_common_question_set.pdf) | [PDF](sources/uk/warwick-common-question-set_2026-11-26.pdf) · [텍스트](sources/uk/warwick-common-question-set_2026-11-26.txt.md) |
| Researchfish 공통 성과 유형 개요 (Warwick) | [원문](https://warwick.ac.uk/services/ris/systems/researchfish/researchfish_common_outcomes_overview_december2016.pdf) | [PDF](sources/uk/warwick-common-outcomes-overview_2026-11-26.pdf) · [텍스트](sources/uk/warwick-common-outcomes-overview_2026-11-26.txt.md) |
| Researchfish Common Question Set (UWE) | [원문](https://www.uwe.ac.uk/-/media/uwe/documents/research/research-outcomes-common-question-set.pdf) | [PDF](sources/uk/uwe-common-question-set_2026-11-26.pdf) · [텍스트](sources/uk/uwe-common-question-set_2026-11-26.txt.md) |
| Cambridge 성과보고·Researchfish 안내 | [원문](https://www.research-services.admin.cam.ac.uk/manage-project/share-your-research/research-outcomes-and-researchfish) | [텍스트](sources/uk/cambridge-research-outcomes_2026-11-26.md) |
| Cambridge Researchfish 운영 워크숍 | [원문](https://www.research-services.admin.cam.ac.uk/sites/default/files/Researchfish%20Node%20Admin%20Workshop%2004%20Dec%202025.pdf) | [PDF](sources/uk/cambridge-researchfish-workshop_2026-11-26.pdf) · [텍스트](sources/uk/cambridge-researchfish-workshop_2026-11-26.txt.md) |
| CASRAI Researchfish 가이드 (스핀아웃 정의) | [원문](https://www.casrai.org/guides/researchfish) | [텍스트](sources/uk/casrai-researchfish_2026-11-26.md) |
| EPSRC Research Outcomes 2022 | [원문](https://www.ukri.org/wp-content/uploads/2023/05/EPSRC-04052023-EPSRC-Research-Outcomes-2022-Final.pdf) | [텍스트](sources/uk/epsrc-outcomes-2022_2026-11-26.txt.md) (원본 11.5MB, 텍스트만) |
| Gateway to Research 첫 화면 | [원문](https://gtr.ukri.org/) | [텍스트](sources/uk/gtr-top_2026-11-26.md) · [화면](sources/uk/gtr-top_2026-11-26.png) |
| Researchfish 2027 종료 안내 | [원문](https://www.dementiaresearcher.nihr.ac.uk/researchfish-closure-2027/) | [텍스트](sources/uk/researchfish-closure_2026-11-26.md) |
| LSE Researchfish 안내 (실현 성과만 보고) | [원문](https://info.lse.ac.uk/staff/divisions/research-and-innovation/research/Researchfish.aspx) | [텍스트](sources/uk/lse-researchfish_2026-11-26.md) |

## 한국 — 기준 보고서

| 문서 | 원문 | 보존 사본 |
|---|---|---|
| KISTI 연차보고서 (ScienceON 과제) | [원문](https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400000471) | [과제 페이지](sources/korea/kisti-scienceon-por_2026-11-26.md) · [화면](sources/korea/kisti-scienceon-por_2026-11-26.png) |
| KISTI 연차보고서 2024 원문 (202쪽) | ScienceON 뷰어 내부 `orgDocDown.do` (TRKO202400000471) | [전체 텍스트](sources/korea/kisti-kreonet-report_2026-11-26.txt.md) · [초록](sources/korea/kisti-kreonet-abstract_2026-11-26.png) · [요약문](sources/korea/kisti-kreonet-summary_2026-11-26.png) · [정량성과 표](sources/korea/kisti-kreonet-quant-table_2026-11-26.png) · [SUMMARY 박스](sources/korea/kisti-kreonet-summary-boxed_2026-11-26.png) · [목차 박스](sources/korea/kisti-kreonet-toc-boxed_2026-11-26.png) (전체 39MB는 미커밋) |
| KISTI 연차보고서 2025 원문 (260쪽) | [ScienceON 과제 TRKO202600020985](https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202600020985) · 뷰어 내부 `orgDocDown.do` | [전체 텍스트](sources/korea/kisti-2025-report_2026-11-26.txt.md) · [초록](sources/korea/kisti-2025-abstract_2026-11-26.png) · [2024 vs 2025 초록 비교](sources/korea/kisti-abstract-2024-vs-2025_2026-11-26.png) · [목차(표 박스, 1쪽)](sources/korea/kisti-2025-toc-boxed_2026-11-26.png) · [SUMMARY(표 박스)](sources/korea/kisti-2025-summary-boxed_2026-11-26.png) (전체 20MB는 미커밋) |

## 연구망 운영 기관의 연차보고서 (대응 기관 비교)

| 문서 | 원문 | 보존 사본 |
|---|---|---|
| 国立情報学研究所年報 2024년도 (NII, 280쪽) | [원문](https://www.nii.ac.jp/about/upload/2024-nii-nenpou.pdf) · [연보 목록](https://www.nii.ac.jp/about/overview/annualreport/) | [전체 텍스트](sources/japan/nii-nenpou-2024_2026-11-26.txt.md) · [버드뷰](images/birdview-japan-nii.jpg) (PDF 4MB는 미커밋) |
| ESnet 2024 Annual Report (48쪽) | [원문](https://www.es.net/assets/pubs_presos/ESnet-2024-AR_Cover+Body_digital_fnl_25-SN-10463-.pdf) · [웹 판](https://annualreports.es.net/) | [전체 텍스트](sources/usa/esnet-ar-2024_2026-11-26.txt.md) · [버드뷰](images/birdview-esnet-ar.jpg) (PDF 23MB는 미커밋) |
| CNIC 2025년도 부서 결산서 (26쪽) | [원문](https://cnic.cas.cn/xxgk/bmysgk/202608/P020260810333617128671.pdf) | [전체 텍스트](sources/china/cnic-juesuan-2025_2026-11-26.txt.md) · [버드뷰](images/birdview-china-cnic.jpg) (PDF 1.4MB는 미커밋) |
| CNIC 정보공개 연보 2023 (활동 보고서 아님) | [원문](https://cnic.cas.cn/xxgk/xxgknb/202403/t20240315_7035827.html) | 본문 요약은 [별첨 E](appendix-e-tables.md) |
| GÉANT 연차보고서 (웹 판) | [ar.geant.org](https://ar.geant.org/) | 웹 전용, 미보존 |

## 접속 실패·대체 요약

| 문서 | 사유 | 조치 |
|---|---|---|
| 저장성 과기상 추천서 (.doc) | 404 삭제 | 동일 구조 동지대 공개본으로 복구·보존 |
| NIH RPPR 안내 (UMD) | 404 삭제 | eRA 공식 페이지·Instruction Guide로 대체 |
| SBIR 양식 정의 (OMB) | 403 (해결) | 원문을 직접 받아 sources/usa/ 에 보존 |
| ERC 과학보고 가이드라인 | 404 경로 변경 | ERC 사이트에서 최신본 재확인 필요 |
| H2020 확산·활용 (Business Finland) | 404 경로 변경 | Vinnova 자료로 동일 내용 확인 |
