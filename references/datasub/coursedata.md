# 课程实时推送的消息

课程包括了LMS的各项活动，目前提供实时消息推送的活动和内容包括：

- **作业提交**  
- **作业成绩**
- **测验成绩**
- **答题卡成绩**
- **讨论活动的评论数据**

注：创建在无单元主题下的活动，也会有一个单元id，不需要的话可以忽略。

## 作业提交推送

推送时机：学生提交作业后触发实时推送

| 字段            | 类型   | 说明                     |
| --------------- | ------ | ------------------------ |
| Cmd             | String | 消息类型：HomeworkSubmit |
| SID             | Int64  | 机构ID                   |
| CourseID        | Int64  | 班级ID                   |
| CourseName      | String | 班级名称                 |
| Data            | 对象   | 作业内容                 |
| └ UnitId        | Int64  | 单元ID                   |
| └ UnitName      | String | 单元名称                 |
| └ ActivityId    | Int64  | 活动（作业）ID           |
| └ ActivityName  | String | 活动（作业）标题         |
| StudentTotal       | Int64  | 当前活动布置人数 10      |
| SubmitTotal      | Int64  | 已提交人数   6           |
| SubmissionTime    | Int64  | 作业提交时间时间戳         |
| IsSubmitLate      | Int64  | 是否逾期补交作业: 0否  1是                 |
| IsRevision      | Int64  | 是否订正: 0否  1是                 |
| Content | String | 作业文本内容   html格式          |
| Files  | 对象   | 作业附件列表             |
| 	└  Src | String | 文件下载地址             |
| 	└  FileName       | String | 文件名                   |
| 	└  FileExtension     | String | 文件格式                 |
| StudentInfo    | 对象   | 学生信息                                           |
| 	└ StudentUid     | Int64  | 学生UID                                            |
| 	└ StudentName    | String | 学生姓名：客户端作业模块展示的姓名                 |
|	└ StudentAccount | String | 学生账号：有手机号时推送手机号，没有手机号推送邮箱 |
| TeacherInfo    | 对象   | 活动教师信息                                       |
|	└ TeacherUid     | Int64  | 教师UID                                            |
|	└ TeacherName    | String | 教师姓名：客户端作业模块展示的姓名                 |
|	└ TeacherAccount | String | 教师账号：有手机号时推送手机号，没有手机号推送邮箱 |

```json

{
    "ActionTime": 1741334951,
    "CourseID": 26901289,
    "TimeStamp": 1741335551,
    "SafeKey": "d9a20c9bf3ac660766ddbfac4988ca31",
    "Cmd": "HomeworkSubmit",
    "CourseName": "test course",
    "SID": 1068502,
    "_id": "67caa9a7976eb388db162139",
    "Data": {
        "UnitId": 255618,
        "UnitName": "test unit",
        "ActivityId": 54911996,
        "ActivityName": "Magic Key",
        "StudentTotal": 2,
        "SubmitTotal": 1,
        "SubmissionTime": 1741334950,
        "Content": "<section class=\"eeo-editor-wrapper\" style=\"font-size:15px;color:#38404A;\"><p>start\u00a0</p></section>",
        "IsSubmitLate": 1,
        "IsRevision": 0,
        "Files": [
            {
                "FileExtension": "png",
                "src": "https://static.eeo.cn/upload/files/file01/20250307/03_0-0cc8-577183e60485_1741334949147.png",
                "fileName": "eeo.png"
            }
        ],
        "TeacherInfo": {
            "TeacherName": "Lucy",
            "TeacherAccount": "001-38102248",
            "TeacherUid": 10602
        },
        "StudentInfo": {
            "StudentName": "GoodGuy",
            "StudentAccount": "001-72340105",
            "StudentUid": 102494
        }
    }
}

```

## 作业成绩推送

推送时机：作业成绩产生/变更时，一般是老师批阅之后。

