# 删除活动
此为 LMS 活动通用接口，可用于删除任一类型的活动。

**注意**：
- 各类型活动（课堂、作业、测验、答题卡、打卡、讨论等）均支持通过此接口删除。

## URL 

`https://root_url/lms/activity/delete`


## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

### Header 参数
| key | 必填 | 类型 |说明 | 
| ----| ----|----| ----- | 
| X-EEO-SIGN | 是 |string |签名 规则见[这里](../appendix/signature.md)| 
| X-EEO-UID | 是 |string |机构SID |
| X-EEO-TS | 是 |string |时间戳 |


### Body 参数

| key | 必填 | 类型 |说明 | 规则说明 |
| ----| ----|----| ----- | -----|
| courseId | 是 | integer | 班级（课程）ID | | 
| activityId | 是 | integer | 活动创建完成后返回的活动ID | 目前仅支持删除单个活动，不支持传多个ID值 |


## 响应参数
| 参数名 | 类型 | 示例值 | 含义
|-----|---- |---- |-----| 
|code| integer | 1| 错误码 |
|msg| string | "程序正常执行"| 错误信息 |
| data | array | [] | 返回信息数组
|　└  | object |  | 返回信息对象
|　　└ activityId | integer | 25096096 | 活动ID
|　　└ name | string | "api删除活动" | 活动名称


## 示例

 - HTTP 请求

```http
POST /lms/activity/delete HTTP/1.1
Host: root_url
X-EEO-SIGN: 8b2db2eb7bd300f833621a577f38e0b3
X-EEO-UID: 409864
X-EEO-TS: 1722938275
Content-Type: application/json
Content-Length: 84

{
    "courseId": 414193,
    "activityId": 25096096
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: 8b2db2eb7bd300f833621a577f38e0b3' \
     -H 'X-EEO-UID: 409864' \
     -H 'X-EEO-TS: 1722938275' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 414193, "activityId": 25096096}' \
     'https://root_url/lms/activity/delete'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": {
        "activityId": 25096096,
        "name": "api删除活动"
    }
}
```


## 错误码说明

| 错误码 | 说明 |
|:------|:----|
| 147 | 没有此课程信息 |
| 29149 | 活动已删除 |
| 30002 | 活动不存在 |
| 40005 | 课堂活动进行中不可删除 |
| 40006 | 课堂活动已结束，不可删除 |
| 101001001 | 参数错误 |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |

