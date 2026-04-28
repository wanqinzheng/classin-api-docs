# 课节内实时推送的消息

课节内（即上课过程中）实时推送的消息，包括：举手，奖励，摄像头位置，授权，进入教室，退出教室，踢出，全体静音，个人静音，答题器，抢答器，上下台，课节网络状态报告（每隔5分钟发送一次，为5分钟内的汇总信息），教室内设备检测报告，教室内老师和学生求助，延长课节时长，启动录课详情，教室大黑板板书图片，直播页面用户登录，直播预约，直播观看明细，直播点赞，直播商品点击明细。

这些数据将会在上课过程中实时推送。
 
## 举手

|字段 | 类型 | 说明
|----|------|----
|Cmd|Int32| 命令字67375105
|Color|String|hands up+用户ID
|Handsup|Boolean|True表示举手状态，False表示放手状态

## 奖励

|字段 | 类型 | 说明
|----|------|----
|Cmd|Int32| 命令字67375105
|Color|String|award + 用户ID
|Times|Int32|奖励次数

## 摄像头位置

|字段 | 类型 | 说明
|----|------|----
|Cmd|Int32| 命令字67375105
|Color|String|webcamPosition + 用户ID
|Area|Struct|摄像头区域
|   └ X1|Int32|左上角X坐标
|   └ Y1|Int32|左上角Y坐标
|   L X2|Int32|右下角X坐标
|   L Y2|Int32|右下角Y坐标
|OnTop|Bool|是否在坐席区，0：不在坐席区；1：在坐席区
|Channel|Int32|摄像头序号，0：主摄像头；1：辅摄像头


## 授权

|字段 | 类型 | 说明
|----|------|----
|Cmd|Int32| 命令字67371520
|Operation|Boolean|True为授权，False为取消授权



## 进入教室字段

|字段 | 类型 | 说明
|----|------|----
|Cmd|Int32| 命令字67371107
|NickName|String|用户昵称
|AllowEnterTime|Int32|用户被踢出后，允许再次进入时间
|UID|Int32|用户ID
|LoginMobile|String|手机号
|LoginEmail|String|邮箱账号
|ClientID|Int32|双设备登录模式中，第一个进入的设备为0，第二个进入的设备为1
|Identity|Int32|用户身份 1：学生，2：旁听，3：老师，4：联席教师，193：机构校长，194：校长助理
|Device|Int32|登陆客户端类型 0: PC, 1: iphone, 2: ipad, 3: web客户端 4: Android手机, 5: Android平板, 6: Android电视, 7: PC-TV, 8: Andriod-ChromeBook, 9: PC-x64, 10: PC-TV-x64 11: PC-ARM, 12: Harmony-Pad, 13: Harmony-Phone, 14: Web页面


## 退出教室字段

|字段 | 类型 | 说明
|----|------|----
|Cmd|Int32| 命令字67371111
|UID|Int32| 用户ID
|Identity|Int32|用户身份
|ClientID|Int32|双设备登录模式中，第一个进入的设备为0，第二个进入的设备为1
|Reason|Int32|退出原因，0：未知异常，1：正常退出，2：教室关闭，3：异常退出，4：被踢出教室，5：服务关闭，6：断线，7：取消排课，8：用户角色变更，54：客户端本机重复登陆，56：服务端与客户端网络连接中断，60：被新登录的客户端挤下线，101：按返回键退出（仅安卓设备），102：来电话退出，111：App进入后台


## 踢出

|字段 | 类型 | 说明
|----|------|----
|Cmd|Int32| 命令字67371523
|Duration|Int64|踢出维持时间
|TargetUID|Int32|被踢出ID
|Operation|Int32|1 被踢出


## 静音

|字段 | 类型 | 说明
|----|------|----
|Cmd|Int32|单独静音为67371522，全部静音为67371586
|TargetUID|Int32|静音对象ID
|Operation|Int32|1静音，0取消静音


## 答题器

