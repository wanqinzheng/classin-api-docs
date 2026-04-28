# 课程下多个课节添加学生

**![!deprecated](../../img/waring.png)通知：此接口为原课节类接口，2025年5月26日之后可继续使用，但不再更新 ，建议使用LMS活动类接口（多个课节需要多次调用）：[添加活动成员](LMS/addStudent.md)**

课程下多个课节添加学生，**建议一次性添加课节不超过100个**，需要 SID，safekey，timeStamp，课程 ID，学生UID，课节数组（需要的课节 ID）。返回的数据中包括每节课添加执行后的说明。

## URL

`https://root_url/partner/api/course.api.php?action=addCourseClassStudent`  

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
| studentUid | 是 | 无 | 学生 UID | 注册用户接口返回的用户UID|
| classJson |	是 |	无 |	课节 ID 数组 |	无|
|  └ 课节1的 ID |	是 |	无 |	课节 ID |	无|
|  └ 课节2的 ID |	否 |	无 |	课节 ID |	无|
|  └ ······ |	否 |	无 |	课节 ID |	无|


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| data | array | [] |	返回 Data 信息数组|
| └ data返回信息1 |	object |	|	返回信息对象|
| 　 └ errno |	number |	1 |	错误代码|
| 　 └ error	| string |	"程序正常执行" |	错误详情|
| └ data返回信息2 |	object |	| 返回信息对象|
| 　 └ errno |	number |	1 |	错误代码|
| 　 └ error |	string |	"程序正常执行" |	错误详情|
| └ ······ |	object |	|	返回信息对象|
| 　 └ errno |	number |	··· |	错误代码|
| 　 └ error |	string |	··· |	错误详情|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=addCourseClassStudent HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=dcbc0d041c043f3a4decabe6d24e61dd&timeStamp=1493712683&courseId=490583&studentUid=1001001&classJson=[1395045,1395044,1395043]
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "courseId=123456" \
      -d "studentUid=1001001" \
      -d "classJson=[1212131,1212123]" \
      "https://root_url/partner/api/course.api.php?action=addCourseClassStudent"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": [
    {
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
| 1   | 表示成功执行
| 100	| 表示参数不全或错误
| 102	| 表示无权限（安全验证没通过）
| 113	| 表示手机账户未注册
| 114	| 表示服务器异常
| 129	| 表示老师不能添加为学生
| 134	| 表示手机号不合法
| 142	| 表示该课程下无此课节信息
| 144	| 表示机构下无此课程信息
| 145	| 表示该课节已经结束
| 149	| 表示课程已删除
| 153	| 表示课程已过期
| 155	| 表示学生数组不可为空
| 157	| 表示已超出课节下学生数量
| 158	| 表示课节下添加学生失败
| 164	| 表示课程下已存在此旁听
| 166	| 表示课节下已存在此学生
| 212	| 表示该课节已删除
| 228 | 机构下无此学生 |
| 332 | 课程老师或联席教师不能添加为课程学生或旁听
| 333 | 班主任不能添加为课程学生
| 369 | 该课程/课节类型暂不支持该操作
| 400 | 表示请求数据不合法
| 466 | 表示通过客户端-创建课堂产生的课节只能在客户端编辑（接口不支持添加lms课节学生）
| 886 | 学生帐号已注销 |
