# 课程下删除学生/旁听（单个）
课程下删除学生/旁听（单个），需要 SID，safekey，timeStamp，该课程的课程 ID，学生或旁听的识别，需要删除的学生UID。返回执行后的说明。

## URL

`https://root_url/partner/api/course.api.php?action=delCourseStudent`

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
| identity |	是 | 无 |	学生和旁听的识别(1 为学生,2 为旁听) |	无|
| studentUid | 是 | 无 | 需要删除的学生 UID | 注册用户接口返回的用户 UID|

## 响应参数

| key | 类型 | 示例值 | 含义|
| ----|----|----| ----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|



## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=delCourseStudent HTTP/1.1
Host: www.eeo13.test
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=1002289&safeKey=ee982747b6b6333cdc40644b06b7c57d&timeStamp=1493030859&courseId=1431&identity=1&studentUid=1001001
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "courseId=442447" \
      -d "identity=1" \
      -d "studentUid=1001001" \
      "https://root_url/partner/api/course.api.php?action=delCourseStudent"
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
| 106	| 表示无可用数据
| 114	| 表示服务器异常
| 144	| 表示机构下无此课程
| 147	| 表示没有此课程信息
| 149	| 表示课程已删除
| 153	| 表示课程已过期
| 162 | 表示课程下无此成员
| 369 | 该课程/课节类型暂不支持该操作
| 400 | 表示请求数据不合法