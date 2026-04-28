#  排课信息同步消息（限免）

本类消息提供了班级和课堂信息的变动情况，包括班级信息变动（增删改），课堂信息变动（增删改），以及班级学生变动和课堂活动学生变动消息。

## 班级信息改动

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'eeoCourseInfoChange' |
|opType|整数|操作类型 1:增加， 3:修改|
|opTime|整数|操作时间|
|UID|整数|操作人UID|
|CourseId|整数|课程id（班级ID）|
|opSource|整数|操作来源 3后台、客户端和机构LMS类API，6:机构v1类API|
|opData|对象|非新增时，只包含被编辑信息|
| 　 └ courseId | 整数  | 课程id |
| 　 └ courseName | String  | 课程名称 |
| 　 └ expiryTime | 整数 | 课程过期时间戳，0：为永久有效 |
| 　 └ courseType | 整数  | 课程类型，1=标准课、2=公开课、3=双师课(旧) |
| 　 └ courseStatus | 整数  | 课程状态，1=还没开课、2=开课中、3=已结课、4=已删除 |
| 　 └ category | String  | 组织架构名称（限中小学后台） |
| 　 └ categoryId | 整数  | 组织架构ID（限中小学后台） |
| 　 └ subjectId | 整数  | 课程学科（限中小学后台），0:空; 1:语文; 2:数学; 3:英语; 4:物理; 5:化学; 6:生物; 7:政治; 8:历史; 9:地理; 10:思想品德; 11:音乐; 12:体育; 13:美术; 14:通用技术; 15:信息技术; 16:科学; 99:其他学科  |
| 　 └ mainTeacherInfo | 对象  | 班主任信息 |
| 　 　  └ teacherName | String  | 老师姓名 |
| 　 　  └ teacherUid | 整数  | 老师账号uid |
| 　 　  └ teacherNo | String  | 老师工号（限中小学后台） |
| 　 └ labelInfos | 数组  | 标签信息 |
| 　  　  　 └ labelName | string  | 标签名称 |
| 　  　  　 └ labelId | 整数  | 标签ID |



#### 实例
```json
{
    "opType":1,
    "opTime":1686728238,
    "UID":123456,
    "CourseId":24071593,
    "TimeStamp":1686728838,
    "SafeKey":"b80e0d659c32fd1a46dbe7e50b10b5fe",
    "Cmd":"eeoCourseInfoChange",
    "opData":{
        "category":"小学",
        "courseType":1,
        "courseName":"语文课程1",
        "expiryTime":0,
        "subjectId":1,
        "courseId":24071593,
        "courseStatus":1,
        "categoryId":32385
    },
    "SID":3534928,
    "ActionTime":1686728238,
    "_id":"64896e2ea9f6c04afffb1027",
    "opSource":1,
    "uuid":"4a5f150c-0a86-11ee-8613-2a5156a9cd6f"
}
```

## 课节信息改动

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'eeoClassInfoChange' |
|ClassID|整数|课节id|
|CourseId|整数|课程id|
|opType|整数|操作类型 1:增加，2:删除，3:修改|
|opTime|整数|操作时间|
|UID|整数|操作人UID|
|opSource|整数|操作来源 3后台、客户端和机构LMS类API，6:机构v1类API|
|opData|对象|非新增时，只包含被编辑信息|
| 　 └ seatNum | 整数  | 上台人数，默认加1，例如seatNum=9，即1V8上台 |
| 　 └ isAutoOnstage | 整数 | 是否自动上台，0=自动，1=不自动 |
| 　 └ courseId | 整数  | 课程id |
| 　 └ classType | 整数 | 课节类型，1=标准课 2=公开课 3=双师课（旧双师主子课节） 9=新双师子课节 |
| 　 └ className | String  | 课节名称 |
| 　 └ courseName | String  | 课程名称 |
| 　 └ beginTime | 整数  | 课节开始时间戳 |
| 　 └ endTime | 整数  | 课节结束时间戳 |
| 　 └ classId | 整数  | 课节id |
| 　 └ classStatus | 整数  | 课节状态，1=还没开课 2=上课中 3=上课结束 4=已删除 |
| 　 └ MainClassId | 整数| 主课节ID，子课节新建的时候会传主课节ID，其他课节新建的时候传0，编辑、删除的时候不传|  
| 　 └ teacherInfo | 对象  | 授课教师信息 |
| 　 　 └ teacherName | String  | 老师姓名 |
| 　 　 └ teacherUid | 整数  | 老师账号uid |
| 　 　 └ teacherNo | String  | 老师工号（限中小学后台） |
| 　 └ assistantTeacherInfos | 数组  | 联席教师列表 |
| 　 　 └ teacherName | String  | 联席教师姓名 |
| 　 　 └ teacherUid | 整数  | 联席教师账号uid |
| 　 　 └ teacherNo | String  | 联席教师工号（限中小学后台） |
| 　 └ labelInfos | 数组  | 标签信息 |
| 　  　  　 └ labelName | string  | 标签名称 |
| 　  　  　 └ labelId | 整数  | 标签ID |


