# 修改教师授权云盘的课件资源

修改教师授权云盘的课件资源，需要提供 SID，safekey，timeStamp，teacherUid，folderIdJson。

** ![!deprecated](../../img/waring.png)警告：在 2024年8月30号 停用并删除此接口 **


## URL

`https://root_url/partner/api/course.api.php?action=updateTeacherCloudFolders`  

## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

| key | 必填 | 更多限制  |	说明 | 规则说明|
| ----| ----|----|----| ----- |
| SID | 是 | 无 |	机构认证 ID	| 通过 eeo.cn 申请机构认证可获得|
| safeKey |	是 | 固定 32 位全小写字符  | 机构认证安全密钥 |	safeKey=MD5(SECRET+timeStamp)|
| timeStamp	| 是 | 无 | 当前调用接口20分钟以内的 Unix Epoch 时间戳 | Unix Epoch 时间戳是 1970年1月1日00:00:00 (世界标准时间) 起经过的秒数|
| teacherUid | 是 | 无 | 教师UID（注册接口返回的UID） | bigint（数字类型）|
| folderIdJson | 是 | 无 | 云盘文件夹ID组成的JSON，string（json类型） | 可传一个或多个ID（最多40个文件夹ID，超出数量报852错误码）<br>如果想清空授权文件夹则传参[]即可<br>如果folderIdJson不为[]时，则更新老师的授权文件夹（即之前的设置会被覆盖） |


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|



## 示例

 - HTTP 请求

```http
POST /partner/api/course.api.php?action=updateTeacherCloudFolders HTTP/1.1
Host: www.eeo.cn
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=10a6f11c7e2194146c88650439aa0f2e&timeStamp=1493792469&teacherUid=1000083&folderIdJson=[29726,30054]
```

 - Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
        -d "SID=1234567" \
        -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
        -d "timeStamp=1484719085" \
        -d "teacherUid=1000083" \
        -d "folderIdJson=[29726,30054]" \
        "https://root_url/partner/api/course.api.php?action=updateTeacherCloudFolders"
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
| 1     | 表示成功执行
| 100	| 表示参数不全或错误
| 102	| 表示无权限（安全验证没通过）
| 104	| 表示操作失败
| 136   | 机构下面没有该老师，请在机构下添加该老师
| 387 	| 老师已被停用
| 800 	| 老师被停用中
| 852   | 授权云盘文件夹个数超出限制 |
| 860 	| 部分文件夹不存在
| 861 	| 部分文件夹已删除
| 862 	| 部分文件夹不属于本机构

