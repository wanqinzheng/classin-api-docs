# 更换课程老师
更换课程老师，需要 SID，safekey，timeStamp，课程 ID，老师UID，返回的数据中包括课节 ID，执行后的说明。  
**注意：课程下所有未开始课节都改为此老师**
**注2：课程下的双师课节不支持更换老师，请调用双师接口编辑老师**

## URL

`https://root_url/partner/api/course.api.php?action=modifyCourseTeacher`  

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
| courseId |	是 | 无 |	课程 ID |	无|
| teacherUid | 是 | 无 | 老师 UID | 注册用户接口返回的用户 UID|

## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| data | array | []	|	返回 Data 信息数组|
| └ data返回信息1 |	object |	|	返回课节信息|
| 　 └ classId |	number |	1369235 |	课节 ID|
| 　 └ errno |	number |	1 |	错误代码|
| 　 └ error |	string |	"程序正常执行" |	错误详情|
| └ data返回信息2 |	object |	|	返回课节信息|
| 　 └ classId |	number |	1369235 |	课节 ID|
| 　 └ errno |	number |	1 |	错误代码|
| 　 └ error |	string |	"程序正常执行" |	错误详情|
| └ ······ |	object |	 |	返回课节信息|
| 　 └ classId	| number |	··· |	课节 ID|
| 　 └ errno |	number |	··· |	错误代码|
| 　 └ error |	string |	··· |	错误详情|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

 -  HTTP 请求

```http
POST /partner/api/course.api.php?action=modifyCourseTeacher HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=d8e6b1b7b55483ba93da7bc8e1d9514f&timeStamp=1493728253&courseId=523689&teacherUid=1001001
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "courseId=123456" \
      -d "teacherUid=1001001" \
      "https://root_url/partner/api/course.api.php?action=modifyCourseTeacher"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": [
    {
      "classId": "1395045",
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
| 104	| 表示操作失败（未知错误）
| 114	| 表示服务器异常
| 134	| 表示手机号码不合法
| 136	| 表示机构下面没有该老师，请在机构下添加该老师
| 144	| 表示机构下无此课程
| 146	| 表示课程已结束
| 147	| 表示没有此课程信息
| 149	| 表示课程已删除
| 153	| 表示课程已过期
| 172	| 表示课程下的学生不能添加为老师
| 173	| 表示课程下的旁听不能添加为老师
| 187	| 表示课节下的学生不能添加为老师
| 188	| 表示没有未开课的课节
| 189	| 表示课节老师更换失败
| 190	| 表示该课程未创建完成
| 324 | 表示课节老师加入教师列表失败
| 328 | 表示课节联席教师不能添加为老师
| 369 | 该课程/课节类型暂不支持该操作
| 387 | 表示老师已被停用
| 400 | 表示请求数据不合法
| 466 | 表示通过客户端-创建课堂产生的课节只能在客户端编辑
| 805 | 表示老师被停用中
| 884 | 老师帐号已注销 
