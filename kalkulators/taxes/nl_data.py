# The data can be obtained from the official website of the Dutch tax authority
# https://www.belastingdienst.nl/wps/wcm/connect/nl/personeel-en-loon/content/hulpmiddel-loonbelastingtabellen
# Though this dictionary is imported from the wonderful https://thetax.nl/ website
# https://raw.githubusercontent.com/stevermeister/dutch-tax-income-calculator-npm/ae6bb245d8becd2cb7e584c3a6ddca22c5fbcc8e/data.json
NL_DATA = {
  "currentYear":2024,
  "years":[
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
    2022,
    2023,
    2024
  ],
  "defaultWorkingHours":40,
  "workingWeeks":52,
  "workingDays":255,
  "rulingThreshold":{
    "2015":{
      "normal":36705,
      "young":27901,
      "research":0
    },
    "2016":{
      "normal":36889,
      "young":28041,
      "research":0
    },
    "2017":{
      "normal":37000,
      "young":28125,
      "research":0
    },
    "2018":{
      "normal":37296,
      "young":28350,
      "research":0
    },
    "2019":{
      "normal":37743,
      "young":28690,
      "research":0
    },
    "2020":{
      "normal":38347,
      "young":29149,
      "research":0
    },
    "2021":{
      "normal":38961,
      "young":29616,
      "research":0
    },
    "2022":{
      "normal":39467,
      "young":30001,
      "research":0
    },
    "2023":{
      "normal":41954,
      "young":31891,
      "research":0
    },
    "2024":{
      "normal":46107,
      "young":35048,
      "research":0
    }

  },
  "payrollTax":{
    "2015":[
      {
        "bracket":1,
        "min":0,
        "max":19822,
        "rate":0.0835
      },
      {
        "bracket":2,
        "min":19823,
        "max":33589,
        "rate":0.1385
      },
      {
        "bracket":3,
        "min":33590,
        "max":57585,
        "rate":0.42
      },
      {
        "bracket":4,
        "min":57586,
        "rate":0.52
      }
    ],
    "2016":[
      {
        "bracket":1,
        "min":0,
        "max":19922,
        "rate":0.0840
      },
      {
        "bracket":2,
        "min":19923,
        "max":33715,
        "rate":0.1205
      },
      {
        "bracket":3,
        "min":33716,
        "max":66421,
        "rate":0.402
      },
      {
        "bracket":4,
        "min":66422,
        "rate":0.52
      }
    ],
    "2017":[
      {
        "bracket":1,
        "min":0,
        "max":19981,
        "rate":0.089
      },
      {
        "bracket":2,
        "min":19982,
        "max":33790,
        "rate":0.1315
      },
      {
        "bracket":3,
        "min":33791,
        "max":67071,
        "rate":0.408
      },
      {
        "bracket":4,
        "min":67072,
        "rate":0.52
      }
    ],
    "2018":[
      {
        "bracket":1,
        "min":0,
        "max":20141,
        "rate":0.089
      },
      {
        "bracket":2,
        "min":20142,
        "max":33993,
        "rate":0.132
      },
      {
        "bracket":3,
        "min":33994,
        "max":68506,
        "rate":0.4085
      },
      {
        "bracket":4,
        "min":68507,
        "rate":0.5195
      }
    ],
    "2019":[
      {
        "bracket":1,
        "min":0,
        "max":20383,
        "rate":0.09
      },
      {
        "bracket":2,
        "min":20384,
        "max":34299,
        "rate":0.1045
      },
      {
        "bracket":3,
        "min":34300,
        "max":68506,
        "rate":0.381
      },
      {
        "bracket":4,
        "min":68507,
        "rate":0.5175
      }
    ],
    "2020":[
      {
        "bracket":1,
        "min":0,
        "max":34711,
        "rate":0.097
      },
      {
        "bracket":2,
        "min":34712,
        "max":68507,
        "rate":0.3735
      },
      {
        "bracket":3,
        "min":68507,
        "rate":0.495
      }
    ],
    "2021":[
      {
        "bracket":1,
        "min":0,
        "max":35129,
        "rate":0.0945
      },
      {
        "bracket":2,
        "min":35130,
        "max":68507,
        "rate":0.3710
      },
      {
        "bracket":3,
        "min":68508,
        "rate":0.495
      }
    ],
    "2022":[
      {
        "bracket":1,
        "min":0,
        "max":35472,
        "rate":0.0942
      },
      {
        "bracket":2,
        "min":35473,
        "max":69399,
        "rate":0.3707
      },
      {
        "bracket":3,
        "min":69399,
        "rate":0.495
      }
    ],
    "2023":[
      {
        "bracket":1,
        "min":0,
        "max":37149,
        "rate":0.0928
      },
      {
        "bracket":2,
        "min":37150,
        "max":73031,
        "rate":0.3693
      },
      {
        "bracket":3,
        "min":73032,
        "rate":0.495
      }
    ],
    "2024":[
      {
        "bracket":1,
        "min":0,
        "max":38097,
        "rate":0.0932
      },
      {
        "bracket":2,
        "min":38098,
        "max":75517,
        "rate":0.3697
      },
      {
        "bracket":3,
        "min":75518,
        "rate":0.495
      }
    ]
  },
  "socialPercent":{
    "2015":[
      {
        "bracket":1,
        "min":0,
        "max":33590,
        "rate":0.3650,
        "social":0.2815,
        "older":0.1025
      }
    ],
    "2016":[
      {
        "bracket":1,
        "min":0,
        "max":33716,
        "rate":0.3655,
        "social":0.2815,
        "older":0.1025
      }
    ],
    "2017":[
      {
        "bracket":1,
        "min":0,
        "max":33791,
        "rate":0.3655,
        "social":0.2765,
        "older":0.0975
      }
    ],
    "2018":[
      {
        "bracket":1,
        "min":0,
        "max":33994,
        "rate":0.3655,
        "social":0.2765,
        "older":0.0975
      }
    ],
    "2019":[
      {
        "bracket":1,
        "min":0,
        "max":34300,
        "rate":0.3665,
        "social":0.2765,
        "older":0.0975
      }
    ],
    "2020":[
      {
        "bracket":1,
        "min":0,
        "max":34712,
        "rate":0.3735,
        "social":0.2765,
        "older":0.0975
      }
    ],
    "2021":[
      {
        "bracket":1,
        "min":0,
        "max":35129,
        "rate":0.3710,
        "social":0.2765,
        "older":0.0975
      }
    ],
    "2022":[
      {
        "bracket":1,
        "min":0,
        "max":35472,
        "rate":0.3707,
        "social":0.2765,
        "older":0.0975
      }
    ],
    "2023":[
      {
        "bracket":1,
        "min":0,
        "max":37150,
        "rate":0.3693,
        "social":0.2765,
        "older":0.0975
      }
    ],
    "2024":[
      {
        "bracket":1,
        "min":0,
        "max":38097,
        "rate":0.3697,
        "social":0.2765,
        "older":0.0975
      }
    ]
  },
  "generalCredit":{
    "2015":[
      {
        "bracket":1,
        "min":0,
        "max":19822,
        "rate":2203
      },
      {
        "bracket":2,
        "min":19823,
        "max":56935,
        "rate":-0.02320
      },
      {
        "bracket":3,
        "min":56936,
        "rate":1342
      }
    ],
    "2016":[
      {
        "bracket":1,
        "min":0,
        "max":19922,
        "rate":2242
      },
      {
        "bracket":2,
        "min":19923,
        "max":66417,
        "rate":-0.04822
      },
      {
        "bracket":3,
        "min":66418,
        "rate":0
      }
    ],
    "2017":[
      {
        "bracket":1,
        "min":0,
        "max":19982,
        "rate":2254
      },
      {
        "bracket":2,
        "min":19983,
        "max":67068,
        "rate":-0.04787
      },
      {
        "bracket":3,
        "min":67069,
        "rate":0
      }
    ],
    "2018":[
      {
        "bracket":1,
        "min":0,
        "max":20142,
        "rate":2265
      },
      {
        "bracket":2,
        "min":20143,
        "max":68507,
        "rate":-0.04683
      },
      {
        "bracket":3,
        "min":68508,
        "rate":0
      }
    ],
    "2019":[
      {
        "bracket":1,
        "min":0,
        "max":20384,
        "rate":2477
      },
      {
        "bracket":2,
        "min":20384,
        "max":68507,
        "rate":-0.05147
      },
      {
        "bracket":3,
        "min":68508,
        "rate":0
      }
    ],
    "2020":[
      {
        "bracket":1,
        "min":0,
        "max":20711,
        "rate":2711
      },
      {
        "bracket":2,
        "min":20711,
        "max":68507,
        "rate":-0.05672
      },
      {
        "bracket":3,
        "min":68508,
        "rate":0
      }
    ],
    "2021":[
      {
        "bracket":1,
        "min":0,
        "max":21043,
        "rate":2837
      },
      {
        "bracket":2,
        "min":21043,
        "max":68507,
        "rate":-0.05977
      },
      {
        "bracket":3,
        "min":68508,
        "rate":0
      }
    ],
    "2022":[
      {
        "bracket":1,
        "min":0,
        "max":21318,
        "rate":2888
      },
      {
        "bracket":2,
        "min":21318,
        "max":69398,
        "rate":-0.06007
      },
      {
        "bracket":3,
        "min":69399,
        "rate":0
      }
    ],
    "2023":[
      {
        "bracket":1,
        "min":0,
        "max":22661,
        "rate":3070
      },
      {
        "bracket":2,
        "min":22661,
        "max":73031,
        "rate":-0.06095
      },
      {
        "bracket":3,
        "min":73032,
        "rate":0
      }
    ],
    "2024":[
      {
        "bracket":1,
        "min":0,
        "max":24813,
        "rate":3362
      },
      {
        "bracket":2,
        "min":24813,
        "max":75518,
        "rate":-0.06630
      },
      {
        "bracket":3,
        "min":75519,
        "rate":0
      }
    ]
  },
  "labourCredit":{
    "2015":[
      {
        "bracket":1,
        "min":0,
        "max":9010,
        "rate":0.0181
      },
      {
        "bracket":2,
        "min":9011,
        "max":19463,
        "rate":0.19679
      },
      {
        "bracket":3,
        "min":19464,
        "max":49770,
        "rate":2220
      },
      {
        "bracket":4,
        "min":49771,
        "max":100670,
        "rate":-0.04
      },
      {
        "bracket":5,
        "min":100671,
        "rate":184
      }
    ],
    "2016":[
      {
        "bracket":1,
        "min":0,
        "max":9147,
        "rate":0.01793
      },
      {
        "bracket":2,
        "min":9148,
        "max":19758,
        "rate":0.27698
      },
      {
        "bracket":3,
        "min":19759,
        "max":34015,
        "rate":3103
      },
      {
        "bracket":4,
        "min":34016,
        "max":111590,
        "rate":-0.04
      },
      {
        "bracket":5,
        "min":111591,
        "rate":0
      }
    ],
    "2017":[
      {
        "bracket":1,
        "min":0,
        "max":9309,
        "rate":0.01772
      },
      {
        "bracket":2,
        "min":9310,
        "max":20108,
        "rate":0.28317
      },
      {
        "bracket":3,
        "min":20109,
        "max":32444,
        "rate":3223
      },
      {
        "bracket":4,
        "min":32445,
        "max":121972,
        "rate":-0.036
      },
      {
        "bracket":5,
        "min":121973,
        "rate":0
      }
    ],
    "2018":[
      {
        "bracket":1,
        "min":0,
        "max":9468,
        "rate":0.01764
      },
      {
        "bracket":2,
        "min":9469,
        "max":20450,
        "rate":0.28064
      },
      {
        "bracket":3,
        "min":20451,
        "max":33112,
        "rate":3249
      },
      {
        "bracket":4,
        "min":33113,
        "max":123362,
        "rate":-0.036
      },
      {
        "bracket":5,
        "min":123363,
        "rate":0
      }
    ],
    "2019":[
      {
        "bracket":1,
        "min":0,
        "max":9694,
        "rate":0.01754
      },
      {
        "bracket":2,
        "min":9694,
        "max":20940,
        "rate":0.28712
      },
      {
        "bracket":3,
        "min":20941,
        "max":34060,
        "rate":3399
      },
      {
        "bracket":4,
        "min":34061,
        "max":90710,
        "rate":-0.06
      },
      {
        "bracket":5,
        "min":90711,
        "rate":0
      }
    ],
    "2020":[
      {
        "bracket":1,
        "min":0,
        "max":9921,
        "rate":0.02812
      },
      {
        "bracket":2,
        "min":9921,
        "max":21430,
        "rate":0.28812
      },
      {
        "bracket":3,
        "min":21430,
        "max":34954,
        "rate":0.01656
      },
      {
        "bracket":4,
        "min":34954,
        "max":98604,
        "rate":-0.06
      },
      {
        "bracket":5,
        "min":98604,
        "rate":0
      }
    ],
    "2021":[
      {
        "bracket":1,
        "min":0,
        "max":10108,
        "rate":0.04581
      },
      {
        "bracket":2,
        "min":10108,
        "max":21835,
        "rate":0.28771
      },
      {
        "bracket":3,
        "min":21835,
        "max":35652,
        "rate":0.02663
      },
      {
        "bracket":4,
        "min":35652,
        "max":105736,
        "rate":-0.06
      },
      {
        "bracket":5,
        "min":105736,
        "rate":0
      }
    ],
    "2022":[
      {
        "bracket":1,
        "min":0,
        "max":10351,
        "rate":0.04541
      },
      {
        "bracket":2,
        "min":10351,
        "max":22357,
        "rate":0.28461
      },
      {
        "bracket":3,
        "min":22357,
        "max":36650,
        "rate":0.02610
      },
      {
        "bracket":4,
        "min":36650,
        "max":109347,
        "rate":-0.05860
      },
      {
        "bracket":5,
        "min":109347,
        "rate":0
      }
    ],
    "2023":[
      {
        "bracket":1,
        "min":0,
        "max":10741,
        "rate":0.08231
      },
      {
        "bracket":2,
        "min":10741,
        "max":23201,
        "rate":0.29861
      },
      {
        "bracket":3,
        "min":23201,
        "max":37692,
        "rate":0.03085
      },
      {
        "bracket":4,
        "min":37692,
        "max":115296,
        "rate":-0.06510
      },
      {
        "bracket":5,
        "min":115296,
        "rate":0
      }
    ],
    "2024":[
      {
        "bracket":1,
        "min":0,
        "max":11490,
        "rate":0.08425
      },
      {
        "bracket":2,
        "min":11490,
        "max":24820,
        "rate":0.31433
      },
      {
        "bracket":3,
        "min":24820,
        "max":39957,
        "rate":0.02471
      },
      {
        "bracket":4,
        "min":39957,
        "max":124934,
        "rate":-0.06510
      },
      {
        "bracket":5,
        "min":115296,
        "rate":0
      }
    ]
  },
  "lowWageThreshold":{
    "2015":6035,
    "2016":6134,
    "2017":6166,
    "2018":6196,
    "2019":6758,
    "2020":7258,
    "2021":7646,
    "2022":7790,
    "2023":8313,
    "2024":9094
  },
  "elderCredit":{
    "2015":[
      {
        "bracket":1,
        "min":0,
        "max":35770,
        "rate":1042
      },
      {
        "bracket":2,
        "min":35770,
        "rate":152
      }
    ],
    "2016":[
      {
        "bracket":1,
        "min":0,
        "max":35949,
        "rate":1187
      },
      {
        "bracket":2,
        "min":35949,
        "rate":70
      }
    ],
    "2017":[
      {
        "bracket":1,
        "min":0,
        "max":36057,
        "rate":1292
      },
      {
        "bracket":2,
        "min":36057,
        "rate":71
      }
    ],
    "2018":[
      {
        "bracket":1,
        "min":0,
        "max":36346,
        "rate":1418
      },
      {
        "bracket":2,
        "min":36346,
        "rate":72
      }
    ],
    "2019":[
      {
        "bracket":1,
        "min":0,
        "max":36783,
        "rate":1596
      },
      {
        "bracket":2,
        "min":36783,
        "max":47423,
        "rate":-0.15
      },
      {
        "bracket":3,
        "min":47423,
        "rate":0
      }
    ],
    "2020":[
      {
        "bracket":1,
        "min":0,
        "max":37372,
        "rate":1622
      },
      {
        "bracket":2,
        "min":37372,
        "max":48185,
        "rate":-0.15
      },
      {
        "bracket":3,
        "min":48185,
        "rate":0
      }
    ],
    "2021":[
      {
        "bracket":1,
        "min":0,
        "max":37970,
        "rate":1703
      },
      {
        "bracket":2,
        "min":37970,
        "max":49323,
        "rate":-0.15
      },
      {
        "bracket":3,
        "min":49323,
        "rate":0
      }
    ],
    "2022":[
      {
        "bracket":1,
        "min":0,
        "max":38465,
        "rate":1726
      },
      {
        "bracket":2,
        "min":38465,
        "max":49972,
        "rate":-0.15
      },
      {
        "bracket":3,
        "min":49972,
        "rate":0
      }
    ],
    "2023":[
      {
        "bracket":1,
        "min":0,
        "max":40889,
        "rate":1835
      },
      {
        "bracket":2,
        "min":40889,
        "max":53123,
        "rate":-0.15
      },
      {
        "bracket":3,
        "min":53123,
        "rate":0
      }
    ],
    "2024":[
      {
        "bracket":1,
        "min":0,
        "max":44770,
        "rate":2010
      },
      {
        "bracket":2,
        "min":44770,
        "max":58170,
        "rate":-0.15
      },
      {
        "bracket":3,
        "min":58170,
        "rate":0
      }
    ]
  }
}
