# 课程分组-编辑课程分组


## URL

`https://root_url/partner/api/course.api.php?action=editCourseGroup`

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
| courseId  |	是 |	无 |	课程 ID |	无|
| groupId   |	是 |	无 |	分组 ID |	无|
| groupList |	是 |	json字符串 |1.其中studentUid和isLeader字段必须填写，每组有且仅有一个组长 (isLeader代表是否为组长 1是 0否)  2.组员不能重复|	[ [{ "studentUid": 1000152,"isLeader": 1}, {"studentUid": 1000109,"isLeader": 0}],[{"studentUid": 1000101,"isLeader": 1}, {"studentUid": 1000100,"isLeader": 0}]]  |
| groupName |	是 |	1-20位字符，不区分中英文，超过20个字符会自动截取为20个 |	分组名称 |	无
	


## 响应参数


| key | 类型 | 示例值 | 含义
| ----|-----|-----| ----|
| error_info | 	object |	|	返回信息对象
| └ errno |	number |	1	 | 错误代码
| └ error |	string |	"程序正常执行" |	错误详情
	
## 示例

 -  HTTP 请求

```
POST /partner/api/course.api.php?action=editCourseGroup HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache


SID=1234567&safeKey=3276433ab0216d9aec2621431cc12248&timeStamp=1494407873&courseId=176465&groupId=139&groupName=课程分组&groupList=[[{"studentUid": 1000152, "isLeader": 1 }, { "studentUid": 1000109, "isLeader": 0}],[{"studentUid": 1000101,"isLeader": 1}, {"studentUid": 1000100,"isLeader": 0}]]
```

 - Shell cURL模拟请求指令

```
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
       -d "SID=1234567" \
       -d "safeKey=b4bbe6c28f6d6d6536742c2fe0ab41bf" \
       -d "timeStamp=1637132493" \
       -d "courseId=176465" \
       -d "groupId=139" \
       -d "groupName=课程分组" \
       -d 'groupList= [[{"studentUid": 1000152, "isLeader": 1 }, { "studentUid": 1000109, "isLeader": 0}],[{"studentUid": 1000101,"isLeader": 1}, {"studentUid": 1000100,"isLeader": 0}]]'\
       "https://root_url/partner/api/course.api.php?action=editCourseGroup"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```
{
"error_info": {
    "errno": 1,
    "error": "程序正常执行"}
}
```

## 备注

```
补充说明groupList字段
[
[{
"studentUid": 1000152,
"isLeader": 1
    
},
{"studentUid": 1000109,
"isLeader": 0
    
}],
[{
"studentUid": 1000101,
"isLeader": 1
    
},
{"studentUid": 1000100,
"isLeader": 0
    
}]
]
1.其中studentUid和isLeader字段必须填写，每组有且仅有一个组长 (isLeader代表是否为组长 1是 0否)
2.组员不能重复
```


## 错误码说明

| 错误码 |	错误详情|
|:-------|-----|
| 1   | 程序正常执行
| 100	| 参数不全或错误
| 102	| 无权限
| 104	| 操作失败/未知错误
| 890	| 设置课程分组信息失败
| 893	| 操作失败，此课程分组不存在

