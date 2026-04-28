# 创建在线双师课节

**接口功能：** 支持用户传主课节ID、子课节信息（批量），完成创建子课节并将主子课节进行绑定。

**接口说明：**
- 主课节为标准课程下课节或课堂，参考创建课节或创建课堂
- 主课节和子课节不能在同一个课程下。子课节之间也不能是同一个课程
- 返回每个子课节创建成功与否的信息，信息包含子课节所在课程ID、子课节ID、子课节名称
- 子课节无需传递主讲教师和时间，继承主课节的主讲教师和时间
- 子课节继承其所属课程的云盘资源
- subClassJson最大100，限制单个主课节最多绑定100个子课节
- 单个课程下课节数不能超过限制（包括双师课和非双师课总课节数）。否则会创建失败并报错，错误码121601070。    
- 子课节如果需要设置录课直播回放，需同时传递useCoMainRecord、recordState、recordType、liveState、openState，否则会报参数错误

## URL 

`https://root_url/lms/onlineDoubleTeacher/addClass`


## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

### Header 参数
| key | 必填 | 类型 |说明 | 
| ----| ----|----| ----- | 
| X-EEO-SIGN | 是 |string |签名 生成规则见[这里](../appendix/signature.md)| 
| X-EEO-UID | 是 |string |机构SID |
| X-EEO-TS | 是 |string |时间戳 |


### Body 参数

|  key            |  必填  |  类型  |  说明                                                    |  规则说明                                                  |
| ----------------- | -------- | -------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| mainCourseId      | 是       | integer      | 主课节所属课程ID                                   |                                                              |
| mainClassId       | 是       | integer      | 主课节ID                                                   | 主课节可以是课节或课堂                                       |
| subClassJson      | 是       | array     | 子课节数据                                                 | subClassJson最大100，限制单个主课节最多绑定100个子课节       |
|  └ courseId        | 是       | integer      | 子课节所属课程ID                                           | 每个子课节的课程ID                                           |
|  └ className       | 是       | string   | 子课节名称                                                 | 长度不超过50                                                    |
|  └ assistantUids   | 否       | array     | 联席教师UID列表                                            | 示例：[1000082,1000083]，UID为integer，不传默认无联席教师                |
|  └ cameraHide      | 否       | integer      | 是否隐藏坐席区，0=显示坐席区，1=隐藏坐席区    | 默认为0，不传使用默认值，当cameraHide=1时，isAutoOnstage会始终被设置为1，即不自动上台  |
|  └ isAutoOnstage   | 否       | integer      | 学生进入教室是否自动上台，1=不自动，2=自动                 | 默认为1，不传使用默认值 |
|  └ seatNum         | 否       | integer      | 上台人数，新双师上台人数与V1版本创建课节API有所区别；         | 7=1v6上台，即包含教师头像，例：传1时，表示1v0，台上只显示老师头像，默认为7（1v6），不传使用默认值，如机构最大台上人数配置小于1v6，会默认为机构最大台上人数 |
|  └ isHd            | 否       | integer      | 是否高清，0=非高清，1=高清，2=全高清                                  | 默认为0，不传使用默认值，目前仅支持 1v1和1v6， 即seatNum=2或seatNum=7使用 |
|  └ isDc            | 否       | integer      | 双摄模式，是否开启副摄像头，0=不开启，3=开启全高清副摄像头 | 默认为0，不传使用默认值；仅支持1v1使用，即seatNum=2 |
|  └ useCoMainRecord | 否       | integer      | 是否使用主课录播，1=使用，0=不使用 | useCoMainRecord为1，recordState、recordType、liveState、openState 四个录课相关参数传值只能为0，否则报错 |
|  └ recordState     | 否       | integer      | 是否开启录课 ，0=关闭， 1=开启           | 默认为0，不传使用默认值，若需要网页直播或者网页回放，则必须选择录课，否则无法开启网页直播、网页回放 |
|  └ recordType       | 否       | integer      | 录课类型， 0=录制教室 、1=录制现场、2=两个都录                 | 设置录课时必传 |
|  └ liveState       | 否       | integer      | 是否开启直播， 0=关闭，1=开启           | 默认为0，不传使用默认值，若需要网页直播，则必须开启录课                  |
|  └ openState       | 否       | integer      | 是否公开回放， 0=关闭，1=开启            | 默认为0，不传使用默认值，若需要网页回放，则必须开启录课                  |
|  └ uniqueIdentity  | 否       | string   | 课节唯一标识，若存在则本次创建失败，返回历史课节ID                           | 32位字符，超限报错，机构可传唯一标识，传入此值后，我们会校验机构下是否已存在此唯一标识 |

