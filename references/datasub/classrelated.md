# 课节结束后推送的消息

课节结束后（即课后）推送的消息，包括：课节汇总数据，课节教师和学生评价评分数据，课后生成的录课文件数据，课后上传回放视频完成后的消息，多人多题EDU答题信息，网页回放观看明细，客户端回放观看统计。

由于课节有 20 分钟拖堂时间，上述数据最晚是在课节结束 20 分钟后进行推送。

**注：统计时长位置单位为秒。**
## 课节汇总数据

课节汇总数据会在课节关闭后生成，推送时间将在课节结束 20 分钟后推送，json格式。UID 可以在 [注册用户](../user/register.md) 接口中获得。<br><br>
因客户端和后台增加了提前下课功能，增加了RealCloseTime字段用于判断下课时间，判断逻辑如下：<br>
1）、判断是否有RealCloseTime字段（掉线、异常退出可能会导致没有RealCloseTime字段）<br>
2）、如果没有RealCloseTime字段，以CloseTime为准<br>
3）、有RealCloseTime字段，当RealCloseTime=0时，以CloseTime的时间为准；当RealCloseTime!=0时，比较RealCloseTime和CloseTime的值，以小的为准<br>

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|类型为字符串，'End'|
|Data|对象|包含教室内各类消息汇总|
| └ stageEnd|对象|上下台；统计上下台次数以及台上台下时间，如果进入教室就在台上，整节课都在教室内，并且没有被下台，则上台次数为1，台上时间为在课节时间|
| 　 └ UID|对象|用户UID|
| 　  　 └ DownCount|Int32|下台次数|
| 　  　 └ DownTotal|Int32|台下时间|
| 　  　 └ UpCount|Int32|上台次数|
| 　  　 └ UpTotal|Int32|台上时间|
| └ handsupEnd|对象|举手；统计举手次数和时间。如果举手放下的间隔时间较短，则单次举手时间可能为0|
| 　 └ UID|对象|用户UID|
| 　  　 └ CTime|Int64|举手时间|
| 　  　 └ Total|Int32|举手次数|
| └ inoutEnd|对象|进出教室|
| 　 └ UID|对象|用户UID|
| 　  　 └ Total|Int64|个人在教室时间总和（秒）|
| 　  　 └ Details|对象数组|个人进出教室记录|
| 　  　  　 └ Type|String|进入或退出教室："In"或者"Out"|
| 　  　  　 └ Device|Int32|进入教室设备，只在Type为"In"时有效（定义参考进入教室消息字段）；|
| 　  　  　 └ Time|Int64|进出教室时间|
| 　  　 └ Identity|Int32|用户身份 1：学生，2：旁听，3：老师，4：联席教师，193：机构校长，194：校长助理|
| 　  　 └ Deputies|对象数组|副端进出教室记录，如果有副端进出教室记录，则会推送该字段；如果多个副端，则会存在多个对象|
| 　  　  　  └ ClientID|Int32|多端登录教室时，客户端标识，1,2...
| 　 　 　    └ Total|Int64|个人使用该端在教室时间总和（秒）|
| 　 　 　    └ Details|对象数组|个人进出教室记录|
|　  　 　  　   └ Type|String|进入或退出教室："In"或者"Out"|
| 　  　  　  　 └ Device|Int32|进入教室设备，只在Type为"In"时有效（定义参考进入教室消息字段）；|
| 　  　  　  　 └ Time|Int64|进出教室时间|
| └ awardEnd|对象|奖励|
| 　 └ UID|对象|用户UID|
| 　  　 └ Total|Int32|获得奖励次数|
| └ timerEnd|对象|计时器|
| 　 └ Count|Int32|使用定时器次数|
| 　 └ Timing_Count|Int32|使用计时器次数|
| └ muteEnd|对象|静音，教室内没有静音操作时，无此字段|
| 　 └ Persons|对象|针对个人静音|
| 　  　 └ Total|Int64|个人处于能发言状态的时间总和|
| 　 └ MuteAll|对象|老师使用全体静音|
| 　  　 └ Count|Int32|全体静音次数|
| 　  　 └ Total|Int64|全体静音时间|
| └ smallboardEnd|对象|画板小黑板|
| 　 └ Count|Int32|画板小黑板的使用次数|
| 　 └ Total|Int64|使用画板小黑板的总时长|
| 　 └ Period|数组|每次使用画板小黑板的时间段|
| 　 └ DCount|Int32|每次使用画板小黑板时的分发次数|
| └ textboardEnd|对象|文本小黑板|
| 　 └ Count|Int32|文本小黑板的使用次数|
| 　 └ Total|Int64|使用文本小黑板的总时长|
| 　 └ Period|数组|每次使用文本小黑板的时间段|
| 　 └ DCount|Int32|每次使用文本小黑板时的分发次数|
| └ authorizeEnd|对象|授权|
| 　 └ UID|对象|用户ID|
| 　  　 └ Count|Int32|授权次数|
| 　  　 └ Total|Int64|授权总时长|
| └ diceEnd|对象|骰子|
| 　 └ Count|Int32|使用骰子次数|
| └ answerEnd|对象|答题器|
| 　 └ Count|Int32|使用答题器总次数|
| 　 └ AverageAccuracy|float|平均答题正确率|
| 　 └ Answers|对象数组|每次答题情况|
| 　  　 └ 答题人|对象|答题情况|
| 　  　  　 └ SelectedItem|String|答题者所选答案|
| 　  　  　 └ LastCommitTime|Int64|答题者提交答案时间|
| 　  　  　 └ RecvQuestionTime|Int64|答题者收到答题时间|
| 　  　 └ Participants|对象数组|参与答题者描述|
| 　  　  　 └ Identity|Int32|答题者身份|
| 　  　  　 └ Uid|Int32|答题者ID|
| 　  　  　 └ ShowName|String|答题者昵称|
| 　  　 └ CorrectItems|String|正确答案|
| 　  　 └ Accuracy|float|本题正确率|
| └ screenshareEnd|对象|屏幕共享|
| 　 └ Count|Int32|屏幕共享使用次数|
| 　 └ Total|Int64|屏幕共享总时长|
| 　 └ Period|数组|每次使用屏幕共享时间段|
| └ responderEnd|对象|抢答器|
| 　 └ Count|Int32|抢答器使用次数|
| 　 └ Persons|对象|参与抢答用户|
| 　  　 └ 抢答人|对象|
| 　  　  　 └ Count|Int32|此人参与抢答次数|
| 　  　  　 └ SCount|Int32|此人抢中次数|
| └ kickoutEnd|对象|踢出|
| 　 └ UID|对象数组|被踢出人ID|
| 　  　 └ Duration|Int64|踢出持续时间|
| 　  　 └ Time|Int64|踢出时间|
| └ sharewidgetEnd|对象|课件|
| 　 └ Files|对象数组|每次使用课件详情|
| 　  　 └ StartTime|Int64|课件打开时间|
| 　  　 └ EndTime|Int64|课件关闭时间|
| 　  　 └ FileName|String|课件名|
| 　 └ Count|Int32|使用课件总次数|
| 　 └ Total|Int64|使用课件总时长|
| └ edbEnd|对象|edb课件|
| 　 └ Files|对象数组|每次打开edb详情|
| 　  　 └ FileKey|String|课件索引，本地edb文件打开为"0"|
| 　  　 └ ActionTime|Int32|课件打开时间|
| 　  　 └ FileSource|Int32|课件来源：0，本地；1，云盘|
| 　  　 └ FileName|String|课件名字|
| └ equipmentsEnd|对象|设备信息汇总|
| 　 └ UID|对象|用户ID|
| 　  　 └ Microphone|对象|麦克风信息|
| 　  　  　 └ Total|Int32|麦克风打开时间总计，仅包括在台上时间|
| 　  　  　 └ TotalNotDisabled|Int32|麦克风打开时间总计，包括台上及台下时间|
| 　  　 └ Camera|对象|摄像头信息|
| 　  　  　 └ Total|Int32|摄像头打开时间总计，仅包括在台上时间|
| 　  　  　 └ TotalNotDisabled|Int32|摄像头打开时间总计，包括台上及台下时间|
| └ mdscreenEnd|对象|多向屏幕共享汇总|
| 　 └ Total|Int32|使用总时长|
| 　 └ Count|Int32|使用总次数|
| └ randomselEnd|对象|随机选人汇总|
| 　 └ Count|Int32|使用总次数|
| └ groupEnd|对象|每节课分组详细信息|
| 　 └ Grouping|对象|分组变动信息|
| 　  　 └ Count|Int32|分组次数|
| 　  　 └ Duration|Int64|分组累积时间|
| 　  　 └ Items|对象数组|分组记录|
| 　  　  　 └ Duration|Int64|每次分组时长|
| 　  　  　 └ StartTime|Int32|分组开始时间|
| 　  　  　 └ Groups|对象数组|分组成员|
| 　  　  　  　 └ GroupId|Int32|小组ID|
| 　  　  　  　  　 └ Role|Int32|组内角色,1:组长,0:组员|
| 　  　  　  　  　 └ UID|对象|用户UID|
| └ classsetEnd|对象|每节课教室标志位操作详细信息|
| 　 └ Seat|对象数组|每节课坐席区操作详细信息|
| 　  　 └ Group0|对象|小组ID|
| 　  　  　 └ Count|Int32|坐席区操作次数|
| 　  　  　  　 └ Hidden|Int32|坐席区隐藏次数|
| 　  　  　  　 └ Display|Int32|坐席区显示次数|
| 　  　  　 └ Total|Int32|坐席区状态累积时间|
| 　  　  　  　 └ Hidden|Int32|坐席区隐藏时长|
| 　  　  　  　 └ Display|Int32|坐席区显示时长|
| 　  　  　 └ Details|对象数组|坐席区操作详细记录|
| 　  　  　  　 └ Type|Int32|坐席区操作类型|
| 　  　  　  　 └ Time|Int32|坐席区操作时间|
| └ silenceEnd|对象|聊天框禁言，教室内没有聊天框禁言操作时，无此字段|
| 　 └ Persons|对象|针对个人聊天框禁言|
| 　  　 └ Total|Int64|个人处于能聊天状态的时间总和|
| 　 └ SilenceAll|对象|老师使用全体聊天框禁言|
| 　  　 └ Count|Int32|全体聊天框禁言次数|
| 　  　 └ Total|Int64|全体聊天框禁言时间|
| └ screenchangeEnd|对象|大屏标准屏切换操作|
| 　 └ UID|对象|用户ID|
| 　  　 └ WindowTotal|Int32|标准屏使用时长|
| 　  　 └ FullTotal|Int32|全屏使用时长|
| 　  　 └ WindowCount|Int32|标准屏使用次数|
| 　  　 └ FullCount|Int32|全屏使用次数|
| 　  　 └ Details|数组|切屏操作详细|
| 　  　  　  　 └ Type|Int32|切屏操作类型|
| 　  　  　  　 └ Time|Int32|切屏操作时间|
| └ teachingcameraEnd|对象|教学摄像头操作|
| 　 └ Total|Int32|使用总时长|
| 　 └ Times|Int32|使用总次数|
| 　 └ Details|Int32|使用时长详细|
| 　  　 └ Local|Int32|本地摄像头使用时长|
| 　  　 └ Net|Int32|网络摄像头使用时长|
| 　  　 └ Video|Int32|本地视频使用时长|
| └ videowallEnd|对象|视频墙操作|
| 　 └ Total|Int32|使用总时长|
| 　 └ Times|Int32|使用总次数|












### 实例

```json
{
    "ClassID": 25672,
    "CourseID" : 116576,
    "Cmd" : "End",
    "CloseTime" : 1499718000,
    "StartTime" : 1499653800,
    "SID" : 1000082,
    "Data" : {
        "edbEnd" : {
            "Files" : [ 
                {
                    "FileKey" : "49450405-9650126",
                    "ActionTime" : 1577188373,
                    "FileSource" : 1,
                    "FileName" : "小二 奥数 第5讲 火柴游戏.edb"
                }, 
                {
                    "FileKey" : "49179155-9650126",
                    "ActionTime" : 1577188447,
                    "FileSource" : 1,
                    "FileName" : "小二 奥数 第4讲 锯木头.edb"
                }, 
                {
                    "FileKey" : "49450405-9650126",
                    "ActionTime" : 1577188619,
                    "FileSource" : 1,
                    "FileName" : "小二 奥数 第5讲 火柴游戏.edb"
                }
            ]
        },
        "stageEnd" : {
            "1002646" : {
                "DownCount" : 0,
                "UpTotal" : 965,
                "UpCount" : 1,
                "DownTotal" : 0
            },
            "1002647" : {
                "DownCount" : 1,
                "DownTotal" : 7,
                "UpCount" : 2,
                "UpTotal" : 957
            },
            "1002648" : {
                "DownCount" : 3,
                "DownTotal" : 11,
                "UpCount" : 4,
                "UpTotal" : 816
            }
        },
        "handsupEnd" : {
            "1002647" : {
                "CTime" : 3,
                "Total" : 1
            }
        },
        "awardEnd" : {
            "1002647" : {
                "Total" : 2
            },
            "1002648" : {
                "Total" : 2
            }
        },
        "timerEnd" : {
            "Count" : 3,
            "Timing_Count" : 0
        },
        "muteEnd" : {
            "Persons" : {
                "1002646" : {
                    "Total" : 965
                },
                "1002647" : {
                    "Total" : 957
                },
                "1002648" : {
                    "Total" : 34
                }
            },
            "MuteAll" : {

            }
        },
        "groupEnd" : {
                        "Grouping" : {
                            "Count" : 2,
                            "Items" : [ 
                                {
                                    "Duration" : 6,
                                    "Groups" : [ 
                                        {
                                            "1" : [ 
                                                {
                                                    "Role" : 1,
                                                    "UID" : 1013566
                                                }, 
                                                {
                                                    "Role" : 0,
                                                    "UID" : 1013567
                                                }
                                            ]
                                        }, 
                                        {
                                            "2" : [ 
                                                {
                                                    "Role" : 0,
                                                    "UID" : 1013564
                                                }, 
                                                {
                                                    "Role" : 1,
                                                    "UID" : 1013565
                                                }
                                            ]
                                        }
                                    ],
                                    "StartTime" : 1594868086
                                }, 
                                {
                                    "Duration" : 4,
                                    "Groups" : [ 
                                        {
                                            "1" : [ 
                                                {
                                                    "Role" : 1,
                                                    "UID" : 1013564
                                                }, 
                                                {
                                                    "Role" : 0,
                                                    "UID" : 1013567
                                                }
                                            ]
                                        }, 
                                        {
                                            "2" : [ 
                                                {
                                                    "Role" : 1,
                                                    "UID" : 1013566
                                                }
                                            ]
                                        }, 
                                        {
                                            "3" : [ 
                                                {
                                                    "Role" : 1,
                                                    "UID" : 1013565
                                                }
                                            ]
                                        }
                                    ],
                                    "StartTime" : 1594868093
                                }
                            ],
                            "Duration" : 10
                        }
        },
        "inoutEnd" : {
            "1002646" : {
                "Total" : 965,
                "Details" : [
                    {
                        "Type" : "In",
                        "Device": 0,
                        "Time" : 1499673085
                    },
                    {
                        "Type" : "Out",
                        "Time" : 1499674050
                    }
                ],
                "Identity": 1,
                "Deputies" : [
                    {
                        "clientID":1,
                        "Total":100,
                        "Details":[
                            {
                                "Device":0,
                                "Type":"In",
                                "Time":1689145418
                            },
                            {
                                "Type" :"Out",
                                "Time":1689145544
                            }
                        ]
                    },
                    {
                        "clientID":2,
                        "Total":100,
                        "Details":[
                            {
                                "Device":1,
                                "Type":"In",
                                "Time":1689145418
                            },
                            {
                                "Type" :"Out",
                                "Time":1689145544
                            }
                        ]
                    }
                ]
            },
            "1002647" : {
                "Total" : 964,
                "Details" : [
                    {
                        "Type" : "In",
                        "Device": 0,
                        "Time" : 1499673094
                    },
                    {
                        "Type" : "Out",
                        "Time" : 1499674058
                    }
                ],
                "Identity": 3
            },
            "1002648" : {
                "Total" : 827,
                "Details" : [
                    {
                        "Type" : "In",
                        "Device": 0,
                        "Time" : 1499673196
                    },
                    {
                        "Type" : "Out",
                        "Time" : 1499674023
                    }
                ],
                "Identity": 1
            }
        },
        "smallboardEnd" : {
            "Count" : 1,
            "Total" : 309,
            "Period" : [
                309
            ],
            "DCount" : 4
        },
                "randomselEnd" : {
                    "Count":3
                },
                "mdscreenEnd"  : {
                    "Count" : 1,
                    "Total" : 309
                },
        "textboardEnd" : {
            "Count" : 1,
            "Total" : 218,
            "Period" : [
                218
            ],
            "DCount" : 1
        },
        "authorizeEnd" : {
            "1002646" : {
                "Count" : 0,
                "Total" : 0
            },
            "1002647" : {
                "Count" : 2,
                "Total" : 38
            },
            "1002648" : {
                "Count" : 0,
                "Total" : 0
            }
        },
        "diceEnd" : {
            "Count" : 5
        },
        "answerEnd" : {
            "Count" : 2,
            "AverageAccuracy" : 0.5,
            "Answers" : [
                {
                    "1002647" : {
                        "SelectedItem" : "B",
                        "LastCommitTime" : 1499673922,
                        "RecvQuestionTime" : 1499673916
                    },
                    "Participants" : [
                        {
                            "Identity" : 1,
                            "Uid" : 1002647,
                            "ShowName" : "236...0002"
                        },
                        {
                            "Identity" : 1,
                            "Uid" : 1002648,
                            "ShowName" : "236...0003"
                        }
                    ],
                    "CorrectItems" : "A",
                    "1002648" : {
                        "SelectedItem" : "A",
                        "LastCommitTime" : 1499673920,
                        "RecvQuestionTime" : 1499673915
                    },
                    "Accuracy" : 0.5
                },
                {
                    "1002647" : {
                        "SelectedItem" : "BCE",
                        "LastCommitTime" : 1499673972,
                        "RecvQuestionTime" : 1499673968
                    },
                    "Participants" : [
                        {
                            "Identity" : 1,
                            "Uid" : 1002647,
                            "ShowName" : "236...0002"
                        },
                        {
                            "Identity" : 1,
                            "Uid" : 1002648,
                            "ShowName" : "236...0003"
                        }
                    ],
                    "CorrectItems" : "BCE",
                    "1002648" : {
                        "SelectedItem" : "ABC",
                        "LastCommitTime" : 1499673978,
                        "RecvQuestionTime" : 1499673967
                    },
                    "Accuracy" : 0.5
                }
            ]
        },
        "screenshareEnd" : {
            "Count" : 1,
            "Total" : 31,
            "Period" : [
                31
            ]
        },
        "responderEnd" : {
            "Count" : 2,
            "Persons" : {
                "1002647" : {
                    "Count" : 2,
                    "SCount" : 1
                },
                "1002648" : {
                    "Count" : 2,
                    "SCount" : 1
                }
            }
        },
        "sharewidgetEnd" : {
            "Files" : [
                {
                    "EndTime" : 1502178862,
                    "StartTime" : 1502178812,
                    "FileName" : "animal.wmv"
                }
            ],
            "Count" : 1,
            "Total" : 50
        },
        "kickoutEnd" : {
            "1002648" : [
                {
                    "Duration" : 300,
                    "Time" : 1499674023
                }
            ]
        },
        "equipmentsEnd": {
            "100092": {
                "Microphone": {
                    "Total": 381,
                    "TotalNotDisabled":450
                },
                "Camera": {
                    "Total": 25,
                    "TotalNotDisabled":300
                }
            }
        },
        "classsetEnd" : {
            "Seat" : {
                "Group0" : {
                    "Count" : {
                        "Hidden" : 4, 
                        "Display" : 4
                    }, 
                    "Total" : {
                        "Hidden" : 918,
                        "Display" : 1569
                    }, 
                    "Details" : [
                        {
                            "Type" : 0, 
                            "Time" : 1605602050
                        }, 
                        {
                            "Type" : 1, 
                            "Time" : 1605602567
                        }, 
                        {
                            "Type" : 0, 
                            "Time" : 1605602864
                        }, 
                        {
                            "Type" : 1, 
                            "Time" : 1605603120
                        }, 
                        {
                            "Type" : 0, 
                            "Time" : 1605603397
                        }, 
                        {
                            "Type" : 1, 
                            "Time" : 1605603728
                        }, 
                        {
                            "Type" : 0, 
                            "Time" : 1605603873
                        }, 
                        {
                            "Type" : 1, 
                            "Time" : 1605604338
                        }
                    ]
                }
            }
        },
        "silenceEnd" : {
            "Persons" : {
                "1002646" : {
                                "Total" : 965
                            },
                "1002647" : {
                                "Total" : 957
                            }
                        },
            "SilenceAll" : {
                "Count":0,
                "Total":0
                           }
        },
        "screenchangeEnd" : {
            "102322" : {
                "WindowTotal" : 23,
                "Details" : [ 
                    {
                        "Type" : 0,
                        "Time" : 1610350682
                    }, 
                    {
                        "Type" : 1,
                        "Time" : 1610350705
                    }, 
                    {
                        "Type" : 1,
                        "Time" : 1610350706
                    }
                ],
                "FullTotal" : 724,
                "WindowCount" : 1,
                "FullCount" : 2
            },
            "102020" : {
                "WindowTotal" : 697,
                "Details" : [ 
                    {
                        "Type" : 1,
                        "Time" : 1610350626
                    }, 
                    {
                        "Type" : 0,
                        "Time" : 1610350731
                    }, 
                    {
                        "Type" : 0,
                        "Time" : 1610350733
                    }
                ],
                "FullTotal" : 105,
                "WindowCount" : 2,
                "FullCount" : 1
            }
        },
        "teachingcameraEnd" : {
            "Total" : 9,
            "Details" : {
                "Video" : 0,
                "Net" : 2,
                "Local" : 7
            },
            "Times" : 2
        },
        "videowallEnd" : {
            "Total" : 4,
            "Times" : 1
        }
    }
}

```


