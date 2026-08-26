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
  },
  "ConnectedNodes" : [
    {
      "unit-id": 2,
      "Class" : "node",
      "Type" : "sensor-node/level0",
      "Model" : "DEF-SENNODE",
      "Name" : "기상대노드",
      "CommSpec" : {
        "KS B 7958" : {
          "read" : {
            "starting-register" : 203,
            "items": ["opid", "status", "control"]
          },
          "write" : {
            "starting-register" : 503,
            "items": ["operation", "opid", "control"]
          }
        }
      }
    },
    {
      "unit-id": 3,
      "Class" : "node",
      "Type" : "sensor-node/level0",
      "Model" : "DEF-SENNODE",
      "Name" : "내부환경센서노드",
      "CommSpec" : {
        "KS B 7958" : {
          "read" : {
            "starting-register" : 206,
            "items": ["opid", "status", "control"]
          },
          "write" : {
            "starting-register" : 506,
            "items": ["operation", "opid", "control"]
          }
        }
      }
    },
    {
      "unit-id": 4,
      "Class" : "node",
      "Type" : "actuator-node/level0",
      "Model" : "DEF-ACTNODE",
      "Name" : "내부구동기노드",
      "CommSpec" : {
        "KS B 7958" : {
          "read" : {
            "starting-register" : 209,
            "items": ["opid", "status", "control"]
          },
          "write" : {
            "starting-register" : 509,
            "items": ["operation", "opid", "control"]
          }
        }
      }
    },
    {
      "unit-id": 5,
      "Class" : "node",
      "Type" : "integrated-node/level0",
      "Model" : "DEF-NUTNODE",
      "Name" : "양액기노드",
      "CommSpec" : {
        "KS B 7958" : {
          "read" : {
            "starting-register" : 212,
            "items": ["opid", "status", "control"]
          },
          "write" : {
            "starting-register" : 512,
            "items": ["operation", "opid", "control"]
          }
        }
      }
    }
  ]
}
