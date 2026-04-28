# 修改课节信息

**![!deprecated](../../img/waring.png)通知：此接口为原课节类接口，2025年5月26日之后可以继续使用，但不再更新，建议使用LMS活动类接口：[编辑课堂活动](LMS/updateClassroom.md)**


修改课节信息，需要提供 SID，safekey，timeStamp，课程 ID，课节名称，上下课时间，老师账号，老师姓名，云盘目录 ID，录课，直播，回放，联席教师、教学模式，是否自动上台，老师UID、联席教师UID、网页直播回放、允许未登录用户参与直播聊天和点赞等。其中 SID、safeKey、timeStamp、courseId、classId为必填项，其他参数需要修改那个就填写那个（修改录课、直播、回放三个参数任意一个，其他两个参数则必填。否则不生效）。修改录制现场时，录课、直播和回放三个参数必填。返回执行后的成功说明，修改上台人数需要调用 [修改课节上台学生数](modifyClassSeatNum.md)。

注意事项：

- 开课前20分钟内不能修改课节名称、上课时间、云盘资源、台上人数、是否自动上台、教学模式。
- 如果上课中修改课节老师，则正在上课的老师会退出教室。
- 如果课节设置录课（没有设置直播），则more_data返回课节直播播放器地址，拉流地址为空。
- 如果课节设置录课、直播，则more_data返回课节直播播放器地址和拉流地址。
- 如果编辑或者设置其他参数，没有改变录课/直播/回访任何参数，则按照创建时返回more_data。
- 开课前如已设置联席教师，开课后可更换或删除联席教师；开课前如未设置联席教师，开课后可添加联席教师。
- **编辑课节更多参数规则可参考 [参数规则](../appendix/rules.md)。**

## URL

`https://root_url/partner/api/course.api.php?action=editCourseClass`

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
| classId | 是 | 无 | 课节 ID | 无|
| className |	否 |	1-50个字，不区分中英文，超过会自动截取为50字 |	课节名称 |	无|
| beginTime |	否 |	开课时间须在3年以内 |	上课时间 |	Unix Epoch 时间戳（秒单位）|
| endTime |	否 |	若填写了 beginTime,则必须填写 endTime |	下课时间 |	Unix Epoch 时间戳（秒单位）|
| teacherUid | 否 | 无 | 教师 UID | 注册用户接口返回的用户 UID|
| folderId |	否 |不传默认为课程授权云盘ID |	云盘目录 ID |	无|
| record |	否 |	默认为 0 ,所有非 1 的数字,都会当成 0 处理 |	录课(0 关闭，1 开启) |	无|
| recordScene |	否 |	默认为 0 ,所有非 1 的数字,都会当成 0 处理 |	录制现场(0 关闭，1 开启) |	无|
| live	| 否 |	默认为 0 ,所有非 1 的数字,都会当成 0 处理 |	直播(0 关闭，1 开启) |	无|
| replay |	否 |	默认为 0 ,所有非 1 的数字,都会当成 0 处理 |	回放(0 关闭，1 开启) |	无|
| assistantUid | 否 | 与assistantUids参数不能同时传。此参数传空时为删除助教。 | 联席教师 UID | 注册用户接口返回的用户 UID |
| assistantUids | 否 | 与assistantUid 参数不能同时传。此参数为整型数组，如果传空数组为删除助教。 | 联席教师 UID 数组[1001002,1001003]| 注册用户接口返回的用户 UID  |
| teachMode | 否 | 不传不修改，传了则会检查传的值是否正确，不正确报100错误 | 教学模式，1=在线教室，2=智慧教室 | 当teachMode=2时，isAutoOnstage会始终被设置为1（也就是说，teachMode=2时，API会忽略传参isAutoOnstage的值） |
| isAutoOnstage | 否 | 0=自动，1=不自动，可不填，不填则不修改，所有非1的数字,都会当成0处理 | 学生进入教室时是否自动上台 | 无 |
| classIntroduce | 否 | 0-1000字，不区分中英文，超过1000会自动截取为1000字 | 课节简介 | 无 |
| watchByLogin  | 否 | 不传或传错，都不修改 | 只允许登录ClassIn账号后才可观看，未登录不可观看，0=未开启，1=开启 | 未开启录课、直播、回放中的两项及以上，此参数设置了也用不到 |
| allowUnloggedChat  | 否 | 不传或传错，都不修改 | 允许未登录用户参与直播聊天和点赞，0=不允许，1=允许 | 未开启录课和直播，此参数设置了也用不到 |
| omoStationBroadcast | 否   | 默认0，不传或者传错都用默认值   | 是否开启OMO站播，0-关闭，1-开启                      |  需要机构打开这个增值服务才能生效，否则会报错    | 

## 响应参数

| 参数名 | 类型 |	示例值 |	含义|
| ---- |---- |----| ----|
| more_data | array | [] | 返回 Data 信息数组
|　└ live_url | string | https://www.eeo.cn/live.php?lessonKey=0fdc12bc3558164d | 课节直播播放器地址|
|　└ live_info | array | [] | 返回 Data 信息数组|
|　　└ RTMP | string | "rtmp://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 直播拉流地址|
|　　└ HLS | string | "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.m3u8?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 直播拉流地址|
|　　└ FLV | string | "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.flv?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 直播拉流地址|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