## 课节教师和学生评价评分数据

老师或学生退出教室，可以给出自己的课后评价和评分：

1. 每个人做出的评价分别推送：老师对所有学生的评价为一条，每个学生对老师的评价各为一条；

2. 如果用户多次进出教室并作出评价时，此类消息会推送多次，每次为当前的最新评价；



| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|类型为字符串，'Rating'|
|TUID|Int32|老师UID|
| └ Comments|对象|评价内容|
| 　 └ UID|对象|学生UID|
| 　  　 └ Account|String|学生帐号|
| 　  　 └ studentEmail|String|学生邮箱账号|
| 　  　 └ T2S或S2T|对象|如果是老师对学生的评价为T2S，如果是学生对老师的评价为S2T|
| 　  　  　 └ Comment|String|评价内容|
| 　  　  　 └ Score|Int32|评分|




### 实例

#### 老师对学生的评价


```json
{
    "ActionTime" : 1513150417,
    "ClassID" : 4136927,
    "CourseID" : 1232019,
    "Cmd" : "Rating",
    "Comments" : {
        "1044042" : {
            "T2S" : {
                "Comment" : "Good student!",
                "Score" : 5
            },
            "Account" : "23605370012"
        },
        "1044040" : {
            "T2S" : {
                "Comment" : "",
                "Score" : 3
            },
            "Account" : "23605370011"
        }
    },
    "TUID" : 1024920,
    "SID" : 1024920
}
```


