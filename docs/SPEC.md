# 기술 규격 (Description Specification) 

본 문서는 한국 산업표준 (KS X 3267/3286/3288, KS B 7958-1..4) 의 스마트 온실 장비 통신 규격을 JSON 파일로 표현하기 위한 **기술 규격 파일 형식** 을 정의한다. 

## 목차

1. [개요](#1-개요)
2. [파일명 규칙](#2-파일명-규칙)
3. [JSON 구조 — 노드 기술 규격](#3-json-구조--노드-기술-규격)
4. [JSON 구조 — 장비 기술 규격](#4-json-구조--장비-기술-규격)
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

기술 규격 파일은 한 노드 또는 한 장비의 Modbus 레지스터 맵을 JSON 으로 기술한다.
노드 정보(`org`, `mfg`, `type`, `code`, `protocol`, `max_devices`) 가 결정되면
대응하는 기술 규격 파일이 식별되고, 해당 파일이 어느 주소에서 어떤 값을 어떤 형식
으로 읽고 쓸지를 정의한다.

기술 규격은 두 가지 입자도(granularity) 로 표현된다:

- **노드 기술 규격** (§3): 한 노드 전체 — 노드 자체 통신 영역 + 슬롯별 장비 배열
- **장치 기술 규격** (§4): 한 장비 — 노드 기술규격의 `Devices` 안에 인라인 또는 device 템플릿 파일 (§11) 로 분리

---

## 2. 파일명 규칙

### 2.1 노드 기술 규격 파일명

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

### 2.2 단일 장비 기술 규격 파일명 (옵션)

자율배치(§9) 에서 사용되는 device 단위 템플릿. 노드 기술규격과 구분하기 위해
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

## 3. JSON 구조 — 노드 기술 규격

```json
{
    "Class": "node",
    "Type": "actuator-node/level1",
    "Model": "FARMOS-AN-LV1-5",
    "Name": "FarmOS 5채널 구동기노드 Lv1",
    "CommSpec": {
        "KS B 7958:2027": {
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
| `nutrient-node/level0..3` | 양액기 / 복합 노드 (type=3) |
| `gateway-node/level0..1` | 게이트웨이 노드 (type=4) |

`level` 은 KS 표준이 정의한 기능 등급 (level 0=수동, 1=기본 제어, 2+=고급).

---

## 4. JSON 구조 — 장비 기술 규격

```json
{
    "Class": "actuator",
    "Type": "switch/level1",
    "Model": "FARMOS-SW1",
    "Name": "전등1",
    "CommSpec": {
        "KS B 7958:2027": {
            "read":  { "starting-register": 204, "items": ["opid", "status", "remain-time"] },
            "write": { "starting-register": 504, "items": ["operation", "opid", "hold-time"] }
        }
    }
}
```

### 4.1 `Class` / `Type` 가능한 값

| Class | Type 예 | 비고 |
|-------|---------|------|
| `sensor` | `temperature-sensor`, `humidity-sensor`, `EC-sensor`, `pH-sensor`, `flow-sensor`, ... | KS B 7958-4 부속서 C |
| `actuator` | `switch/level0..2`, `retractable/level0..2`, `nutrient-supply/level0..3` | level 별로 명령 셋이 다름 |
| `actuator` (표시기) | `fnd` | device code 301 |

전체 device code 표는 KS B 7958-4 부속서 C 참고.

### 4.2 구동기 level 의미

- **level 0**: 상태 read-only (수동 장비)
- **level 1**: ON/OFF + timed 명령
- **level 2**: level 1 + 위치/비율 (개폐기 position, 스위치 ratio)
- **level 3** (양액기): area bitmap zone 선택 + EC/pH 목표값

---

## 5. `CommSpec` — 통신 영역 정의

`CommSpec` 의 키는 적용 표준 라벨이다. 첫 키만 의미를 가지며, 둘 이상 정의해도
파서는 첫 항목을 사용한다.

```json
"CommSpec": {
    "KS B 7958:2027": { "read": {...}, "write": {...} }
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
| `control` | 1 | 제어권 (1=LOCAL, 2=REMOTE, 3=IMMUTABLE_LOCAL_MANUAL) — 필드 부재 시 노드에 제어권 개념 없음 |

### 5.3 노드 write items 의 표준 항목

| 항목 | 크기 | 의미 |
|------|:----:|------|
| `operation` | 1 | 명령 코드 |
| `opid` | 1 | 새 명령 ID |
| `control` | 1 | 제어권 변경 명령 시 새 모드 (선택) |

### 5.4 주소 계산 규칙

기술 규격 작성자는 다음 규칙을 따라야 한다:

1. 첫 장비의 `starting-register` = 노드 read 영역 다음 주소
   (예: 노드 영역 201-203 → 첫 장비 204)
2. 다음 장비 = 이전 장비 영역의 다음 주소 (이전 영역 크기만큼 +)
3. write 영역도 동일 규칙 (501 부터)

작성된 주소는 그대로 신뢰되어야 한다 — 파서가 자동 보정하지 않는다.

---

## 6. Items 인코딩

### 6.1 표준 아이템 타입

| 아이템 | regs | 데이터 타입 | 용도 |
|--------|:----:|------------|------|
| `value` | 2 | float (IEEE 754) | 센서 측정값 |
| `EC` | 2 | float | 양액기 EC |
| `pH` | 2 | float | 양액기 pH |
| `status` | 1 | uint16 | 상태 코드 |
| `opid` | 1 | uint16 | 명령 ID (1-65535, 0 미사용) |
| `operation` | 1 | uint16 | 명령 코드 |
| `control` | 1 | uint16 | 제어권 |
| `ratio`, `position` | 1 | uint16 | 스위치 비율 / 개폐기 위치 |
| `area`, `alert` | 1 | uint16 | 양액기 zone / 경고 |
| `remain-time`, `hold-time`, `time` | 2 | int32 | 잔여/유지/지속 시간 (초) |
| `on-sec`, `remain-sec` | 2 | int32 | 양액기 관수·잔여 시간(초) |
| `start-area`, `stop-area` | 1 | uint16 | 양액기 관수 시작구역/종료구역 |
| `open-time`, `close-time` | 1 | uint16 | 개폐기 총 열리는 시간(초), 닫히는 시간(초) |
| `area-bitmap` | 2 | int32 | 양액기 구역 bitmap |
| `epoch` | 2 | int32 | 세계시 시각 (Unix epoch) |
| `sig-digit` | 1 | int16 (signed) | FND 표시 자릿수 |
| `tz-offset` | 1 | int16 (signed) | 시각대 오프셋 (시 단위) |
| `short` | 1 | uint16 | 일반 16-bit 값 (오류 코드 등) |
| `vfloat` | 2 | float | 일반 float (확장용) |
| `vint` | 1 | uint16 | 일반 short (확장용) |

### 6.2 다중 레지스터 값 인코딩 (KS B 7958-1 §4.4)

2 레지스터 이상의 값(float, int32) 은 **little-endian word order** 로 인코딩 —
낮은 register 주소가 low word, 높은 주소가 high word.

```python
import struct
# float 인코딩 (4 bytes → 2 regs)
hi, lo = struct.unpack('<2H', struct.pack('<f', 23.5))
registers[addr]   = lo   # low word at lower addr
registers[addr+1] = hi
```

명시적 little-endian 포맷(`'<f'`, `'<i'`) 을 사용해 플랫폼 독립성을 확보한다.

### 6.3 Signed 항목

`sig-digit`, `tz-offset` 은 16-bit signed 정수로 해석한다 (two's complement).
파서는 sign-extend 처리해야 한다 — 그렇지 않으면 음수가 큰 unsigned 로 잘못
읽힌다 (`-3` → `65533`).

---

## 7. Command code vs register opcode

KS 표준의 외부 노출 **command code** (예: `ON=201`, `OFF=0`, `OPEN=301`,
`CLOSE=302`, `STOP=303`, `ONCE_SUPPLY=401`, `WATER_SUPPLY=402`,
`NUT_SUPPLY=403`, `DISPLAY_VALUE=501`) 와 일부 구현체가 레지스터에 실제
기록하는 **register opcode** 가 다를 수 있다.

`write.operations[]` (§8) 가 정의된 경우 `opcode` 필드는 command code 와 일치
한다 — 파서가 수신한 operation 값으로 opcode 별 layout 을 선택하는 것이 §8 의
메커니즘.

---

## 8. `write.operations[]` — opcode 가변 레이아웃

양액기 Lv2/Lv3, FND 표시기 등 **opcode 마다 레지스터 레이아웃이 다른** 장비를 위한
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

노드 기술규격의 `Devices` 배열은 두 가지 모드로 사용된다:

### 9.1 명시 모드 — `Devices` 에 직접 작성

각 슬롯 장비를 §4 의 형식으로 작성. 각 장비의 `starting-register` 도 직접 명시.

### 9.2 자율배치 모드 — `Devices: []`

`Devices` 를 빈 배열 `[]` 로 두면 파서가 다음 절차로 자동 배치:

1. 노드의 devinfo 영역(레지스터 101-200) 을 읽어 슬롯별 device code 획득
2. 각 device code 에 대응하는 device 템플릿 파일을 참조 (§11)
3. 템플릿의 `CommSpec.read` / `CommSpec.write` 의 `items` 만 사용 (`starting-register` 는 템플릿에 명시하지 않음)
4. 노드 자체 영역 끝부터 순차로 `starting-register` 계산
5. 장비 인스턴스 생성

자율배치는 같은 노드 기술규격으로 사이트별 다양한 슬롯 구성을 지원할 때 유용하다.

---

## 10. `ConnectedNodes` — 게이트웨이 자식

게이트웨이 노드(type=4) 는 자식 노드를 명시하거나 자동 발견할 수 있다.

### 10.1 명시 모드

`ConnectedNodes` 배열에 자식 노드 기술규격을 직접 작성:

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
노드를 자동 발견. 자식의 `starting-register` 는 게이트웨이 기술규격의 `CommSpec` 에서
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

만약 새 protocol 32 가 자체 영역 4칸을 정의하면 기술규격의 `items` 만 4 개 채우면 된다 —
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
- 값: device 기술 규격 객체
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

- 파일 내용 = device 기술 규격 객체 그 자체 (dict 의 **값** 부분만)
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

다음 표준들은 제정 협의 중 (P1~P4) 으로, 제정되면 본 표준들이 우선한다:

- **KS B 7958-1** (P1)
- **KS B 7958-2** (P2)
- **KS B 7958-3** (P3)
- **KS B 7958-4** (P4)

코드 발급/협의는 서울대학교, 한국농업기술진흥원 등 표준화 기관에 문의한다.

