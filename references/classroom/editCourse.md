# 编辑课程
编辑课程，需要提供 SID，safekey，timeStamp，课程 ID，新的文件夹 ID，新的课程名称，过期时间，班主任账号，是否加入教师列表，课程封面图片，课程简介，教室设置 ID（主要用来设置教室皮肤等其他选项），禁言，班主任 UID，allowAddFriend，allowStudentModifyNickname；其中 SID，safekey，timeStamp，courseId 是必填项，其他参数需要修改那个就传递那个。返回执行后的说明。<br>


**备注：**
1. 可以对课程设置班主任。课程的班主任能够在（PC&Android&iOS）客户端进行管理班级（例如：创建/编辑/删除课节及学生、以及结束课程等）。请注意：班主任在客户端的操作行为，其数据不会返回至您的对接系统里（例如，班主任通过客户端创建的课节，该课节信息不回同步至您的系统里）。
2. 不支持删除课程班主任，一旦设置了班主任，则只支持修改。当传参mainTeacherUid为空时（即""），等效于不传，表示不做任何修改。


## URL

`https://root_url/partner/api/course.api.php?action=editCourse`

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
| courseId |	是 |	无 |	课程 ID |	无|
| folderId |	否 |	无 |	新的资源文件夹 ID |	更新课程云盘 folderId 时：<br>（1）如果该课程下未开课的课节绑定的云盘资源与课程下原有云盘资源相同，则同时更新此课节绑定的云盘资源。<br>（2）如果该课程下未开课的课节绑定的云盘资源与课程下原有云盘资源不相同，则不更新此课节绑定的云盘资源。|
| courseName |	否 |	1-40位字符，不区分中英文，超过40个字符会自动截取为40个 |	新的课程名称 |	无 |	
| expiryTime |	否 | 过期时间传空，不修改；传0，修改成永不过期；传非0的时间戳，则修有效期为传过来的时间；如果设置有效期，则有效期只能传当前时间5年之内的时间戳 |	过期时间 | 如果后继创建课节，有效期会按课节时间顺延3个月;<br>Unix Epoch 时间戳（秒单位）|
| mainTeacherUid | 否 | 无 | 班主任 UID | 注册用户接口返回的用户 UID  |
| subjectId | 否 | 不传或不符合规则的值默认为0，该字段仅支持中小学课程  | 课程学科分类 | 0:空; 1:语文; 2:数学; 3:英语; 4:物理; 5:化学; 6:生物; 7:政治; 8:历史; 9:地理; 10:思想品德; 11:音乐; 12:体育; 13:美术; 14:通用技术; 15:信息技术; 16:科学; 99:其他学科  |
| catId | 否 | 该字段仅支持中小学课程 | 课程组织架构ID | 设置课程组织架构归属，需同时传courseName | 
| stamp | 否 | 1加入，2不加入，默认为1 | 原班主任是否加入教师列表 | 无|
| Filedata | 否 | 二进制流 | 上传的课程封面图片 | 无|
| courseIntroduce | 否 | 0-400个字符，超过400会自动截取为400字 | 课程简介 | 无|
| classroomSettingId | 否 | 不传默认为0 | 教室设置 ID | 教室设置 ID 查找方式：登录到  eeo.cn 后台，找到机构设置，教室设置，每套教室设置上会显示教室设置 ID；选择此套设置后，该课程下所有教室内会依照此设置展示。<br/> 教室设置包含：A. 教室皮肤，B. 开关设置（头像下方工具栏、聊天窗口、学生端花名册，课后评价，教室工具箱，云盘等），C. 参数设置（录课倒计时，教室聊天时间间隔等）|
| allowAddFriend | 否 | tinyint，最大长度1 | 无 | 是否允许班级成员在群里互相添加好友，0=不允许，1=允许，传非0或非1报参数错误，不传则不设置 |
| allowStudentModifyNickname | 否 | tinyint，最大长度1 | 无 | 是否允许学生在群里修改其班级昵称，0=不允许，1=允许，传非0或非1报参数错误，不传不修改 |
| notAllowDeleteCourseStudentReplay | 否 | int  | 不传不修改，传错报【参数错误】 | 是否不允许离开班级的学生或班级解散后，可查看课程内容	0=否（允许），1=是（不允许） |

## 响应参数

| key | 类型 | 示例值 | 含义|
| ----|-----|-----| ----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

- HTTP 请求

```http
POST /partner/api/course.api.php?action=editCourse HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=f834fff59eb3bc8a2ff26a3cb59155f0&timeStamp=1492792399&courseId=352861&folderId=22419&courseName=Today+is+a+good+day&expiryTime=&mainTeacherUid=1001001&Filedata=@~/photo.jpg&courseIntroduce=ClassIn,真正专业的在线教室&classroomSettingId=235
```

- Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
       -d "SID=1234567" \
       -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
       -d "timeStamp=1484719085" \
       -d "courseId=352861" \
       -d "folderId=22419" \
       -d "courseName=Today is a good day" \
       -d "expiryTime=1484811085" \
       -d "mainTeacherUid=1001001" \
       -d "stamp=2" \
       -d "Filedata=@~/photo.jpg" \
       -d "courseIntroduce=ClassIn,真正专业的在线教室" \
       -d "classroomSettingId=235" \
       -d "allowAddFriend=1" \
       -d "allowStudentModifyNickname=0" \
       "https://root_url/partner/api/course.api.php?action=editCourse"
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
| 103 | 表示图片放入服务器失败
| 104	| 表示操作失败（未知错误）
| 114	| 表示服务器异常
| 144	| 表示机构下无此课程
| 147	| 表示无此课程信息
| 149	| 表示该课程已删除
| 151	| 表示过期时间至少要1天以后
| 152	| 过期时间不能小于最后一节课的结束时间
| 153	| 表示课程已过期
| 154	| 表示过期时间只能是5年以内的时间
| 160	| 表示机构下无此云盘目录
| 260 | 表示添加班主任失败
| 310 | 表示新班主任不存在
| 311 | 表示课程下的学生不能添加为班主任
| 312 | 表示课程下的旁听不能添加为班主任
| 314 | 表示原班主任有未上完的课节，不能更换
| 331 | 表示班主任账号格式不正确
| 334 | 表示班主任不是本机构的老师
| 369 | 该课程/课节类型暂不支持该操作
| 371 | 表示教室设置不存在
| 373 | 表示教室设置不属于本机构
| 389 | 表示班主任已被停用
| 400 | 表示请求数据不合法
| 805 | 表示班主任被停用中
| 883 | 班主任帐号已注销 
