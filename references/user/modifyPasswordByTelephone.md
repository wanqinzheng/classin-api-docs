# 修改用户密码（不提供原密码）

 修改用户密码，需要 SID，safekey，timeStamp，用户uid、新密码（有明文和 MD5 加密两种方式可以选择），返回执行后的说明

## URL

`https://root_url/partner/api/course.api.php?action=modifyPasswordByTelephone`

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
| uid | 是 | 无 | 用户 UID | 注册用户接口返回的用户 UID |
| password | 是(与 md5pass 2选1) | 6-20位，不符合会报错 | 新密码 | 无|
| md5pass | 是(与 password 2选1) | 32位md5小写 | 新md5密码 | 无|


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

- HTTP 请求

```http
POST /partner/api/course.api.php?action=modifyPasswordByTelephone HTTP/1.1
Host: root_url
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=8d3fb00ceddd29638e2d5dd12d69841d&timeStamp=1492793638&uid=1001001&password=123456&md5pass=
```

- Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
    -d "SID=1234567" \
    -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
    -d "timeStamp=1484719085" \
    -d "uid=1001001" \
    -d "md5pass=e10adc3949ba59abbe56e057f20f88232" \
    "https://root_url/partner/api/course.api.php?action=modifyPasswordByTelephone"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
  {
    "error_info":{
      "errno":"1",
      "error":"程序正常执行"
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
| 113	| 表示手机号码未注册
| 114	| 表示服务器异常
| 134	| 表示手机号不合法
| 137	| 表示密码长度不合法(6-20位)
| 227	| 表示没有修改该此用户登录密码的权限（需要调用添加学生或者添加老师接口）
| 400   | 表示请求数据不合法 |
