# 스마트 온실 장비 규격 저장소

이 프로젝트는 스마트 온실 KS 표준 — `KS X 3267` / `3286` / `3288` + `KS B 7958` 시리즈 — 의 모드버스 통신 규격을 **JSON 장비 규격 파일(.spec)** 로 표현하기 위한 형식 정의를 관리합니다.

## 목표

이 프로젝트는 스마트 온실 KS 표준을 위한 디폴트 장비 규격을 제공하여, 표준 적용을 하려는 제조사들의 표준 적용을 돕는 것이 목표입니다.

향후 노드 제조사가 자사 제품을 위한 **자체 장비 규격 패키지** 를 작성·배포하면, 온실 통합 제어기 구현체가 디폴트 패키지와 함께 이를 동시에 적재(integrated load) 하여 다벤더 환경에서도 일관된 모드버스 통신을 수행할 수 있도록 지원합니다.

## 저장소 구성

```
ksspec_archive/
├── docs/
│   └── SPEC.md              # 장비 규격 파일 형식 정의 — 정본 (597줄)
├── specs/
│   └── defaults/            # 디폴트 장비 규격 패키지 — KS 표준 reference (org=0, mfg=0)
│       ├── vendor.json
│       ├── <org>_<mfg>_<type>_<code>_<protocol>_<max_devices>.spec   # 노드 장비 규격
│       ├── <org>_<mfg>_<type>_<code>_<protocol>.spec                 # max_devices fallback
│       └── devices/         # device 템플릿 (자율배치용)
│           ├── <org>_<mfg>_0_<device_code>_<protocol>.spec           # 단일 장비
│           ├── sensor.spec / actuator.spec                            # generic dict
│           └── sensor_<protocol>.spec                                 # protocol-specific dict
├── LICENSE
└── README.md
```

상세 파일 형식·인코딩·자율배치·게이트웨이 자식 처리 등은 [`docs/SPEC.md`](docs/SPEC.md) 참조.
공식 규격의 변경·검토·테스트 데이터·릴리스 관리 규칙은 [`docs/SPEC_MANAGEMENT.md`](docs/SPEC_MANAGEMENT.md) 참조.
프로젝트 소개 사이트는 GitHub Pages에서 배포하며, 사이트 원본은 [`site/`](site/)에 있다.

## 디폴트 장비 규격 패키지

`specs/defaults/` 는 **KS 표준을 그대로 따르는 노드를 위한 reference 패키지** (`org=0, mfg=0`).

| Protocol 코드 | 표준 | 비고 |
|:---:|---|---|
| 10 | KS X 3267 (RS485) | 일반 센서·구동기 노드 |
| 20 | KS X 3288 (RS485) | 양액기 노드 |
| 30 / 31 | KS B 7958 (TCP) | 게이트웨이 + TCP 변형 |
| (등록 절차) | KS X 3286 | 자율배치 메커니즘 (SPEC.md §9) |

KS 표준을 그대로 구현한 노드는 본 디폴트 패키지만으로 동작 가능.

## 두 가지 사용자

### 1. 컨트롤러 구현자

온실 통합 제어기·모니터링 시스템을 개발하는 경우. 본 저장소의 디폴트 장비 규격 패키지 + 외부 장비 규격 패키지를 동시에 적재하고, 노드의 `(org, mfg, type, code, protocol, max_devices)` 정보로 적합한 spec 파일을 매칭해 모드버스 레지스터 맵을 구성합니다.

### 2. 노드 제조사 

자사 제품을 위한 자체 장비 규격 패키지를 작성·배포해 위 컨트롤러 구현체가 그 패키지를 적재하면 자사 제품을 즉시 인식·운용할 수 있도록 지원합니다.

## 제조사 장비 규격 패키지 작성 가이드

### 1단계 — 식별 코드 발급