|字段 | 类型 | 说明 |
|----|------|-------|
|Cmd|	String|	消息类型：HomeworkScore	
|SID|	Int64	|机构ID	
|CourseID|	Int64|	班级ID	
|CourseName	|String|	班级名称|	
|Data| 对象|	作业内容和成绩|	
|└ UnitId|	Int64|	单元ID	|
|└ UnitName|	String|	单元名称|	
|└ ActivityId|	Int64|	活动（作业）ID	|
|└ ActivityName|	String|	活动（作业）标题	|
|└ Score	|float	|总分	|
|└ State | Int64 | 状态: 40 已批阅; 50 已打回 |
| └ StudentInfo|对象|学生信息|
| 　 └ StudentUid|Int64|学生UID|
| 　 └ StudentName|String|学生姓名：客户端作业模块展示的姓名|
| 　 └ StudentAccount|String|学生账号：有手机号时推送手机号，没有手机号推送邮箱|
|└ SubmissionTime	|Int64	|作业提交时间	|
|└ CorrectionTime	|Int64|	批阅时间	|
|└ StudentScoringRate	|float|	学生得分率：小数，例如0.8；计算逻辑：学生得分/满分 |
|└ GradingPlan   | String | 评分显示方法             | 
|└ StudentScore  | String | 学生按评分方式的打分     | 
|└ ReviewDetails | 对象   | 详细成绩内容             |   
| 　 └ Correct       | Int64    | 正确个数                 
| 　 └ Wrong         | Int64    | 错误个数                 | 
| 　 └ Trophy        | Int64    | 奖杯个数                 |                
| 　 └ Excellent     | Int64    | 0表示不是优秀，1表示优秀 |             
| 　 └ Comment       | String | 评语                     |  
| └ TeacherInfo|对象|批阅教师信息|
| 　 └ TeacherUid|Int64|教师UID|
| 　 └ TeacherName|String|教师姓名：客户端作业模块展示的姓名|
| 　 └ TeacherAccount|String|教师账号：有手机号时推送手机号，没有手机号推送邮箱|

### 实例

```json

{
    "Cmd" : "HomeworkScore",
    "SID" : 2803666,
    "CourseID" : 2279909,
    "CourseName" : "Test",
    "Data" : {
        "UnitId" : 256,
        "UnitName" : "Unit One",
        "ActivityId" : 185647,
        "ActivityName" : "Test Homework",
        "Score" : 100, 
        "StudentScore": "90", 
        "State": 40,
        "ReviewDetails": {
            "Trophy": 9,
            "Comment": "<section class=\"eeo-editor-wrapper\" style=\"font-size: 15px; color: #38404a;\"><p>good job *2\u00a0</p></section>",
            "Wrong": 6,
            "Correct": 10,
            "Excellent": 1
        },
        "StudentInfo" : {
                "StudentUid" : 1000083,
                "StudentName" : "Amy",
                "StudentAccount" : "13451113311"
        },
        "SubmissionTime" : 1713053774,
		"GradingPlan": "\u5206\u6570\u5236",
        "CorrectionTime" : 1713083674,
        "StudentScoringRate" : 0.9,
        "TeacherInfo" : {
                "TeacherUid" : 1000082,
                "TeacherName" : "Mike",
                "TeacherAccount" : "13466668866"
        }
    }
}

```

## 测验成绩推送
推送时机：测验成绩产生时。自动判分或者老师判分都会产生成绩。只产生部分成绩不会推送。如果修改答案导致成绩变化也会推送。
注：10月30日上线新字段。

