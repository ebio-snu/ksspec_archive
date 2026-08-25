# 장비 규격 (Description Specification) 

본 문서는 한국 산업표준 (KS X 3267/3286/3288, KS B 7958-1..5) 의 스마트 온실 장비 통신 규격을 JSON 파일로 표현하기 위한 **장비 규격 파일 형식** 을 정의한다. 

## 목차

1. [개요](#1-개요)
2. [파일명 규칙](#2-파일명-규칙)
3. [JSON 구조 — 노드 장비 규격](#3-json-구조--노드-장비-규격)
4. [JSON 구조 — 장비 규격](#4-json-구조--장비-규격)
5. [`CommSpec` — 통신 영역 정의](#5-commspec--통신-영역-정의)
6. [Items 인코딩](#6-items-인코딩)
7. [Command code vs register opcode](#7-command-code-vs-register-opcode)
8. [`write.operations[]` — opcode 가변 레이아웃](#8-writeoperations--opcode-가변-레이아웃)
9. [`Devices` 와 자율배치](#9-devices-와-자율배치)
10. [`ConnectedNodes` — 게이트웨이 자식](#10-connectednodes--게이트웨이-자식)
11. [Device 템플릿 파일](#11-device-템플릿-파일)
12. [Fallback 규칙](#12-fallback-규칙)
13. [표준 참조](#13-표준-참조)

---

## 1. 개요

장비 규격 파일은 한 노드 또는 한 장비의 Modbus 레지스터 맵을 JSON 으로 기술한다.
노드 정보(`org`, `mfg`, `type`, `code`, `protocol`, `max_devices`) 가 결정되면
대응하는 장비 규격 파일이 식별되고, 해당 파일이 어느 주소에서 어떤 값을 어떤 형식
으로 읽고 쓸지를 정의한다.

장비 규격은 두 가지 입자도(granularity) 로 표현된다:

- **노드 장비 규격** (§3): 한 노드 전체 — 노드 자체 통신 영역 + 슬롯별 장비 배열
- **장비 규격** (§4): 한 장비 — 노드 장비 규격의 `Devices` 안에 인라인 또는 device 템플릿 파일 (§11) 로 분리

---

## 2. 파일명 규칙

### 2.1 노드 장비 규격 파일명

```
{org}_{mfg}_{type}_{code}_{protocol}_{max_devices}.spec
```

| 세그먼트 | 의미 | 값 예 |
|----------|------|-------|
| `org` | 기관 코드 (KS 표준화 기관 발급) | `0`=KS 표준 |
| `mfg` | 제조사 코드 (각 기관에서 발급) | `0`=표준, `1..N`=제조사 |
| `type` | 노드 종류 | `1`=센서, `2`=구동기, `3`=복합, `4`=게이트웨이 |
| `code` | 제품 코드 (제조사 자율) | 정수 |
| `protocol` | 프로토콜 버전 | `10`=KS X 3267, `20`=KS X 3288, `30`/`31`=KS B 7958 |
| `max_devices` | 최대 장비 수 | 정수 |

예: `1_5_2_3_31_5.spec` = org=1 / 제조사=5 / 구동기노드 / 제품코드=3 / KS B 7958 protocol 31 / 최대 5 슬롯.

### 2.2 단일 장비 규격 파일명 (옵션)

자율배치(§9) 에서 사용되는 device 단위 템플릿. 노드 장비 규격과 구분하기 위해
`type` 자리에 `0` 마커를 두고, `code` 자리에 device code 를 둔다:

```
{org}_{mfg}_0_{device_code}_{protocol}.spec
```

| 세그먼트 | 의미 |
|----------|------|
| `org`, `mfg` | 기관·제조사 코드 |
| `0` (3번째) | **device-level 마커** (필수) |
| `device_code` | 장비 코드 (1=온도, 12=EC, 101=스위치 Lv0, 301=FND 등) |
| `protocol` | 활성화 protocol (해당 protocol 의 노드에서만 유효) |

예: `0_0_0_1_31.spec` = KS 표준 / 표준 제조사 / device-level / 온도센서(1) / KS B 7958 protocol 31.

---

## 3. JSON 구조 — 노드 장비 규격

```json
{
    "Class": "node",
    "Type": "actuator-node/level1",
    "Model": "FARMOS-AN-LV1-5",
    "Name": "FarmOS 5채널 구동기노드 Lv1",
    "CommSpec": {
        "KS B 7958": {
            "read":  { "starting-register": 201, "items": ["status", "opid", "control"] },
            "write": { "starting-register": 501, "items": ["operation", "opid", "control"] }
        }
    },
    "Devices": [
        /* 슬롯별 장비 spec — §4 */
    ]
}
```

| 필드 | 타입 | 의미 |
|------|------|------|
| `Class` | string | 노드의 클래스는 항상 `"node"` |
| `Type` | string | 노드 종류 (§3.1) |
| `Model` | string | 모델명 (자유) |
| `Name` | string | 사람 읽기 이름 |
| `CommSpec` | object | 노드 자체 통신 영역 (§5) |
| `Devices` | array | 슬롯별 장비 규격 — 비우면 자율배치 (§9) |
| `ConnectedNodes` | array | 게이트웨이의 자식 노드 목록 (§10) — 게이트웨이만 |

### 3.1 `Type` 의 값

| Type | 노드 종류 |
|------|-----------|
| `sensor-node/level0..1` | 센서 노드 (type=1) |
| `actuator-node/level0..1`, `actuator-node/auto` | 구동기 노드 (type=2) |
| `integrated-node/level1` | 복합 노드 (type=3) — 센서와 구동기를 함께 단다 |
| `gateway-node/level0..1` | 게이트웨이 노드 (type=4) |

`level` 은 KS 표준이 정의한 기능 등급 (level 0=수동, 1=기본 제어, 2+=고급).

**노드의 `level` 과 장비의 `level` (§4.2) 은 별개다.** 예컨대 `0_0_3_5_31_21.spec` 은
노드 자체는 `integrated-node/level1` 이면서 슬롯에 `nutrient-supply/level4` 를 단다 —
모델명의 "레벨4" 는 **양액기 장비의 등급**이지 노드의 등급이 아니다.

---

## 4. JSON 구조 — 장비 규격

```json
{
    "Class": "actuator",
    "Type": "switch/level1",
    "Model": "FARMOS-SW1",
    "Name": "전등1",
    "CommSpec": {
        "KS B 7958": {
            "read":  { "starting-register": 204, "items": ["opid", "status", "remain-time"] },
            "write": { "starting-register": 504, "items": ["operation", "opid", "hold-time"] }
        }
    }
}
```

### 4.1 `Class` / `Type` 가능한 값

| Class | Type 예 | 비고 |
|-------|---------|------|
| `sensor` | `air-temperature-sensor`, `EC-sensor`, `pH-sensor`, `cumulative-flow-sensor`, `event-detector`, ... | KS B 7958-5 부속서 A.2 |
| `actuator` | `switch/level0..2`, `retractable/level0..2`, `nutrient-supply/level0..4` | level 별로 명령 셋이 다름 |
| `actuator` (표시기) | `fnd` | device code 301 |

전체 device code 표는 [`../specs/codes.json`](../specs/codes.json) 의 `device-type` 에 있다 (근거: KS B 7958-5 부속서 A.2 센서 정보 · A.3 구동기 정보 · §7.1). **참조가 아니라 데이터다** — 도구가 device code 를 상수로 들고 있으면 안 된다.

#### 번들 vendor pack 이 구 영문명을 쓰는 코드가 있다 (의도적 보류)

`codes.json` 은 **KS B 7958-5 rev6 의 현행 영문명**을 싣지만, `specs/defaults/devices/`
의 센서 템플릿 4종은 **구 영문명을 그대로 유지**하고 있다:

| device code | `codes.json` (현행) | 템플릿 (유지) |
|---|---|---|
| 1 | `air-temperature-sensor` | `temperature-sensor` |
| 2 | `(relative-)humidity-sensor` | `humidity-sensor` |
| 23 | `battery-level-sensor` | `battery-sensor` |
| 24 | `event-detector` | `event-trigger` |

**오타가 아니라 보류다.** rev5 가 이 4종의 영문 식별자를 바꿨는데 코드값은 그대로여서
통신은 깨지지 않는 대신 식별자를 키로 쓰는 구현물이 전부 영향을 받는다. 표준 쪽에서
구 표기의 별칭 병기 여부가 정해지기 전까지 배포된 `Type` 문자열을 바꾸지 않는다.

구 표기는 각 값의 `deprecated-alias` 에 **데이터로** 실려 있다. 검사 도구는 `Type` 을
`name` 뿐 아니라 `deprecated-alias` 와도 대조해야 한다 — 그러지 않으면 이 4종이
`unknown-type` (§9.1.3) 으로 떨어지고, **코드 0 으로 해석돼 슬롯 대조가 통째로 꺼진다**
(§9.1.1 이 경고하는 상태).

### 4.2 구동기 level 의미

#### 스위치
- **level 0**: 상태 read-only (수동 장비)
- **level 1**: ON/OFF + timed 명령
- **level 2** 스위치 : level 1 + 비율 (ratio)

#### 개폐기
- **level 0**: 상태 read-only (수동 장비)
- **level 1**: OPEN/CLOSE/OFF + timed 명령
- **level 2**: level 1 + 위치 (position)

#### 양액기
- **level 0**: 상태 read-only (수동 장비)
- **level 1**: 1회 관수
- **level 2**: level 1 + 원수관수
- **level 3**: level 2 + 양액관수 (start-area, stop-area, on-sec, EC/pH 목표값)
- **level 4**: level 3 + 구역지정 원수|양액 관수 (area bitmap zone 선택)

---

## 5. `CommSpec` — 통신 영역 정의

`CommSpec` 의 키는 적용 표준 라벨이다. 첫 키만 의미를 가지며, 둘 이상 정의해도
파서는 첫 항목을 사용한다.

```json
"CommSpec": {
    "KS B 7958": { "read": {...}, "write": {...} }
}
```

값으로는 `read` / `write` 두 영역을 정의:

```json
"read":  { "starting-register": 201, "items": ["status", "opid", "control"] },
"write": { "starting-register": 501, "items": ["operation", "opid", "control"] }
```

| 키 | 타입 | 의미 |
|----|------|------|
| `starting-register` | int | **1-based** Modbus 주소 |
| `items` | array of string | 영역의 필드 이름 — 순서대로 배치 (§6) |

영역 크기 = `Σ items[i].register_size` (§6.1 의 표 참조).

### 5.1 KS 표준 레지스터 영역 (KS B 7958-1 표 2)

| 주소 범위 | 용도 | 비고 |
|-----------|------|------|
| 1-100 | 노드 정보 | `[org, mfg, type, code, protocol, max_devices]` 등 |
| 101-200 | 장비 정보 (devinfo) | 슬롯별 device code 배열 |
| 201+ | read 영역 | `starting-register` 로 명시 |
| 501+ | write 영역 | `starting-register` 로 명시 |

### 5.2 노드 read items 의 표준 항목

| 항목 | 크기 | 의미 |
|------|:----:|------|
| `status` | 1 | 노드 상태 코드 |
| `opid` | 1 | 가장 최근 처리된 명령 ID |
| `control` | 1 | 제어권 (1=LOCAL, 2=REMOTE, 3=`IMMUTABLE_LOCALMANUAL`(KS B 7958-5) / `MANUAL`(KS X 3267)) — 필드 부재 시 노드에 제어권 개념 없음. **값의 정본은 [`../specs/codes.json`](../specs/codes.json)** (§7.1) |

### 5.3 노드 write items 의 표준 항목

| 항목 | 크기 | 의미 |
|------|:----:|------|
| `operation` | 1 | 명령 코드 |
| `opid` | 1 | 새 명령 ID |
| `control` | 1 | 제어권 변경 명령 시 새 모드 (선택) |

### 5.4 주소 계산 규칙

장비 규격 작성자는 다음 규칙을 따라야 한다:

1. 첫 장비의 `starting-register` = 노드 read 영역 다음 주소
   (예: 노드 영역 201-203 → 첫 장비 204)
2. 다음 장비 = 이전 장비 영역의 다음 주소 (이전 영역 크기만큼 +)
3. write 영역도 동일 규칙 (501 부터)

작성된 주소는 그대로 신뢰되어야 한다 — 파서가 자동 보정하지 않는다.

### 5.5 라벨과 protocol 코드 — `specs/protocols.json`

파서는 라벨 문자열을 대조하지 않고 **첫 키만** 집는다(§5). 그래서 라벨이 틀려도
동작이 바뀌지 않고, **틀린 채로 영원히 남는다.** 어떤 라벨이 어떤 protocol 코드에
허용되는지는 [`../specs/protocols.json`](../specs/protocols.json) 이 정하며,
그 파일이 **유일한 원천**이다 — 검사 도구가 라벨을 상수로 들고 있으면 안 된다.

| protocol 코드 | 표준 | 라벨 |
|---|---|---|
| `10` | KS X 3267 | `KS X 3267` |
| `20` | KS X 3288 | `KS X 3288` |
| `30` | KS B 7958 | `KS B 7958` |
| `31` | KS B 7958 (다음 개정판) | `KS B 7958` |

코드 ↔ 라벨은 **1:N** 이다. `30` 과 `31` 은 같은 표준을 가리키므로 라벨이 같다.
`31` 개정판의 연도가 확정되면 `protocols.json` 의 `labels` 에 **추가**하고 기존 표기는
그대로 둔다 — 새 파일부터 새 라벨을 쓰면 되고, 이미 발행된 파일은 여전히 유효하다.
**연도를 확정하기 전까지는 `KS B 7958:2027` 같은 표기를 쓰지 않는다.**

#### Device 템플릿의 protocol 귀속 (§11)

- 접미사가 붙은 파일(`sensor_31.spec`)은 **그 protocol 전용**이다. 라벨도 그 protocol 것을 쓴다.
- 접미사 없는 파일(`sensor.spec` · `actuator.spec`)은 **protocol 무관 baseline** 이다 (§11.1).

#### 한 파일 안에 라벨이 섞이는 것은 정상이다

장비의 라벨은 **그 장비를 정의한 표준**을 가리키지, 노드의 protocol 을 가리키지 않는다.
양액기(`nutrient-supply/level0..4`, 코드 201~205)는 KS X 3267 이 정의하지 않고
KS X 3288 이 정의하므로, protocol 10 노드에 달려도 라벨은 `KS X 3288` 이다.
`devices/actuator.spec` 이 스위치·개폐기·표시기는 `KS X 3267`, 양액기는 `KS X 3288` 로
적는 것이 이 때문이다. 이런 예외는 `protocols.json` 의 `device-label-exceptions` 에
데이터로 적는다.

> protocol 30·31 노드에서는 양액기도 `KS B 7958` 을 쓴다 — 그 표준이 양액기까지
> 함께 정의하기 때문이다.

같은 이유로 **센서 코드 25~34** (기압·습구온도·엽온·엽면습윤·줄기직경·과실직경·과실길이·
당도·과실경도·엽록소) 는 `devices/sensor.spec` 에서도 `KS B 7958` 라벨을 쓴다. KS B 7958-5
rev6 이 신설한 장비여서 2022 년 발행본인 KS X 3267 에는 정의가 없다.

**라벨이 다르면 `items` 배치도 그 표준을 따른다.** 센서 read 영역은 KS X 3267 이
`["value", "status"]`, KS B 7958 이 `["status", "value"]` 로 순서가 반대다 (§5.1 — `items`
는 순서대로 배치). 라벨만 바꾸고 순서를 두면 레지스터 해석이 어긋난다.

---

## 6. Items 인코딩

### 6.1 표준 아이템 타입

장비 규격의 `items` 배열에 쓰는 어휘는 **KS B 7958-4 부속서 A.3 (규정) 「레지스터 표현을
위한 주요 단어」** 가 정본이다. 근거 열이 각 항목의 출처이며, 표준 미등재 항목은 `확장` 으로
표시한다.

| 아이템 | regs | 데이터 타입 | 용도 | 근거 |
|--------|:----:|------------|------|------|
| `value` | 2 | float (IEEE 754) | 센서 측정값 | P4 A.3 |
| `event` | 1 | uint16 | 이벤트 발생기가 올린 이벤트 코드 (값은 제조사 기술규격) | P4 A.3 · P2 §6.1 표 3 |
| `EC` | 2 | float | 양액기 EC | P4 A.3 |
| `pH` | 2 | float | 양액기 pH | P4 A.3 |
| `status` | 1 | uint16 | 상태 코드 | P4 A.3 |
| `opid` | 1 | uint16 | 명령 ID (1-65535, 0 미사용) | P4 A.3 |
| `operation` | 1 | uint16 | 명령 코드 | P4 A.3 |
| `control` | 1 | uint16 | 제어권 | P4 A.3 |
| `ratio`, `position` | 1 | uint16 | 스위치 비율 / 개폐기 위치 | P4 A.3 |
| `area`, `alert` | 1 | uint16 | 양액기 zone / 경고 | P4 A.3 |
| `zone-id` | 1 | uint16 | 노드가 위치한 농장 내 구역 식별자 (`0`=온실 외부) | P4 A.3 · P2 §6.2 표 4 |
| `pos-x`, `pos-y`, `pos-z` | 2 | **int32 (signed)** | 위치 이동형 노드의 좌표 (cm) | P4 A.3 · P2 §6.2 표 4 |
| `remain-time`, `hold-time`, `time` | 2 | uint32 | 잔여/유지/지속 시간 (초) | P4 A.3 |
| `on-sec`, `remain-sec` | 2 | uint32 | 양액기 관수·잔여 시간(초) | P4 A.3 |
| `start-area`, `stop-area` | 1 | uint16 | 양액기 관수 시작구역/종료구역 | P4 A.3 |
| `open-time`, `close-time` | 1 | uint16 | 개폐기 총 열리는 시간(초), 닫히는 시간(초) | P4 A.3 |
| `area-bitmap` | 2 | uint32 | 양액기 구역 bitmap | P4 A.3 |
| `epoch` | 2 | uint32 | 세계시 시각 (Unix epoch) | P4 A.3 · P2 §6.3 표 8 |
| `sig-digit` | 1 | int16 (signed) | 표시기가 실수를 표시할 때의 유효자릿수 | P4 A.3 · P2 §6.3 표 7 |
| `tz-offset` | 1 | int16 (signed) | 시간대 오프셋 (시 단위, 한국 `+9`) | P4 A.3 · P2 §6.3 표 8 |
| `short` | 1 | **int16 (signed)** | 표시기에 표시할 사용자 지정 정수 코드 | P4 A.3 · P2 §6.3 표 9 |
| `blank` | 1 | uint16 (값 무시) | 사용하지 않는 레지스터 (자리 채움) | P4 A.3 |
| `vfloat` | 2 | float | 일반 float — **ksspec 확장** (표준 미등재) | 확장 |
| `vint` | 1 | uint16 | 일반 short — **ksspec 확장** (표준 미등재) | 확장 |

#### `event` 와 `blank` 는 짝으로 쓴다

이벤트 발생기(device code 24) 는 관측치 자리에 **float 이 아니라 1 레지스터짜리 UINT16
이벤트 코드**를 싣는다.

> 센서가 이벤트 발생기인 경우에는 FLOAT32이 아니라 UINT16 의 이벤트 코드를 기록한다.
>
> — KS B 7958-2 `2026-draft-rev5` 부속서 A.4 각주 c

그런데 같은 부속서의 센서 슬롯은 **장비 종류와 무관하게 3 레지스터 고정 stride** 다
(`202 + (3N-2)` 상태 / `202 + (3N-1)` 관측치·이벤트 코드 / `202 + (3N)`). 따라서 이벤트
발생기를 `["status", "event"]` 로만 적으면 2 레지스터가 되어, §5.4 순차 주소 계산에서
**뒤따르는 센서가 전부 한 칸씩 당겨진다.** 남는 한 칸을 `blank` 로 채워야 한다:

```json
"items": ["status", "event", "blank"]
```

`blank` 는 값을 갖지 않는다 — 파서는 자리만 소비하고 항목을 만들지 않는다.

> **`event` 는 P4 `2026-draft-rev6` 에서 부속서 A.3 에 등재됐다** (`uint16 / 1` · 이벤트발생기 ·
> 상태 영역). 같은 라운드에서 `tz-offset` 도 등재됐고 (`int16 / 1` · 표시기 · 제어 영역),
> P2 `2026-draft-rev6` 이 표 3 의 `Status` · `Event` 를 소문자로 내리면서 두 부의 표기가
> 정합됐다. 그 전까지 이 두 항목은 P2 규정 표에만 있던 미등재 어휘였다.

### 6.2 다중 레지스터 값 인코딩 (KS B 7958-1 §4.4)

2 레지스터 이상의 값(float, int32) 은 **little-endian word order** 로 인코딩 —
낮은 register 주소가 low word, 높은 주소가 high word.

```python
import struct
# float 인코딩 (4 bytes → 2 regs)
lo, hi = struct.unpack('<2H', struct.pack('<f', 23.5))
registers[addr]   = lo   # low word at lower addr
registers[addr+1] = hi
```

명시적 little-endian 포맷(`'<f'`, `'<i'`) 을 사용해 플랫폼 독립성을 확보한다.

### 6.3 Signed 항목

`sig-digit`, `tz-offset`, `short` 는 16-bit signed 정수로 해석한다 (two's complement).
파서는 sign-extend 처리해야 한다 — 그렇지 않으면 음수가 큰 unsigned 로 잘못
읽힌다 (`-3` → `65533`).

`pos-x` · `pos-y` · `pos-z` 는 **32-bit signed** 다 (2 레지스터, §6.2 의 word order
적용). **부호는 선택 사항이 아니다** — ECEF 좌표계는 지구 중심이 원점이라 세 축 모두
음수를 갖고, 온실 내부 좌표계도 원점을 온실 한가운데로 잡으면 음수가 나온다.
unsigned 로 읽으면 음수 좌표가 20억대의 양수로 뒤집힌다.

```python
import struct
lo, hi = registers[addr], registers[addr + 1]
pos_x = struct.unpack('<i', struct.pack('<2H', lo, hi))[0]   # cm
```

---

## 7. Command code vs register opcode

KS 표준의 외부 노출 **command code** 와 일부 구현체가 레지스터에 실제 기록하는
**register opcode** 가 다를 수 있다.

command code 의 정본은 [`../specs/codes.json`](../specs/codes.json) 이다 (§7.1).
예: 스위치형 `OFF=0` · `ON=201` · `TIMED_ON=202`, 개폐형 **`STOP=0`** · `OPEN=301` ·
`CLOSE=302` · `TIMED_OPEN=303` · `TIMED_CLOSE=304`.

**정지 명령은 `0` 이다.** `303` 은 `TIMED_OPEN`(열림방향 일정 시간 작동)이다 —
KS X 3267:2022 부속서 B.3. 이전 판본의 이 절은 `STOP=303` 이라 적고 있었다.

양액기(`ONCE_SUPPLY=401` · `WATER_SUPPLY=402` · `NUT_SUPPLY=403` · `AREA_WATER_SUPPLY=404` ·
`AREA_NUT_SUPPLY=405`)와 표시기(`VALUE_DISPLAY=501` · `TIME_DISPLAY=502` · `CODE_DISPLAY=503`)는
KS X 3267 범위 밖이며 **KS B 7958-5 부속서 B.3** 이 정의한다 — `codes.json` 에 수록돼 있다(§7.1).

개폐기 305·306 은 표준마다 이름이 다르다 — `SET_POSITION`/`MOVE_POSITION`,
`SET_CONFIG`/`SET_OC_TIME`. 값과 기능은 같다.

`write.operations[]` (§8) 가 정의된 경우 `opcode` 필드는 command code 와 일치
한다 — 파서가 수신한 operation 값으로 opcode 별 layout 을 선택하는 것이 §8 의
메커니즘.

### 7.1 코드 일람표 — `specs/codes.json`

`status`·`operation`·`control`·제품 타입의 **코드 값 ↔ 의미** 대응은
[`../specs/codes.json`](../specs/codes.json) 이 정하며, 그 파일이 **유일한 원천**이다.
§5.5 가 라벨에 대해 그렇듯, 도구·프롬프트가 코드값을 상수로 들고 있으면 안 된다.

수록 범위는 두 갈래다.

| 근거 | tier | protocol | 내용 |
|---|---|---|---|
| **KS X 3267:2022 부속서 B** (발행본) | `normative` | `10` | 제품 타입 · 상태 · 명령 · 제어권 |
| **KS B 7958-5:2027 부속서 A·B** (제정 협의 중, `2026-draft-rev6`) | `draft` | `30` · `31` | 위 전부 + **양액기 경보(`alert`)** · **device code(`device-type`)** · 게이트웨이 노드 타입 |

부속서 A·B 는 **규정(normative) 부속서**이나 **표준 자체가 발행 전**이다. 원문 초안(docx)은
아카이브에 두지 않고 값만 싣는다. **`draft` 값은 발행 시 바뀔 수 있다.**

두 표준이 같은 코드를 정의하는 경우 값은 같고 **이름이 갈리는 지점이 있다** — 각 값의
`std` 와 `also` 를 확인할 것. 갈리는 지점은 §7.1 아래 `interop-notes` 가 모아 둔다.

수록되지 않은 코드를 만나면 소비처는 **추측하거나 구현체에서 옮겨 오면 안 된다** —
'아카이브에 근거가 없다'고 말할 것.

`codes.json` 은 값마다 `tier` 를 갖는다 — `normative`(KS X 3267:2022 발행본, protocol
`10`)와 `draft`(KS B 7958-5 제정 협의 중, protocol `30`/`31`). **`draft` 값은 발행 시
바뀔 수 있으므로 그에 근거한 판정을 단정하면 안 된다.**

`codes.json` 의 `interop-notes` 는 표준 코드가 현장 구현에서 갈리는 지점을 기록한다 —
코드 정의가 아니라 오진 방지용 주의 사항이다. 특히 **수동 상태의 표현이 protocol 마다
다르고**, **`status` 와 `operation` 은 같은 숫자가 다른 뜻**이다.

> `operation` 의 `STOP` 표기 오류는 해소됐다 — 정지는 `0`, `303` 은 `TIMED_OPEN` 이다.
>
> `control` 코드 3 은 **오류가 아니라 표준 간 차이**였다. KS X 3267 은 `MANUAL`,
> KS B 7958-5 는 `IMMUTABLE_LOCALMANUAL` 이다. 값(3)과 뜻(원격으로 바꿀 수 없는 수동)은
> 같으므로 어느 쪽도 틀리지 않았다 — **protocol 에 따라 이름을 골라야 한다.**

---

## 8. `write.operations[]` — opcode 가변 레이아웃

양액기 Lv2/Lv4, FND 표시기 등 **opcode 마다 레지스터 레이아웃이 다른** 장비를 위한
write 영역 정의. flat `write.items` 와 공존한다 (둘 중 하나 사용).

```jsonc
// flat: 모든 명령이 같은 items
"write": { "items": ["operation", "opid", "hold-time"] }

// operations: opcode 별 items
"write": {
    "starting-register": 504,
    "operations": [
        { "opcode": 501, "items": ["operation", "opid", "value", "sig-digit"] },
        { "opcode": 502, "items": ["operation", "opid", "epoch", "tz-offset"] },
        { "opcode": 503, "items": ["operation", "opid", "short"] }
    ]
}
```

### 8.1 영역 크기

`operations` 구조의 write 영역 크기는 **모든 opcode 의 items 크기 중 최대**:

```
write_size = max(Σitems[opcode].register_size  for each opcode)
```

이 크기로 데이터스토어를 할당하고, 다음 장비의 write 주소를 계산한다.

### 8.2 활성 opcode 결정

수신한 `operation` 레지스터 값과 일치하는 `opcode` 항목의 `items` 가 활성 layout
이다. 일치하는 opcode 가 없으면 (예: `OFF=0` 같은 공통 명령), 가장 짧은 opcode
items 의 공통 prefix (`[operation, opid]`) 만 유효하다.

---

## 9. `Devices` 와 자율배치

노드 장비 규격의 `Devices` 배열은 두 가지 모드로 사용된다:

### 9.1 명시 모드 — `Devices` 에 직접 작성

각 슬롯 장비를 §4 의 형식으로 작성. 각 장비의 `starting-register` 도 직접 명시.

#### 9.1.1 `Devices` 인덱스 = devinfo 슬롯 (필수 계약)

파서는 `Devices` 배열을 **인덱스 순서로** devinfo 슬롯과 짝짓는다:

```python
for idx, dev_spec in enumerate(spec["Devices"]):
    device_code = devinfo[idx]        # 배열 위치가 곧 슬롯 번호
```

따라서 다음 네 가지가 **장비 규격 작성자의 의무**다:

| 규칙 | 내용 |
|------|------|
| 인덱스 = 슬롯 | `Devices[i]` 는 **1-based 슬롯 번호 `i+1`** 이며 devinfo 레지스터의 `i` 번째 값과 대응한다 |
| 길이 일치 | `len(Devices)` 는 `nodeinfo` 의 **연결장비수**(6번째 값) 와 같아야 한다 |
| 빈 슬롯 유지 | **미장착 슬롯(devinfo=0)도 항목을 빼면 안 된다.** 빼는 순간 이후 슬롯이 전부 한 칸씩 당겨져 장비 종류가 어긋난다 |
| 주소 연속 | 같은 `Class` 가 이어지는 구간에서는 `starting-register` 가 등차로 이어져야 한다 |

> **왜 위험한가**: 어긋난 슬롯의 양옆이 `devinfo=0` 이면 **devinfo 코드 대조만으로는
> 통과한다** (양쪽 다 활성 슬롯이 아니라 검사 조건에 걸리지 않는다). 실제 사고 사례로,
> 34개 장비 규격에서 미장착 슬롯 2개가 누락돼 36슬롯 노드의 슬롯 30·31·32·34 가
> 잘못된 장비로 인식됐는데 코드 대조는 통과했다. 이 유형은 **주소 연속성 검사**로만
> 잡힌다 (§9.1.3).

#### 9.1.2 미장착 슬롯 표기 — `Type: "reserved"`

장비가 붙지 않는 슬롯은 **삭제하지 말고** 예약어로 자리를 지킨다:

```json
{
  "Class": "sensor",
  "Type": "reserved",
  "Model": "",
  "Name": "예비슬롯29",
  "CommSpec": { "KS X 3267": { "read": { "starting-register": 311, "items": ["value", "status"] } } }
}
```

- `reserved` 는 장비 코드 0 으로 해석돼 **파서가 인스턴스를 만들지 않는다**.
- "알 수 없는 Type" 경고(§9.1.3) 대상에서 **제외**된다 — 오타와 의도적 예비 슬롯을 구분하기 위한 예약어다.
- `CommSpec.read` 는 그 슬롯이 차지하는 주소 공간을 그대로 적는다 (주소 연속성 유지).

#### 9.1.3 검증 규칙

§9.1.1 의 계약 위반은 다음 검사로 드러난다. 파서와 장비 규격 작성 도구는 노드 장비
규격을 로드할 때 이 검사를 수행하고 결과를 보고해야 한다:

| `code` | level | 검사 |
|--------|-------|------|
| `slot-code-mismatch` | warning | 슬롯의 devinfo 코드 ↔ 규격 `Type` 코드 불일치 |
| `unknown-type` | warning | 알 수 없는 `Type` — 코드 0 이라 슬롯 검사가 꺼지므로 타입당 1회 경고 |
| `length-mismatch` | warning | `len(Devices)` ↔ 연결장비수 ↔ `len(devinfo)` 불일치 |
| `devinfo-overflow` | error | devinfo 활성 슬롯이 `Devices` 범위 초과 — 조용히 누락됨 |
| `address-gap` | warning | 같은 `Class` 구간에서 `starting-register` 갭 — 슬롯 누락 의심 |
| `address-overlap` | error | 주소 역행·중첩 |

> `Class` 가 바뀌는 경계(예: 센서 블록 → 양액기 블록)는 영역 분리로 보고 주소 검사를
> 건너뛴다. `Devices` 가 빈 배열(자율배치) 이면 대조할 슬롯 정의가 없으므로 검사 대상이 아니다.

> `unknown-type` 판정은 `codes.json` 의 `name` 과 **`deprecated-alias` 를 함께** 대조해야
> 한다 (§4.1). 번들 vendor pack 의 device code 1 · 2 · 23 · 24 가 구 영문명을 유지하고
> 있어, `name` 만 보면 이 4종이 미지 타입으로 떨어진다.

> **참고 구현**: KSDevice 0.3.31+ 는 본 절의 표기와 검사를
> `ksdevice.common.spec_validation.validate_node_spec()` 으로 제공하며, 서버
> `Node.__init__` 과 클라이언트 `NodeSpec.__init__` 이 기동 시 자동 호출한다. 패키지
> 번들 `999_999_2_1_10_24.spec` 이 `reserved` 표기의 참조 예다 (스위치8 + 개폐기2 +
> 예비 14).

### 9.2 자율배치 모드 — `Devices: []`

`Devices` 를 빈 배열 `[]` 로 두면 파서가 다음 절차로 자동 배치:

1. 노드의 devinfo 영역(레지스터 101-200) 을 읽어 슬롯별 device code 획득
2. 각 device code 에 대응하는 device 템플릿 파일을 참조 (§11)
3. 템플릿의 `CommSpec.read` / `CommSpec.write` 의 `items` 만 사용 (`starting-register` 는 템플릿에 명시하지 않음)
4. 노드 자체 영역 끝부터 순차로 `starting-register` 계산
5. 장비 인스턴스 생성

자율배치는 같은 노드 장비 규격으로 사이트별 다양한 슬롯 구성을 지원할 때 유용하다.

---

## 10. `ConnectedNodes` — 게이트웨이 자식

게이트웨이 노드(type=4) 는 자식 노드를 명시하거나 자동 발견할 수 있다.

### 10.1 명시 모드

`ConnectedNodes` 배열에 자식 노드 장비 규격을 직접 작성:

```json
{
    "Class": "node",
    "Type": "gateway-node/level1",
    "CommSpec": {
        "KS B 7958": {
            "read":  { "starting-register": 201, "items": ["status", "opid"] },
            "write": { "starting-register": 501, "items": ["operation", "opid"] }
        }
    },
    "ConnectedNodes": [
        {
            "unit-id": 2,
            "Class": "node",
            "Type": "sensor-node/level0",
            "CommSpec": {
                "KS B 7958": {
                    "read":  { "starting-register": 203, "items": ["status", "opid", "control"] },
                    "write": { "starting-register": 503, "items": ["operation", "opid", "control"] }
                }
            }
        }
    ]
}
```

### 10.2 자동 발견 모드

`ConnectedNodes` 를 생략하면 파서가 unit_id 2..max_devices+1 범위를 스캔해 자식
노드를 자동 발견. 자식의 `starting-register` 는 게이트웨이 장비 규격의 `CommSpec` 에서
**자동 계산**:

```
child[N].starting-register
    = base + Σ(self_items.register_size) + (N - 1) × 3
      ↑       ↑                              ↑
      gateway gateway 자체 영역 크기         자식은 항상 3 reg
      base
```

| Protocol | 게이트웨이 자체 영역 (read items) | 자체 영역 크기 | 자식 N=1 (uid=2) read 시작 |
|----------|-------------------------------------|----------------|------------------------------|
| 30       | `[]` (없음) | 0 칸 | 201 |
| 31+      | `["status", "opid"]` | 2 칸 | 203 |

write 영역도 동일 공식 (base=501, 31+ 는 503 부터).

만약 새 protocol 32 가 자체 영역 4칸을 정의하면 장비 규격의 `items` 만 4 개 채우면 된다 —
형식 자체가 protocol 분기를 데이터에 위임한다.

### 10.3 자식 영역 구조

각 자식 노드의 게이트웨이 read 영역은 항상 3 register: `[status, opid, control]`.
write 영역도 3 register: `[operation, opid, control]`.

---

## 11. Device 템플릿 파일

자율배치(§9.2) 에서 사용되는 device 단위 템플릿. **단독 폴더 (관습적으로 `devices/`) 안에 모아 둔다.** 세 가지 파일 형식이 공존:

### 11.1 Generic dict 파일

파일명: 자유 (예: `sensor.spec`, `actuator.spec`, `nutrients.spec`)

```jsonc
{
    "1": {
        "Class": "sensor",
        "Type": "temperature-sensor",
        "Model": "SEN-TEMP",
        "Name": "온도센서",
        "CommSpec": { "KS X 3267": { "read": { "items": ["value", "status"] } } }
    },
    "12": { /* EC sensor */ }
}
```

- 키: device code 의 문자열 표현 (`"1"`, `"12"`, `"101"`, …)
- 값: 장비 규격 객체
- protocol 무관 — 모든 호출에서 baseline 으로 적용

### 11.2 Protocol-specific dict 파일

파일명: `<class>_<protocol>.spec` (예: `sensor_31.spec`)

```jsonc
{
    "1": {
        "Class": "sensor", "Type": "temperature-sensor",
        "CommSpec": { "KS B 7958": { "read": { "items": ["value", "status", "tz-offset"] } } }
    }
}
```

- 같은 dict 구조
- 노드 protocol 일치 시에만 활성화

### 11.3 단일 장비 파일

파일명: `{org}_{mfg}_0_<code>_<protocol>.spec` (§2.2)

```jsonc
// 0_0_0_1_31.spec — 온도센서 protocol 31 전용
{
    "Class": "sensor",
    "Type": "temperature-sensor",
    "CommSpec": {
        "KS B 7958": { "read": { "items": ["value", "status", "tz-offset"] } }
    }
}
```

- 파일 내용 = 장비 규격 객체 그 자체 (dict 의 **값** 부분만)
- 파일명의 4번째 세그먼트가 device code 로 자동 매핑
- 노드 protocol 이 5번째 세그먼트와 일치할 때만 활성화

### 11.4 우선순위 (개념)

같은 device code 가 여러 파일에 정의됐을 때 더 구체적인 파일이 이긴다:

```
generic dict (11.1)  <  protocol-specific dict (11.2)  <  단일 장비 (11.3)
```

protocol-specific 과 단일 장비는 노드 protocol 이 일치할 때만 적용된다. 정확한
적용 알고리즘 (캐싱, vendor 격리 등) 은 구현체 책임 — 본 형식 reference 의 범위
밖이다.

### 11.5 `starting-register` 는 적지 않음

세 형식 모두 device 템플릿의 `CommSpec.read/write` 에 **`starting-register` 를
적지 않는다**. 자율배치 시 파서가 노드 자체 영역 끝부터 순차 계산해 주입한다.
`items` 배열만 정의하면 충분.

---

## 12. Fallback 규칙

파일명에 `max_devices` 까지 명시한 형식 (`{org}_{mfg}_{type}_{code}_{proto}_{max}.spec`)
이 없을 때, `max_devices` 를 제외한 형식 (`{org}_{mfg}_{type}_{code}_{proto}.spec`)
을 fallback 으로 시도한다.

예: `0_0_2_3_31_5.spec` 부재 → `0_0_2_3_31.spec` 매칭.

같은 제품 코드에서 슬롯 수만 다른 변종을 한 파일로 커버할 때 유용하다 — 자율배치
(§9.2) 와 결합하면 `Devices: []` 인 한 파일로 다양한 슬롯 구성 지원.

---

## 13. 표준 참조

본 형식은 다음 한국 산업표준에서 정의된 통신 규격을 JSON 으로 표현한다:

- **KS B 7958** (2024-12-20 제정)
- **KS X 3267**
- **KS X 3286**
- **KS X 3288**

표준 간 충돌 시 **KS B 7958 (2024)** 이 우선한다.

다음 표준들은 제정 협의 중 (P1~P5) 으로, 제정되면 본 표준들이 우선한다
(P1 `2026-draft-rev4` / P2 · P4 `2026-draft-rev6` / P3 `2026-draft-rev3` /
P5 `2026-draft-rev6` 기준 — rev2 에서 4부 → 5부로 재배치됨):

- **KS B 7958-1** (P1) — 일반 요구사항
- **KS B 7958-2** (P2) — 부가 장비와 추가 기능
- **KS B 7958-3** (P3) — 노드 발견 (mDNS·DNS-SD, rev2 신설)
- **KS B 7958-4** (P4) — 장비 규격의 확장 (옛 P3)
- **KS B 7958-5** (P5) — 코드일람표 (옛 P4)

코드 발급/협의는 서울대학교, 한국농업기술진흥원 등 표준화 기관에 문의한다.

