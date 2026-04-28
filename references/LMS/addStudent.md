# 添加活动成员
此为 LMS 活动通用接口，用于为活动添加成员。 

**注意**  
- 活动创建时候默认是包含所有班级成员，无须调用添加成员接口。
- 作业测验活动暂不支持调用此接口。
- 除课堂外的其他活动，人员可选范围为本班级下的学生&旁听生。
- 课堂活动的人员可选范围包括机构下所有学生，如果学生不在班级下则作为插班生加入课堂。但学生必须在机构下。
- 添加活动成员，每个成员有单独的返回码，返回码在data里。
- 如果成员已存在活动中，不会返回错误码，会返回1，正常执行

## URL 

`https://root_url/lms/activity/addStudent`


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
| courseId | 是 | integer | 班级（课程）ID |  |
| activityId | 是 | integer | 活动创建完成后返回的活动ID |  |
| studentUids | 是 | array[string] | 学生UID数组|   |


## 响应参数

| 参数名 | 类型 | 示例值 | 含义 |
|-----|---- |---- |-----|
| code | integer | 1 | 错误码 |
| msg | string | "程序正常执行" | 错误信息 |
| data | array[integer] | null | 返回信息 |
| └ studentUid | integer |  | 返回信息 |
| └ code | integer | 1 | 返回信息 |
| └ msg | string | "程序正常执行" | 返回信息 |


## 示例

 - HTTP 请求

```http
POST /lms/activity/addStudent HTTP/1.1
Host: root_url
X-EEO-SIGN: ceb7a2c0534999960c02c191d409c41e
X-EEO-UID: 409864
X-EEO-TS: 1722938382
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
     -H 'X-EEO-SIGN: ceb7a2c0534999960c02c191d409c41e' \
     -H 'X-EEO-UID: 409864' \
     -H 'X-EEO-TS: 1722938382' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 414193, "activityId": 25096097, "studentUids": [504026, 504028]}' \
     'https://root_url/lms/activity/addStudent'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
	"code": 1,
	"msg": "程序正常执行",
	"data": [
    {
		"studentUid": 504026,
		"code": 40030,
		"msg": "学生没在班级中"
	}, 
    {
		"studentUid": 504028,
		"code": 1,
		"msg": "程序正常执行"
	}
    ]
}
```


## 错误码说明


| 错误码 | 说明 |
|:------|:----|
| 147 | 没有此课程信息 |
| 29149 | 活动已删除 |
| 30002 | 活动不存在 |
| 40030 | 学生没在班级中（课堂除外） |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 110100069 | 活动已结束 |
| 110100070 | 活动类型错误（作业，测验不支持） |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |
