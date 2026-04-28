# 创建课堂

此接口用于在单元下新建课堂活动。

**注意**：
- 接口有频次限制，不超过1000次/分钟。超出会报错。      
- 此接口仅支持创建标准课堂，不支持创建在线双师子课堂。
- 单个课程下可创建的课堂总数存在限制，如果超出限制会报错。单个单元下的可创建活动数存在限制（包括课堂），目前是100个活动。超出会报错。
- 不要求传递 screenMode（屏幕模式）和 teachMode（教学模式）。根据 cameraHide（是否隐藏坐席区）给 screenMode、teachMode 参数赋相应的值。
    - cameraHide=0（显示坐席区）时，teachMode=1（在线教室），screenMode=1（标准模式）
    - cameraHide=1（隐藏坐席区）时，teachMode=2（智慧教室），screenMode=2（大屏模式）
- 此接口不支持设置发布对象，发布对象默认为 `发布给全部成员`。
- 此接口仅支持创建已发布的课堂，不支持草稿。
- 如课堂开启录课但未开启网页直播，则 data 返回 课堂直播播放器地址 liveUrl，拉流地址为空。
- 如课堂开启录播、网页直播，则会给该课堂绑定3个拉流地址（RTMP，HLS ，FLV），data 返回课堂直播播放器地址 liveUrl 和拉流地址 liveInfo。如该课堂后续取消直播，3个拉流地址仍然存在且与该课堂绑定。
- 如课堂不开启录课，则 data 里的课堂直播播放器地址 liveUrl 和拉流地址 liveInfo 均为空。
- recordType、recordState、liveState、openState为一组完整参数，不可只传其中部分参数。否则会报错。


## URL 

`https://root_url/lms/activity/createClass`


## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

### Header 参数
| key | 必填 | 类型 |说明 | 
| ----| ----|----| ----- | 
| X-EEO-SIGN | 是 |string |签名 规则见[这里](../appendix/signature.md)| 
| X-EEO-UID | 是 |string |机构SID |
| X-EEO-TS | 是 |string |时间戳 |


### Body 参数

