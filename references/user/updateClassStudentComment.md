# 更新课节教师对学生评价

更新课节学生评价，需要 SID，safekey，timeStamp，课节 ID、评论数据等。返回该课节下修改评价后的详情。

## URL

`https://root_url/partner/api/course.api.php?action=updateClassStudentComment`  

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
| classId |	是 | 无 |	课节 ID |	无|
| commentJson | 是 |  |评论数据结构 | 无 |
| 　 └ studentUid | 是 | 无 | 学生 UID | 注册用户接口返回的用户 UID|
| 　 └ starNum | 是 | startNum 为数字，0-5之间，小于0重置为0，大于5重置为5 | 评分（星级） | 无 |
| 　 └ comment | 是 | comment 为字符串，长度小于1000字，不区分大小写，超过1000会自动截取为1000个字 | 评价内容 | 无 |
| 　 └ customColumn | 否 | customColumn可以为空，如果不为空，长度1-50，不区分中英文，超过50会自动截取为50字 | 用户自定义标识 | 无|



## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| data | array | []	|	返回 Data 信息数组|
| └ data返回信息1 |	object |	|	返回学生评价信息|
| 　 └ studentUid |	string | "1001001" |	用户 UID|
| 　 └ customColumn |	string |	自定义字段，传什么返回什么，不传则不返回该字段 |	自定义字段|
| 　 └ errno |	string | 1 |	错误代码|
| 　 └ error | string | "程序正常执行" | 错误详情|
| └ data返回信息2 |	object |	|	返回学生评价信息|
| 　 └ studentUid |	string | "1001002" |	用户 UID|
| 　 └ customColumn |	string |	自定义字段，传什么返回什么，不传则不返回该字段 |	自定义字段|
| 　 └ errno |	string | 1 |	错误代码|
| 　 └ error | string | "程序正常执行" | 错误详情|
| error_info | 	object |	|	返回信息对象|
|　 └ errno |	number |	1	 | 错误代码|
|　 └ error |	string |	"程序正常执行" |	错误详情|


## 示例

 -  HTTP 请求

```http
POST /partner/api/course.api.php?action=updateClassStudentComment HTTP/1.1
Host: root_url
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=d8e6b1b7b55483ba93da7bc8e1d9514f&timeStamp=1493728253&classId=27981=commentJson=[{"studentUid":"1001001","starNum":"5","comment":"评价内容","customColumn":"学生1"},{"studentUid":"1001002","starNum":"5","comment":"评价内容","customColumn":"学生2"}]
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "classId=27981" \
      -d 'commentJson= \
        [ \
          { \
            "studentUid": "1001002", \
            "starNum": "5", \
            "comment": "评价内容", \
            "customColumn": "用户自定义标识" \
          } \
        ]' \
      "https://root_url/partner/api/course.api.php?action=updateClassStudentComment"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "data": [
        {
            "studentUid": "1001001",
            "customColumn": "学生1",
            "errno": 1,
            "error": "程序正常执行"
        },
        {
            "studentUid": "1001002",
            "customColumn": "学生2",
            "errno": 1,
            "error": "程序正常执行"
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
|  1  | 表示成功执行
| 100 | 表示参数不全或错误
| 102 | 表示无权限（安全验证没通过）
| 104 | 表示操作失败（未知错误）
| 167 | 表示课节下不存在此学生
| 228 | 表示机构下无此学生
| 233 | 表示机构下无此课节
| 369 | 该课程/课节类型暂不支持该操作
| 400 | 表示请求数据不合法
