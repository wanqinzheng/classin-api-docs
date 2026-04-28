# 课节下删除学生（多个）

**![!deprecated](../../img/waring.png)通知：此接口为原课节类接口，2025年5月26日之后可继续使用，但不再更新 ，建议使用LMS活动类接口：[删除活动成员](LMS/deleteStudent.md)**



课节下删除学生（多个），需要 SID，safekey，timeStamp，课程 ID，课节 ID，学生识别（1为学生），需要删除的学生账号数组，其中包括要删除的学生UID。返回每个账号的执行后的说明。

## URL

`https://root_url/partner/api/course.api.php?action=delClassStudentMultiple`

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
| classId |	是 |	无 |	课节 ID |	无|
| identity |	是 |	无 |	学生识别(1为学生) |	无|
| studentUidJson |	是 |	数组如果不为空，长度至少为1，可多个UID |	需要删除学生UID数组 |	无|
|　└ 学生1 UID | 是 |	无 |	学生 UID | 注册用户接口返回的用户 UID，例如： 1001001|
|　└ 学生2 UID |	否 |	无 |	学生 UID | 注册用户接口返回的用户 UID，例如： 1001002|
|　└ ······ |	否 |	无 |	学生 UID | 注册用户接口返回的用户 UID，例如： 1001003|



## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- |---- |-----|
| data | array | []	|	返回 Data 信息数组|
| └ data返回信息1 | object |	|	返回信息对象|
| 　 └ errno | number |	1 |	错误代码|
| 　 └ error | string |	"程序正常执行" |	错误详情|
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
 POST /partner/api/course.api.php?action=delClassStudentMultiple HTTP/1.1
 Host: www.eeo.cn
 Content-Type: application/x-www-form-urlencoded
 Cache-Control: no-cache

 SID=2339736&safeKey=00ab6e63b2f13891a79a067aa4290854&timeStamp=1494410390&courseId=542163&classId=1474563&identity=1&studentUidJson=["1001001"]
 ```

 - Shell cURL 模拟请求指令

 ```bash
 curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
     -d "SID=1234567" \
     -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
     -d "timeStamp=1484719085" \
     -d "courseId=442447" \
     -d "classId=2447" \
     -d "identity=1" \
     -d 'studentUidJson=["1001001","1001002"]' \
     "http://www.eeo.cn/partner/api/course.api.php?action=delClassStudentMultiple"
 ```      


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": [
    {
      "errno": 1,
      "error": "程序正常执行"
    },
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

| 错误码 |	说明|
|:-------|-----|
| 1   | 表示成功执行
| 100	| 表示参数不全或错误
| 102	| 表示无权限（安全验证没通过）
| 113	| 表示手机号码未注册
| 114	| 表示服务器异常
| 142	| 表示该课程下无此课节信息
| 143	| 表示没有此课节信息
| 144	| 表示机构下无此课程
| 145	| 表示该课节已经结束
| 155	| 表示学生数组不可为空
| 159	| 表示课节下目前只支持对学生的操作
| 167	| 表示课节下不存在此学生
| 171	| 表示课节下删除学生失败
| 212	| 表示该课节已删除
| 369 | 该课程/课节类型暂不支持该操作
| 400 | 表示该请求数据不合法
| 466 | 表示通过客户端-创建课堂产生的课节只能在客户端编辑（接口不支持删除lms课节学生）