#### 学生对老师的评价


```json
{
    "ActionTime" : 1513150527,
    "ClassID" : 4136927,
    "CourseID" : 1232019,
    "Cmd" : "Rating",
    "Comments" : {
        "1044040" : {
            "Account" : "23605370011",
            "S2T" : {
                "Comment" : "Good teacher!",
                "Score" : 4
            }
        }
    },
    "TUID" : 1024920,
    "SID" : 1024920
}
```


## 课后生成的录课文件数据

课节的录课文件可能被分段为多个文件，有录课文件生成时会以如下 `json` 格式通知（实例数据见文末尾）；<br>
**授课期间一旦产生视频文件即实时推送（录课中断即会产生回放），一节课可能会推送多条视频信息。**


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|类型为字符串，'Record'
|VUrl|String|视频文件的链接地址|
|VST|Int64|视频开始时间|
|VET|Int64|视频结束时间|
|Duration|Int64|视频时长|
|FileId|String|文件Id|
|Size|Int64|文件大小|
|CIDExt|String|MP4数据来源 ClassRoom：教室；Camera.3：教师摄像头（现场）|


### 实例


```json

{
    "ClassID": 51345,
    "ActionTime": 1562838399,
    "CourseID": 18041431,
    "SID": 257,
    "TimeStamp": 1562839007,
    "VET": 1501747090,
    "VST": 1501746988,
    "Cmd": "Record",
    "VUrl": "http://1252412222.vod2.myqcloud.com/e0d4af56vodgzp1252412222/6a0543209031868223084052851/f0.mp4",
    "Duration": 12345,
    "FileId": '123',
    "CIDExt": "ClassRoom",
    "Size": 100
    
}


```



