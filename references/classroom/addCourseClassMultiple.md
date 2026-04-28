# 创建课节(多个)

**![!deprecated](../../img/waring.png)通知：此接口为原课节类接口，2025年5月26日之后将不再更新(但是可以继续使用原功能。)，建议使用LMS活动类接口：[创建课堂活动](LMS/createClassroom.md)**

创建课节（多个），**建议一次性创建课节不超过30个**，同时，单个课程下课节总数存在限制。超过限制会报错，错误码121601070。           
批量创建课节，需要 SID、safekey、timeStamp、课程 ID、课节名称、上下课时间、老师账号、老师姓名、云盘目录 ID、学生上台数、是否开启第二摄像头、教学模式，是否自动上台，录课、直播、回放、唯一标识、课节简介、老师UID、联席教师UID、网页直播回放、允许未登录用户参与直播聊天和点赞等。返回创建的课节 ID、课节名称、创建课节的错误码和错误说明。      
**注意：目前仅支持 1v1 或者 1v6 高清、全高清，所以选择高清（即isHd等于1或者2）时，上台人数seatNum只能传1或者6 。当选择双摄模式时，即启用第二摄像头（即副摄像头，isDc等于3）时，只能选择1V1全高清（即seatNum只能传1。如果seatNum不等于1的话，则会返回错误码808）。** <br>
用户可以传递自定义字段customColumn，接口会原样将参数返回。不传递则不会返回。<br>

机构传入唯一标识courseUniqueIdentity后，该接口会校验机构下所有已创建课节中是否有此唯一标识，如果有，则返回之前创建成功的课节 ID和more_data 。如果没有，则正常执行。<br>
[删除课节](../classroom/delCourseClass.md)时，唯一标识courseUniqueIdentity也会被删除，如果您创建该课节时传了唯一标识courseUniqueIdentity的话。

注意事项：
- 如果课节设置录课（没有设置直播），则more_data返回 课节直播播放器地址 ，拉流地址为空；
- 如果课节设置录播、直播，则会给该课节绑定3个拉流地址（RTMP，HLS ，FLV），more_data返回课节直播播放器地址和拉流地址（不论该课节后续是否取消直播，这3个地址仍然存在且与该课节绑定）；
- 当课节没有设置录课，则more_data里的课节直播播放器地址和拉流地址均为空。
- 如果要设置录制现场，则必须设置录课，否则无法开启录制现场。

附拉流地址优缺点对比，以下对比仅供参考。

|     | RTMP | HLS | FLV（HTTP-FLV） |
| --- | ---- | --- | --- |
| 全称 | Real Time Message Protocol | HTTP Liveing Streaming |  | 
| 协议 | TCP 长连接 | HTTP 短连接 | HTTP 长连接 |
| 原理 | 每个时刻的数据收到后立刻转发 | | |
| 延时 | 1-3s | 5-20s(依切片情况) | 1-3s |
| Web 支持 | H5 中需要使用插件 | 支持 H5 | H5 中需要使用插件 |
| 其他 | 跨平台支持较差，需要 Flash 技术支持 | 播放时需要多次请求，对于网络质量要求高 | 需要 Flash 技术支持，不支持多音频流、多视频流，不便于 seek（即拖进度条） |

