# 创建课程
创建课程，需要提供 SID，safekey，timeStamp，课程名称，可用文件夹 ID，课程封面图片(二进制流)，过期时间，班主任账号，课程简介，教室设置 ID（主要用来设置教室皮肤等其他选项），唯一标识，班主任 UID，allowAddFriend，allowStudentModifyNickname；其中SID、safeKey、timeStamp、课程名称是必填项。返回的是课程 ID 及执行后的说明。<br>
机构传入唯一标识后，该接口会校验已创建课程中是否有此唯一标识，如果有，则返回之前创建成功的课程 ID。如果没有，则正常执行。

每创建一个标准课程时，系统会自动创建一个班级群（可以在 ClassIn IM 查看此群）。创建班级群时，系统默认地使用 **用户昵称** 来设置群成员的名字，我们称之为 **班级昵称**。<br>
如果您希望把用户姓名同步至班级昵称的话，可以在创建好课程，以及添加好课程学生/旁听生后，再调用接口 [修改群成员的班级昵称](../group/modifyGroupMemberNickname.md) 来修改课程下所有学生和旁听生的 **班级昵称**。


**备注：**
1. 可以对课程设置班主任。课程的班主任能够在（PC&Android&iOS）客户端进行管理班级（例如：创建/编辑/删除课节及学生、以及结束课程等）。请注意：班主任在客户端的操作行为，其数据不会返回至您的对接系统里（例如，班主任通过客户端创建的课节，该课节信息不回同步至您的系统里）。
2. 当传参mainTeacherUid为空时（即""），等效于不传，表示不设置课程班主任。


## URL 

`https://root_url/partner/api/course.api.php?action=addCourse`


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
| courseName |	是 |	1-90位字符，不区分中英文，超过会自动截取为90字 |	课程名称 |	无|
| folderId |	否	| 不传则默认空目录 |	可用资源文件夹 ID |	无|
| Filedata |	否 |	二进制流 | 上传的课程封面图片 |	当此字段为空时，且设置了学校的默认课程封面，则会使用默认封面作为课程的封面<br>设置学校的默认课程封面的方法：登录到  eeo.cn 后台，点击左侧导航：学校设置 -- 基本设置 |
| expiryTime |	否 |	过期时间不传、传0、传空均当成0，课程过期时间设置为永不过期；如果设置有效期，则有效期只能传当前时间5年之内的时间戳 |	过期时间 |	如果后继创建课节，有效期会按课节时间顺延3个月;<br>Unix Epoch 时间戳（秒单位）|
| mainTeacherUid | 否 | 班主任uid，不传以及传空都不设置班主任 | 班主任 UID | 注册用户接口返回的用户 UID  |
| subjectId | 否 | 不传或不符合规则的值默认为0，该字段仅支持中小学课程 | 课程学科分类 | 0:空; 1:语文; 2:数学; 3:英语; 4:物理; 5:化学; 6:生物; 7:政治; 8:历史; 9:地理; 10:思想品德; 11:音乐; 12:体育; 13:美术; 14:通用技术; 15:信息技术; 16:科学; 99:其他学科 | 
| catId | 否 | 该字段仅支持中小学后台课程 | 课程组织架构ID | 设置课程组织架构归属 | 
| courseIntroduce | 否 | 0-400个字符，超过会自动截取为400字 | 课程简介 | 无|
| classroomSettingId | 否 | 不传默认为0 | 教室设置 ID | 教室设置 ID 查找方式：登录到  eeo.cn 学校后台，点击左侧导航：我的学校 -- 学校设置 -- 教室设置，每套教室设置上会显示教室设置 ID；选择此套设置后，该课程下所有教室内会依照此设置展示。<br/> 教室设置包含：A. 教室皮肤，B. 开关设置（头像下方工具栏、聊天窗口、学生端花名册，课后评价，教室工具箱，云盘等），C. 参数设置（录课倒计时，教室聊天时间间隔等）|
| courseUniqueIdentity | 否 | 例如： 45s8d5a6asaa1ssf（1-32 位字符，不符合规则的值接口会返回 100 错误） | 唯一标识  | 机构可传唯一标识，传入此值后，我们会检验已创建课程中是否有该唯一标识|
| allowAddFriend | 否 | tinyint，最大长度1 | 无 | 是否允许班级成员在群里互相添加好友，0=不允许，1=允许<br>传非0或非1报参数错误<br>不传则使用设置项 **允许班级成员互相添加好友默认开启状态设置** （设置项入口：登录eeocn学校后台 -- **学校设置** -- **班级设置**）的值 |
| allowStudentModifyNickname | 否 | tinyint，最大长度1 | 无 | 是否允许学生在群里修改其班级昵称，0=不允许，1=允许，传非0或非1报参数错误，不传默认0 |
| notAllowDeleteCourseStudentReplay | 否 | int  | 不传不修改，传错报【参数错误】 | 是否不允许离开班级的学生或班级解散后，可查看课程内容	0=否（允许），1=是（不允许） |

## 响应参数

| key | 类型 | 示例值 | 含义|
| ----|-----|-----| ----|
| data | number	| 352861 |	创建成功返回的课程 ID|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|


## 示例

- HTTP 请求

```http
POST /partner/api/course.api.php?action=addCourse HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=f834fff59eb3bc8a2ff26a3cb59155f0&timeStamp=1492792399&courseName=Good+Day&folderId=22419&Filedata=@~/photo.jpg&expiryTime=1492795000&mainTeacherUid=1001001&courseIntroduce=ClassIn，真正专业的在线教室&classroomSettingId=235&courseUniqueIdentity=532512
```

- Shell cURL模拟请求指令

```bash
curl -X "POST" \
     -d "SID=1234567" \
     -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
     -d "timeStamp=1484719085" \
     -d "courseName=Good Day" \
     -d "folderId=22419" \
     -d "Filedata=@~/photo.jpg" \
     -d "expiryTime=1523428688" \
     -d "mainTeacherUid=1001001" \
     -d "courseIntroduce=ClassIn，真正专业的在线教室" \
     -d "classroomSettingId=235" \
     -d "courseUniqueIdentity=24545" \
     -d "allowAddFriend=1" \
     -d "allowStudentModifyNickname=0" \
     "https://root_url/partner/api/course.api.php?action=addCourse"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": 352861,
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
| 103	| 文件上传到服务器失败
| 104 | 表示操作失败
| 114 | 表示服务器异常
| 151 | 表示过期时间至少要一天以后
| 154 | 表示过期时间只能是5年以内的时间
| 160 | 表示机构下无此云盘目录
| 260 | 表示添加班主任失败
| 331 | 表示班主任账号格式不正确
| 334 | 表示班主任不存在
| 389 | 表示班主任已被停用
| 371 | 表示教室设置不存在
| 373 | 表示教室设置不属于本机构
| 398 | 表示数据已经存在（唯一标识已存在）
| 400 | 表示请求数据不合法
| 460 | 表示课程或课节正在被其他请求创建（并发创建会遇到）
| 805 | 表示班主任被停用中
| 883 | 班主任帐号已注销 |