|字段 | 类型 | 说明
|----|------|----
|Area|Struct|窗口坐标
|   └ X1,Y1,X2,Y2|Int32| 无
|Color|String|发题时为‘standaloneSelectorToolglobalData’，学生答题时为‘standaloneSelectorTool’ + 学生ID
|Cmd|Int32| 命令字67375105
|QSentTime|Int32|发放时间
|CurState|Int32|当前答题状态 0：开始状态，1：发题状态，2：收题状态
|QCollectTime|Int32|收题时间
|CorrectItems|String|正确答案
|Commited|Int32|学生答题状态 0：开始状态，1：答题状态，2：提交
|SelectedItem|String|学生选择的答案
|AllItems|String|所有备选答案
|Participants|Struct|参与答题人
|   └ ShowName|String|答题人昵称
|   └ Uid|Int32|答题人ID
|   L Identity|Int32|答题人身份
|RecvQuestionTime|Int32|学生收到试题时间
|LastCommitTime|Int32|学生提交答案时间



## 抢答器

|字段 | 类型 | 说明
|----|------|----
|Area|Struct|窗口坐标
| └ X1,Y1,X2,Y2|Int32| 无
|Color|String|发题消息为standaloneResponderToolglobalData，学生抢答消息为standaloneResponderTool+UID
|Cmd|Int32| 命令字67375105
|RandomTopLeft|Struct|随机位置坐标
| └ X,Y|Int32| 无
|Participants|Struct|参与抢答者
| └ ShowName|String|答题人昵称
| └ Uid|Int32|答题人ID
| L Identity|Int32|答题人身份
|EndTime|Int32|抢答结束时间
|CurState|Int32|当前状态，0：起始状态，1：开始抢答，2：学生抢答，3：抢答后等待，4：结束
|nId|Int32|最快抢答者ID
|FastestGuyTime|Int32|最快抢答时间
|FastestGuyName|String|最快抢答者


## 上下台

|字段 | 类型 | 说明
|----|------|----
|Cmd|Int32| 命令字67371521
|Operation|Int32|0为下台，1为上台


## 课节网络状态报告
课节实时网络与CPU占用率状态反馈，每5分钟发送一次，为5分钟内的汇总


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|类型为字符串，'Net'|
|Data|对象|状态统计|
| └ localIP | String | 用户ip （最后一位隐藏）| 
| └ socket | String | UDP/TCP，当前上报时间教室媒体实际通讯使用的协议 | 
| └ mediaPort | 整数 | 媒体端口 | 
| └ reportTime | String | 触发上报数据的时间戳 | 
| └ mediaDuration | 整数 | 上传周期的时间长度（秒） | 
| └ good | 整数 | UDP good的总次数 |
| └ normal | 整数 | UDP normal的总次数 |
| └ bad | 整数 | UDP bad的总次数 |
| └ poor | 整数 | UDP poor的总次数 |
| └ notReach | 整数 | UDP notReach的总次数 |
| └ total | 整数 | UDP 的总次数 |
| └ avgDelay | String | UDP 平均延时 |
| └ avgVariance | String | UDP 平均方差 |
| └ loss | 整数 | UDP 的实际丢包数量 |
| └ udpTotalPkts | 整数 | UDP 的实际测速总报文量 |
| └ tcpGood | 整数 | TCP good的总次数 |
| └ tcpNormal | 整数 | TCP normal的总次数 |
| └ tcpBad | 整数 | TCP bad的总次数 |
| └ tcpPoor | 整数 | TCP poor的总次数 |
| └ tcpNotReach | 整数 | TCP notReach的总次数 |
| └ tcpTotal | 整数 | tcp 的总次数 |
| └ tcpAvgDelay | String | tcp 平均延时 |
| └ tcpAvgVariance | String | tcp 平均方差 |
| └ gatewayGood | 整数 | 用户网关good的总次数 |
| └ gatewayNormal | 整数 | 用户网关normal的总次数 |
| └ gatewayBad | 整数 | 用户网关bad的总次数 |
| └ gatewayPoor | 整数 | 用户网关poor的总次数 |
| └ gatewayNotReach | 整数 | 用户网关notReach的总次数 |
| └ gatewayTotal | 整数 | 用户网关的总次数 |
| └ gatewayTtl | String | 用户网关TTL |
| └ gatewayAddress | String | 用户网关 |
| └ gatewayAvgDelay | String | 用户网关平均延时 |
| └ gatewayAvgVariance | String | 用户网关平均方差 |
| └ gatewayLoss | 整数 | 用户网关的实际丢包数量 |
| └ gateway2Good | 整数 | 接入网关good的总次数 |
| └ gateway2Normal | 整数 | 接入网关normal的总次数 |
| └ gateway2Bad | 整数 | 接入网关bad的总次数 |
| └ gateway2Poor | 整数 | 接入网关poor的总次数 |
| └ gateway2NotReach | 整数 | 接入网关notReach的总次数 |
| └ gateway2Total | 整数 | 接入网关的总次数 |
| └ gateway2Ttl | String | 接入网关TTL |
| └ gateway2Address | String | 接入网关 |
| └ gateway2AvgDelay | String| 接入网关平均延时 |
| └ gateway2AvgVariance | String | 接入网关平均方差 |
| └ gateway2Loss | String | 接入网关的实际丢包数量 |
| └ cpuLow | 整数 | low的总次数 |
| └ cpuMedium |整数  | medium的总次数 |
| └ cpuHigh | 整数 | high的总次数 |
| └ cpuBusy | 整数 | busy的总次数 |
| └ cpuTotal |整数  | cpu的总次数 |

