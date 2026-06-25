# 添加客户端回放可观看人员

此为 LMS 课堂活动接口，用于为课堂活动添加客户端回放可观看成员。 

**注意**  
1. 关于客户端回放观看的名单设置有以下几个通用逻辑： 
   - 仅支持课堂活动，仅在课堂结束后可设置（包括接口和后台）。
   - 人员默认值=课节授课教师+课节联席教师+课节学生（含插班生）+ 班级下其他老师 + 班级班主任
   - 人员可选范围=课节授课教师+课节联席教师+班级下学生+班级下其他老师+班主任  
1. 关于本接口--删除客户端回放可观看人员 
    - 这是一个增量接口。添加新人员不会影响已有成员
    - 添加可观看人员，每个人员有单独的返回码，返回码在data里。
    - 如果添加的人员已存在列表中，不会返回错误码，会返回在成功列表，正常执行
    - 如果将所有可选人员全部添加为可观看人员，可使用[设置客户端回放为全员可看](../LMS/setPlaybackAllViewable.md)接口
    - 如果将所有可选人员全部设为不可观看人员，可使用[设置客户端回放为全员不可看](../LMS/setPlaybackAllForbidden.md)接口

## URL 

`https://root_url/playback/addPlaybackUser`


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

| key | 必填 | 类型 |说明 | 规则说明 |
| ----| ----|----| ----- | -----|
| courseId | 是 | integer | 班级（课程）ID |  |
| classId | 是 | integer | 活动创建完成后返回的课堂ID |  |
| uidList | 是 | array[string] | 学生UID数组|   |


## 响应参数

| 参数名 | 类型 | 示例值 | 含义 |
|-----|---- |---- |-----|
| code | integer | 1 | 错误码 |
| msg | string | "程序正常执行" | 错误信息 |
| data | object | null | 返回信息 |
| └ successList | array[int] |  | 添加成功的人员uid |
| └ failedList | array[object] | 1 | 添加失败的人员信息 |
|     └ uid | int |  | 人员uid |
|     └ code | int |  | 错误码 |
|     └ msg | string |  | 错误信息 |

## 示例

 - HTTP 请求

```http
POST /playback/addPlaybackUser HTTP/1.1
Host: root_url
X-EEO-SIGN: ceb7a2c0534999960c02c191d409c41e
X-EEO-UID: 409864
X-EEO-TS: 1722938382
Content-Type: application/json
Content-Length: 117

{
    "courseId": 414193,
    "classId": 25096097,
    "uidList": [
        504026,
        504028
    ]
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: ceb7a2c0534999960c02c191d409c41e' \
     -H 'X-EEO-UID: 409864' \
     -H 'X-EEO-TS: 1722938382' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 414193, "classId": 25096097, "uidList": [504026, 504028]}' \
     'https://root_url/playback/addPlaybackUser'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
	"code": 1,
	"msg": "程序正常执行",
	"data": {
		"successList": [504026],

		"failedList": [
            {
                "uid":504028,
        		"code": 121609003,
		        "msg": "该用户不在课节所属班级中，不可添加"
	        }
        ]
    }
}
```


## 错误码说明


| 错误码 | 说明 |
|:------|:----|
| 147 | 没有此课程信息 |
| 29149 | 活动已删除 |
| 30002 | 活动不存在 |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |
| 121609003 | 该用户不在课节所属班级中，不可添加 |  
| 121609004 | 课节不存在或不属于该机构 | 
| 121609005 | 课节未结束 |  
| 121609006 | 课节未开启录课 |  
