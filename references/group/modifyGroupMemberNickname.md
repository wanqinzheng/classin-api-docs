# 修改群成员的班级昵称

修改群成员的班级昵称，需要传参 SID，safekey，timeStamp，课程ID。

每创建一个标准课程时，系统会自动创建一个班级群（可以在 ClassIn IM 查看此群）。创建班级群时，系统默认地使用 **用户昵称** 来设置群成员的名字，我们称之为 **班级昵称**。

接口功能描述：此接口用课程下所有学生和旁听生，在机构下的学生姓名（eeo管理后台设置的名字），来修改群里学生和旁听生的 **班级昵称**。修改后，学生在客户端的 IM 班级群里，以及该课程下的教室里上课时，显示的名字均为学生姓名，而非用户昵称。

此接口解决了，学生在ClassIn客户端修改用户昵称后，老师经常在群里和教室里上课时，对不上号的问题。

推荐使用场景：在创建好课程，以及添加好课程学生/旁听生后，再调用此接口来修改课程下所有学生和旁听生的 **班级昵称**。

## URL

`https://root_url/partner/api/course.api.php?action=modifyGroupMemberNickname`  

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
| courseId | 是 | 无 | 课程 ID | 无 |

## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- |---- |-----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|




## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=modifyGroupMemberNickname HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=1234567&safeKey=0f7781b3033527a8cc2b1abbf45a5fd2&timeStamp=1484719085&courseId=561294
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "courseId=561294" \
      "https://root_url/partner/api/course.api.php?action=modifyGroupMemberNickname"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "error_info": {
        "errno": 1,
        "error": "程序正常执行"
    }
}
```


## 错误码说明

| 错误码 |	说明|
|:-------|-----|
| 1 | 程序正常执行 |
| 100 | 参数不全或错误 |
| 102 | 无权限（安全验证没通过） |
| 104 | 操作失败/未知错误 |
| 144 | 机构下无此课程 |
| 147 | 没有此课程信息 |
| 149 | 该课程已经删除 |
| 153 | 该课程已过期 |
| 842 | 修改成员班级昵称部分失败 |
| 843 | 修改成员班级昵称全部失败 |
| 21323 | 表示已删除的学生不支持修改班级昵称
