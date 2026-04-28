# 修改课节上台学生数

**![!deprecated](../../img/waring.png)通知：此接口为原课节类接口，2025年5月26日之后可以继续使用，但不再更新，建议使用LMS活动类接口：[编辑课堂活动](LMS/updateClassroom.md)**



修改课节上台学生数，需要提供 SID，safekey，timeStamp，课程 ID，课节 ID，上台学生数，设置摄像头清晰度，是否开启双摄模式（即启用第二摄像头）。返回执行后的成功说明。seatNum 能修改的最大值为机构最大上台人数，如果需要修改超过机构最大上台人数请联系客户经理。**注意：seatNum 和 isHd 至少传递一个**

## URL

`https://root_url/partner/api/course.api.php?action=modifyClassSeatNum`

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
| seatNum |	是 | 最多只能修改为机构最大上台学生数 | 上台学生数（不包含老师）| 例如修改为 1v6，此参数值应为 6|
| isHd | 否 |0=非高清，1=高清，2=全高清，非1的数字都会当做0来处理 | 是否高清 | seatNum 和 isHd 至少传递一个 |
| isDc | 否 | 默认为0，不传或传错，都使用默认值 | 双摄模式，是否开启副摄像头，0=不开启，3=开启全高清副摄像头 | 如果isDc等于3，课节的台上人数不是1v1（即seatNum不等于1），则返回808错误<br>如果isDc等于3，且seatNum等于1的话，则isHd一定会被设置为2（即这种情况API会忽略isHd的传参值） |


## 响应参数

| 参数名 | 类型 |	示例值 |	含义|
| ---- |---- |----| ----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

- HTTP 请求

```http
POST /partner/api/course.api.php?action=modifyClassSeatNum HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=58ce17711abea665f40f67d550ce96fb&timeStamp=1493364941&courseId=490583&classId=1395039&seatNum=6
```

- Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
     -d "SID=1234567" \
     -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
     -d "timeStamp=1484719085" \
     -d "courseId=442447" \
     -d "classId=23644"  \
     -d "seatNum=6"
     "https://root_url/partner/api/course.api.php?action=modifyClassSeatNum"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
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
| 140	| 表示该课节正在上课，不能编辑和删除
| 142	| 表示该课程下无此课节信息
| 143	| 表示无此课节信息
| 144	| 表示机构下无此课程
| 145	| 表示该课节已经结束
| 147 | 表示没有此课程信息
| 149 | 表示该课程已经删除
| 153 | 表示课程已过期
| 212 | 表示该单课已经删除
| 259 | 表示上台人数设置超出最大限制(最大上台人数12)
| 348 | 表示开课前20分钟内不能修改上台人数
| 349 | 表示上台人数修改失败
| 367 | 表示修改课节属性（高清）失败
| 368 | 表示当前学生上台数不支持高清
| 369 | 该课程/课节类型暂不支持该操作
| 466 | 表示通过客户端-创建课堂产生的课节只能在客户端编辑（接口不支持编辑lms课节）|
| 808 | 表示该设置不支持双摄 |
|121601012|清晰度超出限制|
|121601007|台上人数参数错误|
|121601011|不支持设置双摄模式|