#### 实例


```json
{
    "ClassID": 290274,
    "ActionTime": 1521547386,
    "UID": 1001920,
    "CourseID": 122982,
    "TimeStamp": 1521547387,
    "Cmd": "Net",
    "_id": "5ab0f87aa3251e6e49b9e892",
    "SID": 1001920,
    "Data": {
        "avgVariance": "35.890",
        "reportTime": "1720082915",
        "gatewayAvgVariance": "38.284",
        "gateway2Poor": 0,
        "gatewayNormal": 0,
        "total": 592,
        "mediaPort": 8080,
        "gateway2AvgDelay": "16.240",
        "udpTotalPkts": 92,
        "localIP": "123.24.205.*",
        "avgDelay": "68.258",
        "gatewayAvgDelay": "6.794",
        "poor": 10,
        "good": 560,
        "notReach": 3,
        "gateway2AvgVariance": "74.474",
        "normal": 19,
        "gatewayTtl": 1,
        "gatewayTotal": 300,
        "gateway2Loss": 6,
        "gateway2Good": 293,
        "gateway2NotReach": 6,
        "loss": 4,
        "gateway2Ttl": 3,
        "gateway2Total": 299,
        "gatewayLoss": 0,
        "gatewayNotReach": 0,
        "gateway2Address": "123.25.27.93",
        "socket": "UDP",
        "gateway2Bad": 0,
        "gatewayPoor": 0,
        "bad": 0,
        "gateway2Normal": 0,
        "gatewayGood": 300,
        "gatewayBad": 0,
        "mediaDuration": 300,
        "gatewayAddress": "10.0.30.1",
        "cpuHigh": 0,
        "cpuMedium": 0,
        "cpuBusy": 0,
        "cpuLow": 299,
        "cpuTotal": 299
    }
}


```


#### 实例


```json

{
    "ClassID": 290274,
    "ActionTime": 1521547386,
    "UID": 1001920,
    "CourseID": 122982,
    "TimeStamp": 1521547387,
    "Cmd": "Net",
    "_id": "5ab0f87aa3251e6e49b9e892",
    "SID": 1001920,
    "Data": {
        "poor": 0,
        "bad": 0,
        "total": 331,
        "good": 331,
        "normal": 0,
        "notReach": 0,
        "cpuLow": 0,
        "cpuMedium": 10,
        "cpuHigh": 31,
        "cpuBusy": 3,
        "cpuTotal": 44,
        "localIP": "1.2.3.*"
    }
}

```


