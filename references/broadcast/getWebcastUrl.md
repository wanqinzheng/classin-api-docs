# 获取课程直播/回放播放器地址

　　我们为您提供了一个多平台支持的播放器页面，可以根据本接口获得的链接来观看在 ClassIn 上录的课。根据课程 ID 和课节 ID 来获取直播、回放的播放器地址。**注：课程或者课节的链接地址是固定不变的，无须重复获取。**

```
    小贴士： 针对 iOS 11+ 可能存在 cookie 写入不进去的情况
    但仍想用 iframe 嵌套直播页面，可以在 H5 页面头部，所有js之前引入
    <script src="//www.eeo.cn/js/live/eeolive_fix.js"></script>    
```

　　在直播页面我们植入了聊天室功能。为了方便您搜集潜在客户信息，所有用户需要填写手机号登陆后才可以聊天，如下图。当然，为了您更便捷的使用此功能，我们提供了您机构下所有学生免登陆的操作，请参考下方的 [机构直播聊天室免二次登陆](#机构直播聊天室免二次登录)。


![登陆聊天](../../img/webcast.jpg)


## 机构直播聊天室免二次登录
- 当您通过本接口获得播放器链接之后
  + 例：`https://www.eeo.cn/webcast.php?courseKey=xxx&lessonid=xxx`
  + 从直播器地址中可以获得 courseKey、lessonid
  + 您需要增加 account、nickname、checkCode 拼接在 `https://live.eeo.cn/webcast_partner.html` 地址后边，**注意：这个免二次登录地址与直播播放器地址不是同一个地址**
- 具体参数及规则如下
  + 具体参数有 courseKey、lessonid、account、nickname、checkCode
  + 其中 lessonid 为可选，其他参数皆为必选
  + account 为学生账号(长度小于32个字符)，nickname 为学生昵称(长度小于24个字符)
  + checkCode = md5(secret+courseKey+account+nickname)
  + secret 为SECRET，在 EEO.cn API 对接密钥处可获得
- URL 拼接示例
  + `https://live.eeo.cn/webcast_partner.html?courseKey=7be856f28907f1a2&lessonid=123456&account=18600123456&nickname=eeo&checkCode=febe50cd50ba4d3af506bfa118a3845b`



## URL

`https://root_url/partner/api/course.api.php?action=getWebcastUrl`  


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
| courseId | 是 | 无 | 课程 ID | 无 |
| classId | 否 | 无 | 课节 ID | 无|


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| data |	string |	`https://www.eeo.cn/webcast.php?courseKey=xxx&lessonid=xxx` |	返回直播回放页面地址|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

 -  HTTP 请求

```http
POST /partner/api/course.api.php?action=getWebcastUrl HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=c23f15a4382fd1da7e91a9697955b9bf&timeStamp=1493901829&courseId=536317&classId=1432593
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
        -d "SID=1234567" \
        -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
        -d "timeStamp=1484719085" \
        -d "courseId=123456" \
        -d "classId=9876" \
    "https://root_url/partner/api/course.api.php?action=getWebcastUrl"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": "https://www.eeo.cn/webcast.php?courseKey=4fe1167f8060e809&lessonid=123456",
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
| 142	| 表示该课程下无此课节信息
| 143	| 表示没有此课节信息
| 144	| 表示机构下无此课程
| 149	| 表示课程已删除
| 212 |	表示该课节已经删除
| 369 | 该课程/课节类型暂不支持该操作
