{
  "Class" : "node",
  "Type" : "actuator-node/level1",
  "Model" : "DEF-ACTNODE-001",
  "Name" : "표시기노드 노드",
  "CommSpec" : {
    "KS B 7958:2027" : {
      "read" : {
        "starting-register" : 201,
        "items": ["opid", "status"]
      },
      "write": {
        "starting-register" : 501,
        "items": ["operation", "opid"]
      }
    }
  },
  "Devices" : [
  ]
}
