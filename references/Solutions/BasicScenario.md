# 快速实现从同步用户到创建在线课堂  

ClassIn-API 最基本的对接方案。通过本文档您可以了解如何快速实现用户及排课数据的同步。  
本文档举例说明了当用户在您的平台注册并加入某个课堂的过程，平台后端怎么调用一系列对应接口，将用户、排课数据同步到 ClassIn 平台的过程。  
**注：本方案仅限于实现快速对接，以满足平台通过API同步数据的目的。为了更好的衔接您的平台与 ClassIn，需完善相关数据修改、删除的操作。**

##  数据同步须知

- **API 对接，数据为单向同步，即您平台→ eeo，eeo 的操作数据不会反向同步至您平台；eeo 目前没有获取相关数据的接口，为避免两个系统数据不对称问题；我们有以下建议供您参考**  

  **1. 平台方需主动存储相关数据（包括不限于用户ID、课程ID、课节ID等）至平台数据库；**  
  **2. eeo.cn 后台机构子账号非必要不给予“课程中心”权限；**  
  **3. 课程非必要不设置班主任；**  
  **4. 中小学后台非必要不给予教师“客户端建班/公开课”权限；**  

## 一 添加用户

在给用户安排课程前应提前处理用户数据，并将用户注册添加到 eeo；UID 是用户在 ClassIn 的唯一标识，UID 可以在学校下同时拥有多种身份，例如机构教师、学生、后台子账号等等；

#### 1.1 流程说明

  - 调用注册接口获取用户 UID，具体参考[注册用户](https://docs.eeo.cn/api/zh-hans/user/register.html)，并传入 addToSchoolMember 参数将用户添加为对应的身份；
  - 添加用户身份还可以调用[添加老师](https://docs.eeo.cn/api/zh-hans/user/addTeacher.html)、[添加学生](https://docs.eeo.cn/api/zh-hans/user/addSchoolStudent.html)接口。推荐只使用注册用户接口完成注册并添加老师/学生身份；

#### 1.2 注意事项

  - **用户账号已注册 ClassIn 时，传入 addToSchoolMember，此时用户仍会被添加至机构后台并赋予对应身份，但账号密码、头像、昵称不会被重置；**  
  - **添加接口（添加老师、添加学生）返回的 data 为用户和学校的关系 ID，排课时不应使用该参数，需使用注册接口返回的 UID；** 

## 二 排课

#### 2.1 场景一：学校排课

- 由学校管理员或者老师预先在您的平台创建好课程，安排课程学生，并进行课节排课，学生只需要按课节时间在ClassIn进入在线教室进行上课即可。**请注意：排课行为应在[添加用户](#一-添加用户)完成后进行；**

  - **step 1** 根据平台课程（班级）信息，调用创建课程，参考[创建课程](https://docs.eeo.cn/api/zh-hans/classroom/addCourse.html)；  
  - **step 2** 将学生添加到课程下，参考[课程下添加学生/旁听（单个）](https://docs.eeo.cn/api/zh-hans/classroom/addCourseStudent.html)、[课程下添加学生/旁听（多个）](https://docs.eeo.cn/api/zh-hans/classroom/addCourseStudentMultiple.html)；  
  - **step 3 创建单元和课堂，参考[创建单元](../LMS/createUnit.md) 、[创建课堂](../LMS/createClassroom.md) ；

#### 2.2 场景二：约课平台排课

- **请注意：约课行为应在[添加用户](#一-添加用户)完成后进行；**

  - **step 1** 约课平台需为学生创建专属课程，参考[创建课程](https://docs.eeo.cn/api/zh-hans/classroom/addCourse.html)；  
  - **step 2** 将学生添加到专属课程下，参考[课程下添加学生/旁听（单个）](https://docs.eeo.cn/api/zh-hans/classroom/addCourseStudent.html)；  
  - **step 3** 根据学生的预约信息创建创建单元和课堂，参考[创建单元](../LMS/createUnit.md) 、[创建课堂](../LMS/createClassroom.md) ；
  - **step 4** 发生调课，可以针对单个课堂进行人员调整，参考[添加活动成员](../LMS/addStudent.md)、[删除活动成员](../LMS/deleteStudent.md)


#### 2.3 场景三  使用LMS学习系统创建课堂和其他活动

- 由学校管理员或者老师预先在您的平台创建好班级，注册班级学生，创建学习单元，并排好课堂，目前其他活动仍需在客户端创建或者从TeacherIn导入。创建成功后，学生只需要按课堂活动时间在ClassIn进入在线教室进行上课即可。**请注意：排课行为应在[添加用户](#一-添加用户)完成后进行；**

  - **step 1** 根据平台课程（班级）信息，调用创建课程（班级），参考[创建课程](https://docs.eeo.cn/api/zh-hans/classroom/addCourse.html)；  

  - **step 2** 将学生添加到课程（班级）下，参考[课程下添加学生/旁听（单个）](https://docs.eeo.cn/api/zh-hans/classroom/addCourseStudent.html)、[课程下添加学生/旁听（多个）](https://docs.eeo.cn/api/zh-hans/classroom/addCourseStudentMultiple.html)；  
  - **step 3** 创建单元及课堂，参考[创建单元](../LMS/createUnit.md)、[创建课堂](../LMS/createClassroom.md)；

  这个时候，课堂会出现在LMS的课程单元活动列表中。


 
## 问题：
### 我们是1v1的课程，对接后学生端出现了好多班级怎么回事？
这种情况应该是为每个学生的每个课节创建了一个课程。其实没有必要，如果是同一个学生，就用同一个课程即可。

