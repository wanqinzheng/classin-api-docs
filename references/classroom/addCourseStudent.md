# 课程下添加学生/旁听（单个）
课程下添加学生/旁听(单个)，需要 SID，safekey，timeStamp，课程 ID，学生和旁听的识别(1为学生，2为旁听)，需要添加的账号，需要添加的名称、学生UID等。返回执行后的说明。该课程下添加的学生可以上该课程下的所有课节。**备注：旁听人数默认最多可添加 20 人。**

**备注**：<br>
如果您的 eeocn 机构管理后台开关 **将新加入课程的学生的后台姓名同步设为其ClassIn班级昵称** （设置路径为：机构设置 - 班级设置 - 同步班级昵称设置）为开启状态，调用此接口添加学生/旁听生后，系统会用新添加成员在机构下的姓名，来修改其在群里的**班级昵称**。修改后，学生在客户端的 IM 班级群里，以及该课程下的教室里上课时，显示的名字均为学生姓名，而非用户昵称。<br>
此开关的开启，解决了学生在ClassIn客户端修改用户昵称后，老师经常在群里和教室里上课时，对不上号的问题。<br>
请注意：当这个开关开启时，调用本接口时会有极小概率出现 841 错误码，此时推荐您再调用接口 [修改群成员的班级昵称](../group/modifyGroupMemberNickname.md)。

## URL

`https://root_url/partner/api/course.api.php?action=addCourseStudent`

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
| courseId |	是 | 无 |	课程 ID |	无|
| identity |	是 | 无 |	学生和旁听的识别(1 为学生,2 为旁听) |	无|
| studentUid | 是 | 无 | 学生 UID | 注册用户接口返回的用户 UID|
| studentName |	否 | 1-24字，不区分中英文，超过24会自动截取为24字 |	机构后台旁听生的姓名 | 仅用于当identity为2（旁听身份）时，才使用此参数。当identity为2时，如果没有传此参的话，则使用手机号码作为旁听生的名字 |


## 响应参数

| key | 类型 | 示例值 | 含义|
| ----|----|----| ----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=addCourseStudent HTTP/1.1
Host: www.eeo13.test
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=1002289&safeKey=bd53aabe936c69a85f3d2e329ab8e080&timeStamp=1493030202&courseId=1431&identity=1&studentUid=1001001
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "courseId=442447" \
      -d "identity=1" \
      -d "studentUid=1001001" \
      "https://root_url/partner/api/course.api.php?action=addCourseStudent"
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
| 1   | 表示成功执行
| 100	| 表示参数不全或错误
| 102	| 表示无权限（安全验证没通过）
| 104 |	表示操作失败（未知错误）
| 113	| 表示手机账号未注册
| 114	| 表示服务器异常
| 129	| 表示老师不能添加为学生
| 130	| 表示超过能添加的帐号数量
| 134	| 表示手机号不合法
| 144	| 表示机构下无此课程
| 147	| 表示无此课程信息
| 149	| 表示课程已删除
| 153	| 表示课程已过期
| 155 | 表示学生数组不可为空
| 163	| 表示课程下已存在此学生
| 164	| 表示课程下已存在此旁听
| 174	| 表示老师不能添加为旁听
| 228 | 机构下无此学生 |
| 332 | 课程老师或联席教师不能添加为课程学生或旁听
| 333 | 班主任不能添加为课程学生
| 369 | 该课程/课节类型暂不支持该操作
| 400 | 表示请求数据不合法
| 841 | 表示成员添加成功，班级昵称同步失败 |
| 886 | 学生帐号已注销 |
| 887 | 旁听帐号已注销 |

