# 移除课程老师
移除课程老师，需要 SID，safekey，timeStamp，课程 ID，老师UID，返回的数据中包括课节 ID，执行后的说明。如果将老师从该课程下移除，该课程下未开课的课节中就不能有该账号；移除老师后，在 eeo.cn 课程详情中的教师列表中不再显示该老师，ClassIn 客户端的班级群中也不再显示该老师。

## URL

`https://root_url/partner/api/course.api.php?action=removeCourseTeacher`  

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
| courseId |	是 | 无 |	课程 ID |	无|
| teacherUid | 是 | 无 | 老师 UID | 注册用户接口返回的用户 UID|

## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

 -  HTTP 请求

```http
POST /partner/api/course.api.php?action=removeCourseTeacher HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=d8e6b1b7b55483ba93da7bc8e1d9514f&timeStamp=1493728253&courseId=523689&teacherUid=1001001
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "courseId=123456" \
      -d "teacherUid=1001001" \
      "https://root_url/partner/api/course.api.php?action=removeCourseTeacher"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
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
| 104	| 表示操作失败（未知错误）
| 114	| 表示服务器异常
| 122 | 表示老师账号格式不正确
| 136	| 表示机构下面没有该老师，请在机构下添加该老师
| 144	| 表示机构下无此课程
| 147	| 表示没有此课程信息
| 149	| 表示课程已删除
| 153	| 表示课程已过期
| 315 | 表示删除教师失败
| 316 | 表示教师列表不存在该老师
| 317 | 表示教师有未结束的课节
| 369 | 该课程/课节类型暂不支持该操作
| 400 | 表示请求数据不合法
