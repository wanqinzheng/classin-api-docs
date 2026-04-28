# 编辑在线双师课节

**接口功能：** 修改在线双师主子课节的主讲教师、助教、时间等信息  

**接口说明：**
- 此接口仅支持修改在线双师主子课节
- 主课节修改主讲教师、时间时会同步修改子课节
- 子课节不允许修改主讲教师、时间
- 此接口支持仅传递需修改的参数，可传一个或多个；全都不传，报【参数不全】错误
- 子课节如果需要修改录课直播回放，需同时传递useCoMainRecord、recordState、recordType、liveState、openState，否则会报参数错误

## URL 

`https://root_url/lms/onlineDoubleTeacher/editClass`


## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

### Header 参数
|   key      | 必填| 类型  |  说明 | 
| ---------- | ----|-------| ----- | 
| X-EEO-SIGN | 是  |string |签名 生成规则见[这里](../appendix/signature.md)| 
| X-EEO-UID  | 是  |string |机构SID|
| X-EEO-TS   | 是  |string |时间戳 |


### Body 参数
|   key           |   必填   |   类型   |   说明                                                     |   规则说明                                                 |
| --------------- | -------- | -------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| courseId        | 是       | integer      | 课程ID                                                     | 创建课程完成后返回的课程ID（courseId）                       |
| classId         | 是       | integer      | 课节ID                                                     | 课节创建完成后返回的课节ID（classId）                        |
| className       | 否       | string   | 子课节名称                                                 | 长度不超过50字符                                             |
| teacherUid      | 否       | integer      | 主讲教师UID（仅主课节）                                    | 仅主课节支持该参数，如需调整子课联席教师请使用assistantUids  |
| startTime       | 否       | integer      | 课节开始时间（仅主课节）                                   | 1. Unix Epoch 时间戳（秒单位）；<br />2. 仅主课节支持修改，子课节不支持单独调整，主课修改时会同步调整子课开课时间<br />3. 可选择未来2年内的时间； |
| endTime         | 否       | integer      | 课节结束时间（仅主课节）                                   | 1. Unix Epoch 时间戳（秒单位）；<br />2. 仅主课节支持修改，子课节不支持单独调整，主课修改时会同步调整子课结束时间 |
| assistantUids   | 否       | array     | 联席教师UID列表                                            | 不传不修改；示例：[1000082,1000083]，UID为integer，不传默认无联席教师 |
| cameraHide      | 否       | integer      | 是否隐藏坐席区，0=显示坐席区，1=隐藏坐席区                 | 不传不修改；当cameraHide=1时，isAutoOnstage会始终被设置为1，即不自动上台   |
| isAutoOnstage   | 否       | integer      | 学生进入教室是否自动上台，1=不自动，2=自动                 | 不传不修改                                                   |
| seatNum         | 否       | integer      | 上台人数                                                   | 1. 不传不修改；<br />2. 新双师上台人数与V1版本创建课节API有所区别；此时7=1v6上台；例：传1时，表示1v0，台上只显示老师头像；<br />3. 传递的台上人数大于配置的最大台上人数，则会被重置为最大台上人数 |
| isHd            | 否       | integer      | 是否高清，0=非高清，1=高清，2=全高清                       | 不传不修改；目前仅支持 1v1和1v6， 即seatNum=2或seatNum=7使用 |
| isDc            | 否       | integer      | 双摄模式，是否开启副摄像头，0=不开启，3=开启全高清副摄像头 | 不传不修改；仅支持1v1使用，即seatNum=2                       |
| useCoMainRecord | 否       | integer      | 使用主课节的录课回放；1=使用，0=不使用（仅支持子课使用）   | useCoMainRecord为1，recordState、recordType、liveState、openState 四个录课参数传值只能为0，否则报错 |
| recordType      | 否       | integer      | 录课类型， 0=录制教室 、1=录制现场、2=两个都录                 | 不传不修改；如需修改需要同时传递录课、直播、回放信息，否则不生效；子课修改还需传递useCoMainRecord |
| recordState     | 否       | integer      | 是否开启录课 ，0=关闭， 1=开启                             | 不传不修改； 若需要网页直播或者网页回放，则必须选择录课，否则无法开启网页直播、网页回放 |
| liveState       | 否       | integer      | 是否开启直播， 0=关闭，1=开启                              | 不传不修改；若需要网页直播，则必须开启录课                   |
| openState     | 否       | integer      | 是否公开回放， 0=关闭，1=开启                              | 不传不修改；若需要网页回放，则必须开启录课                   |

