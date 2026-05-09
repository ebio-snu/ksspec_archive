{
  "Class": "node",
  "Type": "actuator-node/auto",
  "Model": "DEF-ACTNODE-AUTO-4",
  "Name": "자율배치 구동기노드 (4 슬롯)",
  "_comment": "Devices 를 비워두어 devinfo + specs/defaults/devices/ 로 자동 배치",
  "CommSpec": {
    "KS X 3267": {
      "read": {
        "starting-register": 201,
        "items": ["opid", "status"]
      }
    }
  },
  "Devices": []
}
