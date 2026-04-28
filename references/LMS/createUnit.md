# 创建单元

**注意**：
- 创建单元的时候，不支持创建名称重复的单元。如课程下有同名单元，不管是否草稿状态，均会报 `单元已存在` 的错误。  


## URL 

`https://root_url/lms/unit/create`


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
| name| 是 | String | 单元名称 | 长度不超过50字。注：课程下不支持创建同名单元 | 
| publishFlag|是 |  integer | 是否发布 | 0 = 草稿，2 = 已发布（显示）  | 
| content| 否 |  String | 单元介绍 | 不传默认为空 |   

## 响应参数
| 参数名 | 类型 | 示例值 | 含义
|-----|---- |---- |-----| 
|code| integer | 1| 错误码 |
|msg| string | "程序正常执行"| 错误信息 |
| data | array | [] | 返回信息数组
|　└  | object |  | 返回信息对象
|　　└ name | integer | 创建单元 | 单元名
|　　└ unitId | integer | 26019953 | 单元ID



## 示例

- HTTP 请求

```http
POST /lms/unit/create HTTP/1.1
Host: root_url
X-EEO-SIGN: 37471286c6cfb95c4afb899396b884e2
X-EEO-UID: 409864
X-EEO-TS: 1722937773
Content-Type: application/json
Content-Length: 165

{
    "courseId": 414193,
    "name": "创建单元",
    "content": "单元内容描述",
    "publishFlag": 2
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
     -d '{"courseId": 414193, "name": "创建单元", "content": "单元内容描述", "publishFlag": 2}' \
     'https://root_url/lms/unit/create'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": {
        "name": "创建单元",
        "unitId": 26020895
    }
}
```


## 错误码说明

| 错误码 | 说明 |
|:------|:----|
| 147 | 没有此课程信息 |
| 29200 | 单元创建失败 |
| 29208 | 单元已存在 |
| 29213 | 单元创建成功 |
| 40031 | 超过班级下单元最大限制 |
| 101001001 | 参数错误 |
| 101002005 | 签名异常 |
| 101002006 | 时间戳过期 |
| 101002008 | 时间戳不存在 |
| 121601020 | 业务参数错误 |
| 121601021 | 课程不属于当前机构下 |
| 121601022 | 课程不是标准课 |
| 121601023 | 课程已过期 |

