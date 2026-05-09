{
  "Class" : "node",
  "Type" : "integrated-node/level1",
  "Model" : "DEF-NUT-NODE-LV3",
  "Name" : "디폴트 지정구역 제어가능 양액기노드 레벨3",
  "CommSpec" : {
    "KS X 3288" : {
      "read" : {
        "starting-register" : 201,
        "items": ["status", "opid", "control"]
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