## 教室内设备检测报告

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|类型为字符串，'Check'|
|Data|对象|设备检测结果详细|
| └ OperatingSystem | string  |	操作系统|
| └ CPU | string | 用户 CPU|
| └ NetworkDelay | string  | 网络延迟|
| └ FrameLoss  | string | 丢包率
| └ MicrophoneArbitrary | number | 麦克风状态，1为已安装，2为disable或不存在|
| └ HeadphoneArbitrary | number | 耳机状态，1为已安装，2为disable或不存在|
| └ CameraArbitrary | number	| 摄像头状态，1为已安装，2为disable或不存在|
| └ EEO_VIDEO_DEVICE_NAME | string	| 选用摄像头设备名称
| └ EEO_AUDIO_DEVICE_NAME | string	| 选用麦克风设备名称
| └ EEO_AUDIO_OUTPUT_NAME | string	| 选用耳机设备名称
| └ EEO_DEVICE_LIST | 对象 | 硬件列表
| 　 └ camera | array | 所有摄像头设备名称列表
| 　 └ micphone | array | 所有麦克风设备名称列表
| 　 └ speaker | array	| 所有扬声器设备名称列表
| └ MicrophoneImpersonal | number | 程序检测的麦克风状态（1正常，2不正常或未收到声音数据）,移动端此字段无效
| └ CameraImpersonal | number | 程序检测的摄像头状态（1正常，2不正常或未收到摄像头数据）,移动端此字段无效
| └ HeadphoneImpersonal | number | 无法对此设备进行程序检测,移动端此字段无效
| └ MicrophoneAttachment  | string | 麦克风附件
| └ HeadphoneAttachment   | string	| 耳机附件 （暂时为空）
| └ CameraAttachment   | string	| 摄像头附件
| └ ClassInVersion  | string | 客户端版本
| └ Mac   | string	| MAC 地址
| └ addTime   | string	| 自检时间（时间戳）
| └ InfoSource   | number	| 上传自检时机：1，设备初始化；2，设备选择，3，自检完成；4，设备插拔；5，设置完成；7，自检中断；
| └ DeviceType   | number   | 设备类别：0，未知；1，Windows；2，iPhone；3，iPad；4，Android Phone；5，Android Pad；6，Mac；
| └ ClientIP     | string   | 用户IP(最后一位隐藏)



#### 实例


```json
{
    "ClassID": 290274,
    "ActionTime": 1521547218,
    "UID": 1001920,
    "CourseID": 122982,
    "TimeStamp": 1521547219,
    "Cmd": "Check",
    "_id": "5ab0f7d2a3251e6e49b9e88b",
    "SID": 1001920,
    "SafeKey": "7e0a589d8fd68a82a523ac86c95c9d1d",
    "Data": {
        "MicrophoneArbitrary": null,
        "ClassInVersion": "2.1.1.60",
        "EEO_AUDIO_OUTPUT_NAME": "\u626c\u58f0\u5668 (Realtek High Definition Au",
        "FrameLoss": "",
        "EEO_AUDIO_DEVICE_NAME": "\u9ea6\u514b\u98ce (HD Webcam C270)",
        "CameraImpersonal": 0,
        "addTime": 1521547218,
        "CPU": "Intel(R) Core(TM) i5-4570 CPU @ 3.20GHz",
        "OperatingSystem": "Windows 10 (1709)",
        "Mac": "00:15:5D:33:74:C4",
        "CameraArbitrary": null,
        "EEO_VIDEO_DEVICE_NAME": "Logitech HD Webcam C270",
        "ServerName": "EEO-A0134 (Auto)",
        "HeadphoneAttachment": "",
        "ClientIP": "10.0.1.*",
        "MicrophoneAttachment": "https://root_url/upload/autocheck/",
        "EEO_DEVICE_LIST": "{\"camera\": [\"Logitech HD Webcam C270\"], \"micphone\": [\"HD Webcam C270\"], \"speaker\": [\"LG HDR 4K\"]}",
        "MicrophoneImpersonal": 0,
        "CameraAttachment": "",
        "HeadphoneArbitrary": null,
        "InfoSource": 3,
        "NetworkDelay": ""
    }
}

```

## 教室内老师和学生求助
上课过程中，老师端和学生端（学生端的求助，需要在机构管理后台的 **教室配置** 里勾选 **学生求助设置**），都能够向eeo.cn发起求助信息

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|'HelpInfo'|
|ClassID|整数|求助课节ID|
|Data|对象|求助内容|
| └ UID | 整数  |	发起求助用户ID|
| └ Message | string | 求助信息|
| └ UserList | 整数数组 | 求助所包含的用户ID|



#### 实例



```json

{
	"SID": 1000958,
	"ClassID": 301417,
	"Data": {
		"UID": 1001558,
		"Message": "Speaker is abnormal. The user can't hear sound",
		"UserList": [1001558, 123456]
	},
	"Cmd": "HelpInfo"
}

```


## 延长课节时长

课节结束前  8 - 3 分钟内，如果老师延长课节时长，将收到此推送消息。<br>
注：只有当机构的 **教室设置** 勾选了课堂延时设置（允许教师延长课节时长），老师才能延长课节时长。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|'ClassLen'|
|StartTime|Int32|课节开始时间，unix时间戳|
|PrelectTimeLength|Int32|新课节时长，单位秒|
|CloseClassDelay|Int32|拖堂延时，单位秒|



