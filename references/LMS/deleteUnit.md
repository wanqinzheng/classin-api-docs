# 删除单元

**注意**：
- 此接口会同时删除单元下的学习活动，请谨慎操作。
- 删除时，如需保留单元下的活动，请先调用[移动单元下的活动接口](moveActivity.md)，将学习活动移动至其他单元。

## URL 

`https://root_url/lms/unit/delete`


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
| courseId | 是 | integer | 班级（课程）ID |单元所属班级ID|
| unitId | 是 |string | 单元ID| | 

## 响应参数
| 参数名 | 类型 | 示例值 | 含义
|-----|---- |---- |-----| 
|code| integer | 1| 错误码 |
|msg| string | "程序正常执行"| 错误信息 |
| data | array | [] | 返回信息数组
|　└  | object |  | 返回信息对象
|　　└ unitId | integer | 26020898 | 单元ID

## 示例

 - HTTP 请求

```http
POST /lms/unit/delete HTTP/1.1
Host: root_url
X-EEO-SIGN: 389454122008cbec73371037e5ce9e91
X-EEO-UID: 409864
X-EEO-TS: 1722938125
Content-Type: application/json
Content-Length: 80

{
    "courseId": 414193,
    "unitId": 26020898
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: 389454122008cbec73371037e5ce9e91' \
     -H 'X-EEO-UID: 409864' \
     -H 'X-EEO-TS: 1722938125' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 414193, "unitId": 26020898}' \
     'https://root_url/lms/unit/delete'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": {
        "unitId": 26020898
    }
}
```


## 错误码说明

| 错误码 | 说明 |
|:------|:----|
| 147 | 没有此课程信息 |
| 29057 | 机构欠费 |
| 29060 | 机构状态不正常 |
| 40001 | 包含上课中或已结束课堂不可删除 |
| 40020 | 单元不存在 |
| 101001001 | 参数错误 |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |
