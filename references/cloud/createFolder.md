# 创建文件夹

创建文件夹，需要提供 SID，safekey，timeStamp，父级文件夹 ID（在哪个文件夹下创建文件夹），文件夹名称。
成功后返回文件夹 ID，失败后返回错误说明。    

### ****注意！！**  **  
文件夹最的目录总数最大限制是5000，深度最多是15级。超过了就会报错，最终创建失败。     
请留意文件夹大小，注意删除不必要的文件夹、文件。

## URL

`https://root_url/partner/api/cloud.api.php?action=createFolder`  

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
| folderId | 是 | 无 | 文件夹 ID | 在哪个文件夹下创建文件夹|
| folderName | 是 | 1-128个字符，不区分中英文，超出会自动截取为128字 | 文件夹名称 | 无|


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| data | string |	123456 |	创建完得到的文件夹 ID|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

 - HTTP 请求

```http
POST /partner/api/cloud.api.php?action=createFolder HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=10a6f11c7e2194146c88650439aa0f2e&timeStamp=1493792469&folderId=747759&folderName=tools
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
        -d "SID=1234567" \
        -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
        -d "timeStamp=1484719085" \
        -d "folderId=123456" \
        -d "folderName=课程1" \
        "https://root_url/partner/api/cloud.api.php?action=createFolder"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": "123456",
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
| 104	| 表示操作失败
| 193	| 表示文件夹不存在
| 194	| 表示文件夹不属于该机构（无权操作）
| 196	| 表示文件夹无操作权限
| 206	| 表示已存在同名文件夹（同时会返回文件夹ID）
| 207	| 表示文件夹层级超出限制
| 208	| 表示文件夹数量超出限制