### 实例



```json

{
	"SID": 1000958,
	"StartTime": 1568862650,
	"PrelectTimeLength": 1200,
	"CloseClassDelay": 1200,
	"Cmd": "ClassLen"
}

```


## 启动录课详情

录课模式等信息，每次录课启动时推送


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|类型为字符串，'LiveDetail'|
|Data|对象|录课详细信息|
| └ Audio mode | 字符串  | 录制声音模式:软件声音为'ClassIn Audio'，系统声音为'System Audio'|
| └ HighBitRate | 字符串  | 录制码率:高码率'High'，普通码率为'Standard'|
| └ IP | 字符串 | 推流IP:可能为域名'livepush.eeo.cn'或具体IP地址|
| └ Micphone is recorded | 字符串 | 是否录麦克风的声音: 'Yes'或'No' |
| └ Video Scope | 字符串 | 录制目标为桌面'Desktop'或教室窗口'Classroom' |
| └ Video Size | 字符串 | 录制大小:高清'HD(1280\*720)'或'FHD(1920\*1080)' |


### 实例

```json

{
	"SID": 1001920,
	"Data": {
		"Audio mode": "ClassIn Audio",
		"HighBitRate": "Standard",
		"IP": "livepush.eeo.cn",
		"Micphone is recorded": "Yes",
		"Video Scope": "Desktop",
		"Video Size": "HD(1280*720)"
	},
	"ClassID": 392429,
	"Cmd": "LiveDetail"
}

```

## 教室大黑板板书图片

每次客户端清空大黑板和课节结束时，系统会把大黑板上的板书数据，转换成为图片并实时推送


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|'EdbImg'|
|Url|String|图片地址链接|
|GroupId|整数| 板书所属分组Id，GroupId=0表示为主教室。当本课节没有使用分组功能，则所有的GroupId为0 |


### 实例

```json

{
	"SID": 1001920,
	"ClassID": 393472,
	"Url": "http://www.eeo.cn/20200819/20200819_393472_0_bb_151823_853.jpg",
	"GroupId": 0,
	"Cmd": "EdbImg"
}

```

## 直播页面用户登录

课节直播状态下登录会产生消息并实时推送，回放状态登录不会产生消息

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
|Cmd|String|'LiveWebLogin'|
|ClassID|整数|直播课节ID|
|Data|对象|内容|
| └ Telephone | String  | 登录用户电话号码或邮箱，以实际登录账号为准 |
| └ LoginTime | 整数 | Unix时间戳 |
| └ Nickname | String | 登录用户昵称 |




#### 实例
```json

{
	"SID": 1000958,
	"ClassID": 301417,
	"Data": {
		"Telephone": "10015584345",
		"LoginTime": 1521547219,
		"Nickname": "XiaoMing"
	},
	"Cmd": "LiveWebLogin"
}

```

## 直播预约
用户预约直播的数据，推送时机：用户提交预约后实时推送。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'LiveReserve' |
|ClassID|整数|直播课节ID|
|Data|对象|内容|
| └ Telephone | String  | 预约观看直播的手机号码或邮箱，以实际登录账号为准 |
| └ ReserveTime | 整数 | 用户提交预约的时间，Unix时间戳 |

#### 实例
```json
{
    "SID": 100088,
    "ClassID": 10086,
    "Cmd": "LiveReserve",
    "Data": {
        "Telephone": "15201114553",
        "ReserveTime": 1625108250
    }
}
```

## 网页直播观看明细
用户观看直播的明细数据，推送时机：用户关闭直播后实时推送。<br>
**请注意**：在用户侧的网络不好、刷新页面、手机休眠等情况下，系统会推送多条InTime相同但LookTime不一样的数据。您在处理数据时，应该使用(Cmd,ClassID,Telephone,Intime)为key，只存储LookTime为最大的那条记录即可。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'LiveDataDetail' |
|ClassID|整数|直播课节ID|
|Data|对象|内容|
| └ Telephone | String  | 用户手机号码或邮箱，以实际登录账号为准，若为游客则为 'yk_' 开头的字符串 |
| └ Nickname | String  | 用户昵称 |
| └ Intime | 整数 | 用户进入观看直播的时间，Unix时间戳 |
| └ LookTime | 整数 | 用户观看时长，单位为秒 |
| └ IP | String  | 用户IP地址 |
| └ ClientType | 整数 | 用户观看直播的终端类型：1-PC端浏览器，2-移动端浏览器，3-小程序 |

