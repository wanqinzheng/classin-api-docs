# 课程分组-删除课程分组


## URL

`https://root_url/partner/api/course.api.php?action=delCourseGroup`

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
| groupId |	是 |  无  |	分组Id |	无|
	


## 响应参数


| key | 类型 | 示例值 | 含义
| ----|-----|-----| ----|
| error_info | 	object |	|	返回信息对象
| └ errno |	number |	1	 | 错误代码
| └ error |	string |	"程序正常执行" |	错误详情

## 示例

 -  HTTP 请求

```
POST /partner/api/course.api.php?action=delCourseGroup HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=1234567&safeKey=5458edceccc78c6698de624e94364285&timeStamp=1493026245&courseId=176465&groupId=139
```

 - Shell cURL模拟请求指令

```
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
       -d "SID=1234567" \
       -d "safeKey=c8e0b0e20c95c3adba9f263e04c598e7" \
       -d "timeStamp=1637133036" \
       -d "courseId=176465" \
       -d "groupId=139" \
       "https://root_url/partner/api/course.api.php?action=delCourseGroup"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```
{
"error_info": {
    "errno": 1,
    "error": "程序正常执行"}
}
```


## 错误码说明

| 错误码 |	错误详情|
|:-------|-----|
| 1   | 程序正常执行
| 100	| 参数不全或错误
| 102	| 无权限
| 104	| 操作失败/未知错误
| 891	| 删除课程分组信息失败
| 893	| 操作失败，此课程分组不存在

