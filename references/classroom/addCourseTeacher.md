# 添加课程教师（API v2）

这个接口使用API v2 调用方式，用于为班级添加教师。
请查阅[这里](../appendix/APIv2Intro.md) 获取关于API v2 的调用说明。 



## URL 

`https://root_url/course/addCourseTeacher`


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
| teacherUids | 是 | array[string] | 教师UID数组|   |


## 响应参数

| 参数名 | 类型 | 示例值 | 含义 |
|-----|---- |---- |-----|
| code | integer | 1 | 错误码 |
| msg | string | "程序正常执行" | 错误信息 |
| data | array[integer] | null | 返回信息 |
| └ teacherUid | integer |  | 返回信息 |
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
    "teacherUids": [
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
     -d '{"courseId": 414193, "teacherUids": [504026, 504028]}' \
     'https://root_url/course/addCourseTeacher'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
	"code": 1,
	"msg": "程序正常执行",
	"data": [
    {
		"teacherUid": 504026,
		"code": 387,
		"msg": "老师已被停用"
	}, 
    {
		"teacherUid": 504028,
		"code": 1,
		"msg": "程序正常执行"
	}
    ]
}
```


## 错误码说明


| 错误码 | 说明 |
|:------|:----|
|104|操作失败|
|133|老师或学生已经存在|
|136|机构下面没有该老师，请在机构下添加该老师|
|144|机构下无此课程|
|147|没有此课程信息|
|149|该课程已经删除|
|172|课程下的学生不能添加为老师|
|173|课程下的旁听不能添加为老师|
|387|老师已被停用|
|884|老师账号已注销|
|30031|课程已结课|
|30013|获取机构类型错误|
|30022|该成员已经是课程班主任|
|101001001|业务参数错误
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 121601020 | 参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601030 | 缺少必传参数 |