## 课后上传回放视频完成后的消息

用户可以通过 eeo.cn 机构管理后台（入口：课程管理 - 课节操作菜单下的“录课视频数据”），手动上传课节回放视频，文件上传完毕会收到此推送消息。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|类型为字符串，'Upload'
|VUrl|String|视频文件的链接地址|
|Duration|Int64|视频时长|
|FileId|String|文件Id|
|Size|Int64|文件大小|


### 实例


```json

{
    "ClassID": 51345,
    "ActionTime": 1562838399,
    "CourseID": 18041431,
    "SID": 257,
    "TimeStamp": 1562839007,
    "Cmd": "Upload",
    "VUrl": "http://1252412222.vod2.myqcloud.com/e0d4af56vodgzp1252412222/6a059031868223084052851/f0.mp4",
    "Duration": 12345,
    "FileId": '123',
    "Size": 100
}


```


## 多人多题EDU答题信息
多人多题的答题统计信息

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|'EduDt'|
|Data|对象|答题内容|
| └ type | 字符串  | QRExam:扫码答题,clientExam:教室答题|
| └ startTime | 整数 | 开始答题时间，单位毫秒|
| └ endTime | 整数 | 结束时间，单位毫秒数|
| └ questionList | 数组 | 题目 |
| 　 └ index | 整数 | 题目序号 |
| 　 └ rightAnswer | 字符串 | 正确答案|
| 　 └ studentAnswers | 数组 | 学生答案 |
| 　  　 └ nickname| 字符串 | 学生昵称 |
| 　  　 └ answer| 字符串 | 学生答案 |　 


### 实例



```json

{
	"SID": 1000082,
	"CID": 380592,
	"Data": {
		"type": "QRExam",
		"startTime": 1573097646000,
		"endTime": 1573097654009,
		"questionList": [{
			"index": 0,
			"rightAnswer": "A,B",
			"studentAnswers": [
			{
			    nickname:'学生1',
			    answer:'A,C'
			},{
			    nickname:'学生2',
			    answer:'A,D'
			}
			]
		}, {
			"index": 1,
			"rightAnswer": "",
			"studentAnswers": []
		}, {
			"index": 2,
			"rightAnswer": "",
			"studentAnswers": []
		}]
	},
	"Cmd": "EduDt"
}

```

## 网页回放观看明细
用户在网页端观看回放的明细数据，推送时机：用户关闭回放后实时推送。<br>
**请注意**：在用户侧的网络不好、刷新页面、手机休眠等情况下，系统会推送多条InTime相同但LookTime不一样的数据。您在处理数据时，应该使用(Cmd,ClassID,Telephone,Intime)为key，只存储LookTime为最大的那条记录即可。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'ReplayDataDetail' | 
|ClassID|整数|课节ID|
|Data|对象|内容|
| └ Telephone | String  | 用户手机号码或邮箱，以实际登录账号为准，若为游客则为'yk_' 开头的字符串 |
| └ Nickname | String  | 用户昵称 |
| └ Intime | 整数 | 用户进入页面观看回放的时间，Unix时间戳 |
| └ LookTime | 整数 | 观看时长，单位为秒 |
| └ IP | String  | 用户IP地址 |
| └ ClientType | 整数 | 用户观看回放的终端类型：1-PC端浏览器，2-移动端浏览器，3-小程序 |

