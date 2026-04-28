# 添加学生
添加学生（机构下添加学生），需要 SID，safekey，timeStamp，学生账号，学生姓名。 

这是对接过程的一个必要接口调用。 为确保接口调用正确，需注意： 

- 这个接口对应后台-学生管理-添加学生。注册用户必须添加为机构下学生，后继才能对其进行排课操作。如果用户并非机构下学生，直接用接口对其排课会返回错误。
- ClassIn新注册用户可以在注册接口里直接添加机构学生，参考注册接口。 如果非新用户，注册接口返回135，则需要调用本接口添加机构学生。



## URL

`https://root_url/partner/api/course.api.php?action=addSchoolStudent`  

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
| studentAccount | 是 | 手机号或者是邮箱，格式为：00国家号-手机号；**注意：中国大陆手机号不写国家号** | 学生账号 | 例如：美国手机号 1 (800) 643-7676 填成 001-8006437676；中国大陆手机号填成 15800000001|
| studentName |	是 |	1-24字，不区分中英文，超过24会自动截取为24字 |	学生名字，会显示在 eeo.cn 管理后台的 **学生管理** 页面 |	无|


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=addSchoolStudent HTTP/1.1
Host: root_url
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=dcbc0d041c043f3a4decabe6d24e61dd&timeStamp=1493712683&studentAccount=18516900101&studentName=Jeck
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "studentAccount=18516900101" \
      -d "studentName=小红" \
      "https://root_url/partner/api/course.api.php?action=addSchoolStudent"
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
| 104 | 表示操作失败（未知错误）
| 113	| 表示手机账户未注册
| 114	| 表示服务器异常
| 128	| 表示机构账号不能添加为学生
| 133 | 已是机构学生
| 134	| 表示手机号不合法
| 288 | 此号码段不合法
| 886 | 学生账号已注销 |
| 101003002	|  重复请求（请勿在5s内发送相同参数的请求）

