{
  "Class" : "node",
  "Type" : "actuator-node/level1",
  "Model" : "DEF-ACTNODE-LV1",
  "Name" : "디폴트 구동기노드 레벨1 (제어권 지원)",
  "CommSpec" : {
    "KS X 3267" : {
      "read" : {
        "starting-register" : 201,
        "items": ["status", "opid", "control"]
      },
      "write" : {
        "starting-register" : 501,
        "items": ["operation", "opid", "control"]
      }
    }
  },
  "Devices" : [
  ]
}
