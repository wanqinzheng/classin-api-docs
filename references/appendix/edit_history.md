# 修订记录

## 6.0.5  2026年01月06日
**消息订阅**：[LMS活动相关的消息](../datasub/coursedata.md) 中作业成绩推送新增以下字段：
 - State: 40 已批阅; 50 已打回  

## 6.0.4  2025年11月24日
* 接口变化：新增错误码：101003002 重复请求。如果在5s内，接口传完全相同的参数，第二个及以后的请求会返回此错误码。    
涉及接口：[注册用户](../user/register.md)、[注册用户（多个）](../user/registerMultiple.md) 、[添加学生](../user/addSchoolStudent.md)、[添加老师](../user/addTeacher.md)接口



## 6.0.3  2025年10月30日
* 接口变化：课堂活动的单元改为非必填参数       
[创建课堂](../LMS/createClassroom.md) unitId 参数从必填改为非必填。 如果不传单元参数，则课堂会创建到无单元主题下 。
* 接口变化：[创建课堂](../LMS/createClassroom.md) 增加频次限制，不超过1000次/分钟

## 6.0.2  2025年9月4日
**消息订阅**：[LMS活动相关的消息](../datasub/coursedata.md) 新增以下数据：
 - 讨论活动的评论数据
 
 推送讨论活动所有的评论、回复和点赞。

## 6.0.1  2025年8月21日
* 接口变化：API支持设置OMO站播     
[创建课堂](../LMS/createClassroom.md)， [编辑课堂](../LMS/updateClassroom.md)接口新增参数：omoStationBroadcast，支持创建OMO站播课堂。


## 6.0  2025年5月27日

**ClassIn 6.0 重磅推出** 

ClassIn 6.0 明确了班级--课程--单元--活动的层级概念，下线了课节概念--所有课节都迁移为课堂，为此API对课节接口做了一系列兼容，**保证原有课节接口仍按正常逻辑创建和修改课节**（自动转为课堂），     

对课节类接口调用及班级概念变化说明如下：

* 原课节类接口包括：创建课节、修改课节信息，修改课节上台学生数，课节下添加学生，课节下删除学生接口，课节设置录课，直播回放。
* **原有课节类接口仍然可以继续调用并创建和修改直播课**，只是在app端不再显示为课节，而是显示为默认单元下的课堂活动。
* 机构不必为此修改任何接口代码。但是建议有能力的机构改为调用LMS创建课堂活动系列接口取代原课节类接口。因为原有接口不再支持新功能，新参数等变化。   
* 新的API LMS类接口创建课堂活动流程，参考 [创建一个直播课活动](../Solutions/CreateClassroom.md)
* 用户、班级、LMS、机构和云盘类接口内外部逻辑均保持不变。
* 因为历史原因，所有接口跟班级以及班级ID相关的参数、在文档及代码里的名词都叫“course/courseID”，因为涉及代码，这个单词我们不再更改。默认就是班级的意思。 而6.0新增的班级下course课程这个名词和概念，暂时在API里并没有涉及。所有的活动和单元，都会创建到班级的主课程下。

这次接口兼容的细节包括   

* 历史数据迁移：班级所有的课节都迁移为课堂，可以在班级的默认课程--默认单元--课堂活动 下找到这些历史课节（已转化为课堂）。
* 课节创建接口：继续可以调用，接口生成一个课堂活动，位于默认课程的默认单元下。仍然返回课节ID,可以用于后继的修改，删除等。
* 涉及到课节的接口可以通过课节ID继续调用，会操作该课节ID对应的课堂活动。相关接口包括：修改课节信息/删除课节/修改台上人数/增删改课节标签/课节设置录课、直播、回放/修改课节锁定状态/获取课节直播回放地址
* 添加/删除课节下学生接口：继续可以调用，作用跟之前一样，用于添加和删除课堂活动的插班生。
* 课堂类接口创建的课堂，请勿使用课节类接口编辑和操作。以免产生数据不一致的问题。


**另外，5月26日23点到5月27日6点会有停服升级维护。** 

届时ClassIn app、后台、API均不可使用。请机构合理安排平台接口调用和课节使用时间。谢谢支持

我们尽量保持API接口调用逻辑不变，如果您在使用中有遇到什么问题，请随时联系ClassIn技术支持。

**关于新对接机构**  

我们建议使用LMS相关接口，用课堂相关接口来替代原来的课节接口。 比如 创建单元--创建课堂活动，来替代原来的创建课节。 


## 5.4.11 2025年3月12日
**消息订阅**：[LMS活动相关的消息](../datasub/coursedata.md) 新增以下数据：
 - 作业提交信息推送
 - 答题卡成绩推送
 - 作业成绩推送优化新增部分字段  

## 5.4.10 2025年2月21日
**消息订阅**：[课节内实时推送消息](../datasub/details.md) 新增网页直播聊天消息推送，用户发送消息后触发实时推送

## 5.4.9 2025年2月20日
消息推送 [课后汇总](../datasub/classrelated.md)  新增字段“TotalNotDisabled”       
新字段在 "End" -> "equipmentsEnd" -> UID -> "Camera"  和  "Microphone" 结构下     
表示摄像头和麦克风处于开启状态的时间（不考虑是否在台上）

## 5.4.8 2025年2月18日
创建课节的时候如果课程下课节总数已经超过机构设置，会创建失败并返回错误码121601070  ，涉及接口：    
[创建课节](../classroom/addCourseClass.md)       
[创建课节（多个）](../classroom/addCourseClassMultiple.md)    
[创建课堂](../LMS/createClassroom.md)     
[创建新双师课](../onlineDoubleTeacher/addClass.md)

## 5.4.7  2024年12月19日
新增添加课程老师接口    
- [添加课程老师](../classroom/addCourseTeacher.md)

优化部分课程课节相关接口对双师课的处理
- [更换课程老师](../classroom/modityCourseTeacher.md)  
如果课程下的课节是双师主或子课节，会报错，该课节不予更换老师,如需更换，需要调用双师相关接口 [编辑在线双师课节](../onlineDoubleTeacher/editClass.md)  
- [课节下添加学生](../classroom/addCourseClassStudent.md) 及 [课节下删除学生](../classroom/delClassStudentMultiple.md)    
不限制双师主子课节，以便为主子课节添加插班生或者调出生。



