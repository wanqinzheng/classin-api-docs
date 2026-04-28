# 删除课节
删除课节，需要 SID、safekey、timeStamp、课程 ID 和课节 ID 等，返回删除后的说明。

注： 如果在创建课节（[创建课节(单个)](../classroom/addCourseClassMultiple.md)、[创建课节(多个)](../classroom/addCourseClassMultiple.md)）时，传了课节唯一标识courseUniqueIdentity的话，则成功删除课节后，课节唯一标识也会被删除的。

## URL

`https://root_url/partner/api/course.api.php?action=delCourseClass`

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
| classId |	是 | 无 |	课节 ID |	无|


## 响应参数

| 参数名 | 类型 |	示例值 |	含义|
| ---- |---- |----| ----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=delCourseClass HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=74522fc7742a006b8bc535d7219a3d2b&timeStamp=1493350512&courseId=490583&classId=1405639
```

- Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=7fe917c22f3afd6ebadd329cfab7d403" \
      -d "timeStamp=1492933564" \
      -d "courseId=14181" \
      -d "classId=23611" \
      "https://root_url/partner/api/course.api.php?action=delCourseClass"
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
| 140	| 表示该课节正在上课，不能编辑和删除
| 142	| 表示该课程下无此课节信息
| 143	| 表示无此课节信息
| 144	| 表示机构下无此课程
| 145	| 表示该课节已经结束，不能删除 |
| 212	| 表示该课节已经删除
| 369 | 该课程/课节类型暂不支持该操作
| 466 | 表示通过客户端-创建课堂产生的课节只能在客户端编辑（接口不支持删除lms课节） 
| 823 | 表示删除课节成功，删除唯一标识失败