在返回的课节直播播放器页面我们植入了聊天室功能。为了方便您搜集潜在客户信息，所有用户需要填写手机号登陆后才可以聊天，如下图。当然，为了您更便捷的使用此功能，我们提供了您机构下所有学生免登陆的操作，请参考下方的 [直播播放器中聊天室免二次登录](#直播播放器中聊天室免二次登录)。

![课节直播登录](../../img/classwebcast.jpg)

## 直播播放器中聊天室免二次登录
- 当您通过本接口获得播放器链接之后
  + 例：`https://www.eeo.cn/live.php?lessonKey=1ca102d29e61175f`
  + 您需要增加 account、nickname、checkCode 拼接在 `https://live.eeo.cn/live_partner.html?lessonKey=00d1c98a91c52568` 地址后边。 **注意：这个免二次登录地址与直播播放器地址不是同一个地址**
- 具体参数及规则如下
  + 具体参数有 secret、lessonKey、account、nickname、checkCode
  + secret 为SECRET，在 EEO.cn API 对接密钥处可获得
  + 从直播器地址中可以获得 lessonKey
  + account 为学生账号(长度小于32个字符)，nickname 为学生昵称(长度小于24个字符)
  + checkCode = md5(secret+lessonKey+account+nickname)
- URL 拼接示例
  + `https://live.eeo.cn/live_partner.html?lessonKey=00d1c98a91c52568&account=13700000000&nickname=classin&checkCode=d8c57caf088529b4ddd15b0f694d847b`

## URL

`https://root_url/partner/api/course.api.php?action=addCourseClassMultiple`

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
| courseId |	是 |	无 |	课程 ID |	无
| classJson | 是 | 无 | 课节信息数组 | 数组长度不大于50个，否则后面的数据会被截断造成排课失败
| └ 课节信息 | 是 | 无 | 需要创建的课节信息 | 无
| 　 └ className |	是 |	1-50个字，不区分中英文，超过50字会自动截取为50字 |	课节名称 |	无 |
| 　 └ beginTime |	是 |	开课时间须在3年以内 |	上课时间 |	Unix Epoch 时间戳（秒单位）
| 　 └ endTime |	是 |	无 |	下课时间 |	Unix Epoch 时间戳（秒单位）
| 　 └ teacherUid | 是 | 无 | 教师 UID | 注册用户接口返回的用户 UID
| 　 └ folderId |	否 |	默认为该课程的 folderId |	云盘目录 ID |	无
| 　 └ teachMode | 否 |  默认为1，不传使用默认值，传错报100错误 | 教学模式<br> 1=在线教室，此时默认显示座位席且学生进入教室自动上台<br>2=智慧教室，此时默认关闭座位席且学生进入教室自动在台下 | 当teachMode=2时，isAutoOnstage会始终被设置为1（也就是说，teachMode=2时，API会忽略传参isAutoOnstage的值） |
| 　 └ isAutoOnstage | 否 | 0=自动，1=不自动，默认为0，所有非1的数字,都会当成0处理 | 学生进入教室是否自动上台 | 无 |
| 　 └ seatNum |	否 |	默认为6，最大上限值调整为12 | 学生上台数<br>传0时为1V0课节（即台上只显示老师） |	无
| 　 └ isHd | 否 | 0=非高清，1=高清，2=全高清，默认为0，除了1和2，所有非0的数字,都会当成0处理 | 是否高清 | 目前仅支持 1V1 或 1V6 高清、全高清 |
| 　 └ isDc | 否 | 默认为0，不传或传错，都使用默认值 | 双摄模式，是否开启副摄像头，0=不开启，3=开启全高清副摄像头 | 如果isDc等于3，课节的台上人数不是1v1（即seatNum不等于1），则返回808错误<br>如果isDc等于3，且seatNum等于1的话，则isHd一定会被设置为2（即这种情况API会忽略isHd的传参值） |
|　  └ assistantUid | 否 | 与assistantUids参数不能同时传。  | 联席教师 UID | 注册用户接口返回的用户 UID |
|　  └ assistantUids | 否 | 与assistantUid 参数不能同时传。此参数为整型数组，  | 联席教师 UID 数组| 注册用户接口返回的用户 UID  |
| 　 └ customColumn | 否 | 1-50字符，超过会自动截取为50字 | 用户自定义标识 | 不为空则原样返回，为空则不返回该字段
| 　 └ record |	否 |	默认为 0 ,所有非 1 的数字,都会当成 0 处理 |	录课(0 关闭，1 开启) |	若需要直播或者回放，则必须选择录课，否则无法无法开启直播、回放 |
| 　 └ recordScene |	否 |	默认为 0 ,所有非 1 的数字,都会当成 0 处理 |	录制现场(0 关闭，1 开启) |	打开录制现场，classin会将授课老师摄像头场景录制下来，可用于网页直播或者网页回放。<br>若需要现录制现场，则必须先打开录课，否则无法开启录制现场|
| 　 └ live	| 否 |	默认为 0 ,所有非 1 的数字,都会当成 0 处理 |	直播(0 关闭，1 开启) |	若需要直播，则必须开启录课 |
| 　 └ replay |	否 |	默认为 0 ,所有非 1 的数字,都会当成 0 处理 |	回放(0 关闭，1 开启) |	若需要回放，则必须开启录课 |
| 　 └ watchByLogin  | 否 | 默认为 0 ,不传或传错，都使用默认值 | 只允许登录ClassIn账号后才可观看，未登录不可观看，0=未开启，1=开启 | 未开启录课、直播、回放中的两项及以上，此参数设置了也用不到 |
| 　 └ allowUnloggedChat  | 否 | 默认为 1 ,不传或传错，都使用默认值 | 允许未登录用户参与直播聊天和点赞，0=不允许，1=允许 | 未开启录课和直播，此参数设置了也用不到 |
| 　 └ courseUniqueIdentity | 否 | 例如：45s8d5a6asaa1ssf（1-32 位字符，不符合规则的值接口会返回 100 错误） | 唯一标识 | 机构可传唯一标识，传入此值后，我们会检验机构下所有已创建课节中是否有该唯一标识 |
| 　 └ classIntroduce | 否 | 0-1000字，不区分中英文，超过1000字会自动截取为1000字。 | 课节简介 | 无 |
| 　 └ omoStationBroadcast | 否   | 默认0，不传或者传错都用默认值   | 是否开启OMO站播，0-关闭，1-开启                      |  需要机构打开这个增值服务才能生效，否则会报错    |  
| └ ...... |	否 |	无 |	需要创建的课节信息 |	无

## 响应参数

| 参数名 | 类型 |	示例值 |	含义 |
| ---- |---- |----| ----|
| data | array | []	|	返回 Data 信息数组 |
| 　 └ data | number |	1369235 |	添加的课节 ID |
| 　 └ className | string |	测试课节-1 |	添加的课节名称 |
| 　 └ customColumn | string |	123 |	用户自定义标识| 
|    └ more_data | array | [] | 返回 Data 信息数组 |
|     　└ live_url | string | https://www.eeo.cn/live.php?lessonKey=0fdc12bc3558164d | 课节直播播放器地址 |
|     　└ live_info | JsonObject |  | 返回 Data 信息 |
|     　 　└ RTMP | string | "rtmp://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96? txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 直播拉流地址 |
|     　 　└ HLS | string | "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.m3u8?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 直播拉流地址 |
|     　 　└ FLV | string | "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.flv?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 直播拉流地址 |
| 　 └ errno	| number |	1 |	该添加课节的错误代码 |
| 　 └ error | string |	"程序正常执行" |	该添加课节的错误详情 |
| error_info | 	object |	|	返回信息对象 |
| 　 └ errno |	number |	1	 | 错误代码 |
| 　 └ error |	string |	"程序正常执行" |	错误详情 |


## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=addCourseClassMultiple HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=5458edceccc78c6698de624e94364285&timeStamp=1493026245&courseId=469383&classJson=[{"className":"Chinese Test-1","beginTime":1493026245,"endTime":1493036245,"teacherUid":"23692341090","folderId":714013,"seatNum":4,"customColumn":123,"isAutoOnstage":0,"watchByLogin":0,"allowUnloggedChat":1",isHd":0,"courseUniqueIdentity":457354},{"className":"Chinses Test-2","beginTime":1493026245,"endTime":1493036245,"teacherUid":"23692341090","folderId":714013,"seatNum":6,"customColumn":124,"isAutoOnstage":0,,"watchByLogin":0,"allowUnloggedChat":1"isHd":0,"courseUniqueIdentity":457354,"classIntroduce ":"ClassIn,真正的在线教室"}]
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
        -d "SID=1234567" \
        -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
        -d "timeStamp=1484719085" \
        -d "courseId=442447" \
        -d 'classJson= \
          [ \
            { \
              "className":"测试课节-1", \
              "beginTime":1493029525, \
              "endTime":1493039525, \
              "teacherUid":"1001001",\
              "seatNum":4,\
              "isDc":0,\
              "record":1,\
              "recordScene":1,\
              "live":0,\
              "replay":1,\
              "assistantUids=['1001002']",\
              "isAutoOnstage":"0", \
              "isHd":"0", \
              "courseUniqueIdentity":123457 \
              "classIntroduce":"ClassIn,真正的在线教室" \
              "watchByLogin":0 \
              "allowUnloggedChat":1" \
            },\
            {\
              "className":"测试课节-2",\
              "beginTime":1493029525,\
              "endTime":1493039525,\
              "teacherUid":"1001002",\
              "seatNum":4,\
              "record":1,\
              "recordScene":1,\
              "live":1,\
              "replay":1,\
              "assistantUids=['1001001']",\
              "isAutoOnstage":"0", \
              "isHd":"0",\
              "courseUniqueIdentity":1234575 \
              "classIntroduce":"ClassIn,真正的在线教室" \
              "watchByLogin":0 \
              "allowUnloggedChat":1" \
            }\
          ]' \
       "https://root_url/partner/api/course.api.php?action=addCourseClassMultiple"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": [
    {
      "data": 23634,
      "className": "测试课节-1",
      "customColumn": "123",
      "more_data": {
        "live_url": "https://www.eeo.cn/live.php?lessonKey=0fdc12bc3558164d",
        "live_info": {
            "RTMP": "rtmp://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
            "HLS": "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.m3u8?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
            "FLV": "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.flv?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
          }
        },
      "errno": 1,
      "error": "程序正常执行"
    },
    {
      "data": 23635,
      "className": "测试课节-2",
      "customColumn": "124",
      "more_data": {
        "live_url": "https://www.eeo.cn/live.php?lessonKey=0fdc12bc3558164d",
        "live_info": {
            "RTMP": "rtmp://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
            "HLS": "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.m3u8?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
            "FLV": "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.flv?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
          }
        },
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
| 1   | 表示成功执行 |
| 100	| 表示参数不全或错误|
| 102	| 表示无权限（安全验证没通过）|
| 104 |	表示操作失败（未知错误）|
| 114	| 表示服务器异常|
| 119 |	表示结束时间须晚于开课时间|
| 120 |	表示开课时间至少一分钟以后|
| 122 | 表示老师账号格式不正确|
| 133 | 表示已经存在（传过来的 classJson 中唯一标识有重复）|
| 136 |	表示机构下面没有该老师，请在机构下添加该老师|
| 144 |	表示机构下无此课程|
| 147 |	表示没有此课程信息|
| 149 |	表示课程已删除|
| 153 |	表示课程已过期|
| 155	| 表示数据数组不可为空|
| 160 |	表示机构下无此云盘目录|
| 161 | 表示单课创建失败|
| 165 |	表示单节课不能少于15分钟且不能超过24小时|
| 172 |	表示课程下的学生不能添加为老师|
| 173 |	表示课程下的旁听不能添加为老师|
| 220 | 表示客户端添加课节失败|
| 259 |	表示上台人数设置超出最大限制|
| 268 | 表示课节开始时间超出允许范围（开课时间须在3年以内）|
| 280 |	表示课节创建成功，录课参数设置错误，录课开启失败|
| 281 |	表示课节创建成功，视频服务有问题，录课开启失败|
| 318 | 表示联席教师不是本机构老师|
| 319 | 表示课程下的学生不能添加为联席教师|
| 320 | 表示课程下的旁听不能添加为联席教师|
| 322 | 课节老师不能添加为联席教师|
| 324 | 表示课节老师加入教师列表失败|
| 326 | 表示课节联席教师加入教师列表失败|
| 330 | 表示联席教师账号格式不正确(2022年4月去除此错误码)|
| 368	| 表示当前学生上台数不支持高清|
| 369 | 该课程/课节类型暂不支持该操作|
| 387 | 表示老师已被停用|
| 388 | 表示联席教师已被停用|
| 398 | 表示数据已经存在（唯一标识已存在）|
| 400 | 表示请求数据不合法|
| 454 | 课节起止时间与系统维护时间有重叠|
| 460 | 表示课程或课节正在被其他请求创建（并发创建会遇到）|
| 800 | 表示老师被停用中|
| 804 | 表示联席教师被停用中|
| 824 | 表示课节添加成功，课节简介设置失败|
| 808 | 表示该设置不支持双摄|
| 884 | 老师帐号已注销|
| 885 | 联席教师帐号已注销|
|21316| 联席教师数据有重复|
|21317| 联席教师数量超出限制|
| 121601001 | 存在当前版本不支持的设置项|
| 121601002 | 操作成功，\[在线教室\]资源已超出用量，为防止业务受影响，请尽快联系客户经理|
| 121601003 | 您当月累计创建课节已达当月上限，无法继续创建，升级账号获取更多权益|
| 121601004 | 您当月累计创建课节已达当月上限，无法继续创建|
| 121601005 | 不支持设网页直播|
| 121601006 | 不支持设置录制现场|
| 121601007 | 台上人数参数错误|
| 121601008 | 不支持设置联席教师|
| 121601009 | 不支持设置网页回放|
| 121601010 | 不支持设置录课|
| 121601011 | 不支持设置双摄模式|
| 121601012 | 清晰度超出限制|
| 121601070  | 单个课程下课节数量超过限制 |
| 121604007  | 不支持设置OMO站播  |
