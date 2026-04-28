# 删除机构标签
删除机构标签，需要 SID，safekey，timeStamp 标签 ID。返回执行后的说明。

## URL

`https://root_url/partner/api/course.api.php?action=deleteSchoolLabel`  

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
| labelId | 是 | 无 | 标签 ID | 无|

## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- |---- |-----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|




## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=deleteSchoolLabel HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=e98b01228fca036bf2ab060f7a8a6ec3&timeStamp=1493725870&labelId=363
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "labelId=363" \
      "https://root_url/partner/api/course.api.php?action=deleteSchoolLabel"
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
| 102 | 表示无权限（安全验证没通过）
| 104 | 表示操作失败（未知错误）
| 355 | 表示标签不属于该机构
| 356 | 表示不存在此 id 的标签
