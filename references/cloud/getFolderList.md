# 获取云盘文件夹列表
通过此接口，您可以查询机构云盘根目录下两级的文件夹列表，返回的数据包含：文件夹 ID，父级 ID，文件夹名称等。

## URL

`https://root_url/partner/api/cloud.api.php?action=getFolderList`

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


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| data |	object |	|	机构云盘根目录下两级文件夹列表。key 是第一级文件夹的 ID，value 是它下面的子目录列表|
| └ 文件夹 1 |	array |	|	一级文件夹下面的子目录列表|
| 　 └ 文件夹 1-1 |	object |	 | 二级文件夹数据 |
| 　　 └ id |	string |	713960 | |
| 　　 └ pid |	string |	713940 |	父级文件夹 ID|
| 　　 └ name |	string |	课程一 |	名称|
|    └ 文件夹 1-2 |	object |	 | 二级文件夹数据 |
| 　　 └ id |	string |	713961 | |
| 　　 └ pid |	string |	713959 |	父级文件夹 ID|
| 　　 └ name |	string |	课程一 |	名称|
|    └ ... |	|	 | 二级文件夹数据 |
| └ ··· | |	|	一级文件夹下面的子目录列表 |
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|



## 示例

- HTTP 请求

```http
POST /partner/api/cloud.api.php?action=getFolderList HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=9974697bf6f886a17cc37fb9fd135d0c&timeStamp=1493798252
```

- Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      "https://root_url/partner/api/cloud.api.php?action=getFolderList"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": {
    "713940": [
      {
        "id": "713960",
        "pid": "713940",
        "name": "全部文件"
      }
    ],
    "713959": [
      {
        "id": "713961",
        "pid": "713959",
        "name": "我的教材"
      }
    ]
  },
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
| 106	| 表示无数据
