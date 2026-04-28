# 删除在线双师课节

**接口功能：** 此接口仅支持删除在线双师主子课节  

**接口说明：**
- 删除主课节，子课节会同步删除；
- 删除子课节，不影响主课节；

## URL 

`https://root_url/lms/onlineDoubleTeacher/deleteClass`


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

|    key   | 必填 |   类型   |  说明   | 规则说明 |
| -------- | ---- | -------- | ------- | -------------------------- |
| courseId | 是   | integer  |  课程ID | 创建课程完成后返回的课程ID |
| classId  | 是   | integer  |  课节ID | 课节创建完成后返回的课节ID |

## 响应参数

| 参数名 | 类型 | 示例值     | 含义     |
| ---------- | -------- | -------------- | ------------ |
| code       | integer  | 1              | 错误码       |
| msg        | string   | "程序正常执行"  | 错误信息     |
| data       | array    | []             | 返回信息数组 |
| └ classId  | integer  |     4157055    | 课节ID       |
| └ code     | integer  |      1         | 错误码       |
| └ msg      | string   |  "程序正常执行" | 错误信息     |

## 示例

 - HTTP 请求

```http
POST /lms/onlineDoubleTeacher/deleteClass HTTP/1.1 
Host: root_url
X-EEO-SIGN: 1da2b4d3f105538572360ad6ae11db97
X-EEO-UID: 2669800
X-EEO-TS: 1732505390
Content-Type: application/json
Content-Length: 41

{
    "courseId": 2337435,
    "classId": 4157055
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: 1da2b4d3f105538572360ad6ae11db97' \
     -H 'X-EEO-UID: 2669800' \
     -H 'X-EEO-TS: 1732505390' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 2337435, "classId": 4157055}' \
     'https://root_url/lms/onlineDoubleTeacher/deleteClass'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": [
        {
            "classId": 4157912,
            "code": 1,
            "msg": "程序正常执行"
        },
        {
            "classId": 4157913,
            "code": 1,
            "msg": "程序正常执行"
        },
        {
            "classId": 4157055,
            "code": 1,
            "msg": "程序正常执行"
        }
    ]
}
```

## 错误码说明

| 错误码 | 说明                       |
| ---------- | ------------------------------ |
| 104        | 未知错误                       |
| 142        | 该课程下无此单课信息           |
| 143        | 没有此单课信息                 |
| 144        | 机构下无此课程                 |
| 147        | 没有此课程信息                 |
| 149        | 该课程已经删除                 |
| 101002005  | 签名异常                       |
| 101002006  | 时间戳过期                     |
| 101002008  | 时间戳不存在                   |
| 121601016  | 删除超过最大数量限制           |
| 121601020  | 业务参数错误                   |
| 121601022  | 课程不是标准课                 |
| 121601031  | 课节不属于该机构               |
| 121601032  | 无权限操作                     |
| 121601034  | 非在线双师课节不支持此操作     |
| 121601042  | 已结束、已删除课节不支持此操作 |
    