자사를 식별하는 `(org, mfg)` 페어를 발급받는다. 코드 발급·협의 채널은 [`docs/SPEC.md`](docs/SPEC.md) §13 참조 (현재 서울대학교, 한국농업기술진흥원 등 표준화 기관).

- `org`: 기관 코드 (코드 발급 권한 기관)
- `mfg`: 제조사 코드 (해당 기관 내에서 자사 식별)

### 2단계 — 디렉토리 구성

자사 장비 규격 패키지를 별도 저장소·디렉토리로 구성한다. 레이아웃은 본 저장소의 `specs/defaults/` 와 동일:

```
my-company-vendor-pack/
├── vendor.json
├── <org>_<mfg>_<type>_<code>_<protocol>_<max_devices>.spec
├── <org>_<mfg>_<type>_<code>_<protocol>.spec       # 슬롯 수 다른 변종을 한 파일로
└── devices/                  # (선택) 자사 device 템플릿
    ├── <org>_<mfg>_0_<device_code>_<protocol>.spec
    └── ...
```

### 3단계 — `vendor.json` 작성

```json
{
    "name": "SGH Greenhouse Devices",
    "org": 1,
    "mfg": 5,
    "description": "SGH 사 스마트 온실 노드 / 장비 규격 패키지",
    "version": "1.0.0"
}
```

`org / mfg` 는 1단계에서 발급받은 코드. `name / description / version` 은 자유 양식.

### 4단계 — 노드 / 장비 규격 작성

[`docs/SPEC.md`](docs/SPEC.md) 의 §3 (노드 장비 규격), §4 (장비 규격), §6 (Items 인코딩) 을 따라 자사 제품의 레지스터 맵을 JSON 으로 표현. 디폴트 패키지의 기존 spec 파일이 참고용 예제로 충분.

자율배치(§9) 를 활용하면 슬롯 구성이 다양한 라인업을 한 노드 spec + device 템플릿 조합으로 표현 가능.

### 5단계 — 등록·배포·버전 관리

자체 장비 규격 패키지의 등록·갱신은 본 저장소와 무관한 **별도의 신청 절차** 를 통해 처리합니다 (구체 채널은 표준화 기관에 문의 — 1단계 코드 발급 절차와 동일하거나 별도).

버전 관리는 제조사 자율 — `vendor.json` 의 `version` 필드를 갱신하며 [SemVer](https://semver.org) 권장.

## 통합 관리 모델

다수의 장비 규격 패키지들이 동시에 적재되어 다음과 같이 협력한다:

```
컨트롤러 시동
    ↓
1. 디폴트 장비 규격 패키지 적재  (specs/defaults/, org=0, mfg=0 — KS reference)
    ↓
2. 외부 장비 규격 패키지 적재    (컨트롤러 구현체가 정의한 경로의 모든 vendor.json)
    ↓
3. 노드 발견                     (예: mDNS) → (org, mfg, type, code, protocol, max_devices) 획득
    ↓
4. spec 매칭                     (org, mfg) → 해당 패키지 선택 → 파일명 매칭 → fallback
    ↓
5. CommSpec 적용                 spec 의 read/write items 를 모드버스 레지스터 맵으로 구성 → 통신 시작
```

### 충돌 처리

- 파일명에 `(org, mfg)` 가 포함되어 있어 **다른 장비 규격 패키지 간 spec 파일 충돌 없음**.
- 같은 `(org, mfg)` 내에서 동일 `(type, code, protocol, max_devices)` 의 spec 파일이 중복되지 않도록 제조사 자체 관리.
- device 템플릿(§11) 은 generic dict / protocol-specific dict / 단일 장비 파일 순으로 구체적인 것이 우선 (SPEC.md §11.4).

## 라이선스 / 문의

- 라이선스: [`LICENSE`](LICENSE)
- 코드 발급 (`org`, `mfg`) / 형식 협의: 서울대학교, 한국농업기술진흥원 등 표준화 기관 ([`docs/SPEC.md`](docs/SPEC.md) §13).