## 响应参数

| 参数名           | 类型    | 示例值                | 含义         |
| ---------------- | ------- | --------------------- | ------------ |
| code             | integer | 1                     | 错误码       |
| msg              | string  | "程序正常执行"        | 错误信息     |
| data             | object  |                       | 返回信息对象 |
| └ mainClassId    | integer | 4157055               | 主课程ID     |
| └ mainCourseId   | integer | 2337435               | 主课程ID     |
| └ subClassData   | array  | [[{子课节数据}]](#子课节数据) | 子课节数据数组|

### 子课节数据

| 参数名             | 类型    | 示例值                                                       | 含义         |
| ------------------ | ------- | ------------------------------------------------------------ | ------------ |
| classId        | integer | 4157912                                                      | 课节ID       |
| courseId       | integer | 2337436                                                      | 课程ID       |
| className      | string  | "2337436-subClassName"                                       | 课节名称     |
| liveUrl        | string  | "https://www.eeo.cn/live.php?lessonKey=7a32f568ed7b725c"     | 直播回放URL  |
| liveInfo       | object  | {}                                                           | 直播流信息对象|
|  └ FLV         | string  | "https://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1ec9c2d2.flv?txSecret=57bd3671122a2e22a2fe306e8af2a0dd&txTime=7d8d37cd" | FLV直播流地址  |
|  └ HLS         | string  | "https://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1ec9c2d2.m3u8?txSecret=57bd3671122a2e22a2fe306e8af2a0dd&txTime=7d8d37cd" | HLS直播流地址  |
|  └ RTMP        | string  | "rtmp://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1ec9c2d2?txSecret=57bd3671122a2e22a2fe306e8af2a0dd&txTime=7d8d37cd" | RTMP直播流地址 |
| uniqueIdentity | string  | ""                                                           | 唯一标识     |
| code           | integer | 1                                                            | 错误码       |
| msg            | string  | "程序正常执行"                                               | 错误信息     |


## 示例

 - HTTP 请求

```http
POST /lms/onlineDoubleTeacher/addClass HTTP/1.1 
Host: root_url
X-EEO-SIGN: 43a81ec4d7b213d20912826d95ba381a
X-EEO-UID: 2669800
X-EEO-TS: 1732270810
Content-Type: application/json
Content-Length: 539

{
    "mainCourseId": 2337435,
    "mainClassId": 4157055,
    "subClassJson": [
        {
            "courseId": 2337436,
            "className": "2337436-subClassName",
            "seatNum": 7,
            "isHd": 2,
            "isDc": 0,
            "cameraHide": 0,
            "isAutoOnstage": 1,
            "liveState": 1,
            "openState": 1,
            "recordState": 1,
            "recordType": 0,
            "useCoMainRecord": 0
        },
        {
            "courseId": 2337437,
            "className": "2337437-subClassName",
            "assistantUids": [
                1445886
            ],
            "seatNum": 7,
            "isHd": 1,
            "isDc": 0,
            "cameraHide": 0,
            "isAutoOnstage": 1,
            "liveState": 1,
            "openState": 1,
            "recordState": 1,
            "recordType": 1,
            "useCoMainRecord": 1
        }
    ]
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: 43a81ec4d7b213d20912826d95ba381a' \
     -H 'X-EEO-UID: 2669800' \
     -H 'X-EEO-TS: 1732270810' \
     -H 'Content-Type: application/json' \
     -d '{"mainCourseId": 2337435, "mainClassId": 4157055, "subClassJson": [{"courseId": 2337436, "className": "2337436-subClassName", "seatNum": 7, "isHd": 2, "isDc": 0, "cameraHide": 0, "isAutoOnstage": 1, "liveState": 1, "openState": 1, "recordState": 1, "recordType": 0, "useCoMainRecord": 0}, {"courseId": 2337437, "className": "2337437-subClassName", "assistantUids": [1445886], "seatNum": 7, "isHd": 1, "isDc": 0, "cameraHide": 0, "isAutoOnstage": 1, "liveState": 1, "openState": 1, "recordState": 1, "recordType": 1, "useCoMainRecord": 1}]}' \
     'https://root_url/lms/onlineDoubleTeacher/addClass'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": {
        "mainClassId": 4157055,
        "mainCourseId": 2337435,
        "subClassData": [
            {
                "classId": 4157912,
                "courseId": 2337436,
                "className": "2337436-subClassName",
                "liveUrl": "https://www.eeo.cn/live.php?lessonKey=7a32f568ed7b725c",
                "liveInfo": {
                    "FLV": "https://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1ec9c2d2.flv?txSecret=57bd3671122a2e22a2fe306e8af2a0dd&txTime=7d8d37cd",
                    "HLS": "https://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1ec9c2d2.m3u8?txSecret=57bd3671122a2e22a2fe306e8af2a0dd&txTime=7d8d37cd",
                    "RTMP": "rtmp://liveplay.eeo.cn/eeolive/576f5a8ccf87-18329106c1ec9c2d2?txSecret=57bd3671122a2e22a2fe306e8af2a0dd&txTime=7d8d37cd"
                },
                "uniqueIdentity": "",
                "code": 1,
                "msg": "程序正常执行"
            },
            {
                "classId": 4157913,
                "courseId": 2337437,
                "className": "2337437-subClassName",
                "liveUrl": "",
                "liveInfo": {},
                "uniqueIdentity": "",
                "code": 1,
                "msg": "程序正常执行"
            }
        ]
    }
}
```

## 错误码说明

| 错误码     | 说明                                                   |
| ---------- | ------------------------------------------------------------ |
| 104        | 未知错误                                                     |
| 124        | 开课前一分钟内不能更改上课时间                               |
| 136        | 机构下面没有该老师，请在机构下添加该老师                     |
| 140        | 该课节正在上课，不能编辑和删除                               |
| 142        | 该课程下无此单课信息                                         |
| 143        | 没有此单课信息                                               |
| 144        | 机构下无此课程                                               |
| 145        | 该单课已经结束                                               |
| 147        | 没有此课程信息                                               |
| 149        | 该课程已删除                                                 |
| 153        | 该课程已过期                                                 |
| 165        | 单节课不能少于15分钟且不能超过24小时                         |
| 172        | 课程下的学生不能添加为老师                                   |
| 173        | 课程下的旁听不能添加为老师                                   |
| 212        | 该单课已经删除                                               |
| 219        | 老师信息不存在                                               |
| 221        | 客户端修改单课视频点播信息失败                               |
| 222        | 客户端修改单课信息失败                                       |
| 226        | 未录课的课节不能修改直播回放状态                             |
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
| 110100073  | 活动老师和助教不能相同  |
| 121601005  | 不支持设置网页直播                                           |
| 121601006  | 不支持设置录制现场                                           |
| 121601008  | 不支持设置联席教师                                           |
| 121601009  | 不支持设置网页回放                                           |
| 121601010  | 不支持设置录制教室                                           |
| 121601011  | 不支持设置双摄模式                                           |
| 121601012  | 清晰度超出限制                                               |
| 121601014| 录课直播相关参数不匹配          |
| 121601020  | 业务参数错误                                                 |
| 121601022  | 课程不是标准课                                               |
| 121601030  | 超过单次创建最大数量（单次最多创建20节子课）                                         |
| 121601031  | 课节不属于该机构                                             |
| 121601032  | 无权限操作                                                   |
| 121601033  | 课堂处理失败                                                 |
| 121601034  | 非在线双师课节不支持此操作                                   |
| 121601035  | 课节名称长度不能超过50                                       |
| 121601036  | 子课节不允许修改授课老师信息和上课时间                       |
| 121601037  | 主课节不存在                                                 |
| 121601038  | 主课节下最多支持子课节数100                                  |
| 121601070  | 单个课程下课节数量超过限制 |
|122301036| 主课堂和子课堂需分布在不同的班级|
|122301037| 录课直播相关参数不匹配|


