{
  "Class" : "node",
  "Type" : "sensor-node/level0",
  "Model" : "DEF-POSSENSORNODE-001",
  "Name" : "디폴트 위치 이동 센서노드",
  "CommSpec" : {
    "KS B 7958" : {
      "read" : {
        "starting-register" : 202,
        "items": ["status", "zone-id", "pos-x", "pos-y", "pos-z"]
      }
    }
  },
  "Devices" : [
  ]
}