|字段 | 类型 | 说明 |
|----|------|-------|
|Cmd|	String|	消息类型：ExamScore|
|SID|	Int64|	机构ID	|
|CourseID	|Int64|	班级ID	|
|CourseName|	String|	班级名称|
|Data	|对象	|测验内容和成绩	|
|└ UnitId	|Int64	|单元ID	|
|└ UnitName|	String|	单元名称	|
|└ ActivityId	|Int64	|活动（测验）ID	|
|└ ActivityName	|String|	活动（测验）标题|  
|└ClassId	|Int64|	课节id（只有在课上新创建的测验才有）	|  	
|└ Score	|float|	总分|	
| └ StudentInfo|对象|学生信息|
| 　 └ StudentUid|Int64|学生UID|
| 　 └ StudentName|String|学生姓名：客户端作业模块展示的姓名|
| 　 └ StudentAccount|String|学生账号：有手机号时推送手机号，没有手机号推送邮箱|
|└ SubmissionTime	|Int64|	测验提交时间|	
|└ AnswerDuration	|Int64|	测验答题时长（秒）|	
|└ CorrectionTime|	Int64|	批阅时间	|
|└ StudentScoringRate|	float	|学生得分率：小数，例如0.8；计算逻辑：学生得分/满分 |
| └ TeacherInfo|对象|批阅教师信息|
| 　 └ TeacherUid|Int64|教师UID，自动批阅则为0|
| 　 └ TeacherName|String|教师姓名：客户端作业模块展示的姓名，自动批阅则为空|
| 　 └ TeacherAccount|String|教师账号：有手机号时推送手机号，没有手机号推送邮箱，自动批阅则为空|  
|└TopicDetails	|array[object]	|数组	|  
| 　 └TopicId|	int|	题目序号，比如 “1” 为第一大题|   	
| 　 └TopicType	|String	|题目类型，传字符串	题型 1：单选，2：多选，3：判断，4：填空，5：问答，6：综合；如使用官方题库，此字段为空|   
| 　 └ TopicResult|	int|	0 = 待批阅，1=正确，3=半对，2=错误，4=未答	
| 　 └TopicScore|	float	|题目总得分（可能会有小题）	|
| 　 └TopicMaxScore|	float|	这道题的满分	|
| 　 └SubTopicDetails|	array[object]	|  如果题目没有小题则没有这一项	没有小题时返回[]，使用时需进行校验|  
| 　  　 └SubTopicId	|int|	小题序号	|
| 　  　 └SubTopicType|String|	小题类型，传字符串	|
| 　  　 └SubTopicResult	|int	|0 = 待批阅，1=正确，3=半对，2=错误，4=未答	|
| 　  　 └SubTopicScore|float|	小题得分|  
| 　  　 └SubTopicMaxScore |int	|小题的满分| 

### 实例

```json
{
	"CourseID": 429724,
	"Cmd": "ExamScore",
	"CourseName": "测试双师课",
	"SID": 187286,
	"Data": {
		"ClassId": 34928113,
		"TeacherInfo": {
			"TeacherName": "我是44401",
			"TeacherAccount": "444401",
			"TeacherUid": 187286
		},
		"ActivityName": "测验  星期二",
		"UnitName": "默认单元",
		"AnswerDuration": 57,
		"ActivityId": 32044258,
		"Score": 24,
		"StudentInfo": {
			"StudentName": "",
			"StudentAccount": "12133333301",
			"StudentUid": 187268
		},
		"UnitId": 32014550,
		"SubmissionTime": 1729576858,
		"TopicDetails": [{
			"TopicId": 1,
			"TopicType": "1",
			"SubTopicDetails": [],
			"TopicResult": [2],
			"TopicMaxScore": 5,
			"TopicScore": 0
		}, 
		{
			"TopicId": 2,
			"TopicType": "5",
			"SubTopicDetails": [],
			"TopicResult": [3],
			"TopicMaxScore": 4,
			"TopicScore": 2
		}, 
		{
			"TopicId": 3,
			"TopicType": "4",
			"SubTopicDetails": [],
			"TopicResult": [2, 2, 2],
			"TopicMaxScore": 6,
			"TopicScore": 0
		}, 
		{
			"TopicId": 4,
			"TopicType": "6",
			"SubTopicDetails": [{
				"SubTopicId": 1,
				"SubTopicType": "1",
				"SubTopicResult": [2],
				"SubTopicScore": 0,
				"SubTopicMaxScore": 5
			}, 
			{
				"SubTopicId": 2,
				"SubTopicType": "2",
				"SubTopicResult": [2],
				"SubTopicScore": 0,
				"SubTopicMaxScore": 4
			}],
			"TopicResult": [2],
			"TopicMaxScore": 9,
			"TopicScore": 0
		}],
		"StudentScoringRate": 0.083333,
		"CorrectionTime": 1729576949
	}
}
```

## 答题卡成绩推送
推送时机：答题卡成绩产生时触发实时推送。自动判分或者老师判分都会产生成绩。只产生部分成绩不会推送。如果修改答案导致成绩变化也会推送。    
ps：批阅老师字段目前没有值。为预留字段。