#### 实例
```json
{
    "ClassID":662391,
    "opType":1,
    "opTime":1686728940,
    "UID":15438,
    "CourseId":2407813,
    "TimeStamp":1686729540,
    "SafeKey":"1746ea56525ca2e60ca1c6c7a74736ee",
    "Cmd":"eeoClassInfoChange",
    "CourseID":2407813,
    "opData":{
        "classId":662391,
        "teacherInfo":{
            "teacherName":"2222",
            "teacherUid":5190814,
            "teacherNo":""
        },
        "seatNum":9,
        "isAutoOnstage":1,
        "courseId":2407813,
        "classType":1,
        "className":"语文课-1",
        "courseName":"语文课程1",
        "classStatus":1,
        "labelInfos":[
            {
                "labelId":304777,
                "labelName":"语文课"
            }
        ],
        "assistantTeacherInfos":[
            {
                "teacherName":"1111",
                "teacherUid":6214610,
                "teacherNo":""
            },
            {
                "teacherName":"王-eeo",
                "teacherUid":3348238,
                "teacherNo":""
            }
        ],
        "endTime":1686731820,
        "beginTime":1686729420
    },
    "SID":353928,
    "ActionTime":1686728940,
    "_id":"648970eca9f6c04afffb1032",
    "opSource":1,
    "uuid":"a7aac6b1-eaf4-3393-3a3d-0c7960e72ac9"
}
```

## 课程学生信息改动

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'eeoCourseStudentChange' |
|CourseId|整数|课程id|
|opType|整数|操作类型 1:增加，2:删除，3:修改|
|opTime|整数|操作时间戳|
|UID|整数|操作人UID|
|opSource|整数|操作来源 |opSource|整数|操作来源 3后台、客户端和机构LMS类API，6:机构v1类API|
|opData|对象|非新增时，只包含被编辑信息|
| 　 └ courseId | 整数  | 课程id |
| 　 └ studentInfos | 数组  | 学生信息 |
| 　  　 └ studentNo | string  | 学生学号（限中小学后台） |
| 　  　 └ studentName | string  | 学生姓名 |
| 　  　 └ studentUid | 整数  | 学生账号uid |
| 　  　 └ labelInfos | 数组  | 学生标签信息 |
| 　  　  　 └ labelName | string  | 标签名称 |
| 　  　  　 └ labelId | 整数  | 标签ID |



#### 实例
```json
{
    "opType":1,
    "opTime":1685344787,
    "UID":114930,
    "CourseId":244489,
    "TimeStamp":1685345429,
    "SafeKey":"8f1784f884be325b8d7baabb35980fcd",
    "Cmd":"eeoCourseStudentChange",
    "opData":
        {
            "courseId":244489,
            "studentInfos":[
                {
                    "studentNo":"",
                    "studentName":"121****0079",
                    "studentUid":280620,
                    "labelInfos":[
                        {
                            "labelName":"批量添加_2",
                            "labelId":23161
                        },
                        {
                            "labelName":"批量添加_4",
                            "labelId":23163
                        },
                        {
                            "labelName":"批量添加_1",
                            "labelId":23165
                        },
                        {
                            "labelName":"批量添加_3",
                            "labelId":23167
                        }
                    ]
                }
            ],
            "courseName":"api创建班级_订阅消息"
        },
    "SID":114930,
    "ActionTime":1685344787,
    "_id":"6474523d8a7f760cde589922",
    "opSource":4,
    "uuid":"4344133e-5d82-700b-2ead-98c92c0f00ae"
}
```

## 课节学生信息改动

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'eeoClassStudentChange' |
|ClassID|整数|课节id|
|CourseId|整数|课程id|
|opType|整数|操作类型 1:增加，2:删除，3:修改|
|opTime|整数|操作时间戳|
|UID|整数|操作人UID|
|opSource|整数|操作来源 3后台、客户端和机构LMS类API，6:机构v1类API|
|opData|对象|非新增时，只包含被编辑信息|
| 　 └ courseId | 整数  | 课程id |
| 　 └ classId | 整数  | 课节id |
| 　 └ className | string  | 课节名称 |
| 　 └ studentInfos | 数组  |  |
| 　  　 └ studentNo | string  | 学生学号（限中小学后台） |
| 　  　 └ studentName | string  | 学生姓名 |
| 　  　 └ studentUid | 整数  | 学生账号uid |
| 　  　 └ labelInfos | 对象  |  |
| 　  　 　  └ labelName | string  | 标签名称 |
| 　  　 　  └ labelId | 整数  | 标签ID |



#### 实例
```json
{
    "ClassID":3864179,
    "opType":1,
    "opTime":1685345060,
    "UID":1149130,
    "CourseId":2444189,
    "TimeStamp":1685345660,
    "SafeKey":"7d549f7cc66bbb44d6a32a6c26af13c7",
    "Cmd":"eeoClassStudentChange",
    "CourseID":2414489,
    "opData":
        {
            "courseId":2441489,
            "classId":3861479,
            "className":"api课节_11",
            "studentInfos":[
                {
                    "studentNo":"",
                    "studentName":"12112190004",
                    "studentUid":1211350,
                    "labelInfos":[
                        {
                            "labelName":"批量添加_1",
                            "labelId":231165
                        },
                        {
                            "labelName":"批量添加_3",
                            "labelId":231167
                        }
                    ]
                },
                {
                    "studentNo":"",
                    "studentName":"test_yk123",
                    "studentUid":19048,
                    "labelInfos":[
                        {
                            "labelName":"批量添加_1",
                            "labelId":2365
                        },
                        {
                            "labelName":"批量添加_3",
                            "labelId":2367
                        }
                    ]
                }
            ]
        },
    "SID":11930,
    "ActionTime":1685345060,
    "_id":"647453248a7f760cde589926",
    "opSource":4,
    "uuid":"8f4423b7-fb8f-eaa5-5844-31ff8fcc9ac0"
}

```