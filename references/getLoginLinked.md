# 获取唤醒客户端并进入教室链接
获取唤醒客户端并进入教室链接，需要 SID、safekey、timeStamp、用户uid、课程 ID、课节 ID，平台识别标志，返回可以在 PC 端或者移动端唤起 ClassIn 客户端的链接。

**2021-03-30重要信息备注：**<br>
自2021年6月1日起，本接口将做如下调整：返回的URL将不再包含临时密钥authTicket了（翼鸥将根据用户账号逐步分批调整，6.30日全部完成调整），也就是说不再支持使用临时密钥authTicket免密登录唤起客户端。<br>

此调整对您的API对接程序没有任何影响，只会影响您的用户在网页唤起后的操作体验，需要您的客服或者运营团队，提前与用户沟通此体验变化：<br>
从2021-06-01日开始，用户首次网页唤起ClassIn客户端后，程序将停留在登录界面等待用户输入密码并点击“登录”，方能进入教室。<br>
请注意：
1. 对于移动端ClassIn软件会自动记住密码；对于PC ClassIn强烈建议用户在输入密码后勾选“记住密码”以便于下次唤起无须再次输入密码。
2. 如果用户忘记密码，可以点击登录页面的“忘记密码”以找回密码。


## URL

`https://root_url/partner/api/course.api.php?action=getLoginLinked`

## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

| key | 必填 | 更多限制  |	说明 | 规则说明
| ----| ----|----|----| ----- |
| SID | 是 | 无 |	机构认证 ID	| 通过 eeo.cn 申请机构认证可获得
| safeKey |	是 | 固定 32 位全小写字符  | 机构认证安全密钥 |	safeKey=MD5(SECRET+timeStamp)
| timeStamp	| 是 | 无 | 当前调用接口20分钟以内的 Unix Epoch 时间戳 | Unix Epoch 时间戳是 1970年1月1日 00:00:00 (世界标准时间) 起经过的秒数
| uid | 是 | 无 | 用户 UID | 注册用户返回的用户 UID
| lifeTime |	否 |	默认为86400秒 |	密钥有效时长（单位：秒）|	无
| courseId |	是 |	无 | 课程 ID |	创建课程后的返回值
| classId	| 是 |	无 |	课节 ID |	创建课节后的返回值
| deviceType | 否 | 默认为1，代表 PC 端 | 平台标志 | 1代表 Windows/Mac OS 端；2代表 iOS 移动端；3代表 Android


## 响应参数

| key | 类型 | 示例值 | 含义
| ----|---- |-----| ----|
| data | string |	`classin://www.eeo.cn/enterclass?telephone=23692341020&classId=1424463&courseId=444451&schoolId=1009478` | 可在网页登录`ClassIn客户端`的链接
| error_info | 	object |	|	返回信息对象
| └ errno |	number |	1	 | 错误代码
| └ error |	string |	"程序正常执行" |	错误详情


## 示例

- HTTP 请求

```http
POST /partner/api/course.api.php?action=getLoginLinked HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=8d3fb00ceddd29638e2d5dd12d69841d&timeStamp=1492793638&uid=1058467&lifeTime=&courseId=332241&classId=1227045&deviceType=1
```


- Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
        -d "SID=1234567" \
        -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
        -d "timeStamp=1484719085" \
        -d "uid=1065864" \
        -d "lifeTime=" \
        -d "courseId=332241" \
        -d "classId=1227045" \
        -d "deviceType=2" \
        "https://root_url/partner/api/course.api.php?action=getLoginLinked"
```


## PC 端网页唤起响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": "classin://www.eeo.cn/enterclass?telephone=23692341020&classId=1424463&courseId=444451&schoolId=1009478",
  "error_info": {
    "errno": 1,
    "error": "程序正常执行"
  }
}
```

## 移动端（iOS）网页唤起响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": "https://www.eeo.cn/client/mobile/ios/enterclass/?telephone=18801391473&classId=2645255&courseId=805773&schoolId=2516840",
  "error_info": {
    "errno": 1,
    "error": "程序正常执行"
  }
}
```

## 移动端（Android）网页唤起响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": "classin://www.eeo.cn/enterclass?telephone=18801391473&classId=296516&courseId=124575&schoolId=1002856",
  "error_info": {
    "errno": 1,
    "error": "程序正常执行"
  }
}
```

# 客户端网页唤醒中间提示页（可选）

## 主要用途：

使用网页唤醒功能时，会有一个页面提示用户如果未启动，或者启动失败，请重新下载安装 ClassIn 客户端，使用方式如下。iOS 移动端返回的链接中已经加入了中间页，无须拼接。

## 效果预览：

[从网页唤醒 12345678901 ClassIn客户端账号](https://www.eeo.cn/client/invoke/index.html?telephone=12345678901&classId=1213545&courseId=394761&schoolId=1009478)


## 使用说明：

https://www.eeo.cn/client/invoke/index.html 这个链接是判断用户是否有安装客户端，如果有安装会直接提示打开客户端。适用于 PC 端和 移动端平台。**如果需要网页唤起并进入教室，需要将本接口返回链接中的所有参数拼接在该地址后面即可**，方式如下方第二行代码所示：

```
  <a href='https://www.eeo.cn/client/invoke/index.html'>打开客户端</a>
  <a href="https://www.eeo.cn/client/invoke/index.html?telephone=12345678901&classId=1213545&courseId=394761&schoolId=1009478">从网页唤醒 12345678901 ClassIn客户端账号</a>
```



## 错误码说明

| 错误码 |	说明|
|:-------|-----|
| 1   | 表示成功执行
| 100	| 表示参数不全或错误
| 102	| 表示无权限（安全验证没通过）
| 104	| 表示操作失败（未知错误）
| 114	| 表示服务器异常
| 134 |	手机号码格式错误
| 142	| 该课程下无此课节信息
| 143	| 无此课节信息
| 144	| 机构下无此课程
| 145	| 该课节已经结束
| 150	| 此用户不属于该机构下学生、老师和旁听，或者不属于该课节成员
| 212	| 该课节已经删除
| 369 | 该课程/课节类型暂不支持该操作  
| 467 | 免密登录仅支持手机账号，请先绑定手机号
| 888 | 用户帐号已注销 |
