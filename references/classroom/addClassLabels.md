# 添加/修改/删除课节标签
添加/修改/删除课节标签，需要 SID，safekey，timeStamp，courseId，classList。其中当标签数组 (classLabelId) 为空时，表示删除课节下所有的标签；当课节下没有标签时，标签数组 (classLabelId) 中填写标签 ID，表示给课节下添加标签；当课节下有标签 ID，标签数组 (classLabelId) 中添加标签 ID，表示修改课节下标签。返回执行后的信息。**注：每个课节下最多可添加10个标签**。

## URL

`https://root_url/partner/api/course.api.php?action=addClassLabels`  

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
| courseId | 是 | 无 | 课程 ID | 无|
| classList | 是 | 无 | 课节数组 | JSON 格式|
|　└  | 是 | 无 | 课节对象 | 无|
|　　└ customColumn | 否 | 长度不超过50个字符。超过会自动截断 | 用户自定义字段 | 无|
|　　└ classId | 是 | 无 | 课节 ID | 无|
|　　└ classLabelId | 否 | 无 | 标签 ID 数组 | **为空数组时表示删除课节下的全部标签**|


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- |---- |-----|
| data | array | [] | 返回信息数组
|　└  | object |  | 返回信息对象
|　　└ customColumn | string | 1 | 自定义字段
|　　└ classId | number | 288352 | 课节 ID
|　　└ errno | number | 1 | 错误代码
|　　└ error | string | 程序正常执行 | 错误详情
|　└  | object |  | 返回信息对象
|　　└ customColumn | string | 1 | 自定义字段
|　　└ classId | number | 288352 | 课节 ID
|　　└ errno | number | 1 | 错误代码
|　　└ error | string | 程序正常执行 | 错误详情
| error_info | 	object |	|	返回信息对象
|　└ errno |	number |	1	 | 错误代码
|　└ error |	string |	"程序正常执行" |	错误详情




## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=addClassLabels HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=e98b01228fca036bf2ab060f7a8a6ec3&timeStamp=1493725870&courseId=25684&classList=[{"customColumn":"1","classId":135120,"classLabelId":[2,6,8]},{"customColumn":"2","classId": 135121,"classLabelId": [4,7,12]}]
```


 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "courseId=25684" \
      -d  'classList=[{"customColumn":"1","classId":135120,"classLabelId":[2,6,8]},{"customColumn":"2","classId":135121,"classLabelId":[4,7,12]}]' \
      "https://root_url/partner/api/course.api.php?action=addClassLabels"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "data": [
        {
            "customColumn": "1",
            "classId": 288325,
            "errno": 1,
            "error": "程序正常执行"
        },
        {
            "customColumn": "2",
            "classId": 288323,
            "errno": 1,
            "error": "程序正常执行"
        }
    ],
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
| 100 | 表示参数不全或错误
| 102 | 表示无权限（安全验证没通过）
| 104 | 表示操作失败（未知错误）|
| 155 | 表示数据数组不可为空
| 144 | 表示机构下无此课程
| 149 | 表示该课程已经删除
| 147 | 表示没有此课程信息
| 212 | 表示该单课已经删除
| 142 | 表示该课程下无此单课信息
| 143 | 表示没有此单课信息
| 358 | 表示部分标签不存在或已删除
| 359 | 表示部分标签不属于本机构
| 357 | 表示超出课节下允许添加数量上限
| 369 | 该课程/课节类型暂不支持该操作
| 466 | 表示通过客户端-创建课堂产生的课节只能在客户端编辑（接口不支持操作lms课节标签）
