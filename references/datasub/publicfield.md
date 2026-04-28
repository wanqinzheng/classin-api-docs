# 数据公共字段

公共字段可能出现在不同类型的消息记录中，除非特殊说明，否则将代表相同的意义

| 参数名 | 类型 | 含义 |
| --- | --- | --- |
|SID|Int64|机构ID
|CourseID|Int64|课程ID
|ClassID|Int64|课节ID
|Cmd|Int32或String|消息类型
|CloseTime|Int64|课节关闭时间（包括固定20分钟拖堂时间）
|StartTime|Int64|课节开始时间（不包括可以提前进教室的时间）
|_id|String|消息标识
|TimeStamp|Int64|机构认证时间戳|
|SafeKey|String|机构认证安全密钥md5(SECRET + TimeStamp)|
|Identity|Int32|用户身份 1：学生，2：旁听，3：老师，4：联席教师，193：机构校长，194：校长助理|



## 其他常见字段

|参数名 | 类型 | 含义
|----|------|----
|ActionTime|Int64|动作时间戳
|SourceUID|Int64|发起用户ID，0 表示没有发起人，是服务产生的消息
|TargetUID|Int64|目标用户ID，0 表示没有目标人，实际目标是教室所有用户