## 响应参数

|   参数名   |   类型   |   示例值       |   含义       |
| ---------- | -------- | -------------- | ------------ |
| code       | integer  | 1              | 错误码       |
| msg        | string   | "程序正常执行"  | 错误信息     |
| data       | array    | [课节数据](#课节数据) | 返回信息数组 |

### 课节数据

| 参数名             | 类型    | 示例值                                                       | 含义         |
| ------------------ | ------- | ------------------------------------------------------------ | ------------ |
| isMainClass    | integer | 1                                                                | 是否为主课，1=是，0=否 |
| classId        | integer | 4157912                                                          | 课节ID       |
| liveUrl        | string  | "https://www.eeo.cn/live.php?lessonKey=7a32f568ed7b725c"         | 直播回放URL  |
| liveInfo       | object  |                               {}                                 | 直播流信息对象|
|  └ FLV         | string  | "https://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1ec9c2d2.flv?txSecret=57bd3671122a2e22a2fe306e8af2a0dd&txTime=7d8d37cd" | FLV直播流地址  |
|  └ HLS         | string  | "https://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1ec9c2d2.m3u8?txSecret=57bd3671122a2e22a2fe306e8af2a0dd&txTime=7d8d37cd" | HLS直播流地址  |
|  └ RTMP        | string  | "rtmp://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1ec9c2d2?txSecret=57bd3671122a2e22a2fe306e8af2a0dd&txTime=7d8d37cd" | RTMP直播流地址 |
| code           | integer | 1                                                                | 错误码       |
| msg            | string  | "程序正常执行"                                                    | 错误信息     |
## 示例

 - HTTP 请求

```http
POST /lms/onlineDoubleTeacher/editClass HTTP/1.1 
Host: root_url
X-EEO-SIGN: 284dab41f025cd7ecd2920575defb189
X-EEO-UID: 2669800
X-EEO-TS: 1732271416
Content-Type: application/json
Content-Length: 357

{
    "courseId": 2337435,
    "classId": 4157055,
    "className": "编辑主课名称+时间",
    "startTime": 1732935660,
    "endTime": 1732950000,
    "teacherUid": 2669800,
    "assistantUids": [
        1340566
    ],
    "seatNum": 8,
    "isHd": 0,
    "cameraHide": 0,
    "isAutoOnstage": 1,
    "liveState": 1,
    "openState": 1,
    "recordState": 1,
    "recordType": 1
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: 284dab41f025cd7ecd2920575defb189' \
     -H 'X-EEO-UID: 2669800' \
     -H 'X-EEO-TS: 1732271416' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 2337435, "classId": 4157055, "className": "编辑主课名称+时间", "startTime": 1732935660, "endTime": 1732950000, "teacherUid": 2669800, "assistantUids": [1340566], "seatNum": 8, "isHd": 0, "cameraHide": 0, "isAutoOnstage": 1, "liveState": 1, "openState": 1, "recordState": 1, "recordType": 1}' \
     'https://root_url/lms/onlineDoubleTeacher/editClass'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": [
        {
            "isMainClass": 1,
            "classId": 4157055,
            "liveUrl": "https://www.eeo.cn/live.php?lessonKey=84b978349296b821",
            "liveInfo": {
                "FLV": "https://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1f9d918c.flv?txSecret=4cb4e8a5aae291d6df409e97fd6dae8c&txTime=7d8d37cd",
                "HLS": "https://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1f9d918c.m3u8?txSecret=4cb4e8a5aae291d6df409e97fd6dae8c&txTime=7d8d37cd",
                "RTMP": "rtmp://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1f9d918c?txSecret=4cb4e8a5aae291d6df409e97fd6dae8c&txTime=7d8d37cd"
            },
            "code": 1,
            "msg": "程序正常执行"
        },
        {
            "isMainClass": 0,
            "classId": 4157912,
            "liveUrl": "",
            "liveInfo": {},
            "code": 1,
            "msg": "程序正常执行"
        },
        {
            "isMainClass": 0,
            "classId": 4157913,
            "liveUrl": "",
            "liveInfo": {},
            "code": 1,
            "msg": "程序正常执行"
        }
    ]
}
```

## 错误码说明

| 错误码|说明 |
|:------|:----|
| 104        | 未知错误                                                     |
| 124        | 开课前一分钟内不能更改上课时间                               |
| 136        | 机构下面没有该老师，请在机构下添加该老师                     |
| 140        | 该课节正在上课，不能编辑和删除                               |
| 142        | 该课程下无此单课信息                                         |
| 143        | 没有此单课信息                                               |
| 144        | 机构下无此课程                                               |
| 145        | 该单课已经结束                                               |
| 147        | 没有此课程信息                                               |
| 153        | 该课程已过期                                                 |
| 165        | 单节课不能少于15分钟且不能超过24小时                         |
| 172        | 课程下的学生不能添加为老师                                   |
| 173        | 课程下的旁听不能添加为老师                                   |
| 212        | 该单课已经删除                                               |
| 219        | 老师信息不存在                                               |
| 221        | 客户端修改单课视频点播信息失败                               |
| 222        | 客户端修改单课信息失败                                       |
| 226        | 未录课的课节不能修改直播回放状态                             |
| 268        | 课节开始时间超出允许范围                                     |
| 269        | 课节信息有误，请删除后重新创建                               |
| 318        | 联席教师不是本机构老师                                       |
| 319        | 课程下的学生不能添加为联席教师                               |
| 320        | 课程下的旁听不能添加为联席教师                               |
| 322        | 课节老师不能添加为联席教师                                   |
| 324        | 联席教师节老师加入教师列表失败                               |
| 325        | 插班生不能添加为老师                                         |
| 326        | 联席教师加入教师列表失败                                     |
| 328        | 联席教师不能添加为老师                                       |
| 350        | 开课前20分钟内不能修改课节名称、上课时间、云盘资源、台上人数等 |
| 368        | 当前学生上台数不支持高清                                     |
| 385        | 已过课节结束时间，不能修改授课教师或联席教师                 |
| 387        | 老师已被停用                                                 |
| 388        | 联席教师已被停用                                             |
| 450        | 数量超出限制                                                 |
| 451        | 课节直播封面和介绍添加失败                                   |
| 454        | 课节起止时间与系统维护时间有重叠                             |
| 767        | 当前版本课节结束时间不允许超过服务期限                       |
| 769        | 教师版或教师试用版，班主任不是本人                           |
| 800        | 老师被停用中                                                 |
| 804        | 联席教师被停用中                                             |
| 808        | 该设置不支持双摄                                             |
| 863        | 课节时长不合规定                                             |
| 875        | 开课前5分钟内不能修改课节名称、上课时间、云盘资源、台上人数、教室模式等 |
| 884        | 老师账号已注销                                               |
| 885        | 联席教师账号已注销                                           |
| 21304      | 非中小学不支持设置学科                                       |
| 21305      | 学科不存在                                                   |
| 21317      | 联席教师数量超出限制                                         |
| 21319      | 老师已删除                                                   |
| 101002005  | 签名异常                                                     |
| 101002006  | 时间戳过期                                                   |
| 101002008  | 时间戳不存在                                                 |
| 121601005  | 不支持设置网页直播                                           |
| 121601006  | 不支持设置录制现场                                           |
| 121601008  | 不支持设置联席教师                                           |
| 121601009  | 不支持设置网页回放                                           |
| 121601010  | 不支持设置录制教室                                           |
| 121601012  | 清晰度超出限制                                               |
| 121601020  | 业务参数错误                                                 |
| 121601021  | 课程不属于当前机构下                                         |
| 121601022  | 课程不是标准课                                               |
| 121601031  | 课节不属于该机构                                             |
| 121601033  | 课节处理失败                                                 |
| 121601034  | 非在线双师课节不支持此操作                                   |
| 121601035  | 课节名称长度不能超过50                                       |
| 121601036  | 子课节不允许修改授课老师信息和上课时间                       |
| 122301037  | 录课直播相关参数不匹配                                       |
| 121601042  | 已结束、已删除课节不支持此操作                               |
| 121601044  | 非本机构老师                                                 |
    
