# 结束课程
结束课程，需要提供 SID，safekey，timeStamp，课程 ID，返回执行后的说明。注意：课程下没有正在上的课节，即可结束课程。如果课程下有尚未开始的课节，会删除未开始的课节之后结束课程，请谨慎使用此功能

## URL

`https://root_url/partner/api/course.api.php?action=endCourse`

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
| courseId |	是 | 无 |	课程 ID | 无|


## 响应参数

| key | 类型 | 示例值 | 含义
| ----|-----|-----| ----|
| error_info | 	object |	|	返回信息对象
| └ errno |	number |	1	 | 错误代码
| └ error |	string |	"程序正常执行" |	错误详情


## 示例

-  HTTP 请求

```http
POST /partner/api/course.api.php?action=endCourse HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=1002289&safeKey=9c5cceb65abc66f7d5f5ac5ff212a1ba&timeStamp=1492925596&courseId=1418
```

- Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
     -d "SID=1234567" \
     -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
     -d "timeStamp=1484719085" \
     -d "courseId=352855" \
     "https://root_url/partner/api/course.api.php?action=endCourse"
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
| 144 | 表示机构下无此课程
| 147	| 表示无此课程信息
| 149	| 表示该课程已删除
| 153	| 表示课程已过期
| 369 | 该课程/课节类型暂不支持该操作
| 394 | 表示课程下有正在上的课节，不能结束
