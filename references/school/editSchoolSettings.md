# 修改学校设置

此接口用于修改后台学校设置配置项。

**注意**  
- 目前仅支持通过此接口修改【上课结束后允许正式学生和教师观看课程回放视频】、【新加入课程的学生，允许观看历史课节的回放视频】两个设置项。
- 本接口支持修改1项或多项学校设置，全都不传，报 `参数不全` 错误
- 本接口为v2接口，使用新签名算法

## URL 

`https://root_url/school/modifySchoolConf`   

## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

### Header 参数
| key | 必填 | 类型 |说明 | 
| ----| ----|----| ----- |  
| X-EEO-SIGN | 是 |string |签名 规则见[这里](signature.md)| 
| X-EEO-UID | 是 |string |机构SID | 通过 eeo.cn 申请添加为机构可获得|
| X-EEO-TS | 是 |string |当前调用接口5分钟以内的 Unix Epoch 时间戳|Unix Epoch 时间戳是 1970年1月1日 00:00:00 (世界标准时间) 起经过的秒数 |


### Body 参数      

| key | 必填 | 类型 |说明 | 规则说明 |
| ----| ----|----| ----- | -----|
| allowViewReplay | 否 | integer | 上课结束后允许正式学生和教师观看课程回放视频 | 	不传不修改，传错报 `参数错误`。0=不允许，1=允许 |
| allowNewStudentViewReplay | 否 | integer | 新加入课程的学生，允许观看历史课节的回放视频 | 不传不修改，传错报 `参数错误`。0=不允许，1=允许 |

## 请求示例

```http
POST /school/modifySchoolConf HTTP/1.1
Host: 
X-EEO-SIGN: f11d835f8c69ec49d2d936e3eb29ace9
X-EEO-UID: 234323
X-EEO-TS: 1721095405
User-Agent: Apifox/1.0.0 (https://apifox.com)
Content-Type: application/json
Content-Length: 64

{
    "allowViewReplay": 0,
    "allowNewStudentViewReplay": 0
}
```

- Shell cURL 模拟请求指令    
```bash
curl --location --request POST '/school/modifySchoolConf' \
--header 'X-EEO-SIGN: f11d835f8c69ec49d2d936e3eb29ace9' \
--header 'X-EEO-UID: 234323' \
--header 'X-EEO-TS: 1721095405' \
--header 'User-Agent: Apifox/1.0.0 (https://apifox.com)' \
--header 'Content-Type: application/json' \
--data-raw '{
    "allowViewReplay": 0,
    "allowNewStudentViewReplay": 0
}'
```

## 响应示例 
```json  
{
  "code": 1,
  "msg": "程序正常执行",
  "data": {}
}
```

## 错误码
| 错误码 | 说明 |
|:------|:----|
|121601030|缺少必传参数|
|101002005|签名异常|
|101002006|时间戳过期|
|101002008|时间戳不存在|
|121601020|业务参数错误|
|101001001|参数错误|
