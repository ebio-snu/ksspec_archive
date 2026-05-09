{
  "Class" : "node",
  "Type" : "gateway-node/level1",
  "Model" : "DEF-GWNODE-001",
  "Name" : "디폴트 게이트웨이노드",
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
            "starting-register" : 201,
            "items": ["status", "opid", "control"]
          },
          "write" : {
            "starting-register" : 501,
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
            "starting-register" : 204,
            "items": ["status", "opid", "control"]
          },
          "write" : {
            "starting-register" : 504,
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
            "starting-register" : 207,
            "items": ["status", "opid", "control"]
          },
          "write" : {
            "starting-register" : 507,
            "items": ["operation", "opid", "control"]
          }
        }
      }
    },
    {
      "unit-id": 5,
      "Class" : "node",
      "Type" : "nutrient-node/level0",
      "Model" : "DEF-NUTNODE",
      "Name" : "양액기노드",
      "CommSpec" : {
        "KS B 7958" : {
          "read" : {
            "starting-register" : 210,
            "items": ["status", "opid", "control"]
          },
          "write" : {
            "starting-register" : 510,
            "items": ["operation", "opid", "control"]
          }
        }
      }
    }
  ]
}