#### 实例
```json
{
    "SID":100088,
    "ClassID":10086,
    "Cmd":"ReplayDataDetail",
    "Data":{
        "Telephone":"15201114553",
        "Nickname":"husky2021",
        "Intime":1625108250,
        "LookTime":60,
        "Ip":"127.0.0.1",
        "ClientType":1
    }
}
```

## 客户端回放观看统计 ！！旧！！
将于8月20日替换为新数据结构，详看  ## 客户端回放观看统计 （新）

用户在ClassIn客户端观看回放的统计数据，推送时机：用户关闭回放后实时推送。<br>

**用户实际观看覆盖时长**：用户观看客户端回放的有效视频时长，计算规则如下
1. 重复观看的部分不计算、拖动进度条的部分不计算，只计算进度条实际播放部分，计算为观看时长。
2. 退出后下次再次观看，已经播放过的部分不再计算覆盖时长，只计算未播放过的部分的时长。
3. 多个视频，观看计算多个视频的总有效时长。  

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'ClientPlaybackDataDetail' |
| ClassID| 整数 | 课节ID |
| Data | 对象 | 内容 |
|  └ UID | 整数  | 用户UID |
|  └ TotalLookCount | 整数  | 客户端观看总次数 |
|  └ TotalLookTime | 整数 | 用户累计观看时长，单位为秒 |
|  └ TotalLookVaildTime | 整数 | 用户实际观看覆盖时长，单位为秒 |
|  └ TopProcess | String  | 用户最高观看进度 单位% |