- HTTP 请求

```http
POST /partner/api/course.api.php?action=editCourseClass HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=58ce17711abea665f40f67d550ce96fb&timeStamp=1493364941&courseId=490583&classId=1395039&className=chinese&beginTime=1493434330&endTime=1493444330&teacherUid=1001001&folderId=&record=1&live=1&replay=1&watchByLogin=0&allowUnloggedChat=1
```

- Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
     -d "SID=1234567" \
     -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
     -d "timeStamp=1484719085" \
     -d "courseId=442447" \
     -d "classId=23644"  \
     -d "className=测试课程" \
     -d "beginTime=1484739085" \
     -d "endTime=1484739085" \
     -d "teacherUid=1001001" \
     -d "folderId=1" \
     -d "record=1" \
     -d "recordScene=1" \
     -d "live=1" \
     -d "replay=1" \
     -d "assistantUids=[1001002,1001003]" \
     -d "watchByLogin=0" \
     -d "allowUnloggedChat=1" \
     "https://root_url/partner/api/course.api.php?action=editCourseClass"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "more_data": {
        "live_url": "https://www.eeo.cn/live.php?lessonKey=0fdc12bc3558164d",
        "live_info": {
            "RTMP": "rtmp://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
            "HLS": "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.m3u8?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
            "FLV": "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.flv?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
        }
    },
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
| 119	| 表示结束时间须晚于开课时间
| 120	| 表示开课时间至少一分钟以后
| 136	| 表示机构下面没有该老师，请在机构下添加该老师
| 140	| 表示该课节正在上课，不能编辑和删除
| 142	| 表示该课程下无此课节信息
| 143	| 表示无此课节信息
| 144	| 表示机构下无此课程
| 145	| 表示该课节已经结束
| 160	| 表示机构下无此云盘目录
| 165	| 表示单节课不能少于15分钟且不能超过24小时
| 172	| 表示课程下的学生不能添加为老师
| 173	| 表示课程下的旁听不能添加为老师
| 212	| 表示该课节已经删除
| 268 | 表示课节开始时间超出允许范围（开课时间须在3年以内）
| 282	| 表示课节修改成功，录课参数设置错误，录课修改失败
| 283	| 表示课节修改成功，开课前20分钟内不能开启录课，录课修改失败
| 284	| 表示课节修改成功，视频服务有问题，录课修改失败
| 318 | 表示联席教师不是本机构老师
| 319 | 表示课程下的学生不能添加为联席教师
| 320 | 表示课程下的旁听不能添加为联席教师
| 321 | 表示插班生不能添加为联席教师
| 322 | 表示课节老师不能添加为联席教师
| 323 | 表示联席教师购买课节失败
| 324 | 表示课节老师加入教师列表失败
| 325 | 表示插班生不能添加为老师
| 326 | 表示课节联席教师加入教师列表失败
| 327 | 表示联席教师退订课节失败
| 328 | 表示课节联席教师不能添加为老师
| 330 | 表示联席教师账号格式不正确(2022年4月去除此错误码)
| 350 | 表示开课前20分钟内不能修改课节名称、上课时间、云盘资源、台上人数、是否自动上台、教学模式
| 369 | 该课程/课节类型暂不支持该操作
| 372 | 表示修改自动上台失败
| 385 | 已过课节结束时间，不能修改授课教师或联席教师
| 387 | 表示老师已被停用
| 388 | 表示联席教师已被停用
| 400 | 表示请求数据不合法
| 454 | 课节起止时间与系统维护时间有重叠
| 466 | 表示通过客户端-创建课堂产生的课节只能在客户端编辑（接口不支持编辑lms课节）  
| 800 | 表示老师被停用中
| 804 | 表示联席教师被停用中
| 825 | 表示课节编辑成功，课节简介设置失败
| 880 | 表示修改课节教学模式失败 |
| 884 | 老师帐号已注销 |
| 885 | 联席教师帐号已注销 |
|21316| 联席教师数据有重复 |
|21317| 联席教师数量超出限制 |
| 121601001 | 存在当前版本不支持的设置项
| 121601002 | 操作成功，\[在线教室\]资源已超出用量，为防止业务受影响，请尽快联系客户经理
| 121601003 | 您当月累计创建课节已达当月上限，无法继续创建，升级账号获取更多权益
| 121601004 | 您当月累计创建课节已达当月上限，无法继续创建
| 121601005 | 不支持设网页直播
| 121601006 | 不支持设置录制现场
| 121601007 | 台上人数参数错误
| 121601008 | 不支持设置联席教师
| 121601009 | 不支持设置网页回放
| 121601010 | 不支持设置录课
| 121601011 | 不支持设置双摄模式
| 121601012 | 清晰度超出限制
| 121604007  | 不支持设置OMO站播  |
