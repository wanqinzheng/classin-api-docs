# ClassIn API 文档总目录

> 本文件是 ClassIn API 知识库的入口索引。加载技能时优先读取此文件，根据用户问题定位对应模块文档。

---

## 文档模块列表

| 模块 | 文件夹 | 主要内容 |
|------|--------|----------|
| 概述 | `/` | 系统概述、API 调用流程、名词解释 |
| 用户管理 | `user/` | 注册用户、添加老师/学生、修改密码、启用停用 |
| 课程课节 | `classroom/` | 创建/编辑/删除课程、创建/修改/删除课节、学生管理 |
| LMS | `LMS/` | 单元管理、活动创建、发布活动、成员管理 |
| 云盘 | `cloud/` | 文件夹操作、文件上传/删除/重命名、课件授权 |
| 消息订阅 | `datasub/` | 订阅说明、实时推送、课后推送、机构维度数据 |
| 直播录制 | `broadcast/` | 录课设置、直播地址、回放地址、视频删除 |
| 机构管理 | `school/` | 机构标签、学校设置 |
| 班级群 | `group/` | 群成员昵称修改 |
| 双师课 | `onlineDoubleTeacher/` | 创建/编辑/删除在线双师课节 |
| 对接方案 | `Solutions/` | 快速入门、大直播方案、唤醒客户端最佳实践 |
| 错误处理 | `Error-Handling/` | 对接前、排课、接口调试常见问题 |
| 附录 | `appendix/` | API v2 签名、签名代码示例、参数规则、修订记录 |

---

## 快速关键词索引

### 鉴权相关
- 签名、AppKey、AppSecret、safeKey → `appendix/signature.md`, `appendix/sign_demo.md`

### 入门
- 快速开始、第一次对接 → `Solutions/BasicScenario.md`, `appendix/Gettingstartedguide.md`

### 用户管理
- 注册用户 → `user/register.md`
- 批量注册 → `user/registerMultiple.md`
- 添加学生 → `user/addSchoolStudent.md`
- 添加老师 → `user/addTeacher.md`
- 修改密码 → `user/modifyPasswordByTelephone.md`
- 停用/启用老师 → `user/stopUsingTeacher.md`, `user/restartUsingTeacher.md`

### 课程管理
- 创建课程 → `classroom/addCourse.md`
- 编辑课程 → `classroom/editCourse.md`
- 结束课程 → `classroom/endCourse.md`

### 课节管理
- 创建课节（单个） → `classroom/addCourseClass.md`
- 创建课节（多个） → `classroom/addCourseClassMultiple.md`
- 修改课节 → `classroom/editCourseClass.md`
- 删除课节 → `classroom/delCourseClass.md`
- 修改上台人数 → `classroom/modifyClassSeatNum.md`
- 更换老师 → `classroom/modifyCourseTeacher.md`

### 学生管理
- 课程下添加学生 → `classroom/addCourseStudent.md`, `classroom/addCourseStudentMultiple.md`
- 课程下删除学生 → `classroom/delCourseStudent.md`, `classroom/delCourseStudentMultiple.md`
- 课节下添加学生 → `classroom/addClassStudentMultiple.md`
- 课节下删除学生 → `classroom/delClassStudentMultiple.md`

### LMS
- 创建单元 → `LMS/createUnit.md`
- 创建课堂活动 → `LMS/createClassroom.md`
- 发布活动 → `LMS/releaseActivity.md`

### 云盘
- 获取文件夹列表 → `cloud/getFolderList.md`
- 上传文件 → `cloud/uploadFile.md`
- 创建文件夹 → `cloud/createFolder.md`

### 直播录制
- 设置录课/直播/回放 → `broadcast/setClassVideoMultiple.md`
- 获取播放地址 → `broadcast/getWebcastUrl.md`

### 消息订阅
- 订阅说明 → `datasub/description.md`
- 课节内实时推送 → `datasub/details.md`
- 课节结束后推送 → `datasub/classrelated.md`

### 错误排查
- 对接前问题 → `Error-Handling/pre-integration.md`
- 接口调试问题 → `Error-Handling/Basic_errors.md`
- 排课问题 → `Error-Handling/Lesson_errors.md`

---

## API 通用信息

- **Base URL**：`https://root_url/partner/api/`
- **编码格式**：UTF-8
- **鉴权方式**：safeKey 签名，`safeKey=MD5(SECRET+timeStamp)`
- **请求方式**：POST（部分接口支持 GET）
- **Content-Type**：`application/x-www-form-urlencoded` 或 `application/json`
