# 获取指定文件夹下的文件及文件夹列表

获取指定文件夹下的文件及文件夹列表，需要 SID，safekey，timeStamp，指定文件夹 ID（没有指定文件夹 ID，会选择顶级文件夹）。返回指定文件夹下的文件夹及文件。

## URL

`https://root_url/partner/api/cloud.api.php?action=getCloudList`  

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
| folderId | 否 | 无 | 	文件夹 ID |	可为空，为空则返回顶级文件夹下的文件夹和文件列表|


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| folder_list |	array |	|	返回数文件夹列表数组|
| └ 文件夹1信息对象 |	object |	|	返回数文件夹 1 对象，包括以下字段|
| 　 └ folder_id |	string |	123456 |	文件夹 ID|
| 　 └ folder_name |	string |	机构网盘 |	文件夹名称|
| 　 └ is_system_folder |	number |	1 |	是否系统文件夹，0 为否，1 为是|
| └ 文件夹2信息对象 |	object |	|	返回数文件夹2对象，包括以下字段|
| 　 └ folder_id |	string |	123457 |	文件夹 ID|
| 　 └ folder_name |	string |	我的教材 |	文件夹名称|
| 　 └ is_system_folder |	number |	1 |	是否系统文件夹，0 为否，1 为是|
| └ ······ |	object |	|	返回数文件夹对象，包括以下字段|
| 　 └ folder_id |	string |	··· |	文件夹 ID|
| 　 └ folder_name |	string |	··· |	文件夹名称|
| 　 └ is_system_folder |	number |	··· |	是否系统文件夹，0 为否，1 为是|
| file_list |	array	 | |	返回数文件列表数组|
| └ 文件1信息对象 |	object	| |	返回数文件1对象，包括以下字段|
| 　 └ id |	string |	1234568 |	文件 ID|
| 　 └ file_name |	string |	机构网盘 |	文件名称|
|　  └ file_size |	string |	10KB |	文件大小|
| └ 文件2信息对象 |	object |	|	返回数文件2对象，包括以下字段|
| 　 └ id |	string |	1234578 |	文件 ID|
| 　 └ file_name |	string |	我的教材 |	文件名称|
| 　 └ file_size |	string |	10KB |	文件大小|
| └ ······ |	object |	|	返回数文件对象，包括以下字段|
| 　 └ id |	string |	··· |	文件 ID|
| 　 └ file_name |	string |	··· |	文件名称|
| 　 └ file_size |	string |	··· |	文件大小|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

- HTTP 请求

```http
POST /partner/api/cloud.api.php?action=getCloudList HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=209f418afc25710c51327f3e97966a89&timeStamp=1494231322&folderId=123456
```

- Shell cURL模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "folderId=123456" \
      "https://root_url/partner/api/cloud.api.php?action=getCloudList"
```  


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "folder_list": [
    {
      "folder_id": "714013",
      "folder_name": "机构网盘",
      "is_system_folder": 1
    },
    {
      "folder_id": "713961",
      "folder_name": "我的教材",
      "is_system_folder": 1
    },
    {
      "folder_id": "748651",
      "folder_name": "helloworld",
      "is_system_folder": 0
    }
  ],
  "file_list": [
    {
      "id": "496225",
      "file_name": "test.php",
      "file_size": "7KB"
    },
    {
      "id": "496229",
      "file_name": "test.png",
      "file_size": "27KB"
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
| 193	| 表示文件夹不存在
| 194	| 表示文件夹不属于该机构（无权操作）