## 5.4.6 2024年11月26日
* 新增在线双师接口：您可以参考[【在线双师课节】](https://help.eeo.cn/docs/kua-ban-lian-ke-zai-xian-shuang-shi-ke-shi-yong-shuo-ming?search=1)了解功能或者咨询业务经理了解  
[创建在线双师课节](../onlineDoubleTeacher/addClass.md)  
[编辑在线双师课节](../onlineDoubleTeacher/editClass.md)  
[删除在线双师课节](../onlineDoubleTeacher/deleteClass.md)  

* 新增同步学生班级昵称接口：
[同步学生班级昵称](../user/modifyCourseStudentNickName.md)  此接口支持将后台“学生管理-姓名”同步到学生所在班级

## 5.4.5 2024年11月
* 新增接口：
[创建非课堂活动](../LMS/createActivityNoClass.md)
通用创建活动草稿接口（课堂活动除外）。

* 接口变化：
[添加活动成员](../LMS/addStudent.md) 接口  已可以支持课堂插班生


## 5.4.4 2024年10月
[测验结果消息](../datasub/coursedata.md)  
新增题目得分明细。 详细字段请看文档说明。


## 5.4.3 2024年9月
[ClassIn下载按钮链接](../iframe.md)  更新js脚本地址。    
代码里原js地址已不可用，我们用新的地址替换原地址，需要您进行更新。


## 5.4.2  2024年10月
云盘接口变化：eeo产品中，原云盘由学校资料改为组织云盘。适配如下
* 原“学校资源”文件统一迁移到组织云盘--“学校资源”文件夹。但原文件夹和文件ID保持不变。之后接口上传的文件对应会传到组织云盘--学校资源相关目录
* 上线之前由接口[获取顶级文件夹 ID](../cloud/getTopFolderId.md)获取的ID，在上线数据迁移之后，不再是组织云盘的顶级ID，而是组织云盘-学校资料文件夹的ID。可以再次获取，得到组织云盘的顶级ID。
* 如果机构尚未初始化组织云盘，第一次调用[获取顶级文件夹 ID](../cloud/getTopFolderId.md) 接口时，将会自动初始化机构组织云盘。

## 5.4.1  2024年9月12日
新增修改新进学生、退出班级学生查看回放、活动权限的接口和参数
* 新增接口：[修改学校设置](../school/editSchoolSettings.md)
* 新增参数：[创建课程](../classroom/addCourse.md)、[修改课程](../classroom/editCourse.md)  接口新增 notAllowDeleteCourseStudentReplay 参数

## 5.4  2024年9月12日
新增 LMS 系列接口。包括单元和活动通用接口，以及课堂活动相关接口。涉及改动有几点
* LMS 系列接口将使用新的接口调用方式，包括接口链接形式、接口数据签名规则，详见[这里](APIv2Intro.md)
* 单元、活动通用接口，包括 [创建单元](../LMS/createUnit.md)、[编辑单元](../LMS/updateUnit.md)、[删除单元](../LMS/deleteUnit.md)、[发布活动](../LMS/releaseActivity.md)、[删除活动](../LMS/deleteActivity.md)、[移动活动](../LMS/moveActivity.md)、[活动下添加学生](../LMS/addStudent.md)、[活动下删除学生](../LMS/deleteStudent.md) 
* 课堂活动类接口包括[创建课堂活动](../LMS/createClassroom.md)、[编辑课堂活动](../LMS/updateClassroom.md) 
* 课堂相关接口将取代原课节系列接口。ClassIn课节概念将逐渐被课堂代替。使用互动教室功能，建议不再对接课节，而是直接创建单元、课堂活动
* 用户、班级等相关接口保持不变。
* 一个完整的对接，将包括老接口：[注册用户](../user/register.md)、[创建课程/班级](../classroom/addCourse.md)、[添加班级学生](../classroom/addCourseStudent.md)，
以及v2新接口：[创建单元](../LMS/createUnit.md)、[创建课堂](../LMS/createClassroom.md)。原 [创建课节](../classroom/addCourseClass.md)接口不再推荐使用。


## 5.3.3 2024年8月30日
新增废弃接口：
* `修改教师授权云盘的课件资源`：接口 updateTeacherCloudFolders 将于 2024-08-30 日后下线。

## 5.3.2 2024年7月31日
创建课程和修改课程：课程过期时间限制由1年内，改为5年内。     
涉及以下接口：    
- [创建课程](../classroom/addCourse.md)     
- [修改课程](../classroom/editCourse.md) 


## 5.3.1 2024年7月30日
因业务逻辑变更，消息订阅 - [客户端回放观看统计](https://docs.eeo.cn/api/zh-hans/datasub/classrelated.html#%E5%AE%A2%E6%88%B7%E7%AB%AF%E5%9B%9E%E6%94%BE%E8%A7%82%E7%9C%8B%E7%BB%9F%E8%AE%A1)（cmd：ClientPlaybackDataDetail）将做如下改动：

（1）去除 TopProcess 、TotalLookCount、TotalLookTime 字段。

（2）新增 视频总时长（TotalDuration）、有效观看次数（ValidWatchCount）、最新详情LatestDetails->TriggerType 1,3,4, 分别表示开始观看、结束观看、超时自动推送字段。

- 其中最新详情 LatestDeatils->TriggerType 当前仅支持“结束观看”，需要在9月份客户端新版本中才能支持“开始观看”。

## 5.3.0 2024年7月26日
新增[LMS活动消息推送](../datasub/coursedata.md)，包括两项内容
* 作业成绩推送：在作业批阅后推送作业批阅者、学生和成绩（总分）
* 测验成绩推送：在测验批阅后推送测验批阅者、学生和成绩（总分）

## 5.2.1 2024年4月24日
新增通过链接唤起 ClassIn 客户端后，直接进入班级LMS活动页面。详见 [唤醒 ClassIn 客户端的最佳实践](../Solutions/wakeUpClassIn.md) 。

## 3.44 2024年01月10日
消息订阅：[课节内实时推送消息](../datasub/details.md)，退出教室Reason字段新增退出原因码：
- 54：客户端本机重复登陆
- 56：服务端与客户端网络连接中断
- 60：被新登录的客户端挤下线
- 101：按返回键退出（仅安卓设备）
- 102：来电话退出
- 111：App进入后台


## 3.43 2023年12月07日
客户端回放观看统计消息新增TotalLookVaildTime字段，即用户本次观看回放的实际观看覆盖时长，涉及页面如下：
* [课节结束后推送的消息](../datasub/classrelated.md)

## 3.42 2023年08月10日
[创建课节(单个)](../classroom/addCourseClass.md) 、[创建课节(多个)](../classroom/addCourseClassMultiple.md)、[修改课节信息](../classroom/editCourseClass.md) 新增错误码：
- 121601001 存在当前版本不支持的设置项
- 121601002 操作成功，\[在线教室\]资源已超出用量，为防止业务受影响，请尽快联系客户经理
- 121601003 您当月累计创建课节已达当月上限，无法继续创建，升级账号获取更多权益
- 121601004 您当月累计创建课节已达当月上限，无法继续创建
- 121601005 不支持设网页直播
- 121601006 不支持设置录制现场
- 121601007 台上人数参数错误
- 121601008 不支持设置联席教师
- 121601009 不支持设置网页回放
- 121601010 不支持设置录课
- 121601011 不支持设置双摄模式
- 121601012 清晰度超出限制

## 3.41 2023年07月07日
##### 一、 消息订阅课节实时推送中的进出教室字段新增ClientID字段，以便于用户通过双端登录后，区分主副端，涉及页面如下：
* [课节内实时推送的消息](../datasub/details.md)

##### 二、 消息订阅课后汇总中进出教室新增字段 Deputies，该字段代表副端（双端进入教室后，会出现该字段，默认原有的 Details 里只有主端的进出教室记录），目前仅双端登录，所以只会体现一个副端的数据，涉及页面如下：
* [课节结束后推送的消息](../datasub/classrelated.md)

##### 三、 注册用户接口功能新增无论是否已注册用户，传入 addToSchoolMember 后都会将其添加到机构下，涉及页面如下：
* [注册用户](../user/register.md)
* [注册用户（多个）](../user/registerMultiple.md)

## 3.40  2023年06月12日

##### 一、 上传文件接口新增错误码 31000，表示存储已满，请删除部分文件或扩容
* [上传文件](../cloud/uploadFile.md)

##### 二、 直播聊天室免二次登录拼接域名由 `www.eeo.cn` 修改为 `live.eeo.cn`，拼接链接后缀由 `.php` 修改为 `.html`
* [创建课节](../classroom/addCourseClass.md)
* [创建课节（多个）](../classroom/addCourseClassMultiple.md)
* [获取课程直播/回放播放器地址](../broadcast/getWebcastUrl.md)

## 3.39  2023年03月21日

##### 一、对接最佳实践中心新增 唤醒ClassIn客户端方案，涉及页面如下：

* [唤醒ClassIn客户端的最佳实践](../Solutions/wakeUpClassIn.md)  

##### 二、新增数据同步说明，数据为单向同步，即您平台→eeo，eeo的操作数据不会反向同步至您平台；涉及页面如下：  
* [快速实现从同步用户到创建在线课堂](../Solutions/BasicScenario.md)

## 3.38  2023年01月10日

##### 一、新增课程学科字段subjectId，不传或传不符合规则的值则为空，该字段仅支持中小学后台课程；涉及接口如下：

* 接口 [创建课程](../classroom/addCourse.md)  
* 接口 [编辑课程](../classroom/editCourse.md)


##### 二、lms活动只允许在ClassIn客户端操作，相关接口新增错误码：466=通过客户端-创建课堂产生的课节只能在客户端编辑，涉及接口如下：
* 接口 [修改课节信息](../classroom/editCourseClass.md)  
* 接口 [修改课节上台学生数](../classroom/modifyClassSeatNum.md)  
* 接口 [删除课节](../classroom/delCourseClass.md)  
* 接口 [课节下添加学生（多个）](../classroom/addClassStudentMultiple.md)  
* 接口 [课节下删除学生（多个）](../classroom/delClassStudentMultiple.md)  
* 接口 [课程下多个课节添加学生](../classroom/addCourseClassStudent.md)  
* 接口 [添加/修改/删除课节标签](../classroom/addClassLabels.md)  
**注：lms客户端版本预计2023-02-07上线**

##### 三、新增对接最佳实践、对接常见问题QA，涉及页面如下:
* [快速实现从同步用户到创建在线课堂](../Solutions/BasicScenario.md)
* [用户账号变更相关](../Solutions/AccountRelated.md)
* [大直播方案](../Solutions/Live&PlaybackScenes.md)
* [接口调试阶段QA](../Error-Handling/Basic_errors.md)
* [消息订阅QA](../Error-Handling/Datasubs_errors.md)
* [排课过程QA](../Error-Handling/Lesson_errors.md)

## 3.37  2022年12月6日

**新增邮箱账号，涉及接口修改如下：**

[注册用户](../user/register.md)、[注册用户（多个）](../user/registerMultiple.md) 、[添加学生](../user/addSchoolStudent.md)、[添加老师](../user/addTeacher.md)接口：   
- 新增错误码：461=表示邮箱已注册
- 新增参数：email

[获取唤醒客户端并进入教室链接](../getLoginLinked.md):
- 网页唤起客户端不支持邮箱账号，如果邮箱账号没有绑定手机号，此接口会报错467，需要绑定手机号之后才能使用
- 新增错误码：467=免密登录仅支持手机账号，请先绑定手机号

**涉及消息订阅修改如下：**
- [直播回放相关](../datasub/details.md)：直播页面用户登录（LiveWebLogin），直播预约（LiveReserve），直播观看明细（LiveDataDetail），直播点赞（LiveLike），直播商品点击明细（LiveGoodsClickDetail），网页回放观看明细（ReplayDataDetail）中的Telephone的值可能是邮箱，也可能是手机号，以用户实际登录的情况为准
- [课节教师和学生评价评分数据（Rating）](../datasub/classrelated.md.md)新增了studentEmail字段
- [更换账号手机号码（ReplacePhoneNumber）](../datasub/ schoolrelated.md)新增了Email字段
- [设置子账号（setSubAccount）](../datasub/ schoolrelated.md) 新增了Email字段

## 3.36  2022年11月20日

[添加机构标签](../school/addSchoolLabel.md)：   
- 当错误码为353时，表示标签已经存在，新增返回对应标签ID；  


## 3.35  2022年10月11日

[创建课程](../classroom/addCourse.md)、[创建课节(单个)](../classroom/addCourseClass.md) 、[创建课节(多个)](../classroom/addCourseClassMultiple.md)、接口：   
- 新增错误码：460=课程或课节正在被其他请求创建（并发创建会遇到，建议调整频率后检查是否有重复数据产生）

[课程下添加学生/旁听（多个）](../classroom/addCourseStudentMultiple.md)接口：
- 新增错误码： 464=课程学生正在被其他请求创建（并发请求会遇到，建议调整频率）

## 3.34  2022年09月20日

**新增 [添加/修改/删除课程标签](../classroom/addCourseLabels.md) 接口：**

[添加/修改/删除课程标签](../classroom/addCourseLabels.md)，需要 SID，safekey，timeStamp，courseId，courseList。其中当标签数组 (labelIds) 为空时，表示删除课程下所有的标签；当课程下没有标签时，标签数组 (labelIds) 中填写标签 ID，表示给课程下添加标签；当课程下有标签 ID，标签数组 (labelIds) 中添加标签 ID，表示修改课程下标签。返回执行后的信息。**注：每个课程下最多可添加10个标签**  

## 3.33  2022年06月08日

**新增录制现场功能，涉及的接口修改如下：**

[创建课节(单个)](../classroom/addCourseClass.md) 、[创建课节(多个)](../classroom/addCourseClassMultiple.md)、[修改课节信息](../classroom/editCourseClass.md)、[课节设置录课、直播、回放(多个)](../broadcast/setClassVideoMultiple.md)接口：   
- 新增请求参数：recordScene，非必填，1开启录制现场。record开启时可开启。

## 3.32  2022年04月11日

**新增多联席教师功能，涉及的接口修改如下：**

[创建课节(单个)](../classroom/addCourseClass.md) 、[创建课节(多个)](../classroom/addCourseClassMultiple.md)、[修改课节信息](../classroom/editCourseClass.md)接口：   
- 新增请求参数：assistantUids，格式[1000082,1000083]，assistantUids和assistantUid只能传一个；    
- 新增错误码：21316=联席教师数据有重复，21317=联席教师数量超出限制；     
- 去掉330错误码。


## 3.31  2022年03月28日

消息订阅新增订阅项：
* 消息订阅 [课节结束后推送的消息](../datasub/classrelated.md) 新增订阅项：[课节聊天消息打包推送](../datasub/classrelated.md#课节聊天消息打包推送)

## 3.30  2022年01月18日

以下接口新增错误码：[创建课节(单个)](../classroom/addCourseClass.md)，[创建课节(多个)](../classroom/addCourseClassMultiple.md)，[修改课节信息](../classroom/editCourseClass.md)
新增判断课节的开始或结束时间是否跟 [系统常规运维时间](https://docs.eeo.cn/product/zh-hans/function/System/Maintainance.html) 有重叠，若重叠，则创建、编辑失败，此时返回454错误码;<br>
相关错误码的定义为：454=课节起止时间与系统维护时间有重叠

消息订阅新增订阅项：
* 消息订阅 [课节结束后推送的消息](../datasub/classrelated.md) 新增订阅项：[客户端回放观看统计](../datasub/classrelated.md#客户端回放观看统计)
* 消息订阅 [机构维度推送的消息](../datasub/schoolrelated.md) 新增订阅项：[设置机构子账号](../datasub/schoolrelated.md#5-设置子账号)

## 3.29  2022年01月05日
将“助教”更改为“联席教师”，接口assistantUid字段传输不做变更，只更新解释含义以及error_info中报错信息；

涉及以下接口：[创建课节(单个)](../classroom/addCourseClass.md)，[创建课节(多个)](../classroom/addCourseClassMultiple.md)，[修改课节信息](../classroom/editCourseClass.md)，[课程下添加学生/旁听（单个）](../classroom/addCourseStudent.md)，[课程下添加学生/旁听（多个）](../classroom/addCourseStudentMultiple.md)，[课节下添加学生（多个）](../classroom/addClassStudentMultiple.md)，[更换课程老师](../classroom/modifyCourseTeacher.md)，[课程下多个课节添加学生](../classroom/addCourseClassStudent.md)以及消息订阅中相关解释；<br>

## 3.28  2021年11月22日
客户端上线更换手机号功能，消息订阅新增订阅项：[更换账号手机号码](../datasub/schoolrelated.md#4-更换账号手机号码)

## 3.27 2021年11月11日
新增三个预分组接口：
* 接口 [创建课程分组](../classroom/addCourseGroup.md)
* 接口 [编辑课程分组](../classroom/editCourseGroup.md)
* 接口 [删除课程分组](../classroom/delCourseGroup.md)

## 3.26 2021年09月03日
以下接口新增注销相关的错误码：[添加学生](../user/addSchoolStudent.md)，[添加老师](../user/addTeacher.md)，[创建课程](../classroom/addCourse.md)，[编辑课程](../classroom/editCourse.md)，[创建课节(单个)](../classroom/addCourseClass.md)，[创建课节(多个)](../classroom/addCourseClassMultiple.md)，[修改课节信息](../classroom/editCourseClass.md)，[课程下添加学生/旁听（单个）](../classroom/addCourseStudent.md)，[课程下添加学生/旁听（多个）](../classroom/addCourseStudentMultiple.md)，[课节下添加学生（多个）](../classroom/addClassStudentMultiple.md)，[更换课程老师](../classroom/modifyCourseTeacher.md)，[课程下多个课节添加学生](../classroom/addCourseClassStudent.md)，[获取唤醒客户端并进入教室链接](../getLoginLinked.md)<br>
相关错误码的定义为：883=班主任账号已注销，884=老师账号已注销，885=联席教师账号已注销，886=学生账号已注销，887=旁听账号已注销，888=用户账号已注销

## 3.25 2021年08月18日
* 消息订阅 [机构维度推送的消息](../datasub/schoolrelated.md) 新增订阅项 [账号注销](../datasub/schoolrelated.md#3-账号注销)

## 3.24 2021年07月31日
自2021年7月31日起，不再提供以下消息订阅类型的推送：   
* 课节内实时推送的消息 - 教室内IM文字聊天
* 课节内实时推送的消息 - 教室内IM图片聊天   

## 3.23 2021年07月22日
* 消息订阅 [课节内实时推送的消息](../datasub/details.md) 新增订阅项 [直播预约](../datasub/details.md#直播预约)，[直播观看明细](../datasub/details.md#直播观看明细)，[直播点赞](../datasub/details.md#直播点赞)，[直播商品点击明细](../datasub/details.md#直播商品点击明细)。
* 消息订阅 [课节结束后推送的消息](../datasub/classrelated.md) 新增订阅项 [回放观看明细](../datasub/classrelated.md#回放观看明细)。

## 3.22 2021年05月08日
更改接口 [创建课程](../classroom/addCourse.md) 传参 allowAddFriend 不传值时的逻辑。

## 3.21 2021年04月23日
1）修改以下两个接口，新增传参 allowStudentModifyNickname 以支持设置“是否允许学生在群里修改其班级昵称”：
* [创建课程](../classroom/addCourse.md)
* [编辑课程](../classroom/editCourse.md)

2）更改接口 [编辑课程](../classroom/editCourse.md) 对传参 folderId 的处理逻辑：
* 如果该课程下未开课的课节绑定的云盘资源与课程下原有云盘资源相同，则同时更新此课节绑定的云盘资源。
* 如果该课程下未开课的课节绑定的云盘资源与课程下原有云盘资源相同，则不更新此课节绑定的云盘资源。

## 3.20 2021年03月30日
自2021年6月1日起，接口 [获取唤醒客户端并进入教室链接](../getLoginLinked.md) 将做如下调整：接口返回的URL将不再包含临时密钥authTicket了（翼鸥将根据用户账号逐步分批调整，6.30日全部完成调整），也就是说不再支持使用临时密钥authTicket免密登录唤起客户端。<br>

此调整对您的API对接程序没有任何影响，只会影响您的用户在网页唤起后的操作体验，因此需要您的客服或者运营团队，提前与用户沟通此体验变化：<br>
从2021-06-01日开始，用户首次网页唤起ClassIn客户端后，程序将停留在登录界面等待用户输入密码并点击“登录”，方能进入教室。<br>
请注意：
1. 对于移动端ClassIn软件会自动记住密码；对于PC ClassIn强烈建议用户在输入密码后勾选“记住密码”以便于下次唤起无须再次输入密码。
1. 如果用户忘记密码，可以点击登录页面的“忘记密码”以找回密码。

## 3.19 2021年03月10日
1） 修改以下三个接口，传参seatNum支持传0，表示创建1V0课节，即台上只显示老师（注：未传seatNum或其值传空时表示创建1V6课节）：
* 接口 [创建课节（单个）](../classroom/addCourseClass.md)
* 接口 [创建课节（多个）](../classroom/addCourseClassMultiple.md)
* 接口 [修改课节上台学生数](../classroom/modifyClassSeatNum.md)

2） 修改以下两个接口，mainTeacherUid字段规则调整，不传以及传空则不设置/更新班主任，详情请参考接口描述：
* 接口 [创建课程](../classroom/addCourse.md)
* 接口 [编辑课程](../classroom/editCourse.md)

## 3.18 2021年03月02日
新增接口 [修改教师授权云盘的课件资源](../cloud/updateTeacherCloudFolders.md) 以支持对教师的授权云盘下的课件资源进行授权。

## 3.17 2021年01月20日
修改以下三个接口，新增传参 teachMode 以支持设置教学模式为“智慧教室”的课节（课节的教学模式默认为“在线教室”），详情请参考接口描述：
* 接口 [创建课节（单个）](../classroom/addCourseClass.md)
* 接口 [创建课节（多个）](../classroom/addCourseClassMultiple.md)
* 接口 [修改课节信息](../classroom/editCourseClass.md)

## 3.16 2021年01月12日
修改以下三个接口，新增传参 isDc 以支持设置是否启用第二摄像头（副摄像头），详情请参考接口描述：
* 接口 [创建课节（单个）](../classroom/addCourseClass.md)
* 接口 [创建课节（多个）](../classroom/addCourseClassMultiple.md)
* 接口 [修改课节上台学生数](../classroom/modifyClassSeatNum.md)

## 3.15 2021年01月05日
1） 下述接口将只支持传参uid，不再支持传参手机号码。涉及的接口包括：[修改用户昵称](../user/editUserInfo.md)，[修改用户密码](../user/modifyPassword.md)，[停用老师](../user/stopUsingTeacher.md)，[启用老师](../user/restartUsingTeacher.md)，[更新课节教师对学生评价](../user/updateClassStudentComment.md)，[创建课程](../classroom/addCourse.md)，[编辑课程](../classroom/editCourse.md)，[创建课节（单个）](../classroom/addCourseClass.md)，[创建课节（多个）](../classroom/addCourseClassMultiple.md)，[修改课节信息](../classroom/editCourseClass.md)，[课程下添加学生/旁听（单个）](../classroom/addCourseStudent.md)，[课程下删除学生/旁听（单个）](../classroom/delCourseStudent.md)，[课程下添加学生/旁听（多个）](../classroom/addCourseStudentMultiple.md)，[课程下删除学生/旁听（多个）](../classroom/delCourseStudentMultiple.md)，[课节下添加学生（多个）](../classroom/addClassStudentMultiple.md)，[课节下删除学生（多个）](../classroom/delClassStudentMultiple.md)，[更换课程老师](../classroom/modifyCourseTeacher.md)，[移除课程老师](../classroom/removeCourseTeacher.md)，[课程下多个课节添加学生](../classroom/addCourseClassStudent.md)

**请注意**：接口 [添加学生](../user/addSchoolStudent.md) 和 [添加老师](../user/addTeacher.md), 仅支持传参手机号码，不支持传参uid。

2）接口域名及协议头：
  * 所有接口 URL 域名请使用 https://api.eeo.cn, 如果您继续使用 https://www.eeo.cn 的话，则会收到 404 状态码；
  * 所有接口 URL 协议头请使用 https，如果您继续使用 http 方式的话，则会收到 403 状态码。

另外，为了便于后期新接口以及重要修改的通知，强烈建议您在 **认证资料** 里填写您的常用邮箱（入口：登录eeo.cn机构管理后台，点击左侧的**认证资料**页面进行填写）。

## 3.14 2020年11月30日
修改以下四个接口，课节新增支持两个参数的设置：watchByLogin-网页直播回放 和 allowUnloggedChat-允许未登录用户参与直播聊天和点赞，详情请参考接口描述：
  * 接口 [创建课节（单个）](../classroom/addCourseClass.md)
  * 接口 [创建课节（多个）](../classroom/addCourseClassMultiple.md)
  * 接口 [修改课节信息](../classroom/editCourseClass.md)
  * 接口 [课节设置录课、直播、回放（多个）](../broadcast/setClassVideoMultiple.md)

## 3.13 2020年09月15日
消息订阅 [课节内实时推送](../datasub/details.md) 新增订阅项 [**教室大黑板板书图片**](../datasub/details.md#教室大黑板板书图片)。

## 3.12 2020年09月03日
接口 [修改课节信息](../classroom/editCourseClass.md) 支持上课中课节添加/更换/删除联席教师。返回错误码385描述更新，课节结束后不能修改联席教师。
[参数规则](rules.md)课节内容下联席教师修改的时间限制更新，支持上课中课节添加/更换/删除联席教师。

## 3.11 2020年08月13日
接口 [创建课程](../classroom/addCourse.md) 支持使用学校设置的默认封面作为班级群的封面。

## 3.10 2020年08月04日
消息订阅 [课节内实时推送](../datasub/details.md) 新增订阅项 [**启动录课详情**](../datasub/details.md#启动录课详情)。

## 3.9 2020年06月01日
* 修改接口：
  * 接口 [课程下添加学生/旁听（单个）](../classroom/addCourseStudent.md)，[课程下添加学生/旁听（多个）](../classroom/addCourseStudentMultiple.md) 支持同步用户姓名至班级昵称，详情请参考接口描述。
  * 接口 [课程下添加学生（多个）](../classroom/addCourseStudentMultiple.md) 和 [课节下添加学生（多个）](../classroom/addClassStudentMultiple.md) 不再支持代注册（代注册指的是：传参的学生手机号码，如果不是ClassIn账号，支持自动注册。）；
  * 课程/课节下添加学生的相关接口（如下四个接口），将不再支持将学生自动添加为机构学生，新增错误码 228 表示“机构下无此学生”。对一个学生或者老师进行排课的标准操作为：**注册** --> **添加机构学生/老师** --> **排课**。涉及的接口包括：
    * [课程下添加学生/旁听（单个）](../classroom/addCourseStudent.md): 请求参数 studentName 项由必填改为非必填。仅用于当identity为2（旁听身份）时，才使用请求参数studentName。当identity为2时，如果没有传此参的话，则使用手机号码作为旁听生的名字。当identity为1（学生身份）时，传了参数studentName也不会被使用。
    * [课程下添加学生/旁听（多个）](../classroom/addCourseStudentMultiple.md): 请求参数 studentJson 里的 name 项由必填改为非必填。仅用于当identity为2（旁听身份）时，才使用请求参数name。当identity为2时，如果没有传此参的话，则使用手机号码作为旁听生的名字。当identity为1（学生身份）时，传了参数studentJson里的name也不会被使用。
    * [课节下添加学生（多个）](../classroom/addClassStudentMultiple.md): 删除了原请求参数中 studentJson 里的 name 项（传了不报错，但也不会使用）。
    * [课程下多个课节添加学生](../classroom/addCourseClassStudent.md): 删除了原请求参数中 studentName 项（传了不报错，但也不会使用）。

* 新增待废弃接口和订阅消息项（已从本文档中删除，详情请查看 [Deprecation](deprecated.md)）：
  * 接口 `删除课程`；
  * 接口 `修改用户信息`，以及下线消息订阅 [机构维度推送的消息](../datasub/schoolrelated.md) 里的项目 **用户修改昵称**；

## 3.8 2020年05月08日
* 新增接口：
  * 接口 [修改群成员的班级昵称](../group/modifyGroupMemberNickname.md) 此接口用课程下所有学生和旁听生，在机构下的学生姓名，来修改群里学生和旁听生的 **班级昵称**。修改后，学生在客户端的 IM 班级群里，以及该课程下的教室里上课时，显示的名字均为学生姓名，而非用户昵称。此接口解决了，学生在ClassIn客户端修改用户昵称后，老师经常在群里和教室里上课时，对不上号的问题。
* 修改接口：
  * 接口 [创建课程](../classroom/addCourse.md)，[编辑课程](../classroom/editCourse.md)，新增课程设置项allowAddFriend，以设置是否允许班级成员相互添加好友。


## 3.7 2020年04月10日
* 修改接口：
  * 接口 [创建课节（单个）](../classroom/addCourseClass.md)，[创建课节（多个）](../classroom/addCourseClassMultiple.md)，[修改课节信息](../classroom/editCourseClass.md) 删除无效参数 teacherName

* 消息订阅：
  * [课节结束后推送的消息](../datasub/classrelated.md) 里的 [**课节汇总数据**](../datasub/classrelated.md#课节汇总数据) 新增子项“equipmentsEnd”，目前其包含子子项“Camera”，记录了摄像头总计打开时间（仅包括在台上时间）。

## 3.6 2020年03月16日
新增待废弃接口：
* `获取唤醒客户端密钥`：接口 getTempLoginKey 将于 2020-04-27 日后下线。替代接口请参考 [获取唤醒客户端并进入教室链接](../getLoginLinked.md)

## 3.5 2020年02月18日
消息订阅 [课节内实时推送](../datasub/details.md) 新增订阅项 [**直播页面用户登录**](../datasub/details.md#直播页面用户登录)。

## 3.4 2020年02月15日
* 修改接口：
  * `删除单个课节视频`，新增参数 fileId 以支持删除课节下某一视频片段文件。详情请参考具体接口 [删除单个课节视频](../broadcast/deleteClassVideo.md)
- 新增待废弃接口：
  - `修改用户信息` 接口将会在 2020.06.01 日后弃用，不再维护。详情请查看具体接口 [修改用户信息](../user/editUserInfo.md)。用户的昵称和头像，属于用户个人隐私数据，故不再支持机构对其进行修改。机构在自己的系统里，应该使用用户在机构下的 **用户姓名** 信息，不应该使用用户昵称信息。
  - `消息订阅 - 机构维度推送的消息 - 用户修改昵称` 该消息订阅项将会在 2020.06.01 日后弃用，不再维护。详情请查看消息订阅 [用户修改昵称](../datasub/schoolrelated.md)。

## 3.3 2019年12月25日
消息订阅 [课节结束后推送的消息](../datasub/classrelated.md) 里的 [**课节汇总数据**](../datasub/classrelated.md#课节汇总数据) 新增子项“edbEnd”：教室打开 edb 课件的统计信息。

## 3.2 2019年12月17日
- 修改对接域名及协议头
  - **所有接口 URL 域名调整为 `https://api.eeo.cn`，之前是 `https://www.eeo.cn`, 将在2020年06月01日将强制只支持 `https://api.eeo.cn`。**
  - **所有接口 URL 协议头仅支持 https，当前是 http 与 https 兼容，将在2020年06月01日将强制只支持 https。**
- 修改接口：
  - `添加老师`，新增 288 错误码，表示此号段不合法。详情请参考具体接口[**添加老师**](../user/addTeacher.md)；
  - `添加学生`，新增 288 错误码，表示此号段不合法。详情请参考具体接口[**添加学生**](../user/addSchoolStudent.md)；
  - `修改用户昵称`，修改接口名称为 `修改用户信息`，并新增参数 `Filedata`，新增错误码等，支持修改用户客户端头像。详情请参考具体接口[**修改用户信息**](../user/editUserInfo.md)；
  - `创建课节（单个）`，开课时间修改为须在3年以内，之前是2年以内。详情请参考具体接口[**创建课节（单个）**](../classroom/addCourseClass.md)；
  - `创建课节（多个）`，开课时间修改为须在3年以内，之前是2年以内。详情请参考具体接口[**创建课节（多个）**](../classroom/addCourseClassMultiple.md)；
  - `获取唤醒客户端秘钥`，新增支持 uid 参数，将原有 telephone 参数改为非必填，两个参数同时传入的情况下以 uid 为准。详情请参考具体接口 [**获取唤醒客户端秘钥**](../getTempLoginKey.md)；
  - `获取唤醒客户端并进入教室链接`，新增支持 uid 参数，将原有 telephone 参数改为非必填，两个参数同时传入的情况下以 uid 为准。详情请参考具体接口 [**获取唤醒客户端并进入教室链接**](../getLoginLinked.md)；
  - `课程下添加学生（多个）`，删除 `isRegister,password`参数，不再支持代注册功能。详情请参考具体接口[**课程下添加学生（多个）**](../classroom/addCourseStudentMultiple.md)；
  - `课节下添加学生（多个）`，删除 `isRegister,password`参数，不再支持代注册功能。详情请参考具体接口[**课节下添加学生（多个）**](../classroom/addClassStudentMultiple.md)；

- 新增接口：
  - `注册用户（多个）`，一次性最多可注册 10 个用户。详情请参考具体接口 [**注册用户（多个）**](../user/registerMultiple.md)；

- 新增待废弃接口：
  - `删除课程` 接口将会在 2020.06.01 日后弃用，不再维护。详情请查看具体接口 [**删除课程**](../classroom/delCourse.md)。

## 3.1 2019年11月15日
为了能够支持**更换ClassIn账号手机号码**（此功能还未上线，后续将支持），我们修改了所有传参手机号码的接口，以支持既可以传参手机号码，也可以uid（手机号码和uid，两者必须传一个，如果两者均传，则以uid为准，即接口不做两者一致性的检查）。<br>

从 2020 年 06 月 01 日起，除了**注册接口**之外，所有原需传参手机号码的接口，将只支持传参uid。<br>
您需要在上述截止日期之前，完成：
* 修改您的API对接代码，支持传参uid；
* 在您的数据库里，保存手机号码和uid之间的对应关系。

以下接口被修改以支持uid，且新增 400 错误码，表示请求数据不合法（即uid不存在或者uid不属于该机构学生或者老师）。
- `修改用户昵称`，新增 uid 参数，将原有 telephone 参数改为非必填，两个参数同时传入的情况下以 uid 为准。详情请参考具体接口 [修改用户昵称](../user/editUserInfo.md)；
- `修改用户密码`，新增 uid 参数，将原有 telephone 参数改为非必填，两个参数同时传入的情况下以 uid 为准。详情请参考具体接口 [修改用户密码](../user/modifyPassword.md)；
- `修改用户密码（不提供原密码）`，新增 uid 参数，将原有 telephone 参数改为非必填，两个参数同时传入的情况下以 uid 为准。详情请参考具体接口 [修改用户密码（不提供原密码）](../user/modifyPasswordByTelephone.md)；
- `添加学生`，新增 studentUid 参数，将原有 studentAccount 参数改为非必填，两个参数同时传入的情况下以 studentUid 为准。详情请参考具体接口 [添加学生](../user/addSchoolStudent.md)；
- `添加老师`，新增 teacherUid 参数，将原有 teacherAccount 参数改为非必填，两个参数同时传入的情况下以 teacherUid 为准。详情请参考具体接口 [添加老师](../user/addTeacher.md)；
- `停用老师`，新增 teacherUid 参数，将原有 teacherAccount 参数改为非必填，两个参数同时传入的情况下以 teacherUid 为准。详情请参考具体接口 [停用老师](../user/stopUsingTeacher.md)；
- `启用老师`，新增 teacherUid 参数，将原有 teacherAccount 参数改为非必填，两个参数同时传入的情况下以 teacherUid 为准。详情请参考具体接口 [启用老师](../user/restartUsingTeacher.md)；
- `更新课节教师对学生评价`，新增 studentUid 参数，将原有 studentAccount 参数改为非必填，两个参数同时传入的情况下以 studentUid 为准，传入 studentAccount 时接口返回 studentAccount；传入 studentUid 时接口返回 studentUid。详情请参考具体接口 [更新课节教师对学生评价](../user/updateClassStudentComment.md)；
- `创建课程`，新增 mainTeacherUid 参数，将原有 mainTeacherAccount 参数改为非必填，两个参数同时传入的情况下以 mainTeacherUid 为准。详情请参考具体接口 [创建课程](../classroom/addCourse.md)；
- `编辑课程`，新增 mainTeacherUid 参数，将原有 mainTeacherAccount 参数改为非必填，两个参数同时传入的情况下以 mainTeacherUid 为准。详情请参考具体接口 [编辑课程](../classroom/editCourse.md)；
- `创建课节（单个）`，新增 teacherUid、assistantUid 参数，将原有 teacherAccount 参数改为非必填。详情请参考具体接口 [创建课节（单个）](../classroom/addCourseClass.md)；
- `创建课节（多个）`，新增 teacherUid、assistantUid 参数，将原有 teacherAccount 参数改为非必填。详情请参考具体接口 [创建课节（多个）](../classroom/addCourseClassMultiple.md)；
- `修改课节信息`，新增 teacherUid、assistantUid 参数，将原有 teacherAccount 参数改为非必填。详情请参考具体接口 [修改课节信息](../classroom/editCourseClass.md)；
- `课程下添加学生/旁听（单个）`，新增 studentUid 参数，将原有 studentAccount 参数改为非必填，两个参数同时传入的情况下以 studentUid 为准。详情请参考具体接口 [课程下添加学生/旁听（单个）](../classroom/addCourseStudent.md)；
- `课程下删除学生/旁听（单个）`，新增 studentUid 参数，将原有 studentAccount 参数改为非必填，两个参数同时传入的情况下以 studentUid 为准。详情请参考具体接口 [课程下删除学生/旁听（单个）](../classroom/delCourseStudent.md)；
- `课程下添加学生/旁听（多个）`，新增 uid 参数，将原有 account 参数改为非必填，两个参数同时传入的情况下以 uid 为准。详情请参考具体接口 [课程下添加学生/旁听（多个）](../classroom/addCourseStudentMultiple.md)；
- `课程下删除学生/旁听（多个）`，新增 studentUidJson 参数，将原有 studentJson 参数改为非必填，两个参数同时传入的情况下以 studentUidJson 为准。详情请参考具体接口 [课程下删除学生/旁听（多个）](../classroom/delCourseStudentMultiple.md)；
- `课节下添加学生（多个）`，新增 uid 参数，将原有 account 参数改为非必填，两个参数同时传入的情况下以 uid 为准。详情请参考具体接口 [课节下添加学生（多个）](../classroom/addClassStudentMultiple.md)；
- `课节下删除学生（多个）`，新增 studentUidJson 参数，将原有 studentJson 参数改为非必填，两个参数同时传入的情况下以 studentUidJson 为准。详情请参考具体接口 [课节下删除学生（多个）](../classroom/delClassStudentMultiple.md)；
- `更换课程老师`，新增 teacherUid 参数，将原有 teacherAccount 参数改为非必填，两个参数同时传入的情况下以 teacherUid 为准。详情请参考具体接口 [更换课程老师](../classroom/modifyCourseTeacher.md)；
- `移除课程老师`，新增 teacherUid 参数，将原有 teacherAccount 参数改为非必填，两个参数同时传入的情况下以 teacherUid 为准。详情请参考具体接口 [移除课程老师](../classroom/removeCourseTeacher.md)；
- `课程下多个课节添加学生`，新增 studentUid 参数，将原有 studentAccount 参数改为非必填，两个参数同时传入的情况下以 studentUid 为准。详情请参考具体接口 [课程下多个课节添加学生](../classroom/addCourseClassStudent.md)；

## 2019年10月15日
**`重要`**：为了给您提供更好的产品和服务，系统会在每个月的 20 日进行定期例行维护，每个月的具体维护时间，请访问以下链接。<br>
https://www.eeo.cn/partner/product_book/zh-hans/function/System/Maintainance.html <br>
请您在排课的时候，确保课节时间与系统维护时间没有重合。在系统维护期间的所有API请求，都会返回 901 的状态码。

## 3.1 2019年10月14日
修改接口：
- `修改课节信息` 新增开课后如未设置助教可添加助教，如开课后已设置助教不可更换和删除。详情请参考具体接口 [修改课节信息](../classroom/editCourseClass.md)；

## 3.0 2019年10月1日
修改接口：
- `创建课程`， 新增过期时间不传、传0、传空均当成0，课程过期时间设置为永不过期0；详情请参考具体接口 [创建课程](../classroom/addCourse.md)
- `编辑课程`， 新增过期时间不传或传空，不修改；传0，修改成永不过期；传非0的时间戳，则修有效期为传过来的时间；详情请参考具体接口 [编辑课程](../classroom/editCourse.md)
- `添创建课节单个`， 新增isHd的值支持传2，表示全高清；详情请参考具体接口 [创建课节单个](../classroom/addCourseClass.md)；
- `创建课节多个`， 新增isHd的值支持传2，表示全高清；详情请参考具体接口 [创建课节多个](../classroom/addCourseClassMultiple.md)；
- `修改课节上台学生数`， 新增isHd的值支持传2，表示全高清；详情请参考具体接口 [修改课节上台学生数](../classroom/modifyClassSeatNum.md)；

## 2.15 2019年09月02日
修改接口：
- `创建课程`， 修改为创建课程时不选择云盘文件夹 ID，默认为空目录。详情请参考具体接口 [创建课程](../classroom/addCourse.md)；

## 2.14 2019年08月09日
新增接口：
- `编辑学生信息`，详情请查看具体接口 [编辑学生信息](../user/editSchoolStudent.md)；

修改接口：
- `删除课程`，新增错误码 822 表示删除课程成功，删除唯一标识失败。详情请参考具体接口 [删除课程](../classroom/delCourse.md)；
- `删除课节`，新增错误码 823 表示删除课节成功，删除唯一标识失败。详情请参考具体接口 [删除课节](../classroom/delCourseClass.md)；
- `编辑老师`，新增参数 teacherUid，支持以用户 UID 编辑老师信息。详情请参考具体接口 [编辑老师](../user/editTeacher.md)；
- `注册用户`，新增参数 addToSchoolMember，以支持注册完直接添加为机构老师或者学生。详情请参考具体接口 [注册用户](../user/register.md)；
- `创建课节（单个）` 新增参数 classIntroduce，支持添加课节简介功能。详情请参考具体接口 [创建课节（单个）](../classroom/addCourseClass.md)；
- `创建课节（多个）` 新增参数 classIntroduce，支持添加课节简介功能。详情请参考具体接口 [创建课节（多个）](../classroom/addCourseClassMultiple.md)；
- `修改课节信息` 新增参数 classIntroduce，支持修改课节简介功能。详情请参考具体接口 [修改课节信息](../classroom/editCourseClass.md)；
- `添加学生`，原名称`机构下添加学生`，修改接口名称为`添加学生`，其内容及功能不变。详情请参考具体接口 [添加学生](../user/addSchoolStudent.md)；


## 2.13 2019年07月31日
- `创建文件夹` 如果云盘已存在同名文件夹，则返回 206 错误码的同时会返回之前云盘文件夹的ID。
- `重命名文件夹` 如果云盘已存在同名文件夹，则返回 206 错误码的同时会返回之前云盘文件夹的ID。

## 2.12 2019年07月8日
- 新增错误码： `800 表示老师被停用中`、`804 表示助教被停用中`、`805 表示班主任被停用中`，被停用中的账号需要等待系统完成停用后再启用，预计等待1-5分钟。涉及接口如下
  - 启用老师，新增 800 错误码
  - 创建课程，新增 805 错误码
  - 编辑课程，新增 805 错误码
  - 更换课程老师，新增 800 错误码
  - 创建课节（单个），新增 800、804 错误码
  - 创建课节（多个），新增 800、804 错误码
  - 修改课节信息，新增 800、804 错误码

## 2.11 2019年07月01日
- 新增已废弃接口（已从本文档中删除，详情请查看 [Deprecation](deprecated.md)）
  - 获取课节列表
  - 获取课程下学生/旁听
  - 获取课程信息
  - 获取课节信息
  - 获取课节直播流地址、回放视频地址
  - 获取单课节直播/回放播放器地址
  - 获取课程列表


## 2.10 2019年06月17日
- 机构消息订阅中 `课节内设备检测报告`、`用户教室外设备检测报告` 中将用户 IP 保留前三位，例如：`127.0.0.*`。详情请参考具体接口。

## 2.9 2019年05月24日
- 机构消息订阅中 `课节内设备检测报告`、`用户教室外设备检测报告` 中新增 `deviceType`表示用户设备信息，详情请参考具体接口。

## 2.8 2019年05月17日
- 机构消息订阅中 `课节内设备检测报告`、`用户教室外设备检测报告` 中删除用户 IP，服务器名称字段。详情请参考具体接口。

## 2.7 2019年04月28日
- `创建课节（单个）`、`创建课节（多个）`、`编辑课节`、`课节设置录课、直播、回放（多个）` 接口新增返回值 `课节直播播放器地址`、`课节直播流地址`，如果在调用接口时开启录课、直播等才会返回，详情请查看具体接口。替代废弃接口 `获取单课节直播/回放播放器地址`、`获取课节直播流地址、回放视频地址`。

## 2.6 2019年04月08日
- 新增待废弃接口
  - `获取课程列表` 接口将会在未来版本中弃用，不再维护。

## 2.5 2019年04月01日
- `ClassIn 下载按钮链接` 接口中从 2019年05月01号开始不再提供 WinXP 下载链接。详情请参考具体接口 [ClassIn 下载按钮链接 API 说明](../iframe.md)。
- 新增待废弃接口
  - `获取课节列表` 接口将会在未来版本中弃用，不再维护。
  - `获取课程下学生/旁听` 接口将会在未来版本中弃用，不再维护。
  - `获取课程信息` 接口将会在未来版本中弃用，不再维护。
  - `获取课节信息` 接口将会在未来版本中弃用，不再维护。
  - `获取课节直播流地址、回放视频地址` 接口将会在未来版本中弃用，不再维护。
  - `获取单课节直播/回放播放器地址` 接口将会在未来版本中弃用，不再维护。

## 2.4 2019年03月25日
- 修改接口中涉及域名的地方，将 www.eeo.cn 修改为 root_url。用户在实际接口环境调用中需要将地址替换为真实环境地址。例如：对接 ClassIn API 的用户需要将 root_url 替换为 www.eeo.cn。
- `获取课节直播流地址、回放视频地址` 接口在返回回放视频地址时新增 Size、FileId、Duration 参数，详情请参考具体接口。

## 2.3 2019年01月25日
- 针对 `获取课程直播/回放播放器地址`、`获取课节直播/回放播放器地址` iframe 嵌套，iOS 11+ cookie 写入不进去的情况，现已修复（在 H5 引入我们的 js 文件即可），详情请参考具体接口。

## 2.3 2019年01月23日
- 修改接口
  - 新增参数 `courseUniqueIdentity`：唯一标识，如果传入此值，则该接口会校验此唯一值是否已存在，如果已存在，则会返回之前已经创建成功的课程/课节ID，如果不存在，则接口正常执行。涉及接口 `创建课程`、`创建课节（单个）`、`创建课节（多个）`。
  - 新增错误码 398，表示数据已存在（唯一标识已存在）。涉及接口 `创建课程`、`创建课节（单个）`、`创建课节（多个）`。
  - 新增错误码 133，表示已存在（传过来的classJson中唯一标识有重复）。如果该 classJson 串中有重复的唯一值，则重复的这个课节不会创建成功。涉及接口 `创建课节（多个）`。


## 2.2.20 2019年01月02日
- 机构消息机构订阅
  - `课节内详细数据` 新增摄像头位置信息，详情请参考具体接口 [课节内详细数据](../datasub/details.md)。

## 2.2.19 2018年10月22日
- 新增废弃接口，（已从本文档删除，详情请查看 [Deprecation](deprecated.md)）
  - 获取课节教师对学生的评价
  - 获取课节学生对教师的评价
  - 获取课节下出勤成员的时间信息

## 2.2.18 2018年09月28日
- 新增废弃接口，（已从本文档删除，详情请查看 [Deprecation](deprecated.md)）
  - 获取用户最新设备自检信息
  - 获取用户课程列表

## 2.2.17 2018年09月18日
- 新增接口
  - `结束课程`，课程下没有正在上的课节，即可结束课程。如果课程下有尚未开始的课节，会先删除未开始的课节之后，再结束课程。详情请参考具体接口 [结束课程](../classroom/endCourse.md)。
- 修改接口
  - `创建课程`、`编辑课程`：接口新增教室设置 ID 参数，选择此套设置后，该课程下所有教室内会依照此设置展示。接口新增错误码：371表示教室设置不存在，373表示教室设置不属于本机构。详情请参考接口 [创建课程](../classroom/addCourse.md)  [编辑课程](../classroom/editCourse.md)
  - `删除课程`：接口新增错误码：393表示课程下有已结束的课节，不能删除。即，该接口之前的逻辑为：只要该课程下有正在上课的课节，就无法删除；修改后的逻辑为：该课程下有已结束的课节或者正在上课的课节，就无法删除。详情请参考接口 [删除课程](../classroom/delCourse.md)。

## 2.2.16 2018年09月06日
- 新增废弃接口，（已从本文档中删除，详情请查看 [Deprecation](deprecated.md)）
  - 获取机构标签（分页）

## 2.2.15 2018年09月05日
- 新增接口
  - `移除课程老师`，移除课程老师后，在 eeo.cn 课程详情中的教师列表中不再显示该老师，ClassIn 客户端的班级群中也不再显示该老师。详情请参考具体接口 [移除课程老师](../classroom/removeCourseTeacher.md)。
  - `修改课节锁定状态`，如果在 eeo.cn 后台开启了自动删除录课视频和监课图片的功能后，将课节修改为锁定状态，则该课节的录课视频和监课图片将不会被自动删除。详情请参考具体接口 [修改课节锁定状态](../broadcast/updateClassLockStatus.md)。
- 更新接口
  - `创建课节（单个）`、`创建课节（多个）`、`修改课节信息` 接口修改错误码 165 表示单节课不能少于15分钟且不能超过24小时，之前限制为至少1分钟。详情请参考具体接口。

## 2.2.14 2018年08月28日
- `ClassIn 下载按钮链接` 新增移动端下载链接和二维码。详情请参考 [ClassIn 下载按钮链接](../iframe.md)
- 机构消息订阅
  - `课节相关消息` 新增教室内老师或者助教往 eeo.cn 管理后台发送的求助信息（只包括文字信息，不包括求助时客户端的截图）。但不包括从 eeo.cn 往教室里发送的任何信息。详情请参考 [课节相关消息](../datasub/classrelated.md#6求助)。

## 2.2.13 2018年08月16日
- 接口新增支持项： 新增支持 1v6 高清，目前高清可选 1v1 和 1v6 。所涉及接口： `创建课节（单个）`、`创建课节（多个）`、`修改课节上台学生数`。

## 2.2.12 2018年08月10日
- 机构消息订阅
  - `课节网络状态报告` 里增加了 "系统CPU占用率" 数据。详情请查看具体接口 [课节相关消息](../datasub/classrelated.md)。
  - `机构相关信息` 增加 "用户修改昵称" 数据，详情请参考具体接口 [机构相关消息](../datasub/schoolrelated.md)。

## 2.2.11 2018年08月09日
- 新增接口
  - 停用老师，详情请参考具体接口 [停用老师](../user/stopUsingTeacher.md)。
  - 启用老师，详情请参考具体接口 [启用老师](../user/restartUsingTeacher.md)。
- 修改接口
  - 创建课程，编辑课程，新增错误码 389 表示班主任已被停用。详情请参考具体接口。
  - 创建课节（单个），创建课节（多个），修改课节信息，新增错误码 387 表示老师已被停用；388 表示助教已被停用。详情请参考具体接口。
  - 更换课程老师，新增错误码 387 表示老师已被停用。详情请参考具体接口。

## 2.2.10 2018年08月07日
- 新增已废弃接口（已从本文档中删除，详情请查看 [Deprecation](deprecated.md)）
  - 获取学生列表
  - 获取机构老师列表
  - 获取学生评论列表
  - 获取上课中课节成员的时间
  - 获取 ClassIn 客户端下载地址

## 2.2.9 2018年07月12日
- 新增接口
  - `删除单个课节视频`，删除后不再产生存储费用，详情请参考具体接口 [删除单个课节视频](../broadcast/deleteClassVideo.md)。

## 2.2.8 2018年07月10日
- 接口新增支持项：学生进入教室是否自动上台，创建课节选择是否 1v1 高清。所涉及接口： `创建单课（单个）`、`创建单课（多个`、`修改课节信息`、`修改课节上台学生数`。
- 新增接口：
  - `更新课节教师对学生评价` ，详情请参考具体接口 [更新课节学生评价](../user/updateClassStudentComment.md)。

## 2.2.7 2018年07月02日
- 机构消息订阅
  - `课节内详细数据` 中退出教室字段新增退出教室原因，详情请参考 [课节内详细数据](../datasub/details.md)。

## 2.2.6 2018年06月28日
- `获取网页唤起客户端并进入教室链接` 支持移动端（Android）网页唤起客户端，详情请参考 [获取网页唤起客户端并进入教室链接](../getLoginLinked.md)。
- 规则修改：以下规则不影响正常调用，可根据自身系统做出相应修改。
  - 机构账号也可以添加为学生/旁听，所涉及接口 `课程下添加学生/旁听（单个）`、`课程下添加学生/旁听（多个）`、`课节下添加学生（多个）`、`课程下多个课节添加学生`，详情请参考相关接口。
  - 上课中可以修改课节老师，所涉及接口 `编辑课节`。详情请参考 [编辑课节](../classroom/editCourseClass.md)。
  - 旁听生最多可以添加 20 个，所涉及接口 `课程下添加学生/旁听（单个）`、`课程下添加学生/旁听（多个）`，详情请参考相关接口。

## 2.2.5 2018年06月11日
- 新增接口：`机构下添加学生`，注册成功后即可调用此接口成功本机构下学生。详情请查看 [机构下添加学生](../classroom/addSchoolStudent.md)。
- `注册用户` 修改描述，详情请参考 [注册用户](../user/register.md)。

## 2.2.4 2018年05月11日
- 机构消息订阅
  + `课节内详细数据` 中答题器下新增两个字段 `SelectedItem 学生选择的答案`，`LastCommitTime 学生提交答案时间`，详情请参考 [课节内详细数据](../datasub/details.md)。
- `获取课节下出勤成员的时间信息` 接口将会在未来版本中弃用，不再维护。
- `获取课节教师对学生的评价` 接口将会在未来版本中弃用，不再维护。
- `获取课节学生对教师的评价` 接口将会在未来版本中弃用，不再维护。

## 2.2.3 2018年04月26日
- `获取用户最新设备自检信息`、`获取用户课程列表` 接口将会在未来版本中弃用，不再维护。

- 机构消息订阅
  + 新增 `用户教室外设备检测报告`，实时监测机构下用户设备检测，用户点击检测设备后，会给机构推送相关数据。详情请参考 [用户教室外设备检测报告](../datasub/schoolrelated.md#2用户教室外设备检测报告)。

## 2.2.2 2018年03月27日
- ClassIn API SDK 正式推出！！！为了更方便您使用 ClassIn API，我们提供了 PHP 语言的 SDK。详情请咨询客户经理。

- 机构消息订阅
  + 新增回调信息 `机构相关消息`，机构上传文件后可收到此消息。详情请参考 [机构相关消息](../datasub/schoolrelated.md)。
  + `课节相关消息` 新增 `课节网络状态报告` 和 `课节内设备监测报告`，并将 `评价消息` 和 `录制文件生成` 合并至 `课节相关消息`，详情请参考 [课节相关消息](../datasub/classrelated.md)。

## 2.2.1 2018年03月20日
- 新增接口`获取单课节直播/回放播放器地址`，并支持机构学生免登陆就可以聊天和点赞，详情请参考 [获取单课节直播/回放播放器地址](../broadcast/getClassWebcastUrl.md)。
- 修改 `课节查询直播、回放地址` 接口名称为 `获取课节直播流地址、回放视频地址`，详情请参考 [获取课节直播流地址、回放视频地址](../broadcast/getClassVideo.md)。
- 修改 `获取直播/回放播放器地址` 接口名称为 `获取课程直播/回放播放器地址`，详情请参考 [获取课程直播/回放播放器地址](../broadcast/getWebcastUrl.md)。

## 2.2.0 2018年03月07日
- 新增错误码 369：表示该课程/课节类型暂不支持该操作。涉及接口：所有传递 courseId 参数的接口。例 [编辑课程](../classroom/editCourse.md)、[创建课节(单个)](../classroom/addCourseClass.md) 等接口。
- `获取课节信息` 接口返回参数新增 `助教账号和姓名`。详情请参考 [获取课节信息](../classroom/getClassInfo.md)。

## 2.1.11 2018年02月07日
- `课节下添加学生（多个）` 新增错误码 164：表示课程下已存在同手机号的旁听。详情请参考 [课节下添加学生（多个）](../classroom/addClassStudentMultiple.md)。

## 2.1.10 2018年02月01日
- `机构消息订阅相关接口` 下 `课节详细数据` 接口中新增获取教室内发言数据（包含文字与图片），详情请参考 [课节详细数据](../datasub/details.md)。  
**以下更新对功能没有任何变化，仅对部分接口增加/修改描述。**
- `获取登陆客户端密钥` 修改接口名称为 `获取唤醒客户端密钥`，详情请参考 [获取唤醒客户端密钥](../getTempLoginKey.md)。
- `获取登陆客户端链接` 修改接口名称为 `获取唤醒客户端并进入教室链接`。添加中间页描述：iOS 移动端返回的链接中已经加入了中间页，无须拼接。详情请参考 [获取唤醒客户端并进入教室链接](,,/getLoginLinked.md)。
- `编辑课程` 声明原有规则，编辑课程时填写课程资源 ID，编辑成功后，所有未开课的课节均会修改为编辑课程成功后的课程资源，不传递课程资源 ID 则不会改变。详情请参考 [编辑课程](../classroom/editCourse.md)。
- `注册用户` 纠正昵称（nickName）参数描述，原有描述：默认注册手机号，最长24位字符，超过24字会自动截取为24字（昵称会显示在教室内摄像头下方）。纠正后：最长24位字符，超过24字会自动截取为24字（昵称会显示在教室内摄像头下方）；客户端显示默认为手机号。不填写昵称，登录客户端会弹出填写昵称的弹框。详情请参考 [注册用户](../user/register.md)。
- `创建课节（单个）`、`创建课节（多个）` ，详情请参考 [创建课节（单个）](../classroom/addCourseClass.md)，[创建课节（多个）](../classroom/addCourseClassMultiple.md)。
  + 录课（record）增加描述：若需要直播或者回放，则必须选择录课，否则无法无法开启直播、回放
  + 直播（live）增加描述：若需要直播，则必须开启录课
  + 回放（replay）增加描述：若需要回放，则必须开启录课
- `参数规则` 增加描述：**时间戳：Unix Epoch 时间戳是 1970年1月1日 00:00:00 (世界标准时间) 起经过的秒数，凡接口中涉及到的时间戳均以此规则传输**，详情请参考 [参数规则](rules.md)。

## 2.1.9 2018年01月20日
- 新增机构标签相关5个接口，机构可以给课节增加标签，以此筛选相关类别的课节。
  + `创建机构标签`，**机构最多可以创建 100 个标签**，详情请参考[创建机构标签](../classroom/addSchoolLabel.md)。
  + `修改机构标签`，详情请参考[修改机构标签](../classroom/updateSchoolLabel.md)。
  + `删除机构标签`，详情请参考[删除机构标签](../classroom/deleteSchoolLabel.md)。
  + `获取机构标签（分页）`，详情请参考[获取机构标签（分页）](../classroom/getSchoolLabels.md)。
  + `添加/修改/删除课节标签`，**每个课节最多可以添加 10 个标签**，详情请参考[添加/修改/删除课节标签](../classroom/addClassLabels.md)。

## 2.1.8 2018年01月10日
- `获取直播回放播放器地址` 返回参数地址协议由 http 修改为 https，原有功能不变。详情请参考 [获取直播回放播放器地址](../broadcast/getWebcastUrl.md)。
- 手机号注册规范格式：国家区号-手机号码，**其中手机号码第一位不能够为 0**。详情请参考 [注册用户](../user/register.md)，[课节下添加学生/旁听（多个）](../classroom/addCourseStudentMultiple.md)，[课程下添加学生（多个）](../classroom/addClassStudentMultiple.md)。

## 2.1.7 2018年01月03日
- 附录
  + 增加 `ClassIn 课节相关字段的限制` 介绍页面，详情请参考 [参数规则概览](rules.md)。
  + 修改 `Postman 示例包` 测试文件及流程，详情请参考 [Postman 示例包](API_Postman.md)。
- 所有 API 中手机号规则修改为：中国大陆手机号直接填写 11 位手机号，不支持填写国家号 0086，否则会提示手机号不合法。
- `课程下添加学生/旁听（多个）`、`课节下添加学生（多个）`新增错误码 288 表示此号段不合法，修改字段 `isRegister` 为选填项。详情请参考[课程下添加学生/旁听（多个）](../classroom/addCourseStudentMultiple.md)，[课节下添加学生（多个）](../classroom/addClassStudentMultiple.md)。

## 2.1.6 2017年12月24日
- 增加 Deprecation 页面，此页面展示废弃接口。详情请参考[Deprecation](deprecated.md)。
  + `获取学生列表`、 `获取机构老师列表`、`获取学生评论列表`、`获取上课中课节成员的时间`、`获取 ClassIn 客户端下载地址` 接口将会在接下来的版本中弃用。
- `机构订阅相关接口` 下 `课节详细数据` 接口进教室字段加了 Device 表示登陆客户端类型，出教室字段加了 Reason 表示退出教室原因，详情请参考[课节详细数据](../datasub/details.md)。
- 增加 `ClassIn 下载按钮链接`，之前存放于 [获取 ClassIn 客户端下载地址](../getDownloadUrl.md) 详情请参考 [ClassIn 下载按钮链接](../iframe.md)。

## 2.1.5 2017年12月18日
- 增加接口 `修改课节上台学生数`，修改的上限值为机构最大上台人数，超出默认为机构最大上台人数，机构最大上台人数默认是 1v12，详情请参考 [修改课节上台学生数](../classroom/modifyClassSeatNum.md)。
- `获取机构老师列表` 接口新增错误码：106 表示无数据（在此之前返回 false），详情请参考 [获取机构老师列表](../user/getTeacherList.md)。

- `修改课节信息` 接口新增错误码 350 表示开课前20分钟内不能修改课节名称、上课时间、云盘资源、台上人数。详情请参考 [修改课节信息](../classroom/editCourseClass.md)。
- `教室内数据相关接口` 修改名称为 `机构订阅相关接口`，`机构消息订阅` 修改名称为 `消息订阅说明`，只对名称做修改，内容不变，详情请参考 [机构订阅相关接口](../datasub/README.md)，[消息订阅说明](../datasub/description.md)。

## 2.1.4 2017年12月13日
- 教室内相关数据接口
  + 数据公共字段增加了课程 ID CourseID，详情请参考 [数据公共字段](../datasub/publicfield.md)。
  + 课节汇总数据进出教室添加了用户身份 Identity 标识，详情请参考[课节汇总数据](../datasub/class_total.md)。
  + 课节详细数据进出教室身份描述增加：194:校长助理，255:管理员，详情请参考[课节详细数据](../datasub/details.md)。
  + 新增 `评价消息` 接口。详情请参考 [评价消息](../datasub/rating.md)。
- `获取上课中课节成员的时间信息` 新增错误码153：表示课程已过期。详情请参考[获取上课中课节成员的时间信息](../classroom/getClassMemberTime.md)。
**（推荐使用 [获取课节下出勤成员时间信息](../classroom/getClassMemberTimeDetails.md)）**。

## 2.1.3 2017年12月4日
- 删除`修改机构学生手机号`。
- 将`修改用户基本信息`接口名称修改为`修改用户昵称`，接口原有功能不变，详情请参考 [修改用户昵称](../user/editUserInfo.md)。

## 2.1.2 2017年12月1日
- `获取登录客户端链接`新增加 `deviceType` （平台标志）参数，1代表 PC，2代表 iOS，3代表 Android。默认为 1，详情请参考 [获取登陆客户端连接](../getLoginLinked.md)。

## 2.1.1：2017年11月27日
- `创建课节（单个）`、`创建课节（多个）`：将 `seatNum`（上台人数）默认值修改为6，机构最大上台人数调整为12，详情请参考 [创建课节（单个）](../classroom/addCourseClass.md)、[创建课节（多个）](../classroom/addCourseClassMultiple.md)。

## 2.1.0：2017年11月14日
- 注册用户：新增加上传用户头像的参数，`Filedata`，详细请参考用户相关接口下 [注册用户](../user/register.md) 接口。
- 获取登录客户端密钥：去掉返回链接中 `identity` 参数。详情请参考 [获取登陆客户端密钥](../getTempLoginKey.md)。
- 注册用户：ClassIn 2.0 后支持国际手机号注册，格式为 00国家号-手机号。中国大陆手机号可以省略国家号，**注：所有关于手机号的参数都支持国际手机号格式。** 详情请参考相关接口。
- 获取学生列表：返回参数总添加参数 `studentUid`，详情请参考 [获取学生列表](../user/getStudentList.md) 接口。

## 2.0.0：2017年10月30日
- EEO 基础 API 新增：`获取课节教师对学生的评价`、`获取课节学生对教师的评价`，详情请参考[获取课节教师对学生的评价](../user/getOneClassStudentComment.md)、[获取课节学生对教师的评价](../user/getOneClassTeacherComment.md)。
- 创建课程：增加了两个参数 `mainTeacherAccount`、`courseIntroduce`，详细请参考[创建课程](../classroom/addCourse.md)。
- 编辑课程：增加了四个参数 `mainTeacherAccount`、`stamp`、`Filedata`、`courseIntroduce`，详细请参考 [编辑课程](../classroom/editCourse.md)。
- 创建课节（单个）：增加了一个参数 `assistantAccount`，详情请参考 [创建课节（单个）](../classroom/addCourseClass.md)。
- 创建课节（多个）：增加了一个参数 `assistantAccount`，详情请参考 [创建课节（多个）](../classroom/addCourseClassMultiple.md)。
- 修改课节信息：增加了一个参数 `assistantAccount`，详情请参考 [修改课节信息](../classroom/editCourseClass.md)。
- `创建课节(多个)`、`课节设置录课、直播、回放(多个)`、`课节下添加学生(多个)`、`课程下添加学生/旁听(多个)`，增加批量接口自定义标识字段`customColumn`，详情请参考具体接口。
- `获取直播、回放播放器地址`：用户从机构的应用进入直播 Web 页面，免登录就可以聊天和点赞，详情请参考 [获取直播、回放播放器地址](../broadcast/getWebcastUrl.md)。
- 修改了一些字段的长度限制，详情请参考具体接口。

## 1.8.0：2017年8月14日

- 增加教室内数据推送服务：机构提供数据接收地址，以接收 EEO Hamster 服务器实时发送的数据。接口文档请参考 [教室内数据相关接口](../datasub/README.md)。

## 1.7.0：2017年6月10日

- EEO 基础 API 新增：`获取用户最新设备自检信息`、`获取 ClassIn 客户端下载地址`、`获取课节下出勤成员的时间信息` 3个接口。详情请参考 [获取用户最新设备自检信息](../user/getUserDeviceCheckInfo.md)、[获取 ClassIn 客户端下载地址](../getDownloadUrl.md)、[获取课节下出勤成员的时间信息](../classroom/getClassMemberTimeDetails.md)。

## 1.6.0：2017年5月10日

- EEO 基础 API 获取用户课程列表接口返回参数 `class_list` 对象增加了 `released` 返回值。详情请参考 [获取课程列表](../classroom/getCourseList.md)。

## 1.5.0：2017年5月8日

- EEO 基础 API 部分参数描述改动，请尽量使用最新文档。web 页 API 文档更新完成。

## 1.4.0：2017年4月24日

- 创建课节（单个）、创建课节（多个）、修改课节信息 这3个接口， 增加了 `record、live、replay` 参数，可以设置课节的直播信息设置，默认均为 0，不填写不影响现有接口。详情请参考 [创建课节（单个）](../classroom/addCourseClass.md)、[创建课节（多个）](../classroom/addCourseClassMultiple.md)、[修改课节信息](../classroom/editCourseClass.md)。

## 1.3.0：2017年4月18日

- 更正 EEO 基础 API 文档部分接口的返回值与实际返回值不一致的情况，请尽量下载阅读最新文档。

## 1.2.0：2017年3月30日

- 此次修改接口：创建课节单个、多个 这两个接口， 增加了 `seatNum` 学生上台数这个参数，可以控制课节下上台的学生人数。详情请参考 [创建课节（单个）](../classroom/addCourseClass.md)、[创建课节（多个）](../classroom/addCourseClassMultiple.md)。
- 获取课节列表、获取课节信息 这两个接口， 增加了四个返回值 `seat_num、record、live、replay`，详细说明见 [获取课节列表](../classroom/getCourseClass.md)、[获取课节信息](../classroom/getClassInfo.md)。

## 1.1.0：2017年3月28日

- 新增直播API，详情请参考 [获取直播、回放播放器地址](../broadcast/getWebcastUrl.md)。

## 1.0.0：2017年3月23日

- 获取课节列表（getCourseClass）接口，返回值新增`"class_btime": "课节开始时间戳","class_etime": "课节结束时间戳"`，详情请参考[获取课节列表](../classroom/getCourseClass.md)。

- 获取课节信息（getClassInfo）接口，返回值新增`"class_btime": "课节开始时间戳","class_etime": "课节结束时间戳"`，详情请参考[获取课节信息](../classroom/getClassInfo.md)。
