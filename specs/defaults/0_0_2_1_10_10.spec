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
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치1", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 204, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 504, "items": ["operation", "opid", "hold-time"] } } } },
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치2", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 208, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 508, "items": ["operation", "opid", "hold-time"] } } } },
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치3", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 212, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 512, "items": ["operation", "opid", "hold-time"] } } } },
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치4", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 216, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 516, "items": ["operation", "opid", "hold-time"] } } } },
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치5", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 220, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 520, "items": ["operation", "opid", "hold-time"] } } } },
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치6", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 224, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 524, "items": ["operation", "opid", "hold-time"] } } } },
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치7", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 228, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 528, "items": ["operation", "opid", "hold-time"] } } } },
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치8", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 232, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 532, "items": ["operation", "opid", "hold-time"] } } } },
    { "Class" : "actuator", "Type" : "retractable/level1", "Model" : "MOTOR-LV1", "Name" : "개폐기1", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 236, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 536, "items": ["operation", "opid", "time"] } } } },
    { "Class" : "actuator", "Type" : "retractable/level1", "Model" : "MOTOR-LV1", "Name" : "개폐기2", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 240, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 540, "items": ["operation", "opid", "time"] } } } }
  ]
}
