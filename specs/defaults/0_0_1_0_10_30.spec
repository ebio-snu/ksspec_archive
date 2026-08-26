{
  "Class" : "node",
  "Type" : "sensor-node/level0",
  "Model" : "DEF-SENSORNODE-001",
  "Name" : "디폴트 센서노드",
  "CommSpec" : {
    "KS X 3267" : {
      "read" : {
        "starting-register" : 202,
        "items": ["status"]
      }
    }
  },
  "Devices" : [
    { "Class" : "sensor", "Type" : "air-temperature-sensor", "Model" : "SEN-TEMP", "Name" : "온도센서1", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 203, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "air-temperature-sensor", "Model" : "SEN-TEMP", "Name" : "온도센서2", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 206, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "air-temperature-sensor", "Model" : "SEN-TEMP", "Name" : "온도센서3", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 209, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "relative-humidity-sensor", "Model" : "SEN-HUM", "Name" : "습도센서1", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 212, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "dewpoint-sensor", "Model" : "SEN-DEW", "Name" : "이슬점센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 215, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "rain-detector", "Model" : "SEN-RAIN-D", "Name" : "감우센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 218, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "cumulative-flow-sensor", "Model" : "SEN-FLOW", "Name" : "누적유량센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 221, "items": ["value", "status"] } } } },
    { "Class" : "sensor", "Type" : "rainfall-sensor", "Model" : "SEN-RAIN-G", "Name" : "강우센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 224, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "pyranometer", "Model" : "SEN-RAD", "Name" : "일사센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 227, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "wind-speed-sensor", "Model" : "SEN-WSPEED", "Name" : "풍속센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 230, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "wind-direction-sensor", "Model" : "SEN-WDIR", "Name" : "풍향센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 233, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "voltage-sensor", "Model" : "SEN-VOL", "Name" : "전압센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 236, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "CO2-sensor", "Model" : "SEN-CO2", "Name" : "이산화탄소센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 239, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "EC-sensor", "Model" : "SEN-EC", "Name" : "EC센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 242, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "quantum-sensor", "Model" : "SEN-QUAN", "Name" : "광양자센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 245, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "soil-moisture-sensor", "Model" : "SEN-SMOI", "Name" : "토양함수율센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 248, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "tensiometer", "Model" : "SEN-TEN", "Name" : "토양수분장력센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 251, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "pH-sensor", "Model" : "SEN-pH", "Name" : "pH센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 254, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "soil-temperature-sensor", "Model" : "SEN-STEMP", "Name" : "지온센서", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 257, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "air-temperature-sensor", "Model" : "SEN-TEMP", "Name" : "온도센서4", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 260, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "air-temperature-sensor", "Model" : "SEN-TEMP", "Name" : "온도센서5", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 263, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "air-temperature-sensor", "Model" : "SEN-TEMP", "Name" : "온도센서6", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 266, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "air-temperature-sensor", "Model" : "SEN-TEMP", "Name" : "온도센서7", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 269, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "air-temperature-sensor", "Model" : "SEN-TEMP", "Name" : "온도센서8", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 272, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "air-temperature-sensor", "Model" : "SEN-TEMP", "Name" : "온도센서9", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 275, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "air-temperature-sensor", "Model" : "SEN-TEMP", "Name" : "온도센서10", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 278, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "relative-humidity-sensor", "Model" : "SEN-HUM", "Name" : "습도센서2", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 281, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "relative-humidity-sensor", "Model" : "SEN-HUM", "Name" : "습도센서3", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 284, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "weight-sensor", "Model" : "SEN-WGT", "Name" : "무게센서1", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 287, "items": ["value", "status"] } } } }, 
    { "Class" : "sensor", "Type" : "weight-sensor", "Model" : "SEN-WGT", "Name" : "무게센서2", "CommSpec" : { "KS X 3267" : { "read" : { "starting-register" : 290, "items": ["value", "status"] } } } } 
  ]
}
