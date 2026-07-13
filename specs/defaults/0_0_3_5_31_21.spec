{
  "Class" : "node",
  "Type" : "integrated-node/level1",
  "Model" : "DEF-NUT-NODE-LV4",
  "Name" : "디폴트 양액기노드 레벨4",
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
    { "Class" : "sensor", "Type" : "EC-sensor", "Model" : "SEN-EC", "Name" : "EC1", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 204, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "EC-sensor", "Model" : "SEN-EC", "Name" : "EC2", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 207, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "EC-sensor", "Model" : "SEN-EC", "Name" : "EC3", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 210, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "pH-sensor", "Model" : "SEN-pH", "Name" : "pH1", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 213, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "pH-sensor", "Model" : "SEN-pH", "Name" : "pH2", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 216, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "pH-sensor", "Model" : "SEN-pH", "Name" : "pH3", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 219, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "pyranometer", "Model" : "SEN-RAD", "Name" : "일사", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 222, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "전체유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 225, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "1구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 228, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "2구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 231, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "3구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 234, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "4구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 237, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "5구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 240, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "6구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 243, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "7구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 246, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "8구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 249, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "9구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 252, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "10구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 255, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "11구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 258, "items": ["status", "value"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "12구역유량", "CommSpec" : { "KS B 7958" : { "read" : { "starting-register" : 261, "items": ["status", "value"] } } } }, 
    { "Class" : "actuator", "Type" : "nutrient-supply/level4", "Model" : "NUT-LV4", "Name" : "양액기Lv4", "CommSpec" : { "KS B 7958" : { 
	"read" : { 
          "starting-register" : 264,
	  "items": ["opid", "status", "area", "alert", "remain-time"] }, 
	"write": { 
          "starting-register" : 505,
	  "operations": [ 
		{ "opcode" : 401, "items":["operation", "opid"] }, 
		{ "opcode" : 402, "items":["operation", "opid", "start-area", "stop-area", "time"] }, 
		{ "opcode" : 403, "items":["operation", "opid", "start-area", "stop-area", "time", "EC", "pH"] }, 
		{ "opcode" : 404, "items":["operation", "opid", "area-bitmap", "time"] }, 
		{ "opcode" : 405, "items":["operation", "opid", "area-bitmap", "time", "EC", "pH"] } 
	  ] 
	} 
    } } 
    } ]
}
