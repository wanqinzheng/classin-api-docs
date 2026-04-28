# 删除单个课节视频
删除单课视频，需要提供 SID，safekey，timeStamp，课节 ID，视频片段（单个视频文件） ID，返回删除后的详情。**注意：删除后课节视频不可恢复，删除后不再产生存储费用**

## URL

`https://root_url/partner/api/course.api.php?action=deleteClassVideo`  

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
| classId | 是 | 无 | 课节 ID | 无 |
| fileId | 否 | string类型 | 课节下某个视频片段文件的ID | 若此项为空或者不传参，则表示删除课节下所有视频片段文件 | 


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|



## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=deleteClassVideo HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=4c375898926f24ad991099df67ebef92&timeStamp=1493729726&classId=1395037
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
        -d "SID=1234567" \
        -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
        -d "timeStamp=1484719085" \
        -d "classId=9876" \
    "https://root_url/partner/api/course.api.php?action=deleteClassVideo"
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
| 100 | 表示参数不全或错误
| 102 | 表示无权限（安全验证没通过） |
| 104 | 表示操作失败 |
| 233 | 表示机构下无此课节
| 254 | 表示该课节没有开启录课，没有视频信息
| 369 | 该课程/课节类型暂不支持该操作
| 384 | 表示该课节还未结束 |
| 630 | 表示视频片段文件不存在 |
| 631 | 表示录课失败未生成视频文件
| 632 | 表示录课视频文件生成但已全部被删除
| 633 | 表示删除失败视频文件被保护锁定 |
| 634 | 表示视频片段文件已被删除 |

