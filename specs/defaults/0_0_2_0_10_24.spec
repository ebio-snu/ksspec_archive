{
  "Class" : "node",
  "Type" : "actuator-node/level0",
  "Model" : "DEF-ACTNODE-001",
  "Name" : "디폴트 구동기노드",
  "CommSpec" : {
    "KS X 3267" : {
      "read" : {
        "starting-register" : 201,
        "items": ["opid", "status"]
      }
    }
  },
  "Devices" : [
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치1", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 203, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 503, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치2", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 207, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 507, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치3", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 211, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 511, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치4", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 215, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 515, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치5", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 219, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 519, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치6", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 223, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 523, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치7", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 227, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 527, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치8", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 231, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 531, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치9", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 235, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 535, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치10", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 239, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 539, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치11", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 243, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 543, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치12", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 247, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 547, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치13", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 251, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 551, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치14", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 255, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 555, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치15", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 259, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 559, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "switch/level1", "Model" : "SWITCH-LV1", "Name" : "스위치16", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 263, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 563, "items": ["operation", "opid", "hold-time"] } } } }, 
    { "Class" : "actuator", "Type" : "retractable/level1", "Model" : "MOTOR-LV1", "Name" : "개폐기1", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 267, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 567, "items": ["operation", "opid", "time"] } } } }, 
    { "Class" : "actuator", "Type" : "retractable/level1", "Model" : "MOTOR-LV1", "Name" : "개폐기2", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 271, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 571, "items": ["operation", "opid", "time"] } } } }, 
    { "Class" : "actuator", "Type" : "retractable/level1", "Model" : "MOTOR-LV1", "Name" : "개폐기3", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 275, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 575, "items": ["operation", "opid", "time"] } } } }, 
    { "Class" : "actuator", "Type" : "retractable/level1", "Model" : "MOTOR-LV1", "Name" : "개폐기4", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 279, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 579, "items": ["operation", "opid", "time"] } } } }, 
    { "Class" : "actuator", "Type" : "retractable/level1", "Model" : "MOTOR-LV1", "Name" : "개폐기5", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 283, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 583, "items": ["operation", "opid", "time"] } } } }, 
    { "Class" : "actuator", "Type" : "retractable/level1", "Model" : "MOTOR-LV1", "Name" : "개폐기6", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 287, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 587, "items": ["operation", "opid", "time"] } } } }, 
    { "Class" : "actuator", "Type" : "retractable/level1", "Model" : "MOTOR-LV1", "Name" : "개폐기7", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 291, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 591, "items": ["operation", "opid", "time"] } } } }, 
    { "Class" : "actuator", "Type" : "retractable/level1", "Model" : "MOTOR-LV1", "Name" : "개폐기8", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 295, "items": ["opid", "status", "remain-time"] }, "write" : {"starting-register" : 595, "items": ["operation", "opid", "time"] } } } }
  ]
}