| 字段名            | 必填 | 类型     | 说明                               | 规则说明               | 
|-------------------|------|----------|---------------------------------|-------------------| 
| courseId          | 是   | integer  | 班级（课程）ID        |      | 
| unitId            | 否   | integer  | 单元ID|  如果不传参数，则会创建在无主题单元下，传空或传错会报错。   | 
| name              | 是   | string   | 课堂活动名称    | 长度不超过50字    |   
| teacherUid        | 是   | integer  | 主讲教师UID  |       |   
| startTime         | 是   | integer  | 活动开始时间    | 可选择未来2年内的时间，Unix Epoch 时间戳（秒单位）   |  
| endTime           | 是   | integer  | 活动结束时间     | Unix Epoch 时间戳（秒单位）   |  
| assistantUids     | 否   | array[integer] | 联席教师UID列表     | 示例：[1000082,1000083]，不传默认无联席教师；UID值为注册用户接口返回的用户 UID      |  
| cameraHide        | 否   | integer  | 是否隐藏坐席区      | 0 = 否（显示坐席区），1 = 是（隐藏坐席区）。默认为0，不传使用默认值，传错报 `参数错误`；当 cameraHide = 1 时，isAutoOnstage 会始终被设置为 0（也就是说，cameraHide = 1时，API 会忽略传参 isAutoOnstage 的值）     |   
| isAutoOnstage     | 否   | integer  | 学生进入教室是否自动上台       | 0 = 不自动，1 = 自动。默认为1，不传使用默认值，传错报 `参数错误`；     |   
| seatNum           | 否   | integer  | 上台人数    | 包含老师，例：传1时，表示1v0，台上只显示老师头像。默认为7（1v6），不传使用默认值，如机构最大台上人数配置小于1v6，会默认为机构最大台上人数。传递的台上人数小于配置的最大台上人数，正常创建；传递的台上人数大于配置的最大台上人数，则会被重置为最大台上人数|   
| isHd              | 否   | integer  | 是否高清     | 0 = 非高清，1 = 高清，2 = 全高清。默认为0，不传使用默认值，传错报 `参数错误`。目前仅支持 1V1 或 1V6 高清、全高清	   |  
| isDc              | 否   | integer  | 双摄模式，是否开启副摄像头    | 0 = 不开启，3 = 开启全高清副摄像头。默认为0，不传使用默认值，传错报 `参数错误`；如果 isDc 等于3，课节的台上人数不是 1v1（即 seatNum 不等于2），则返回 `该设置不支持双摄` ；如果 isDc 等于3，且 seatNum 等于2的话，则 isHd 一定会被设置为2（即这种情况 API 会忽略 isHd 的传参值）  |   
| recordType        | 否   | integer  | 录课类型     | 0 = 录制教室，1 = 录制现场，2 = 两个都录。默认为0，不传使用默认值，传错报 `参数错误`  |   
| recordState       | 否   | integer  | 是否开启录课   | 0 = 不录课（关闭），1 = 录课（开启）。默认为0，不传使用默认值，传错报 `参数错误`。打开录课，ClassIn会将教室互动直播场景录制下来，可用于网页直播或者网页回放。若需要网页直播或者网页回放，则必须选择录课，否则无法开启网页直播、网页回放   |  
| liveState         | 否   | integer  | 是否开启直播        | 0 = 不直播（关闭），1 = 直播（开启）。默认为0，不传使用默认值，传错报 `参数错误`。若需要网页直播，则必须开启录课      |  
| openState         | 否   | integer  | 是否公开回放    | 0 = 不公开（关闭），1 = 公开（开启）。默认为0，不传使用默认值，传错报 `参数错误`。若需要网页回放，则必须开启录课       |         
| isAllowCheck      | 否   | integer  | 是否允许互相查看学习报告和评分    | 0 = 不允许，1 = 允许。默认为1，不传使用默认值，传错报 `参数错误` | 
| uniqueIdentity | 否   | string   | 唯一标识                         | 例如：45s8d5a6asaa1ssf。1-32 位字符，不符合规则的值报 `参数错误`；可传唯一标识，用于校验机构下是否已存在此唯一标识，防止因网络原因导致的重复创建       | 
| omoStationBroadcast | 否   | integer   | 是否开启OMO站播                        |  0-关闭，1-开启，传其他值报业务参数错误     | 




## 响应参数
| 参数名 | 类型 | 示例值 | 含义
|-----|---- |---- |-----| 
|code| integer | 1| 错误码 |
|msg| string | "程序正常执行"| 错误信息 |
| data | object |   | 返回信息对象
|　└ activityId | integer | 25096094 | 活动ID
|　└ classId | integer | 1141162 | 课堂ID
|　└ name | string | "api创建课堂" | 课堂名称
|　└ live_info | object |   |  三个拉流地址
|　　└ RTMP | string |   | RTMP协议的拉流地址
|　　└ HLS | string |    | HLS协议的拉流地址
|　　└ FLV | string |    | FLV协议的拉流地址
|　└ live_url | string |   | 课节直播回放页面



## 示例

 - HTTP 请求

