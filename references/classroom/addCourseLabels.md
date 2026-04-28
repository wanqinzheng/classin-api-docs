# 添加/修改/删除课程标签
添加/修改/删除课程标签，需要 SID，safekey，timeStamp，courseList。其中当标签数组 (labelIds) 为空时，表示删除课程下所有的标签；当课程下没有标签时，标签数组 (labelIds) 中填写标签 ID，表示给课程下添加标签；当课程下有标签 ID，标签数组 (labelIds) 中添加标签 ID，表示修改课程下标签。返回执行后的信息。**注：每个课程下最多可添加10个标签**。

## URL

`https://root_url/partner/api/course.api.php?action=addCourseLabels`  

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
| courseList | 是 | 无 | 课程数组 | JSON 格式|
|　└  | 是 | 无 | 课程对象 | 无|
|　　└ customColumn | 否 | 无 | 用户自定义字段 | 无|
|　　└ courseId | 是 | 无 | 课程 ID | 无|
|　　└ labelIds | 否 | 无 | 标签 ID 数组 | **为空数组时表示删除课程下的全部标签**|


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- |---- |-----|
| data | array | [] | 返回信息数组|
|　└  | object |  | 返回信息对象|
|　　└ customColumn | string | 1 | 自定义字段|
|　　└ courseId | number | 288352 | 课程 ID|
|　　└ errno | number | 1 | 错误代码|
|　　└ error | string | 程序正常执行 | 错误详情|
|　└  | object |  | 返回信息对象|
|　　└ customColumn | string | 1 | 自定义字段|
|　　└ courseId | number | 288352 | 课程 ID|
|　　└ errno | number | 1 | 错误代码|
|　　└ error | string | 程序正常执行 | 错误详情|
| error_info | 	object |	|	返回信息对象|
|　└ errno |	number |	1	 | 错误代码|
|　└ error |	string |	"程序正常执行" |	错误详情|




## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=addCourseLabels HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=e98b01228fca036bf2ab060f7a8a6ec3&timeStamp=1493725870&courseList=[{"customColumn":"1","courseId":135120,"labelIds":[2,6,8]},{"customColumn":"2","courseId": 135121,"labelIds": [4,7,12]}]
```


 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d 'courseList=[{"customColumn":"1","courseId":135120,"labelIds":[2,6,8]},{"customColumn":"2","courseId":135121,"labelIds":[4,7,12]}]' \
      "https://root_url/partner/api/course.api.php?action=addCourseLabels"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "data": [
        {
            "customColumn": "1",
            "courseId": 288325,
            "errno": 1,
            "error": "程序正常执行"
        },
        {
            "customColumn": "2",
            "courseId": 288323,
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
| 147 | 表示没有此课程信息
| 149 | 表示该课程已经删除
| 358 | 表示部分标签不存在或已删除
| 359 | 表示部分标签不属于本机构
| 399 | 表示超出课程标签数量上限
