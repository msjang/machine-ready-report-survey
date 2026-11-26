# ESnet HEP Network Requirements Review: Final Report (2024) — 목차 발췌

- 출처: https://www.es.net/assets/Uploads/20251001-HEP-RR-Final.pdf
- 수집일: 2026-11-26
- 수집 방법: curl + pdftotext (목차 쪽)
- 성격: 공개 보고서(LBNL-2001696)의 구조 보존 발췌. 전체 427쪽·21.5MB 원본은 용량 때문에 레포에 넣지 않고 원문 URL과 대표 쪽 이미지로 대신함
- 비고: 전체 원본은 Internet Archive(web.archive.org) 보존을 권장

---

```text
Table of Contents
Disclaimer							                                                 II

Participants and Contributors                                    III

Report Editors			                                                VI

1 Executive Summary                                               1
   1.1 Summary of Review Findings                                 3
       1.1.1 Facility Management and Readiness                    3
       1.1.2 Scientific Data Management                           3
       1.1.3 Scientific Workflow                                  3
       1.1.4 Computational and Storage Requirements               4
       1.1.5 Remote Collaboration and Operational Requirements    4
       1.1.6 Multifacility Computational Workflows                4
       1.1.7 Networking for Local and Wide-Area Data Mobility     5
       1.1.8 Emerging Needs                                       5
       1.1.9 IRI Responsiveness                                   6
   1.2 Summary of Review Actions                                  6
       1.2.1 Facility Management and Readiness                    6
       1.2.2 Scientific Data Management                           6
       1.2.3 Scientific Workflow                                  7
       1.2.4 Computational and Storage Requirements               7
       1.2.5 Remote Collaboration and Operational Requirements    7
       1.2.6 Multifacility Computational Workflows                7
       1.2.7 Networking for Local and Wide-Area Data Mobility     8
       1.2.8 Emerging Needs                                       8
       1.2.9 IRI Responsiveness                                   8

2 Requirements Review Overview                                    9
   2.1 Purpose and Process                                        9
   2.2 Structure			                                               9
       2.2.1 Background                                          10
       2.2.2 Case Study Methodology                              10
   2.3 ESnet				                                                 12
   2.4 About ASCR		                                              12
   2.5 About the Office of HEP                                   12

3 Assessment of 2020 HEP Requirement Review                      14
   3.1 Prior Action Items                                        14
   3.2 Assessment 		                                             14
       3.2.1 ESnet Actions                                       14
       3.2.2 DOE SC Actions                                      15

High Energy Physics Network Requirements Review: Final Report          VII
4 Review Findings		                                                          17
   4.1 Facility Management and Readiness                                     17
   4.2 Scientific Data Management                                            21
   4.3 Scientific Workflow                                                   26
   4.4 Computational and Storage Requirements                                32
   4.5 Remote Collaboration and Operational Requirements                     36
   4.6 Multifacility Computational Workflows                                 38
   4.7 Networking for Local and Wide-Area Data Mobility                      40
   4.8 Emerging Needs                                                        44
   4.9 IRI Responsiveness                                                    49

5 Review Actions		                                                           53
   5.1 Facility Management and Readiness                                     53
   5.2 Scientific Data Management                                            54
   5.3 Scientific Workflow                                                   54
   5.4 Computational and Storage Requirements                                55
   5.5 Remote Collaboration and Operational Requirements                     56
   5.6 Multifacility Computational Workflows                                 57
   5.7 Networking for Local and Wide-Area Data Mobility                      57
   5.8 Emerging Needs                                                        62
   5.9 IRI Responsiveness                                                    64

6 HEP Case Studies                                                           66
   6.1 Cosmological Simulation Research                                      66
       6.1.1 Discussion Summary                                              67
       6.1.2 Cosmological Simulation Research: Experiment Profile            70
          6.1.2.1 Science Background                                         70
          6.1.2.2 Collaborators                                              71
          6.1.2.3 IRI Readiness                                              72
          6.1.2.4 Instruments and Facilities                                 72
          6.1.2.5 Generalized Process of Science                             73
          6.1.2.6 Remote Science Activities                                  73
          6.1.2.7 Software Infrastructure                                    74
          6.1.2.8 Network and Data Architecture                              74
          6.1.2.9 Emerging Technology Use                                    74
             6.1.2.9.1 Cloud Services                                        74
             6.1.2.9.2 Artificial Intelligence and ML                        75
             6.1.2.9.3 Wireless or Distributed Location Science Activities   75
          6.1.2.10 Data-Related Resource Constraints                         75
          6.1.2.11 Data Mobility Endpoints                                   75
          6.1.2.12 Outstanding Issues                                        75
          6.1.2.13 Facility Profile Contributors                             76

High Energy Physics Network Requirements Review: Final Report                     VIII
   6.2 DESI				                                                                      77
       6.2.1 Discussion Summary                                                      77
       6.2.2 DESI: Experiment Profile                                                80
          6.2.2.1 Science Background                                                 80
          6.2.2.2 Collaborators                                                      81
          6.2.2.3 IRI Readiness                                                      82
          6.2.2.4 Instruments and Facilities                                         82
          6.2.2.5 Generalized Process of Science                                     83
          6.2.2.6 Remote Science Activities                                          83
          6.2.2.7 Software Infrastructure                                            83
          6.2.2.8 Network and Data Architecture                                      84
          6.2.2.9 Emerging Technology Use                                            84
             6.2.2.9.1 Cloud Services                                                84
             6.2.2.9.2 AI and ML                                                     85
             6.2.2.9.3 Wireless or Distributed Location Science Activities           85
          6.2.2.10 Data-Related Resource Constraints                                 85
          6.2.2.11 Data Mobility Endpoints                                           85
          6.2.2.12 Outstanding Issues                                                85
          6.2.2.13 Facility Profile Contributors                                     86
   6.3 Vera C. Rubin Observatory                                                     87
       6.3.1 Discussion Summary                                                      87
       6.3.2 Vera C. Rubin Observatory: Facility Profile                             91
          6.3.2.1 Science Background                                                 91
          6.3.2.2 Collaborators                                                      92
             6.3.2.2.1 North-South Networking                                        93
             6.3.2.2.2 National and International Networking                         94
          6.3.2.3 IRI Readiness                                                      94
          6.3.2.4 Instruments and Facilities                                         95
          6.3.2.5 Generalized Process of Science                                     96
          6.3.2.6 Remote Science Activities                                          96
          6.3.2.7 Software Infrastructure                                            97
               6.3.2.7.1.1 Data and Software Products                                97
                6.3.2.7.1.1.1 Prompt Products Production                             97
                6.3.2.7.1.1.2 Data-Release Production                                99
                6.3.2.7.1.1.3 Calibration and Ancillary Data                        101
                6.3.2.7.1.1.4 Education and Public Outreach (EPO) Data Products     101
                6.3.2.7.1.1.5 Software and Documentation                            101
               6.3.2.7.1.2 Data Rights                                              102
               6.3.2.7.1.3 Science Platform                                         102
                6.3.2.7.1.3.1 Science Platform Resource Allocation                  103
               6.3.2.7.1.4 Interfaces Between Rubin Observatory and the Community   104
               6.3.2.7.1.5 Beyond Rubin Operations: Community-Based Data Analysis   106
          6.3.2.8 Network and Data Architecture                                     109
             6.3.2.8.1 Data Management System                                       109
               6.3.2.8.1.1 Rubin Observatory DMS Architecture                       109

High Energy Physics Network Requirements Review: Final Report                             IX
               6.3.2.8.1.2 Compute and Storage Sizing                            110
                6.3.2.8.1.2.1 Storage Requirements                               111
                6.3.2.8.1.2.2 Compute Requirements                               113
               6.3.2.8.1.3 Chilean Data Center                                   114
                6.3.2.8.1.3.1 Prompt Base                                        114
                6.3.2.8.1.3.2 Archive Base                                       115
                6.3.2.8.1.3.3 Commissioning Cluster                              115
                6.3.2.8.1.3.4 Chilean DAC                                        115
               6.3.2.8.1.4 US Data Facility                                      116
                6.3.2.8.1.4.1 Prompt USDF                                        116
                6.3.2.8.1.4.2 Archive USDF                                       117
                6.3.2.8.1.4.3 Offline Production USDF                            117
                6.3.2.8.1.4.4 US Data Access Center                              118
               6.3.2.8.1.5 Non-US Data Facilities                                119
                6.3.2.8.1.5.1 IN2P3 Data Facility                                119
                6.3.2.8.1.5.2 UKDF                                               120
                6.3.2.8.1.5.3 Offline Processing Satellite                       120
               6.3.2.8.1.6 Backbone Services                                     120
               6.3.2.8.1.7 Wide Area Networks                                    120
                6.3.2.8.1.7.1 Network Requirements                               120
                6.3.2.8.1.7.2 Network Architecture and Design                    122
               6.3.2.8.1.8 Configuration Control, Test, and Release Procedures   125
          6.3.2.9 Emerging Technology Use                                        126
             6.3.2.9.1 Cloud Services                                            126
             6.3.2.9.2 AI and ML                                                 126
             6.3.2.9.3 Wireless or Distributed Location Science Activities       126
          6.3.2.10 Data-Related Resource Constraints                             127
          6.3.2.11 Data Mobility Endpoints                                       127
          6.3.2.12 Outstanding Issues                                            127
          6.3.2.13 Facility Profile Contributors                                 127
   6.4 DESC				                                                                  128
       6.4.1 Discussion Summary                                                  128
       6.4.2 DESC: Experiment Profile                                            132
          6.4.2.1 Science Background                                             132
          6.4.2.2 Collaborators                                                  132
          6.4.2.3 IRI Readiness                                                  133
          6.4.2.4 Instruments and Facilities                                     134
          6.4.2.5 Generalized Process of Science                                 135
          6.4.2.6 Remote Science Activities                                      136
          6.4.2.7 Software Infrastructure                                        137
          6.4.2.8 Network and Data Architecture                                  137
          6.4.2.9 Emerging Technology Use                                        137
             6.4.2.9.1 Cloud Services                                            137
             6.4.2.9.2 Artificial Intelligence and ML                            137
             6.4.2.9.3 Wireless or Distributed Location Science Activities       137

High Energy Physics Network Requirements Review: Final Report                          X
          6.4.2.10 Data-Related Resource Constraints                         137
          6.4.2.11 Data Mobility Endpoints                                   138
          6.4.2.12 Outstanding Issues                                        138
          6.4.2.13 Facility Profile Contributors                             139
   6.5 CMB				                                                               140
       6.5.1 Discussion Summary                                              140
       6.5.2 CMB: Experiment Profile                                         143
          6.5.2.1 Science Background                                         143
          6.5.2.2 Collaborators                                              144
          6.5.2.3 IRI Readiness                                              145
          6.5.2.4 Instruments and Facilities                                 145
             6.5.2.4.1 Observatory in the Chilean Atacama                    145
             6.5.2.4.2 Computing Resources                                   146
          6.5.2.5 Generalized Process of Science                             147
          6.5.2.6 Remote Science Activities                                  147
          6.5.2.7 Software Infrastructure                                    147
             6.5.2.7.1 Data Movement                                         147
             6.5.2.7.2 Data Simulation and Reduction                         148
          6.5.2.8 Network and Data Architecture                              148
          6.5.2.9 Emerging Technology Use                                    149
             6.5.2.9.1 Cloud Services                                        149
             6.5.2.9.2 AI and ML                                             149
             6.5.2.9.3 Wireless or Distributed Location Science Activities   150
          6.5.2.10 Data-Related Resource Constraints                         150
          6.5.2.11 Data Mobility Endpoints                                   150
          6.5.2.12 Outstanding Issues                                        150
          6.5.2.13 Facility Profile Contributors                             151
   6.6 Muon Experimentation at Fermilab: Muon g-2 and Mu2e                   152
       6.6.1 Discussion Summary                                              152
       6.6.2 Muon Experimentation at Fermilab: Experiment Profile            154
          6.6.2.1 Science Background                                         154
             6.6.2.1.1 Muon g-2 Science Background                           155
             6.6.2.1.2 Mu2e Science Background                               156
          6.6.2.2 Collaborators                                              157
             6.6.2.2.1 Muon g-2 Collaborators                                157
             6.6.2.2.2 Mu2e Collaborators                                    157
          6.6.2.3 IRI Readiness                                              159
             6.6.2.3.1 Muon g-2 IRI Readiness                                159
             6.6.2.3.2 Mu2e IRI Readiness                                    159
          6.6.2.4 Instruments and Facilities                                 159
             6.6.2.4.1 Muon g-2 Instruments and Facilities                   159
             6.6.2.4.2 Mu2e Instruments and Facilities                       159
          6.6.2.5 Generalized Process of Science                             161
             6.6.2.5.1 Muon g-2 Process of Science                           161
             6.6.2.5.2 Mu2e Process of Science                               161

High Energy Physics Network Requirements Review: Final Report                      XI
          6.6.2.6 Remote Science Activities                                  163
             6.6.2.6.1 Muon g-2 Remote Science Activities                    163
             6.6.2.6.2 Mu2e Remote Science Activities                        163
          6.6.2.7 Software Infrastructure                                    163
          6.6.2.8 Network and Data Architecture                              164
          6.6.2.9 Emerging Technology Use                                    164
             6.6.2.9.1 Cloud Services                                        164
             6.6.2.9.2 AI and ML                                             164
             6.6.2.9.3 Wireless or Distributed Location Science Activities   164
          6.6.2.10 Data-Related Resource Constraints                         164
          6.6.2.11 Data Mobility Endpoints                                   164
          6.6.2.12 Outstanding Issues                                        164
          6.6.2.13 Facility Profile Contributors                             165
   6.7 Belle II Experiment                                                   166
       6.7.1 Discussion Summary                                              166
       6.7.2 Belle II: Experiment Profile                                    168
          6.7.2.1 Science Background                                         168
          6.7.2.2 Collaborators                                              168
          6.7.2.3 IRI Readiness                                              170
          6.7.2.4 Instruments and Facilities                                 170
          6.7.2.5 Generalized Process of Science                             171
          6.7.2.6 Remote Science Activities                                  171
          6.7.2.7 Software Infrastructure                                    173
             6.7.2.7.1. Rucio                                                173
             6.7.2.7.2. DIRAC                                                174
             6.7.2.7.3. Conditions Database                                  174
             6.7.2.7.4. CVMFS                                                174
          6.7.2.8 Network and Data Architecture                              174
             6.7.2.8.1 Domestic Connectivity                                 174
             6.7.2.8.2 International Connectivity                            178
          6.7.2.9 Emerging Technology Use                                    179
             6.7.2.9.1 Cloud Services                                        179
             6.7.2.9.2 AI and ML                                             179
             6.7.2.9.3 Wireless or Distributed Location Science Activities   179
          6.7.2.10 Data-Related Resource Constraints                         179
          6.7.2.11 Data Mobility Endpoints                                   179
          6.7.2.12 Outstanding Issues                                        179
          6.7.2.13 Facility Profile Contributors                             179
   6.8 Neutrino Experiments at Fermilab: SBN and DUNE                        180
       6.8.1 Discussion Summary                                              180
       6.8.2 Neutrino Experiments at Fermilab: Experiment Profile            185
          6.8.2.1 Science Background                                         185
             6.8.2.1.1 DUNE Science Background                               185
             6.8.2.1.2 SBN Science Background                                186

High Energy Physics Network Requirements Review: Final Report                      XII
          6.8.2.2 Collaborators                                              187
             6.8.2.2.1 DUNE Collaborators                                    187
             6.8.2.2.2 SBN Collaborators                                     188
          6.8.2.3 IRI Readiness                                              189
             6.8.2.3.1 DUNE IRI Readiness                                    189
             6.8.2.3.2 SBN IRI Readiness                                     189
          6.8.2.4 Instruments and Facilities                                 190
             6.8.2.4.1 DUNE Instruments and Facilities                       190
             6.8.2.4.2 SBN Instruments and Facilities                        191
          6.8.2.5 Generalized Process of Science                             192
             6.8.2.5.1 DUNE Process of Science                               192
             6.8.2.5.2 SBN Process of Science                                193
          6.8.2.6 Remote Science Activities                                  195
          6.8.2.7 Software Infrastructure                                    195
             6.8.2.7.1 DUNE Software Infrastructure                          195
             6.8.2.7.2 SBN Software Infrastructure                           196
          6.8.2.8 Network and Data Architecture                              196
             6.8.2.8.1 DUNE Network and Data Architecture                    196
             6.8.2.8.2 SBN Network and Data Architecture                     196
          6.8.2.9 Emerging Technology Use                                    196
             6.8.2.9.1 Cloud Services                                        196
             6.8.2.9.2 Artificial Intelligence and ML                        196
               6.8.2.9.2.1 DUNE AI & ML                                      196
               6.8.2.9.2.2 SBN AI & ML                                       196
             6.8.2.9.3 Wireless or Distributed Location Science Activities   197
          6.8.2.10 Data-Related Resource Constraints                         197
             6.8.2.10.1 DUNE Data-Related Resource Constraints               197
             6.8.2.10.2 SBN Data-Related Resource Constraints                197
          6.8.2.11 Data Mobility Endpoints                                   197
             6.8.2.11.1 DUNE Data Mobility Endpoints                         197
             6.8.2.11.2 SBN Data Mobility Endpoints                          198
          6.8.2.12 Outstanding Issues                                        198
          6.8.2.13 Facility Profile Contributors                             198
   6.9 LHC: ATLAS Experiment                                                 199
       6.9.1 Discussion Summary                                              199
       6.9.2 ATLAS: Experiment Profile                                       202
          6.9.2.1 Science Background                                         203
          6.9.2.2 Collaborators                                              203
          6.9.2.3 IRI Readiness                                              214
          6.9.2.4 Instruments and Facilities                                 214
             6.9.2.4.1 LHC                                                   214
             6.9.2.4.2 ATLAS                                                 215
             6.9.2.4.3 WLCG                                                  216
             6.9.2.4.4 US ATLAS T1 at BNL                                    216
             6.9.2.4.5 US ATLAS T2 Infrastructure                            218

High Energy Physics Network Requirements Review: Final Report                      XIII
            6.9.2.4.6 US ATLAS Analysis Facilities                          219
          6.9.2.5 Generalized Process of Science                            219
            6.9.2.5.1 Computation                                           219
               6.9.2.5.1.1 High-Performance Computing                       223
               6.9.2.5.1.2 Distributed Computing                            223
            6.9.2.5.2 Storage                                               223
            6.9.2.5.3 Network Use Cases & Data Flow                         226
          6.9.2.6 Remote Science Activities                                 231
          6.9.2.7 Software Infrastructure                                   231
            6.9.2.7.1 Rucio                                                 231
            6.9.2.7.2 PanDA                                                 231
            6.9.2.7.3 Frontier                                              232
            6.9.2.7.4 CVMFS                                                 232
            6.9.2.7.5 HTCondor                                              232
            6.9.2.7.6 ROOT                                                  232
          6.9.2.8 Network and Data Architecture                             232
            6.9.2.8.1 US ATLAS T1 at BNL                                    232
            6.9.2.8.2 US ATLAS T2 Infrastructure                            236
          6.9.2.9 Emerging Technology Use                                   241
            6.9.2.9.1 Cloud Services                                        241
            6.9.2.9.2 Artificial Intelligence and ML                        241
            6.9.2.9.3 Wireless or Distributed Location Science Activities   241
          6.9.2.10 Data-Related Resource Constraints                        241
          6.9.2.11 Data Mobility Endpoints                                  242
          6.9.2.12 Outstanding Issues                                       242
          6.9.2.13 Facility Profile Contributors                            242
   6.10 LHC: CMS Experiment                                                 243
       6.10.1 Discussion Summary                                            243
       6.10.2 CMS: Experiment Profile                                       248
          6.10.2.1 Science Background                                       248
          6.10.2.2 Collaborators                                            249
          6.10.2.3 IRI Readiness                                            252
          6.10.2.4 Instruments and Facilities                               252
            6.10.2.4.1 HLT                                                  253
            6.10.2.4.2 Tier-0                                               253
            6.10.2.4.3 Tier-1                                               253
            6.10.2.4.4 Tier-2                                               253
            6.10.2.4.5 CMS Computing Capacity and Planning                  253
            6.10.2.4.6 Tier-3                                               254
            6.10.2.4.7 HPC facilities                                       254
          6.10.2.5 Generalized Process of Science                           256
            6.10.2.5.1 Collision Data                                       256
            6.10.2.5.2 Simulation Data                                      258
            6.10.2.5.3 User Data                                            259

High Energy Physics Network Requirements Review: Final Report                     XIV
            6.10.2.5.4 Event Reconstruction and Analysis Data Creation       260
            6.10.2.5.5 Analysis Data Formats                                 261
            6.10.2.5.6 Data Access                                           263
            6.10.2.5.7 Analysis Group and Researcher Workflows               264
          6.10.2.6 Remote Science Activities                                 264
          6.10.2.7 Software Infrastructure                                   265
          6.10.2.8 Network and Data Architecture                             266
            6.10.2.8.1 The US CMS Tier-1                                     266
            6.10.2.8.2 The US CMS Tier-2s                                    267
          6.10.2.9 Emerging Technology Use                                   269
            6.10.2.9.1 Cloud Services                                        269
            6.10.2.9.2 AI and ML                                             269
            6.10.2.9.3 Wireless or Distributed Location Science Activities   270
          6.10.2.10 Data-Related Resource Constraints                        270
          6.10.2.11 Data Mobility Endpoints                                  270
          6.10.2.12 Outstanding Issues                                       270
          6.10.2.13 Facility Profile Contributors                            271
   6.11 LHC: LHC Operations                                                  272
       6.11.1 Discussion Summary                                             272
       6.11.2 LHC Operations: Profile                                        276
          6.11.2.1 Science Background                                        276
          6.11.2.2 Collaborators                                             277
          6.11.2.3 IRI Readiness                                             277
          6.11.2.4 Instruments and Facilities                                277
            6.11.2.4.1 LHC                                                   277
            6.11.2.4.2 Globally Distributed Computing Sites                  278
          6.11.2.5 Generalized Process of Science                            278
          6.11.2.6 Remote Science Activities                                 278
          6.11.2.7 Software Infrastructure                                   279
            6.11.2.7.1 Data Management Tools                                 279
            6.11.2.7.2 Monitoring Tools                                      281
            6.11.2.7.3 Network Management Tools                              282
               6.11.2.7.3.1 SENSE/Rucio Architecture Overview                282
               6.11.2.7.3.2 Key Components and Functionalities               283
               6.11.2.7.3.3 Testbeds and Site Upgrades                       283
               6.11.2.7.3.4 Benefits Targeted                                283
               6.11.2.7.3.5 Future Plans and Expansion                       283
          6.11.2.8 Network and Data Architecture                             283
          6.11.2.9 Emerging Technology Use                                   285
            6.11.2.9.1 Cloud Services                                        285
            6.11.2.9.2 AI and ML                                             285
            6.11.2.9.3 Wireless or Distributed Location Science Activities   285
            6.11.2.9.4 Data-Centre Interconnect and Spectrum Sharing         285
          6.11.2.10 Data-Related Resource Constraints                        286

High Energy Physics Network Requirements Review: Final Report                      XV
          6.11.2.11 Data Mobility Endpoints                                  286
          6.11.2.12 Outstanding Issues                                       286
          6.11.2.13 Facility Profile Contributors                            287
   6.12 LHC: HL-LHC & Network Research                                       288
       6.12.1 Discussion Summary                                             288
       6.12.2 HL-LHC: Network Research Profile                               293
          6.12.2.1 Science Background                                        293
          6.12.2.2 Collaborators                                             294
          6.12.2.3 IRI Readiness                                             295
          6.12.2.4 Instruments and Facilities                                296
            6.12.2.4.1 ATLAS Computing Infrastructure                        296
            6.12.2.4.2 CMS Computing Infrastructure                          298
          6.12.2.5 Generalized Process of Science                            299
            6.12.2.5.1 Analysis Facilities                                   300
            6.12.2.5.2 Inference As a Service                                301
          6.12.2.6 Remote Science Activities                                 302
          6.12.2.7 Software Infrastructure                                   302
            6.12.2.7.1 ATLAS                                                 302
            6.12.2.7.2 CMS                                                   302
          6.12.2.8 Network and Data Architecture                             303
          6.12.2.9 Emerging Technology Use                                   304
            6.12.2.9.1 Cloud Services                                        304
            6.12.2.9.2 AI and ML                                             304
            6.12.2.9.3 Wireless or Distributed Location Science Activities   304
          6.12.2.10 Data-Related Resource Constraints                        305
          6.12.2.11 Data Mobility Endpoints                                  305
          6.12.2.12 Outstanding Issues                                       306
          6.12.2.13 Facility Profile Contributors                            306
   6.13 Super Cryogenic Dark Matter Search (SuperCDMS SNOLAB)                307
       6.13.1 Discussion Summary                                             307
       6.13.2 SuperCDMS: Experiment Profile                                  309
          6.13.2.1 Science Background                                        309
          6.13.2.2 Collaborators                                             310
          6.13.2.3 IRI Readiness                                             311
          6.13.2.4 Instruments and Facilities                                311
          6.13.2.5 Generalized Process of Science                            312
          6.13.2.6 Remote Science Activities                                 313
          6.13.2.7 Software Infrastructure                                   313
          6.13.2.8 Network and Data Architecture                             313
          6.13.2.9 Emerging Technology Use                                   313
            6.13.2.9.1 Cloud Services                                        313
            6.13.2.9.2 AI and ML                                             314
            6.13.2.9.3 Wireless or Distributed Location Science Activities   314
          6.13.2.10 Data-Related Resource Constraints                        314

High Energy Physics Network Requirements Review: Final Report                      XVI
          6.13.2.11 Data Mobility Endpoints                                  314
          6.13.2.12 Outstanding Issues                                       314
          6.13.2.13 Facility Profile Contributors                            315
   6.14 Alpha Magnetic Spectrometer (AMS) Experiment                         316
       6.14.1 Discussion Summary                                             316
       6.14.2 AMS: Experiment Profile                                        318
          6.14.2.1 Science Background                                        318
          6.14.2.2 Collaborators                                             318
          6.14.2.3 IRI Readiness                                             321
          6.14.2.4 Instruments and Facilities                                322
          6.14.2.5 Generalized Process of Science                            323
          6.14.2.6 Remote Science Activities                                 324
          6.14.2.7 Software Infrastructure                                   325
            6.14.2.7.1 Data Resource Management                              325
            6.14.2.7.2 Data mobility                                         325
            6.14.2.7.3 Data Process                                          325
          6.14.2.8 Network and Data Architecture                             325
            6.14.2.8.1 The LAN Capabilities                                  325
            6.14.2.8.2 The Local Network Configuration                       325
            6.14.2.8.3 Network Bandwidth Connection Speed                    325
          6.14.2.9 Emerging Technology Use                                   325
            6.14.2.9.1 Cloud Services                                        325
            6.14.2.9.2 AI and ML                                             326
            6.14.2.9.3 Wireless or Distributed Location Science Activities   326
          6.14.2.10 Data-Related Resource Constraints                        326
          6.14.2.11 Data Mobility Endpoints                                  326
          6.14.2.12 Outstanding Issues                                       326
          6.14.2.13 Facility Profile Contributors                            326

7 Technology Profiles                                                        327
   7.1 NERSC			                                                              327
       7.1.1 Discussion Summary                                              327
       7.1.2 NERSC: Technology Profile                                       328
          7.1.2.1 Facilities Operated and Supported                          328
             7.1.2.1.1 Computing                                             328
             7.1.2.1.2 Storage                                               328
             7.1.2.1.3 Networking                                            328
             7.1.2.1.4 Planned Computing                                     329
             7.1.2.1.5 HEP Projects Supported by NERSC                       330
               7.1.2.1.5.1 Top 10 HEP Compute Projects                       330
          7.1.2.2 Network and Data Architecture                              332
             7.1.2.2.1 Current NERSC Network                                 332
             7.1.2.2.2 Next (Two to Five Year) Network Design                333
          7.1.2.3 Computational and Storage Infrastructure                   333

High Energy Physics Network Requirements Review: Final Report                      XVII
          7.1.2.4 Cloud Services                                333
          7.1.2.5 AI and ML                                     334
          7.1.2.6 Wireless Capabilities                         334
          7.1.2.7 Data-Related Resource Constraints             334
          7.1.2.8 Data Mobility Endpoints                       334
             7.1.2.8.1 Configuration                            334
             7.1.2.8.2 Access                                   334
             7.1.2.8.3 Available File Systems                   335
             7.1.2.8.4 File Transfer Software                   335
             7.1.2.8.5 Restrictions                             335
          7.1.2.9 Outstanding Issues                            335
          7.1.2.10 Technology Profile Contributors              335
   7.2 ALCF				                                                 336
       7.2.1 Discussion Summary                                 336
       7.2.2 ALCF: Technology Profile                           336
          7.2.2.1 Facilities Operated and Supported             336
          7.2.2.2 Network and Data Architecture                 338
          7.2.2.3 Computational and Storage Infrastructure      339
          7.2.2.4 Cloud Services                                339
          7.2.2.5 AI and ML                                     340
          7.2.2.6 Wireless Capabilities                         340
          7.2.2.7 Data-Related Resource Constraints             341
          7.2.2.8 Data Mobility Endpoints                       341
          7.2.2.9 Outstanding Issues                            341
          7.2.2.10 Technology Profile Contributors              341
   7.3 OLCF				                                                 342
       7.3.1 Discussion Summary                                 342
       7.3.2 OLCF: Technology Profile                           343
          7.3.2.1 Facilities Operated and Supported             343
          7.3.2.2 Network and Data Architecture                 344
          7.3.2.3 Computational and Storage Infrastructure      344
          7.3.2.4 Cloud Services                                346
          7.3.2.5 AI and ML                                     346
          7.3.2.6 Wireless Capabilities                         346
          7.3.2.7 Data-Related Resource Constraints             347
          7.3.2.8 Data Mobility Endpoints                       347
             7.3.2.8.1 Interactive Access                       347
             7.3.2.8.2 Access From Globus Online                347
          7.3.2.9 Outstanding Issues                            347
          7.3.2.10 Technology Profile Contributors              347
   7.4 Fermilab			                                              348
       7.4.1 Discussion Summary                                 348
       7.4.2 Fermilab: Technology Profile                       349
          7.4.2.1 Facilities Operated and Supported             349

High Energy Physics Network Requirements Review: Final Report     XVIII
          7.4.2.2 Network and Data Architecture                                        351
             7.4.2.2.1 Network Perimeter                                               352
             7.4.2.2.2 General Datacenter for Multiple Experiments                     352
             7.4.2.2.3 The US CMS-Tier-1 Network                                       353
               7.4.2.2.3.1 US CMS-Tier-2 Locations                                     354
             7.4.2.2.4 DUNE Network Architecture                                       354
               7.4.2.2.4.1 DUNE WAN                                                    356
               7.4.2.2.4.2 SURF -> Fermilab Data Movement                              356
               7.4.2.2.4.3 Fermilab Distribution of DUNE Data To Collaboration Sites   357
             7.4.2.2.5 NOvA (NuMI Off-axis νe Appearance)                              358
          7.4.2.3 Computational and Storage Infrastructure                             358
             7.4.2.3.1 Storage                                                         358
             7.4.2.3.2 Compute                                                         359
             7.4.2.3.3 Future Storage/Compute Resource Upgrades/Expansion              359
          7.4.2.4 Cloud Services                                                       359
          7.4.2.5 Artificial Intelligence and ML                                       359
          7.4.2.6 Wireless Capabilities                                                360
          7.4.2.7 Data-Related Resource Constraints                                    360
          7.4.2.8 Data Mobility Endpoints                                              360
          7.4.2.9 Outstanding Issues                                                   360
          7.4.2.10 Technology Profile Contributors                                     360
   7.5 BNL				                                                                         361
       7.5.1 Discussion Summary                                                        361
       7.5.2 BNL: Technology Profile                                                   362
          7.5.2.1 Facilities Operated and Supported                                    362
          7.5.2.2 Network and Data Architecture                                        362
             7.5.2.2.1 BNL Network Architectures                                       362
             7.5.2.2.2 BNL Network Perimeter                                           363
               7.5.2.2.2.1 BNL WAN and Internet Circuits                               364
               7.5.2.2.2.2 Connectivity to Science DMZ(s) and Campus Network           365
               7.5.2.2.2.3 BNL’s Support for LHCOPN and LHCONE Services                365
               7.5.2.2.2.4 Network Perimeter Security Features                         366
             7.5.2.2.3 BNL Campus Network                                              366
               7.5.2.2.3.1 BNL Campus Architecture                                     367
             7.5.2.2.4 HTSN                                                            368
             7.5.2.2.5 NSLS2 Network Infrastructure                                    370
               7.5.2.2.5.1 NSLS2 Science Network (N2SN) Components                     370
               7.5.2.2.5.2 NSLS2 Accelerator/Controls Network Components               371
               7.5.2.2.5.3 N2SN Core                                                   371
               7.5.2.2.5.4 N2SN Beamline Network                                       372
               7.5.2.2.5.5 NSLS2 Data Services Block                                   372
               7.5.2.2.5.6 NSLS2 DMZ                                                   373
               7.5.2.2.5.7 NSLS2 Accelerator/Controls Infrastructure 	                 373
               7.5.2.2.5.8 NSLS2 Network Management                                    373
          7.5.2.3 Computational and Storage Infrastructure                             374

High Energy Physics Network Requirements Review: Final Report                                XIX
          7.5.2.4 Cloud Services                                374
          7.5.2.5 Artificial Intelligence and ML                374
          7.5.2.6 Wireless Capabilities                         374
             7.5.2.6.1 Enterprise Wireless                      375
             7.5.2.6.2 LoRaWAN Remote Monitoring                375
             7.5.2.6.3 Site Cellular Network Connectivity       376
             7.5.2.6.4 NSLS2 Wireless Network                   376
          7.5.2.7 Data-Related Resource Constraints             377
          7.5.2.8 Data Mobility Endpoints                       377
          7.5.2.9 Outstanding Issues                            377
          7.5.2.10 Technology Profile Contributors              377
   7.6 SLAC National Accelerator Laboratory                     378
       7.6.1 Discussion Summary                                 378
       7.6.2 SLAC: Technology Profile                           378
          7.6.2.1 Facilities Operated and Supported             378
          7.6.2.2 Network and Data Architecture                 379
          7.6.2.3 Computational and Storage Infrastructure      380
             7.6.2.3.1 Interactive Computing Resources          381
             7.6.2.3.2 Batch Computing Resources                381
             7.6.2.3.3 Service Computing Resources              381
          7.6.2.4 Cloud Services                                382
          7.6.2.5 AI and ML                                     382
          7.6.2.6 Wireless Capabilities                         382
          7.6.2.7 Data-Related Resource Constraints             382
          7.6.2.8 Data Mobility Endpoints                       382
             7.6.2.8.1 bbcp                                     382
             7.6.2.8.2 Globus                                   383
          7.6.2.9 Outstanding Issues                            383
          7.6.2.10 Technology Profile Contributors              383
   7.7 ANL				                                                  384
       7.7.1 Discussion Summary                                 384
       7.7.2 ANL: Technology Profile                            384
          7.7.2.1 Facilities Operated and Supported             385
          7.7.2.2 Network and Data Architecture                 386
             7.7.2.2.1 Overview                                 386
             7.7.2.2.2 WAN                                      387
             7.7.2.2.3 Science DMZ                              387
             7.7.2.2.4 Core                                     387
             7.7.2.2.5 LAN                                      387
          7.7.2.3 Computational and Storage Infrastructure      388
          7.7.2.4 Cloud Services                                388
          7.7.2.5 AI and ML                                     388
          7.7.2.6 Wireless Capabilities                         389
          7.7.2.7 Data-Related Resource Constraints             389
          7.7.2.8 Data Mobility Endpoints                       389

High Energy Physics Network Requirements Review: Final Report         XX
            7.7.2.9 Outstanding Issues                           389
            7.7.2.10 Technology Profile Contributors             389

8 Group Discussion                                               390
   8.1 Topic Summary                                             390
       8.1.1 IRI and the HEP Community                           390
       8.1.2 HEP R&D Efforts                                     391
       8.1.3 Data Challenges                                     392
       8.1.4 LHCONE Support and International Networking         393
   8.2 Outcomes		                                                393
       8.2.1 Facility Management and Readiness                   393
       8.2.2 Scientific Data Management                          394
       8.2.3 Scientific Workflow                                 394
       8.2.4 Computational and Storage Requirements              394
       8.2.5 Remote Collaboration and Operational Requirements   394
       8.2.6 Multifacility Computational Workflows               395
       8.2.7 Networking for Local and Wide-area Data Mobility    395
       8.2.8 Emerging Needs                                      396
       8.2.9 IRI Responsiveness                                  397

List of Abbreviations                                            398

High Energy Physics Network Requirements Review: Final Report          XXI
1 Executive Summary
The world-class research infrastructure at the US Department of Energy (DOE) Office of Science (SC) provides
the research community with premier observational, experimental, computational, and network capabilities.
Each user facility is designed to provide unique capabilities to advance the core DOE mission in science and
technology for its SC program to stimulate rich scientific discoveries and enhance its innovation ecosystem.
Research communities gather and flourish around each user facility, bringing together new and enhanced
perspectives. The continual reinvention of the practice of science — as users and staff forge novel approaches
expressed in research workflows — unlocks new discoveries and propels scientific progress.

Within this research ecosystem, the high-performance computing (HPC) and networking user facilities stewarded
by the SC’s Advanced Scientific Computing Research (ASCR) program play a dynamic cross-cutting role,
enabling complex workflows demanding high-performance data, networking, and computing solutions. The
ASCR facilities enterprise seeks to understand and meet the needs and requirements across SC and DOE domain
science programs and priority efforts, highlighted by the formal requirements review methodology.

Between July and December 2024, the Energy Sciences Network (ESnet) and the Office of High Energy
Physics (HEP) of the DOE-SC organized an ESnet requirements review of HEP-supported program activities.
Preparation for these events included identification of key stakeholders: program and facility management,
research groups, and technology providers. Each stakeholder group was asked to prepare formal case study
documents about its relationship to the HEP program to build a complete understanding of the current, near-
term, and long-term status, expectations, and processes that will support the science going forward.

This review includes case studies from the following HEP user facilities, experiments, and joint collaborative efforts:

      • Cosmological Simulation Research
      • Dark Energy Spectroscopic Instrument (DESI)
      • Vera C. Rubin Observatory
      • Dark Energy Science Collaboration (DESC)
      • Cosmic Microwave Background (CMB)
      • Muon Experimentation at Fermilab: Muon g-2 and Mu2e
      • Belle-II Experiment
      • Neutrino experiments at Fermilab: Short-Baseline Neutrino (SBN) and Deep Underground
           Neutrino Experiment (DUNE)

      • Large Hadron Collider (LHC): A Toroidal LHC Apparatus (ATLAS) Experiment
      • LHC: Compact Muon Solenoid (CMS) Experiment
      • LHC: LHC Operations
      • LHC: HL-LHC and Network Research
      • Super Cryogenic Dark Matter Search (SuperCDMS)
      • Alpha Magnetic Spectrometer (AMS) Experiment

High Energy Physics Network Requirements Review: Final Report                                                        1
```
