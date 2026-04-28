# 删除活动成员
此为 LMS 活动通用接口，用于为活动删减成员。

**注意**：
- 除课堂外的其他活动，人员可选范围为本班级下的学生&旁听生。
- 课堂活动的人员可选范围暂时定为本班级下的学生。后继规划支持插班生（非班级下学生），也可以用这个接口删除。


## URL 

`https://root_url/lms/activity/deleteStudent`


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
| courseId | 是 | integer | 班级（课程）ID |    |
| activityId | 是 | integer | 活动创建完成后返回的活动ID |    |
| studentUids | 是 | array[string] | 学生UID集合	 |     |

## 响应参数
| 参数名 | 类型 | 示例值 | 含义 |
|-----|---- |---- |-----|
| code | integer | 1 | 错误码 |
| msg | string | "程序正常执行" | 错误信息 |
| data | integer | null | 返回信息 |

## 示例

 - HTTP 请求

```http
POST /lms/activity/deleteStudent HTTP/1.1
Host: root_url
X-EEO-SIGN: d8241dd187c9e6ba20d366cfbb3741a2
X-EEO-UID: 409864
X-EEO-TS: 1722938394
Content-Type: application/json
Content-Length: 117

{
    "courseId": 414193,
    "activityId": 25096097,
    "studentUids": [
        504026,
        504028
    ]
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: d8241dd187c9e6ba20d366cfbb3741a2' \
     -H 'X-EEO-UID: 409864' \
     -H 'X-EEO-TS: 1722938394' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 414193, "activityId": 25096097, "studentUids": [504026, 504028]}' \
     'https://root_url/lms/activity/deleteStudent'
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": null
}
```


## 错误码说明

| 错误码 | 说明 |
|:------|:----|
| 147 | 没有此课程信息 |
| 29149 | 活动已删除 |
| 30002 | 活动不存在 |
| 30008 | 活动类型错误（作业，测验不支持） |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 110100069 | 活动已结束 |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |

