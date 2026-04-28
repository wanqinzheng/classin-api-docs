# 课节下添加学生（多个）

**![!deprecated](../../img/waring.png)通知：此接口为原课节类接口，2025年5月26日之后将不再更新(但是可以继续使用原功能。)，建议使用LMS活动类接口：[添加活动成员](../LMS/addStudent.md)**

该接口往课节下添加插班生。支持双师课节。      
**！注意，插班生只能进入直播课堂，无法加入班级群，没有班级聊天，作业等功能。**      
课节下添加学生（多个），**建议一次性添加学生不超过30个**，需要 SID，safekey，timeStamp，课程 ID，课节 ID，学生识别（1为学生），需要添加的账号数组，其中包括学生UID。
返回的是每个账号添加的说明。     
用户可以传递自定义字段，接口会原样将参数返回。不传递则不会返回。   
该课节下添加的学生只可以上该课节，课程下其他课节不可上。     
课节下不能添加旁听生。

## URL

`https://root_url/partner/api/course.api.php?action=addClassStudentMultiple`  

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
| classId |	是 |	无 |	课节 ID |	无|
| identity | 是 |	不填写默认为1 |	学生识别(1为学生) |	无|
| studentJson |	是 |	无 |	需要添加帐号数组 |	无|
| └ 学生1帐号信息对象 |	是 |	无 |	需要添加学生信息对象 |	无|
| 　 └ uid | 是 | 无 | 学生 UID | 注册用户接口返回的用户 UID
| 　 └ customColumn | 否 | 1-50字，不区分中英文，超过50会自动截取为50字 | 用户自定义标识 | 不为空则原样返回，为空则不返回该字段|
| └ ······ |	是 |	无 |	需要添加学生信息对象 |	无|
| 　 └ uid | 是 | 无 | 学生 UID | 注册用户接口返回的用户 UID|
| 　 └ customColumn | 否 | 1-50字，不区分中英文，超过50会自动截取为50字 | 用户自定义标识 | 不为空则原样返回，为空则不返回该字段|

## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|----|---- |-----|
| data | array | []	|	返回 Data 信息数组
| └ data返回信息1 | object |	|	返回信息对象
| 　 └ customColumn | string |	123 |	用户自定义标识
| 　 └ errno | number |	1 |	错误代码
| 　 └ error | string |	"程序正常执行" |	错误详情
| └ data返回信息2 | object |	|	返回信息对象
| 　 └ customColumn | string |	123 |	用户自定义标识
| 　 └ errno | number |	1 |	错误代码
| 　 └ error | string |	"程序正常执行" | 	错误详情
| └ ······ | object |	|	返回信息对象
| 　 └ customColumn | string |	123 |	用户自定义标识
| 　 └ errno | number | ··· |	错误代码
| 　 └ error | string	|··· |	错误详情
| error_info | 	object |	|	返回信息对象
| └ errno |	number |	1	 | 错误代码
| └ error |	string |	"程序正常执行" |	错误详情


## 示例

 -  HTTP 请求

```http
POST /partner/api/course.api.php?action=addClassStudentMultiple HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=a82c69dc799d6520e631f07f69ac6c96&timeStamp=1493726450&courseId=523689&classId=1419691&identity=1&studentJson=[{"uid":"1001001","customColumn":123},{"uid":"1001002","customColumn":123}]
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
        -d "SID=1234567" \
        -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
        -d "timeStamp=1484719085" \
        -d "courseId=442447 " \
        -d "classId=23456" \
        -d "identity=1" \
        -d 'studentJson = \
        [ \
              { \
                "uid":"1001011", \
              }, \
              { \
                "uid":"1001001", \
              } \
        ]' \
        "https://root_url/partner/api/course.api.php?action=addClassStudentMultiple"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": [
    {
      "customColumn": "123",
      "errno": 1,
      "error": "程序正常执行"
    },
    {
      "customColumn": "123",
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
| 113	| 表示手机号码未注册
| 114	| 表示服务器异常
| 125	| 表示学生手机号不合法
| 129	| 表示老师不能添加为学生
| 131	| 表示注册失败
| 142	| 表示该课程下无此课节信息
| 143	| 没有此单课信息
| 144	| 机构下无此课程
| 145	| 表示该课节已经结束
| 155	| 表示学生数组不可为空
| 157	| 表示已超出课节下学生数量
| 158	| 表示课节下添加学生失败
| 159	| 表示课节下目前只支持对学生的操作
| 164 | 表示课程下已存在此旁听
| 166	| 表示课节下已存在此学生
| 212	| 表示该课节已删除
| 228 | 机构下无此学生 |
| 288 | 表示此号段不合法
| 329 | 表示课节联席教师不能添加为同课节的学生
| 332 | 课程老师或联席教师不能添加为课程学生或旁听
| 333 | 班主任不能添加为课程学生
| 369 | 该课程/课节类型暂不支持该操作
| 400 | 表示请求数据不合法
| 466 | 表示通过客户端-创建课堂产生的课节只能在客户端编辑（接口不支持添加lms课节学生）
| 886 | 学生帐号已注销 |

