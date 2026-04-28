# 编辑单元

**注意**：
- 支持修改单元名称、介绍、发布状态中的一项或多项，name、content、publishFlag全都不传时，返回 `参数不全或错误`
- 编辑单元的时候，名字不可与已有单元重复。
- 使用此接口发布单元时，不会同时发布单元下的活动；如需发布活动，请调用[发布活动接口](releaseActivity.md)。

## URL 

`https://root_url/lms/unit/update`


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
| courseId | 是 | integer | 班级（课程）ID | 	单元所属班级ID | 
| unitId| 是 |integer | 单元ID| | 
| name| 否 |string | 单元名称 |长度不超过50字。注意：单元名称不可与课程下已存在单元重复 |    
| content| 否 |string | 单元介绍| 不传不修改 | 
| publishFlag| 否 |integer | 发布状态 | 0 = 草稿，2 = 已发布（显示）。仅支持从【草稿】修改为【已发布】，不支持反向操作| 


## 响应参数
| 参数名 | 类型 | 示例值 | 含义
|-----|---- |---- |-----| 
|code| integer | 1| 错误码 |
|msg| string | "程序正常执行"| 错误信息 |
| data | array | [] | 返回信息数组
|　└  | object |  | 返回信息对象
|　　└ unitId | integer | 26020895 | 单元ID


## 示例

 - HTTP 请求

```http
POST /lms/unit/update HTTP/1.1
Host: root_url
X-EEO-SIGN: a77fcc847b3704afde607bbd0c5231f4
X-EEO-UID: 409864
X-EEO-TS: 1722937832
Content-Type: application/json
Content-Length: 197

{
    "courseId": 414193,
    "unitId": 26020895,
    "name": "编辑单元",
    "content": "编辑单元内容描述",
    "publishFlag": 2
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: a77fcc847b3704afde607bbd0c5231f4' \
     -H 'X-EEO-UID: 409864' \
     -H 'X-EEO-TS: 1722937832' \
     -H 'Content-Type: application/json' \
     -d '{"courseId": 414193, "unitId": 26020895, "name": "编辑单元", "content": "编辑单元内容描述", "publishFlag": 2}' \
     'https://root_url/lms/unit/update'
```



## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": {
        "unitId": 26020895
    }
}
```


## 错误码说明

| 错误码 | 说明 |
|:------|:----|
| 147 | 没有此课程信息 |
| 40004 | 已发布不可修改为草稿 |
| 40020 | 单元不存在 |
| 50003 | 单元名称重复 |
| 101001001 | 参数错误 |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |
