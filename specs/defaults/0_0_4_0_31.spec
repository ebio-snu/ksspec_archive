{
  "Class" : "node",
  "Type" : "gateway/level1",
  "Model" : "DEF-GWNODE-001",
  "Name" : "디폴트 게이트웨이노드",
  "CommSpec" : {
    "KS B 7958" : {
      "read" : { "starting-register" : 201, "items": ["opid", "status"] },
      "write" : { "starting-register" : 501, "items": ["operation", "opid"] }
     }
  }
}