#### 实例
```json
{
    "SID":100088,
    "ClassID":10086,
    "Cmd":"ClientPlaybackDataDetail",
    "Data":{
        "UID":"1341438",
        "TotalLookCount":6,
        "TotalLookTime":23,
        "TotalLookVaildTime":23,
        "TopProcess":"89%"
    }
}
```


## 客户端回放观看统计 （新）
用户在ClassIn客户端观看回放的统计数据。

**用户实际观看覆盖时长（TotalLookVaildTime）**：用户观看客户端回放的有效视频时长，计算规则如下
1. 重复观看的部分不计算、拖动进度条的部分不计算，只计算进度条实际播放部分，计算为观看时长。
2. 退出后下次再次观看，已经播放过的部分不再计算覆盖时长，只计算未播放过的部分的时长。
3. 多个视频，观看计算多个视频的总有效时长。  

**有效观看次数（ValidWatchCount）**： 观看客户端录课回放视频的有效次数，实际观看视频的覆盖时长达到视频总时长的75%时视为一次有效观看。

**推送时机（TriggerType）**：1 用户打开回放时， 3 用户关闭回放后  4、数据超时的时候（用户长久不观看或者程序非正常退出，超时后）

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'ClientPlaybackDataDetail' |
| ClassID| 整数 | 课节ID |
| Data | 对象 | 内容 |
|  └ UID | 整数  | 用户UID |
|  └ TotalDuration | 整数  | 视频总时长 |
|  └ ValidWatchCount | 整数 | 用户有效观看次数|
|  └ TotalLookVaildTime | 整数 | 用户实际观看覆盖时长，单位为秒 |
|  └ LatestDetails | 对象  |  |
|    └ TriggerType | 整数  | 推送时机 |

#### 实例
```json
{
    "ClassID":1,
    "Data":{
        "UID":1000082,    
        "TotalLookVaildTime":883,
        "TotalDuration":1238,
        "ValidWatchCount":2,
        "LatestDetails":{
            "TriggerType":1
        }
    }
}
```

## 课节聊天消息打包推送
用户在教室内聊天(包括文字,图片)数据,在课节结束后会进行打包,然后将相应下载地址推送给客户。<br>

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | ChatContent |
| ClassID| Int32 | 课节ID |
| SID| Int32 | 机构ID |
| Url| String | 聊天消息下载地址 |
| TimeStamp |Int32| 聊天消息打包时间 |

#### 实例
```json
{
  "TimeStamp": 1649216600, 
  "Cmd": "ChatContent", 
  "ClassID": 163937,
  "SID": 100038,
  "Url": "pgdfile.eeo.cn/classchat/202204/8/71c4d8d054cc44b19d9a6c350047359d.zip"
}
```
