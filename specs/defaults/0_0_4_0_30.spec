{
  "Class" : "node",
  "Type" : "gateway-node/level1",
  "Model" : "DEF-GWNODE-001",
  "Name" : "디폴트 게이트웨이노드 (protocol 30)",
  "_comment" : "protocol 30 은 게이트웨이 자체 상태/제어 영역이 없다. items 가 비어있는 region 으로 자체 영역 0 칸을 명시하면, 자식 슬롯은 starting-register 부터 바로 시작한다 (read=201, write=501).",
  "CommSpec" : {
    "KS B 7958" : {
      "read"  : { "starting-register" : 201, "items" : [] },
      "write" : { "starting-register" : 501, "items" : [] }
    }
  },
  "ConnectedNodes" : [
  ]
}