```http
POST /lms/activity/createClass HTTP/1.1
Host: root_url
X-EEO-SIGN: 5cb85cc272274a4353a9dc4c8dcdf0fc
X-EEO-UID: 409864
X-EEO-TS: 1722938160
Content-Type: application/json
Content-Length: 274

{
    "courseId": 414193,
    "unitId": 26020897,
    "name": "api创建课堂",
    "teacherUid": 409864,
    "startTime": 1723010760,
    "endTime": 1723016760,
    "liveState": 1,
    "openState": 1,
    "recordState": 1,
    "recordType": 0
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: 5cb85cc272274a4353a9dc4c8dcdf0fc' \
     -H 'X-EEO-UID: 409864' \
     -H 'X-EEO-TS: 1722938160' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 414193, "unitId": 26020897, "name": "api创建课堂", "teacherUid": 409864, "startTime": 1723010760, "endTime": 1723016760, "liveState": 1, "openState": 1, "recordState": 1, "recordType": 0}' \
     'https://root_url/lms/activity/createClass'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
	"code": 1,
	"msg": "程序正常执行",
	"data": {
		"activityId": 25107347,
		"classId": 1152680,
		"live_info": {
			"RTMP": "rtmp://liveplay.eeo.cn/eeolive/576f5a8c97de-18329123b10cec7d2?txSecret=c10b423a82cab861860081c02d03d87b&txTime=7d8d37cd",
			"HLS": "https://liveplay.eeo.cn/eeolive/576f5a8c97de-18329123b10cec7d2.m3u8?txSecret=c10b423a82cab861860081c02d03d87b&txTime=7d8d37cd",
			"FLV": "https://liveplay.eeo.cn/eeolive/576f5a8c97de-18329123b10cec7d2.flv?txSecret=c10b423a82cab861860081c02d03d87b&txTime=7d8d37cd"
		},
		"live_url": "https://www.eeo.cn/live.php?lessonKey=3dca7b0e14e3bb35",
		"name": "api-0829"
	}
}
```


## 错误码说明

| 错误码 | 说明 |
|:------|:----|
| 100 | 课节参数不全或错误 |
| 104 | 服务端调用失败 |
| 119 | 结束时间是否大于开课时间 |
| 120 | 开课时间不合法 |
| 136 | 机构下面没有该老师,请在机构下添加该老师 |
| 147 | 没有此课程信息 |
| 158 | 课节下添加学生失败 |
| 160 | 机构下无此云盘目录 |
| 161 | 单课创建失败 |
| 165 | 单节课不能少于15分钟且不能超过24小时 |
| 172 | 课程下的学生不能添加为老师 |
| 173 | 课程下的旁听不能添加为老师 |
| 219 | 老师信息不存在 |
| 220 | 客户端添加课节失败 |
| 221 | 客户端修改单课视频点播信息失败 |
| 267 | 课节创建成功,直播信息设置失败 |
| 268 | 课节开始时间超出允许范围 |
| 318 | 联席教师不是本机构老师 |
| 319 | 课程下的学生不能添加为联席教师 |
| 320 | 课程下的旁听不能添加为联席教师 |
| 322 | 课节老师不能添加为联席教师 |
| 324 | 联席教师节老师加入教师列表失败 |
| 325 | 插班生不能添加为老师 |
| 326 | 联席教师加入教师列表失败 |
| 387 | 老师已被停用 |
| 388 | 联席教师已被停用 |
| 390 | 本课程下的课节数量已达到上限 |
| 451 | 课节直播封面和介绍添加失败 |
| 451 | 课节直播封面和介绍添导失败,长度超限 |
| 454 | 课节起止时间与系统维护时间有重叠 |
| 769 | 教师版或教师试用版,班主任不是本人 |
| 800 | 老师被停用中 |
| 804 | 联席教师被停用中 |
| 884 | 老师账号已注销 |
| 885 | 联席教师账号已注销 |
| 21304 | 非中小学不支持设置学科 |
| 21317 | 联席教师数量超出限制 |
| 21319 | 老师已删除 |
| 40031| 超过单元最大数量限制|
| 101001001 | 参数错误 |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 101003001 | 请求频次过快 |
| 110100066 | 该设置不支持双摄 |
| 121601003 | 您当月累计创建课节已达当月上限,无法继续创建,升级账号获取更多权益 |
| 121601004 | 您当月累计创建课节已达当月上限,无法继续创建 |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |
| 121601070  | 单个课程下课堂数量超过限制 |
| 121604007  | 不支持设置OMO站播  |

