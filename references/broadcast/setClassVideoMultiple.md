# 课节设置录课、直播、回放（多个）
课节设置录课、直播、回放（多个），需要提供 SID，safekey，timeStamp，课程 ID，课节信息数组（课节信息对象里包括课节 ID、录课、直播、回放、网页直播回放、允许未登录用户参与直播聊天和点赞。修改录课、直播、回放三个参数任意一个，其他两个参数则必填），返回每节课执行后的说明。修改录制现场时，录课、直播和回放三个参数必填。注意：如果当前课节已结束，则不能设置录播、直播功能。用户可以传递自定义字段，接口会原样将参数返回。不传递则不会返回。

注意事项：

- 如果课节设置录课（没有设置直播），则more_data返回课节直播播放器地址，拉流地址为空；
- 如果课节设置录课、直播，则more_data返回课节直播播放器地址和拉流地址；
- 如果要设置录制现场，则必须设置录课，否则无法开启录制现场。 


## URL

`https://root_url/partner/api/course.api.php?action=setClassVideoMultiple`  

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
| courseId | 是 | 无 | 课程 ID | 无|
| classJson | 是 | 无 | 课节信息数组 | 无|
| └ 课节帐号1信息对象 | 否 | 无 | 设置课节信息对象 | 无|
| 　 └ classId | 是 | 无 |	课节 ID |	无|
| 　 └ record | 否 | 无	| 录课(0关闭，1开启)	| 无|
| 　 └ recordScene | 否 | 无	| 录制现场(0关闭，1开启)	| 无|
| 　 └ live | 否 | 无 |	直播(0关闭，1开启) |	无|
| 　 └ replay | 否 | 无 |	回放(0关闭，1开启)	| 无|
| 　 └ watchByLogin  | 否 | 不传或传错，都不修改 | 只允许登录ClassIn账号后才可观看，未登录不可观看，0=未开启，1=开启 | 未开启录课、直播、回放中的两项及以上，此参数设置了也用不到 |
| 　 └ allowUnloggedChat  | 否 | 不传或传错，都不修改 | 允许未登录用户参与直播聊天和点赞，0=不允许，1=允许 | 未开启录课和直播，此参数设置了也用不到 |
| 　 └ customColumn | 否 | 1-50字，不区分中英文，超过50会自动截取为50字 | 用户自定义标识 | 不为空则原样返回，为空则不返回该字段|
| └ ······ |	否 |	无 |	设置课节信息对象...... |	无|



## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| data |	array |	|	返回数据信息数组，包括以下字段|
|　└ more_data | array | [] | 返回 Data 信息数组|
|　└ live_url | string | https://root_url/live.php?lessonKey=0fdc12bc3558164d | 课节直播播放器地址|
|　└ live_info | array | [] | 返回 Data 信息数组|
|　　└ RTMP | string | "rtmp://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 拉流地址|
|　　└ HLS | string | "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.m3u8?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 拉流地址|
|　　└ FLV | string | "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.flv?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 拉流地址|
|　└ errno |	number |	1 |	错误代码|
|　└ error |	string |	"程序正常执行" |	错误详情|
| └ ...... |	[] |	{......} |	错误信息对象，包括以下字段|
|　└ more_data | array | [] | 返回 Data 信息数组|
|　└ live_url | string | https://root_url/live.php?lessonKey=0fdc12bc3558164d | 课节直播播放器地址|
|　└ live_info | array | [] | 返回 Data 信息数组|
|　　└ RTMP | string | "rtmp://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 直播拉流地址|
|　　└ HLS | string | "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.m3u8?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 直播拉流地址|
|　　└ FLV | string | "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.flv?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd" | 直播拉流地址|
|　　└ errno	| number |	... |	错误代码|
|　　└ error |	string |	"程序正常执行" |	错误详情|
| error_info | 	object |	|	返回信息对象|
|　└ errno |	number |	1	 | 错误代码|
|　└ error |	string |	"程序正常执行" |	错误详情|

## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=setClassVideoMultiple HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=6b5e624027b981fc2da5b1787c974281&timeStamp=1494392466&courseId=523689&classJson=[{"classId":"1419691","record":"1","live":"","replay":"","customColumn":123,"watchByLogin":0,"allowUnloggedChat":1"},{"classId":"1419693","record":"1","live":"","replay":"","customColumn":123,"watchByLogin":0,"allowUnloggedChat":"1"}]
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "courseId=123456" \
      -d 'classJson=[ \
                      { \
                        "classId":"1234", \
                        "record":"1", \
                        "recordScene":"1", \
                        "live":"0", \
                        "replay":"0" \
                        "watchByLogin":0 \
                        "allowUnloggedChat":"1" \
                      }, \
                      { \
                        "classId":"1235", \
                        "record":"1", \
                        "recordScene":"1", \
                        "live":"0", \
                        "replay":"0" \
                        "watchByLogin":0 \
                        "allowUnloggedChat":"1" \                        
                      } \
                    ]' \
    "https://root_url/partner/api/course.api.php?action=setClassVideoMultiple"
```



## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": [
    {
      "customColumn": "123",
      "more_data": {
          "live_url": "https://root_url/live.php?lessonKey=0fdc12bc3558164d",
          "live_info": {
              "RTMP": "rtmp://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
              "HLS": "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.m3u8?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd",
              "FLV": "https://liveplay.eeo.cn/eeolive/576f5a8c97d9-183291632119a96.flv?txSecret=f4bfe1afcf2592de61c11af9e0954c00&txTime=7d8d37cd"，
          }
        },
      "errno": 1,
      "error": "程序正常执行"
    },
    {
      "customColumn": "123",
      "more_data": {
          "live_url": "https://root_url/live.php?lessonKey=0fdc12bc3558164d",
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
| 1   | 表示成功执行
| 100	| 表示参数不全或错误
| 102	| 表示无权限（安全验证没通过）
| 104	| 表示操作失败/未知错误
| 114	| 表示服务器异常
| 142	| 表示该课程下无此课节信息
| 143	| 表示没有此课节信息
| 144	| 表示机构下无此课程
| 149	| 表示课程已删除
| 155	| 表示课节数组不可为空
| 212	| 表示该课节已经删除
| 251	| 表示只有开启了录课，才能开启直播或回放
| 252	| 表示录课/直播状态，只有开课前 20 分钟才可更改
| 253	| 表示视频服务有问题，请稍后重试
| 369 | 该课程/课节类型暂不支持该操作
