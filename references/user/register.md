# 注册用户
注册用户是一个必要的API调用，为机构的用户代注册ClassIn账号。     
**在调用此接口前，请保证所传的手机号或邮箱用户对此代注册操作知情并同意和授权。如若产生用户不知情的代注册，将可能导致学校/机构的代注册功能被停用**  

需要 SID，safekey，timeStamp，使用有效手机号或邮箱注册，作为登录 `ClassIn 客户端` 的账号，昵称和头像为可填项，密码可为明文或 MD5 加密方式(建议使用 MD5 加密)，注册成功后会返回学生的 UID（此 UID 为该账号的唯一 ID，后续接口都会使用到此参数，建议一定保存）。

说明：
- 头像是显示在 ClassIn 客户端的；
- 昵称是显示在 ClassIn 客户端的，如果 addToSchoolMember 传参 1 或者 2 时，其还会作为姓名显示在 eeo.cn 学生/教师管理页面；
- 默认情况下，新注册的用户不会显示在 eeo.cn 的学生/老师管理页面。目前有以下两种方式，可以将用户添加为机构下学生/老师：
  1. 在注册用户接口传参 addToSchoolMember（1：加为机构学生；2：加为机构老师；其他值不加为机构成员）
  2. 调用 [添加学生](./addSchoolStudent.md) 接口即可成为本机构下学生，调用 [添加老师](./addTeacher.md) 接口即可成为本机构下老师。    
- 如果没有经过以上添加机构学生、老师的过程，会在后继排课接口调用的时候报错导致接口调用失败（报错信息举例：该用户不是机构下老师 等）   

**请注意**：
1. 如果手机号码或邮箱已注册ClassIn，调用 register 接口的话，则会返回错误码 135，同时依然会返回UID。
2. 只有第一次注册时，昵称、头像、密码才会生效。
3. 不管是否第一次注册，addToSchoolMember 参数总会生效。

## URL

`https://root_url/partner/api/course.api.php?action=register`

## HTTP Request Methods

- POST

## 编码格式

- UTF-8

## 请求参数

| key                  | 必填               | 更多限制                                            | 说明                             | 规则说明                                              |
|----------------------|--------------------|-----------------------------------------------------|----------------------------------|-------------------------------------------------------|
| SID                  | 是                 | 无                                                  | 机构认证 ID                     | 通过 eeo.cn 申请机构认证可获得                       |
| safeKey              | 是                 | 固定 32 位全小写字符                               | 机构认证安全密钥                 | safeKey=MD5(SECRET+timeStamp)                         |
| timeStamp            | 是                 | 无                                                  | 当前调用接口20分钟以内的 Unix Epoch 时间戳 | Unix Epoch 时间戳是 1970年1月1日 00:00:00 (世界标准时间) 起经过的秒数 |
| telephone            | 是（与 email 2 选 1） | 格式为：00国家号-手机号；**注意：中国大陆手机号不写国家号，手机号第一位不能为0** | 注册手机号                     | 例如：美国手机号 1 (800) 643-7676 填成 001-8006437676；中国大陆手机号填成 15800000001 |
| email                | 是（与 telephone 2 选 1） | 无                                                  | 无                               | 无                                                    |
| nickname             | 否                 | 最长24位字符，超过24字会自动截取为24字           | 昵称、姓名                       | 填写该参数，则会将该参数作为老师或学生的昵称（显示在客户端）；不填写昵称，手机号会作为老师或者学生的昵称（用户登录客户端，会弹窗让用户填写昵称）。昵称显示在教室内用户摄像头下方,最大24个字符 |
| password             | 是（与 md5pass 2 选 1） | 无                                                  | 明文密码                         | 6-20位，不符合会报错                                   |
| md5pass              | 是（与 password 2 选 1） | 无                                                  | MD5 加密密码                     | 32位 MD5 加密                                         |
| Filedata             | 否                 | 二进制流                                           | 上传的用户头像，头像会显示在 ClassIn 客户端；不上传头像，登录客户端时会弹出选择头像的弹窗 | 图片类型：jpg，jpeg，gif，png<br>尺寸：300*300<br>大小：小于 1 M |
| addToSchoolMember    | 否                 | 0 不加为机构成员；1 加为机构学生；2 加为机构老师；其他值不加为机构成员。不填默认为0。 | addToSchoolMember等于1或者2时，用户会显示在 eeo.cn 后台的学生/教师管理页面，并且其 nickname 会被用来设置学生或者老师在 eeo.cn 后台显示的姓名 | 是否加为机构成员（老师、学生）                          |


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| data | number |  | 注册成功返回的用户 UID（此 UID 为该账号唯一 ID）|
| error_info | 	object |	|	返回信息对象|
| └ errno |	number |	1	 | 错误代码|
| └ error |	string |	"程序正常执行" |	错误详情|

## 示例

- HTTP 请求

```http
POST /partner/api/course.api.php?action=register HTTP/1.1
Host: root_url
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=3276433ab0216d9aec2621431cc12248&timeStamp=1494407873&telephone=18516900101&password=123456&Filedata=@~/photo.jpg&addToSchoolMember=1
```

- Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: multipart/form-data" -X "POST" \
      -d "SID=1234567" \
      -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2" \
      -d "timeStamp=1484719085" \
      -d "telephone=12345678900" \
      -d "password=123456" \
      -d "Filedata=@D:\touxiang.jpg" \
      -d "addToSchoolMember=1" \
      "https://root_url/partner/api/course.api.php?action=register"
```


## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
  "data": 1001930,
  "error_info": {
    "errno": "1",
    "error": "程序正常执行"
  }
}
```


## 错误码说明

| 错误码 |	说明 |
|----|-----|
|  1  | 表示执行成功 	
| 100 |	表示参数不全或错误
| 102 |	表示无权限（安全验证没通过）
| 114 |	表示服务器异常
| 131 |	表示注册失败
| 134 |	表示手机号不合法
| 135 |	表示手机号已注册(同时会返回用户UID)
| 137 |	表示密码长度不合法(6-20位)
| 224 | 表示上传图片类型错误
| 288 |	表示此号码段不合法
| 340 | 表示注册成功，用户头像设置失败
| 341 | 表示上传图片尺寸错误（300*300）
| 342 | 表示上传图片大小超出限制（1M）
| 461 | 表示邮箱已注册(同时会返回用户UID)
| 820 | 表示注册成功，加为机构学生失败
| 821 | 表示注册成功，加为机构老师失败
| 845 | 表示超出机构老师最大启用数量
| 101003002	|  重复请求（请勿在5s内发送相同参数的请求）
