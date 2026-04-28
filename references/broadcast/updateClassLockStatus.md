# 修改课节锁定状态
修改课节锁定状态，需要提供 SID，safekey，timeStamp，课节 ID，是否锁定，返回执行后的详情。不修改此状态，默认所有课节都处于不锁定状态。如果在 eeo.cn 后台开启了自动删除录课视频和监课图片的功能后，将课节修改为锁定状态，则该课节的录课视频和监课图片将不会被自动删除。

## URL

`https://root_url/partner/api/course.api.php?action=updateClassLockStatus`  

## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

| key | 必填 | 更多限制  |	说明 | 规则说明|
| ----| ----|----|----| ----- |
| SID | 是 | 无 |	机构认证 ID	| 通过 eeo.cn 申请机构认证可获得|
| safeKey |	是 | 固定 32 位全小写字符  | 机构认证安全密钥 |	safeKey=MD5(SECRET+timeStamp)|
| timeStamp	| 是 | 无 | 当前调用接口20分钟以内的 Unix Epoch 时间戳 | Unix Epoch 时间戳是 1970年1月1日00:00:00 (世界标准时间) 起经过的秒数|
| classId | 是 | 无 | 课节 ID | 无|
| isLock | 是 | 0不锁定，1锁定，所有非1的数字都当做0处理| 是否锁定 | 无|

## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|



## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=updateClassLockStatus HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=4c375898926f24ad991099df67ebef92&timeStamp=1493729726&classId=1395037&isLock=1
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
        -d "SID=1234567" \
        -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
        -d "timeStamp=1484719085" \
        -d "classId=9876" \
        -d "isLock=1" \
    "https://root_url/partner/api/course.api.php?action=updateClassLockStatus"
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
| 104 | 表示操作失败/未知错误
| 233 | 表示机构下无此课节
| 369 | 该课程/课节类型暂不支持该操作
| 391 | 表示未结束的课节不支持修改锁定状态
