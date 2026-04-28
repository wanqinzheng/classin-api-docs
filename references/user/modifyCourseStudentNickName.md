# 同步学生班级昵称

**接口功能：** 此接口支持将后台“学生管理-姓名”同步到学生所在的所有未结课班级  

**接口说明：**
- 支持批量同步，studentUids单次上限为100
- 仅同步至未结课课程的班级昵称


## URL 

`https://root_url/schooluser/modifyCourseStudentNickName`


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
|key|必填|类型|说明|规则说明| 
| ----| ----|----|----| ----- |
|studentUids|是|数组|仅刷新未结课班级的班级昵称|studentUids最大100| 
## 响应参数
|参数名|类型|示例值|含义|
| ----| ----|----|----|
|code|integer|1|错误码|
|msg|string|"程序正常执行"|错误信息|
|data|array|[]|返回信息数组|
|└|studentUid|integer|1445886|
|└|code|integer|1|错误码|
|└|msg|string|"程序正常执行"|错误信息|

## 示例

 - HTTP 请求

```http
POST /schooluser/modifyCourseStudentNickName HTTP/1.1 
Host: root_url
X-EEO-SIGN: 365456d0454e9b0dd793c47e65727e84
X-EEO-UID: 2669800
X-EEO-TS: 1732268163
Content-Type: application/json
Content-Length: 26

{
    "studentUids": [
        1445886
    ]
}
```

 - Shell cURL 模拟请求指令

```bash
curl -X POST \
     -H 'Host: root_url' \
     -H 'X-EEO-SIGN: 365456d0454e9b0dd793c47e65727e84' \
     -H 'X-EEO-UID: 2669800' \
     -H 'X-EEO-TS: 1732268163' \
     -H 'Content-Type: application/json' \
     -d '{"studentUids": [1445886]}' \
     'https://root_url/schooluser/modifyCourseStudentNickName'
```

## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "code": 1,
    "msg": "程序正常执行",
    "data": [
        {
            "studentUid": 1445886,
            "code": 1,
            "msg": "程序正常执行"
        }
    ]
}
```
    
## 错误码说明
|错误码|说明|
| ----| ----|
|101001001|业务参数错误|
|101002005|签名异常|
|101002006|时间戳过期|
|101002008|时间戳不存在|
|101004005|服务内部调用失败|
|110100067|同步班级昵称失败|
|121601058|不存在该机构|
|121601059|机构下无此学生|
|121601060|学生数量超过限制100|