| 字段            | 类型       | 描述                                                                 |
|-----------------|------------|----------------------------------------------------------------------|
| Cmd             | String     | 答题卡成绩，AnswerSheetScore                                                 |
| SID             | Int64      | 学校ID                                                              |
| CourseID        | Int64      | 课程ID                                                              |
| CourseName      | String     | 课程名称                                                            |
| Data            | Object     | 答题卡信息及分数                                                     |
| └ UnitId        | Int64      | 单元ID                                                              |
| └ UnitName      | String     | 单元名称                                                            |
| └ ActivityId    | Int64      | 活动（答题卡）ID                                                    |
| └ ActivityName  | String     | 活动（答题卡）标题                                                  |
| └ ClassId       | Int64      | 课时ID，当答题卡在课节中发布时才有，否则为0                                |
| └ Score         | float      | 满分分值                                                            |
| └ StudentInfo   | Object     | 学生信息                                                            |
| 　└ StudentUid    | Int64      | 学生UID                                                             |
| 　└ StudentName   | String     | 学生姓名（在ClassIn客户端作业模块显示的名字）                        |
| 　└ StudentAccount | String     | 学生账号（优先推送注册手机号，无手机号则推送邮箱）                   |
| └ SubmissionTime | Int64     | 答题卡提交时间                                           |
| └ AnswerDuration | Int64     | 学生答题耗时 单位：秒                                           |
| └ CorrectionTime | Int64     | 批改时间                                                  |
| └ StudentScoringRate | float  | 学生得分率（小数形式，如0.8；计算逻辑：学生得分/满分）              |
| └ TopicDetails   | array[object] | 题目详情数组                                                        |
| 　└ TopicId       | int        | 题目ID（如1）                                                       |
| 　└ TopicType     | String     | 题目类型（字符串类型）：<br>1-单选题，2-多选题，3-判断题，<br>4-填空题，5-问答题，6-综合题 |
| 　└ TopicResult   | int        | 题目结果：<br>0=待批改，1=正确，3=半对，2=错误，4=未作答            |
| 　└ TopicScore    | float      | 学生在该题目上的得分                                                |
| 　└ TopicMaxScore | float      | 该题目的满分分值                                                    |
| 　└ SubTopicDetails | array[object] | 子题目详情数组（若无子题则为空数组[]）                             |
| 　 　└ SubTopicId    | int        | 子题目ID                                                            |
| 　 　└ SubTopicType  | String     | 子题目类型（字符串类型）：同TopicType定义                           |
| 　 　└ SubTopicResult | int[]     | 子题目结果数组（取值同TopicResult）                                 |
| 　 　└ SubTopicScore  | float     | 子题目得分                                                          |
| 　 　└ SubTopicMaxScore | int     | 子题目满分分值                                                      |
| └ TeacherInfo    | Object     | 保留字段-批改教师信息（当前为空）                                    |
| 　└ TeacherUid     | Int64      | 保留字段-教师UID（当前Uid值为0，后续版本会更新）                     |
| 　└ TeacherName    | String     | 保留字段-教师姓名（在ClassIn客户端作业模块显示的名字，当前为空）     |
| 　└ TeacherAccount | String     | 保留字段-教师账号（优先推送注册手机号，无手机号则推送邮箱；自动批改时为空）|

### 实例


```json
{
    "ActionTime": 1741332102,
    "CourseID": 269406477,
    "TimeStamp": 1741332702,
    "SafeKey": "3d8bc13a3ed4a7cb5474848055960ce3",
    "Cmd": "AnswerSheetScore",
    "elapsed": 4,
    "CourseName": "xx测试课程",
    "SID": 27897288,
    "_id": "67ca9e8664ab5ae364892c98",
    "Data": {
        "ClassId": 0,
        "TeacherInfo": {
            "TeacherName": "",
            "TeacherAccount": "",
            "TeacherUid": 0
        },
        "ActivityName": "答题卡 3月7日 星期五",
        "UnitName": "test",
        "AnswerDuration": 5,
        "ActivityId": 63919314,
        "StudentInfo": {
            "StudentName": "CN-张三",
            "StudentAccount": "001-12345678",
            "StudentUid": 27897298
        },
        "UnitId": 33376336,
        "MaximumScore": 14,
        "SubmissionTime": 1741332102,
        "TopicDetails": [
            {
                "TopicId": 1,
                "TopicType": "1",
                "SubTopicDetails": [

                ],
                "TopicResult": [
                    1
                ],
                "TopicMaxScore": 5,
                "TopicScore": 5
            },
            {
                "TopicId": 2,
                "TopicType": "2",
                "SubTopicDetails": [

                ],
                "TopicResult": [
                    3
                ],
                "TopicMaxScore": 4,
                "TopicScore": 2
            },
            {
                "TopicId": 3,
                "TopicType": "3",
                "SubTopicDetails": [

                ],
                "TopicResult": [
                    1
                ],
                "TopicMaxScore": 5,
                "TopicScore": 5
            }
        ],
        "StudentScoringRate": 0.857143,
        "CorrectionTime": 0
    }
}

```

## 讨论活动的评论数据
推送时机：在讨论产生评论、回复或者点赞的时候实时推送    
注： 暂不支持推送附件，所有附件以[附件]占位符形式出现在消息中。


| 字段            | 类型       | 描述    
|-------------------|----------|-----------------------------------------------------|
| Cmd               | String   | 消息类型，  "DiscussionChangeInfo"            |
| SID               | Int64    | 机构ID                                              |
| CourseID          | Int64    | 班级ID                                              |
| CourseName        | String   | 班级名称                        |
| OpType            | Int64    | 操作类型，1: 增加   2: 删除   3: 修改   |
| Data              | Object   | 操作内容对象                                        |
| └ UnitId         | Int64    | 单元ID                                              |
| └ UnitName       | String   | 单元名称                                            |
| └ ActivityId     | Int64    | 活动（讨论）ID                                      |
| └ ActivityName    | String   | 活动标题                                            |
| └ TeacherUid     | Int64    | 老师ID                                              |
| └ TeacherName    | String   | 老师姓名                                            |
| └ TeacherAccount  | String   | 老师账号                                            |
| └ CommentDetail   | Object   | 更多消息内容，此结构内的数据根据消息类型不同，有些字段可能不存在 |
|   └ Type         | Int64    | 评论类型，1: 评论   2: 回复 3: 点赞  |
|   └ CommentId     | Int64    | 消息ID，本次操作的消息ID                            |
|   └ CommentContent | String   | 消息内容，仅评论和回复的增、改操作有此字段​        |
|   └ ParentId      | Int64    | 消息上游ID，仅回复的增、删、改操作有此字段​​ ，一级评论没有此字段 |
|   └ LikeCount     | Int64    | 本消息点赞总数，仅点赞操作有此字段​                |
|   └ TopReplyCount | Int64    | 本消息一级评论回复数，仅回复操作有此字段​          |
| └ CreatorUid      | Int64    | 消息创建者ID                                        |
| └ CreatorName     | String   | 消息创建者姓名                                      |
| └ CreatorAccount   | String   | 消息创建者账号                                      |
| └ CreatorRole     | Int64    | 消息创建者身份，1: 老师   2: 学生   |

### 实例

```json     
{
    "OpType": 1,
    "CourseID": 437144,
    "TimeStamp": 1756196650,
    "SafeKey": "dc92306b95816696f2db57d878b9be0d",
    "Cmd": "DiscussionChangeInfo",
    "CourseName": "测试课程",
    "ActionTime": 1756196050,
    "SID": 104058,
    "_id": "68ad6cd239532ec1259f0ff0",
    "Data": {
        "CommentDetail": {
            "CommentContent": "讨论回复111",
            "CommentId": 18000860,
            "Type": 2,
            "ParentId": 18000859
        },
        "TeacherName": "我是890，请不要随意改昵称和密码",
        "ActivityName": "讨论消息",
        "TeacherUid": 104058,
        "UnitName": "08-22讨论消息订阅",
        "CreatorName": "我是890，请不要随意改昵称和密码",
        "CreatorAccount": "12112160890",
        "CreatorUid": 104058,
        "ActivityId": 54292142,
        "UnitId": 53001768,
        "CreatorRole": 1,
        "TeacherAccount": "12112160890"
    }
}
```



