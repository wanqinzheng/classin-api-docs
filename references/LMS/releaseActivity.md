# 发布活动
此为 LMS 活动通用接口，可用于发布任一类型的活动。

**注意**：
- 各类型活动（课堂、作业、测验、答题卡、打卡、讨论等）均支持通过此接口发布。
- 仅支持从草稿变成发布，不支持反向操作。

## URL 

`https://root_url/lms/activity/release`


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
| courseId | 是 |integer | 班级（课程）ID |   |
| activityIds | 是 |array[integer] |活动ID集合 |    |

## 响应参数
| 参数名 | 类型 | 示例值 | 含义
|-----|---- |---- |-----| 
|code| integer | 1| 错误码 |
|msg| string | "程序正常执行"| 错误信息 |
| data | array | [] | 返回信息数组
|　└  | object |  | 返回信息对象
|　　└ activityId | integer | 25096096 | 活动ID
|　　└ name | string | "api发布活动" | 活动名称



## 示例

 - HTTP 请求

```http
POST /lms/activity/release HTTP/1.1
Host: root_url
X-EEO-SIGN: fe19eb3a5b721c7b66194e4a29ee8ead
X-EEO-UID: 409864
X-EEO-TS: 1722938255
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
     -H 'X-EEO-SIGN: fe19eb3a5b721c7b66194e4a29ee8ead' \
     -H 'X-EEO-UID: 409864' \
     -H 'X-EEO-TS: 1722938255' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 414193, "activityId": 25096096}' \
     'https://root_url/lms/activity/release'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": {
        "activityId": 25096096,
        "name": "api发布活动"
    }
}
```


## 错误码说明

| 错误码 | 说明 |
|:------|:----|
| 147 | 没有此课程信息 |
| 29149 | 活动已删除 |
| 29184 | 活动已发布 |
| 30002 | 活动不存在 |
| 101001001 | 参数错误 |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 110100065 | 活动解锁条件存在草稿 |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |

