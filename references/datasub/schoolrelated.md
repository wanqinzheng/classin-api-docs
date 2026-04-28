# 机构维度推送的消息
机构维度推送的消息，包括：文件转换结果，教室外设备检测，账号注销，更换账号手机号码，设置子账号。

这些数据将会在操作完成后实时推送。

## 1. 文件转换结果

机构账号上传文件转换后可收到此消息


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|类型为字符串，'FileCov'
|FileID|整数|转换文件ID
|Result|整数|转换结果：2为成功，3为失败
|Data|对象|转换文件描述
| └ addTime|整数|上传时间|
| └ changeTime|整数|转换时间|
| └ fileName|字符串|文件名|


### 实例

```json
{
	'ActionTime': 1521541032,
	'Cmd': 'FileCov',
	'Result': 2,
    'SID': 1001921,
	'Data': {
		'addTime': 1521541000,
		'changeTime': 1521541032,
		'fileName': 'origin'
	},
	'FileID': 9300
}

```

## 2. 用户教室外设备检测报告


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|类型为字符串，'UserCheck'|
|UID|Int64|用户UID|
|Data|对象|设备检测结果详细|
| └ OperatingSystem | string  |	操作系统|
| └ CPU | string | 用户 CPU。该字符串对于不同设备类型的含义：PC设备是CPU型号，iOS设备是设备型号和连接的网络类型（取"CPU:"后的信息），Android设备是手机型号、处理器型号和运行内存的信息（取“CPU：”和“，内存”之间的字段。安卓的处理器类型比较多，有些中间是带有“，”的）|
| └ NetworkDelay | string  | 网络延迟,移动端暂不支持（显示为null），"N/A"为测试超时|
| └ FrameLoss  | string | 丢包率
| └ MicrophoneArbitrary | number | 用户选择的麦克风状态(0未检测，1正常，2不正常)|
| └ HeadphoneArbitrary | number | 用户选择的耳机状态(0未检测，1正常，2不正常)|
| └ CameraArbitrary | number	| 用户选择的摄像头状态(0未检测，1正常，2不正常)|
| └ EEO_VIDEO_DEVICE_NAME | string	| 选用摄像头设备名称
| └ EEO_AUDIO_DEVICE_NAME | string	| 选用麦克风设备名称
| └ EEO_AUDIO_OUTPUT_NAME | string	| 选用耳机设备名称
| └ EEO_DEVICE_LIST | 对象 | 硬件列表
| 　 └ camera | array | 所有摄像头设备名称列表
| 　 └ micphone | array | 所有麦克风设备名称列表
| 　 └ speaker | array	| 所有扬声器设备名称列表
| └ MicrophoneImpersonal | number | 程序检测的麦克风状态（0未检测，1正常，2不正常）
| └ HeadphoneImpersonal | number	| 程序检测的耳机状态（0未检测，1正常，2不正常）
| └ CameraImpersonal | number | 程序检测的摄像头状态（0未检测，1正常，2不正常）
| └ MicrophoneAttachment  | string | 麦克风附件
| └ HeadphoneAttachment   | string	| 耳机附件 （暂时为空）
| └ CameraAttachment   | string	| 摄像头附件
| └ ClassInVersion  | string | 客户端版本
| └ ClientIP | string | 用户IP(最后一位隐藏)
| └ Mac   | string	| MAC 地址
| └ addTime   | string	| 自检时间（时间戳）
| └ InfoSource   | number	| 上传自检时机：3，自检完成；6，登录成功，7，自检中断；
| └ DeviceType   | number	| 设备类别：0，未知；1，Windows；2，iPhone；3，iPad；4，Android Phone；5，Android Pad；6，Mac



### 实例


```json
{
    "_id" : "5ae021b6e826ef1964cb18d3",
    "ActionTime" : 1524638134,
    "UID" : 1577526,
    "Cmd" : "UserCheck",
    "SID" : 1228552,
    "Data" : {
        "MicrophoneArbitrary" : null,
        "ClassInVersion" : "2.1.2.123",
        "OperatingSystem" : "Windows 7",
        "FrameLoss" : "0%",
        "EEO_AUDIO_DEVICE_NAME" : "",
        "CameraImpersonal" : 0,
        "addTime" : 1524638134,
        "CPU" : "Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz",
        "EEO_AUDIO_OUTPUT_NAME" : "",
        "Mac" : "00:FF:B3:D7:DC:D2",
        "CameraArbitrary" : null,
        "HeadphoneImpersonal" : 0,
        "EEO_VIDEO_DEVICE_NAME" : "",
        "ServerName" : "EEO-A1012 (Auto)",
        "HeadphoneAttachment" : "",
        "ClientIP" : "59.60.9.*",
        "MicrophoneAttachment" : "https://root_url/upload/autocheck/",
        "EEO_DEVICE_LIST" : "{\"camera\": [\"Logitech HD Webcam C270\"], \"micphone\": [\"HD Webcam C270\"], \"speaker\": [\"LG HDR 4K\"]}",
        "MicrophoneImpersonal" : 0,
        "CameraAttachment" : "",
        "HeadphoneArbitrary" : null,
        "InfoSource" : 3,
        "NetworkDelay" : "50ms"
    }
}
```

## 3. 账号注销
当用户在客户端执行账号注销操作后，机构可收到此消息。<br>
收到此消息后，您需要更新相关用户表。因为账号被注销后，其不能被添加老师，添加学生，设置为课节成员（老师、联席教师、学生）、设置为课程成员（班主任、学生、旁听生）等。

| 参数名 | 类型 | 说明 |
| ----- | ----- | ----- |
| Cmd | String | 类型为字符串，'AccountCancellation' |
| UID | 整数 | 用户UID |
| CancellationTime | 整数 | 账号注销操作时间 |
| AccountStatus | 整数 | 255表示该uid状态为已注销 | 

### 实例

```json
{
    "Cmd":"AccountCancellation",
    "SID":1001920,
    "UID":100191,
    "CancellationTime":1524638134
    "AccountStatus":255
}
```

## 4. 更换账号手机号码
当用户在客户端执行更换账号手机号码操作后，机构可收到此消息。<br>
收到此消息后，您需要更新相关用户表，用新手机号码替换旧的手机号。其他数据不受影响。

| 参数名 | 类型 | 说明 |
| ----- | ----- | ----- |
| Cmd | String | 类型为字符串，'ReplacePhoneNumber' |
| UID | 整数 | 用户UID |
| ReplaceTime | 整数 | 更换手机号码操作时间 |
| Telephone | String | UID对应的新手机号码 | 
| Email | String | UID对应的邮箱 | 

### 实例

```json
{
    "Cmd":"ReplacePhoneNumber",
    "SID":1001920,
    "UID":100191,
    "ReplaceTime":1524638134
    "Telephone":18600000000
}
```

## 5. 设置子账号
当管理员在eeo.cn学校后台成功添加/编辑子账号后，机构可收到此消息。<br>

| 参数名 | 类型 | 说明 |
| ----- | ----- | ----- |
| Cmd | String | 类型为字符串，'setSubAccount' |
| UID | 整数 | 被添加为子账号用户的UID |
| Telephone | String | UID对应的手机号码 |
| Email | String | UID对应的邮箱 | 
| RemarkName | String | UID用户的备注名 |
| PermissionList | String | 分配给UID的操作权限列表，数字之间的分隔符为逗号，数字代表页面的含义如下：<br>1课程管理和课节统计，3学校资料，3_1学校资料删除权限，3_2学校资料下载权限，4教师管理，5学生管理，7监课管理和账号速查，9API对接文档，10财务中心，11教学数据，12学校设置，13存储管理，16作业管理，17资源商品，20直播回放，22测验管理 |
| SetTime | 整数 | 设置子账号的时间 |

### 实例

```json
{
    "Cmd":"setSubAccount",
    "SID":1001920,
    "UID":100191,
    "Telephone":"18600000000",
    "RemarkName":"张三",
    "PermissionList":"1,3,3_1,4,5",
    "SetTime":1524638134
}
```

