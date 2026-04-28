# 移动单元下的活动

此接口用于将A单元下的活动全部移动至B单元。

**注意**：
- 如需保留待删除单元下的学习活动，可通过此接口完成前置操作。
- 此接口也可用作需合并单元的场景。

## URL 

`https://root_url/lms/unit/move`


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
| courseId | 是 | integer | 班级（课程）ID |单元所属班级ID |
| unitId| 是 |integer | 源单元ID|  |
| toUnitId| 是 |integer | 目标单元ID  |  |  

## 响应参数
| 参数名 | 类型 | 示例值 | 含义 |
|-----|---- |---- |-----|
| code | integer | 1 | 错误码 |
| msg | string | "程序正常执行" | 错误信息 |
| data | integer | null | 返回信息 |

## 示例

 - HTTP 请求

```http
POST /lms/unit/move HTTP/1.1
Host: root_url
X-EEO-SIGN: 3184c79587741b9f767db68eb50998a3
X-EEO-UID: 409864
X-EEO-TS: 1722937990
Content-Type: application/json
Content-Length: 102

{
    "courseId": 414193,
    "unitId": 26020700,
    "toUnitId": 26020897
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: 3184c79587741b9f767db68eb50998a3' \
     -H 'X-EEO-UID: 409864' \
     -H 'X-EEO-TS: 1722937990' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 414193, "unitId": 26020700, "toUnitId": 26020897}' \
     'https://root_url/lms/unit/move'
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": null
}
```


## 错误码说明

| 错误码 | 说明 |
|:------|:----|
| 147 | 没有此课程信息 |
| 29046 | 当前单元与目标单元相同 |
| 29048 | 单元不存在 |
| 29050 | 移动单元失败 |
| 29138 | 目标单元活动数量超限 |
| 29203 | 单元删除失败 |
| 50004 | 目标单元不存在 |
| 101001001 | 参数错误 |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |
