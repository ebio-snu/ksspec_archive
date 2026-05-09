{
  "Class" : "node",
  "Type" : "integrated-node/level1",
  "Model" : "DEF-NUT-NODE-LV3",
  "Name" : "디폴트 양액기노드 레벨3",
  "CommSpec" : {
    "KS X 3288" : {
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
    { "Class" : "sensor", "Type" : "EC-sensor", "Model" : "SEN-EC", "Name" : "EC1", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 204, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "EC-sensor", "Model" : "SEN-EC", "Name" : "EC2", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 207, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "EC-sensor", "Model" : "SEN-EC", "Name" : "EC3", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 210, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "pH-sensor", "Model" : "SEN-pH", "Name" : "pH1", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 213, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "pH-sensor", "Model" : "SEN-pH", "Name" : "pH2", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 216, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "pH-sensor", "Model" : "SEN-pH", "Name" : "pH3", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 219, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "pyranometer", "Model" : "SEN-RAD", "Name" : "일사", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 222, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "전체유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 225, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "1구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 228, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "2구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 231, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "3구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 234, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "4구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 237, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "5구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 240, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "6구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 243, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "7구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 246, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "8구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 249, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "9구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 252, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "10구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 255, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "11구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 258, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "12구역유량", "CommSpec" : { "KS X 3288" : { "read" : { "starting-register" : 261, "items": ["value", "status"] } } } }, 
    {
    "Class" : "actuator",
    "Type" : "nutrient-supply/level3",
    "Model" : "NUT-Lv3",
    "Name" : "양액기",
    "CommSpec" : {
      "KS X 3288" : {
        "read" : {
          "starting-register" : 401,
          "items": ["status", "area", "alert", "opid", "remain-time"]
        },
        "write" : {
          "starting-register" : 504,
          "items": ["operation", "opid", "start-area", "stop-area", "on-sec", "EC", "pH"]
        }
      }
    }
  }]
}