#### 实例
```json
{
    "SID": 100088,
    "ClassID": 10086,
    "Cmd": "LiveDataDetail",
    "Data": {
        "Telephone": "15201114553",
        "Nickname": "husky2021",
        "Intime": 1625108250,
        "LookTime": 60,
        "Ip": "127.0.0.1",
        "ClientType": 1
    }
}
```

## 直播点赞
用户观看直播的点赞数据，推送时机：用户点赞后实时推送。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'LiveLike' | 
|ClassID|整数|直播课节ID|
|Data|对象|内容|
| └ Telephone | String  | 用户手机号码或邮箱，以实际登录账号为准；若为游客则为 'yk_' 开头的字符串 |
| └ Time | 整数 | 用户点赞的时间，Unix时间戳 |

#### 实例
```json
{
    "SID": 100088,
    "ClassID": 10086,
    "Cmd": "LiveLike",
    "Data": {
        "Telephone": "15201114553",
        "Time": 1625108250
    }
}
```

## 直播商品点击明细
用户直播过程中点击商品的明细数据，推送时机：用户点击商品后实时推送。

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| Cmd | String | 'LiveGoodsClickDetail' |
|ClassID|整数|直播课节ID|
|Data|对象|内容|
| └ Telephone | String  | 用户手机号码或邮箱，以实际登录账号为准，若为游客则为 'yk_' 开头的字符串 |
| └ Nickname | String  | 用户昵称 |
| └ Time | 整数 | 用户点击商品的时间，Unix时间戳 |
| └ GoodNum | 整数 | 商品编号 |
| └ GoodName | String  | 商品名称 |


#### 实例
```json
{
    "SID": 100088,
    "ClassID": 10086,
    "Cmd": "LiveGoodsClickDetail",
    "Data": {
        "Telephone": "15201114553",
        "Nickname": "husky2021",
        "Time": 1625108250,
        "GoodNum": 60,
        "GoodName": "三字经"
    }
}
```

## 直播聊天消息
用户观看网页直播过程中发送的聊天消息，推送时机：用户发送消息后实时推送。

| 参数名      | 类型   | 说明 |
|----------- | ------ | ------------------------------------------------------------ |
|Cmd         | String | LiveChatMsgDetail                                            |
|ClassID     | 整数   | 直播课节ID                                                   |
|Data        | 对象   |                                                              |
| └ Account  | String | 用户手机号码或邮箱，以实际登录账号为准，若为游客则为 'yk_' 开头的字符串 |
| └ Nickname  | String | 用户昵称                                                     |
| └ TimeStamp | 整数   | 消息发送时间戳                                               |
| └ IP        | String | 用户IP地址                                                   |
| └ MsgDetail | 对象   |                                                              |
|&nbsp;&nbsp; └ msg       | String | 消息文本内容或图片下载地址                                  |
|&nbsp;&nbsp; └ type      | 整数   | type:1-文本，2-图片； type=2时，msg是图片url              |
|&nbsp;&nbsp; └ ext       | 对象   | 扩展信息，可暂时忽略 {\"role\":99,\"roleid\":\"AfJ46f24h\",\"messageID\":\"AfJ46f24h-1739263873\",\"mark\":\"\"} |


#### 实例
```json
{
    "SID": 100086,
    "ClassID": 4185167,
    "ActionTime": 1740042947,
    "SafeKey": "33cc7cfb43315a0057f828f15b70937e",
    "Cmd": "LiveChatMsgDetail",
    "_id": "67b6f2c3ab842f6ad5f86720",
    "Data": {
        "MsgDetail": {
            "msg": "讲的很好",
            "ext": {
                "roleid": "BHH8Ddsm3",
                "messageID": "BHH8Ddsm3-1740042946",
                "role": 1,
                "mark": ""
            },
            "type": 1
        },
        "Account": "12345678901",
        "Nickname": "张三",
        "TimeStamp": 1740042947,
        "IP": "101.251.219.198"
    }
}
```
