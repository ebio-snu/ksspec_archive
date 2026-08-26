{
  "Class" : "node",
  "Type" : "integrated-node/level1",
  "Model" : "DEF-NUT-NODE-LV4",
  "Name" : "디폴트 지정구역 제어가능 양액기노드 레벨4",
  "CommSpec" : {
    "KS B 7958" : {
      "read" : {
        "starting-register" : 201,
        "items": ["opid", "status", "control"]
      },
      "write" : {
        "starting-register" : 501,
        "operations" : [{
		"opcode":  1, "items": ["operation", "opid"]
        }, {
		"opcode":  2, "items": ["operation", "opid", "control"]
        }, {
		"opcode":  3, "items": ["operation", "opid", "epoch"]
        }]
      }
    }
  },
  "Devices" : [
  ]
}
