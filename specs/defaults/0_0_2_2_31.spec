{
  "Class" : "node",
  "Type" : "actuator-node/level0",
  "Model" : "DEF-ACTNODE-001",
  "Name" : "디폴트 자율배치 구동기노드",
  "CommSpec" : {
    "KS B 7958:2027" : {
      "read" : {
        "starting-register" : 201,
        "items": ["opid", "status", "control"]
      },
      "write": {
        "starting-register" : 501,
        "items": ["operation", "opid", "control"]
      }
    }
  },
  "Devices" : [
  ]
}
