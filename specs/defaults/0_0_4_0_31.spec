{
  "Class" : "node",
  "Type" : "gateway-node/level1",
  "Model" : "DEF-GWNODE-001",
  "Name" : "디폴트 게이트웨이노드",
  "CommSpec" : {
    "KS B 7958" : {
      "read" : { "starting-register" : 201, "items": ["status", "opid"] },
      "write" : { "starting-register" : 501, "items": ["operation", "opid"] }
     }
  }
}
