# 创建非课堂活动草稿

**注意**：
- 可以创建除课堂外的活动草稿。 包括以下七种活动：       
作业、测验、打卡、录播课、讨论、学习资料、答题卡  
- 单个单元下的可创建活动数存在限制（包括课堂），目前是100个活动。超出会报错。   




## URL 

`https://root_url/lms/activity/createActivityNoClass`


## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

### Header 参数
| key | 必填 | 类型 |说明 | 
| ----| ----|----| ----- | 
| X-EEO-SIGN | 是 |string |签名 生成规则见[这里](../appendix/signature.md)| 
| X-EEO-UID | 是 |string |机构SID |
| X-EEO-TS | 是 |string |时间戳 |


### Body 参数

| key | 必填 | 类型 |说明 | 规则说明 |
| ----| ----|----| ----- | -----| 
| courseId | 是 | integer | 班级（课程）ID | | 
| unitId | 是 | integer | 单元ID | | 
| activityType | 是 | integer | 活动类型  | 2=作业；3=测验；4=录播课；5=学习资料；6=讨论；7=答题卡；8=打卡 | 
| name| 是 | String | 活动名称 | 长度不超过50字。注：课程下不支持创建同名单元 | 
| teacherUid|是 |  integer | 活动教师ID |  老师必须在机构下，另外，如果老师不在班级下，会自动进班  | 
| startTime         | 否   | integer  | 活动开始时间    | 可选择未来3年内的时间，Unix Epoch 时间戳（秒单位）   |  
| endTime         | 否   | integer  | 活动结束时间    |  Unix Epoch 时间戳（秒单位）   |   

## 响应参数
| 参数名 | 类型 | 示例值 | 含义
|-----|---- |---- |-----| 
|code| integer | 1| 错误码 |
|msg| string | "程序正常执行"| 错误信息 |
| data | array | [] | 返回信息数组
|　└  | object |  | 返回信息对象
|　　└ name | integer | 创建单元 | 活动名
|　　└ activityId | integer | 26019953 | 活动ID



## 示例

- HTTP 请求

```http
POST /lms/activity/createActivityNoClass HTTP/1.1
Host: root_url
X-EEO-SIGN: 37471286c6cfb95c4afb899396b884e2
X-EEO-UID: 409864
X-EEO-TS: 1722937773
Content-Type: application/json
Content-Length: 165

{
    "courseId": 414193,
    "unitId":22360790,
    "activityType":2,
    "name": "创建作业草稿",
    "teacherUid":1006368, 
    "startTime":1724134581,
    "endTime":1724138181
}
```


 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: 37471286c6cfb95c4afb899396b884e2' \
     -H 'X-EEO-UID: 409864' \
     -H 'X-EEO-TS: 1722937773' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 414193,  "unitId":22360790,"activityType":2, "name": "创建作业草稿", "teacherUid":1006368, "startTime":1724134581,"endTime":1724138181}' \
     'https://root_url/lms/activity/createActivityNoClass'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": {
        "name": "创建作业草稿",
        "unitId": 26020895
    }
}
```


## 错误码说明

| 错误码 | 说明 |
|:------|:----|
| 147 | 没有此课程信息 |
| 40020 | 单元不存在 |
| 40031 | 单元活动数量超限 |
| 101001001 | 参数错误 |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |

