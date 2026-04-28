# 课程下删除学生/旁听（多个）
课程下删除学生/旁听（多个），需要 SID，safekey，timeStamp，提供课程 ID，学生或旁听的识别（1为学生，2 为旁听），需要删除的账号数组，数组中包括需要删除的账号、学生/旁听UID等。返回每个账号执行后的说明。

## URL

`https://root_url/partner/api/course.api.php?action=delCourseStudentMultiple`  

## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

| key | 必填 | 更多限制  |	说明 | 规则说明|
| ----| ----|----|----| ----- |
| SID | 是 | 无 |	机构认证 ID	| 通过 eeo.cn 申请机构认证可获得|
| safeKey |	是 | 固定 32 位全小写字符  | 机构认证安全密钥 |	safeKey=MD5(SECRET+timeStamp)|
| timeStamp	| 是 | 无 | 当前调用接口20分钟以内的 Unix Epoch 时间戳 | Unix Epoch 时间戳是 1970年1月1日 00:00:00 (世界标准时间) 起经过的秒数|
| courseId |	是 |	无 |	课程 ID |	无|
| identity |	是 |	无 |	学生和旁听的识别(1 为学生,2 为旁听) |	无|
| studentUidJson | 是 |	数组如果不为空，长度至少为1，可多个UID |	需要删除学生UID数组 |	无|
|　└ 学生1 UID | 是 |	无 |	学生 UID | 注册用户接口返回的用户 UID，例如： 1001001|
|　└ 学生2 UID |	否 |	无 |	学生 UID | 注册用户接口返回的用户 UID，例如： 1001002|
|　└ ······ |	否 |	无 |	学生 UID | 注册用户接口返回的用户 UID，例如： 1001003|


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|-----| ---- |-----|
| data | array | [] |	返回data信息数组|
| └ data返回信息1 | object |	|	返回信息对象|
| 　 └ errno | number |	1 |	错误代码|
| 　 └ error | string	| "程序正常执行" |	错误详情|
| └ data返回信息2 | object |	|	返回信息对象|
| 　 └ errno | number |	1 |	错误代码|
| 　 └ error | string |	"程序正常执行" | 	错误详情|
| └ ······ | object |	|	返回信息对象|
| 　 └ errno | number | ··· |	错误代码|
| 　 └ error | string |	··· |	错误详情|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

- HTTP 请求

```http
POST /partner/api/course.api.php?action=delCourseStudentMultiple HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=b3c832f1b7ae456c38e11320099beecb&timeStamp=1493726325&courseId=490583&identity=1&studentUidJson=["1001001"]
```

- Shell cURL模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "courseId=442447" \
      -d "identity=1" \
      -d "studentUidJson=['1001001']" \
      "https://root_url/partner/api/course.api.php?action=delCourseStudentMultiple"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": [
    {
      "errno": 1,
      "error": "程序正常执行"
    }
  ],
  "error_info": {
    "errno": 1,
    "error": "程序正常执行"
  }
}
```


## 错误码说明

| 错误码 |	说明 |
|:-------|-----|
| 1   | 表示成功执行
| 100	| 表示参数不全或错误
| 102	| 表示无权限（安全验证没通过）
| 104	| 表示操作失败（未知错误）
| 114	| 表示服务器异常
| 134	| 表示手机号不合法
| 144	| 表示机构下无此课程
| 147	| 表示无此课程信息
| 153	| 表示课程已过期
| 155	| 表示数据数组不可为空
| 162	| 表示课程下无此成员
| 369 | 该课程/课节类型暂不支持该操作
| 400 | 表示请求数据不合法
