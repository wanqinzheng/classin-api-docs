# 注册用户（多个）
注册用户（多个），一次性最多注册10个。需要 SID，safekey，timeStamp，使用有效手机号或邮箱注册，作为登录 `ClassIn 客户端` 的账号，昵称为可填项，密码可为明文或 MD5 加密方式(建议使用 MD5 加密)，注册成功后会返回用户的 UID（此 UID 为该账号的唯一 ID，后续接口都会使用到此参数，建议一定保存）。

说明：
- 此接口不支持传参用户头像，如果需要设置的话，您可以调用接口 [修改用户信息](./editUserInfo.md) 以修改单个用户头像信息。
- 昵称是显示在 ClassIn 客户端的，如果 addToSchoolMember 传参 1 或者 2 时，且账号为首次注册ClassIn用户时，其还会作为姓名显示在 eeo.cn 学生/教师管理页面；
- 默认情况下，新注册的用户不会显示在 eeo.cn 的学生/老师管理页面。目前有以下两种方式，可以将用户添加为机构下学生/老师：
  1. 在注册用户接口传参 addToSchoolMember（1：加为机构学生；2：加为机构老师；其他值不加为机构成员）。
  2. 调用 [添加学生](./addSchoolStudent.md) 接口即可成为本机构下学生，调用 [添加老师](./addTeacher.md) 接口即可成为本机构下老师。    
- 如果没有经过以上添加机构学生、老师的过程，会在后继排课接口调用的时候报错导致接口调用失败（报错信息举例：该用户不是机构下老师 等）   

**请注意**：
1. 如果手机号码或邮箱已注册ClassIn，调用 register 接口的话，则会返回错误码 135，同时依然会返回UID。 
2. 只有第一次注册时，昵称、头像、密码才会生效。

## URL

`https://root_url/partner/api/course.api.php?action=registerMultiple`

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
| userJson | 是 | array，至少传一个 | 批量注册的用户数据 | 无|
|　└telephone | 是（与email 2选1） | 格式为：00国家号-手机号；**注意：中国大陆手机号不写国家号，手机号第一位不能为0** | 注册手机号 | 例如：美国手机号 1 (800) 643-7676 填成 001-8006437676；中国大陆手机号填成 15800000001|
|　└email | 是（与telephone 2选1） | 无 | 无 | 无|
|　┖nickname | 否 | 最长24位字符，超过24字会自动截取为24字 | 昵称、姓名 | 填写该参数，则会将该参数作为老师或学生的姓名和昵称；不填写昵称，登录客户端会弹出填写昵称的弹框，手机号会作为老师或者学生的昵称和姓名。昵称显示在教室内用户摄像头下方,最大24个字符；姓名显示在 eeo.cn 后台|
|　┖password | 是(与 md5pass 2选1) | 无 | 明文密码 | 6-20位，不符合会报错|
|　┖md5pass	| 是(与 password 2选1) | 无 | MD5 加密密码 | 32位 MD5 加密|
|　┖addToSchoolMember | 否 | 0 不加为机构成员；1 加为机构学生；2 加为机构老师；其他值不加为机构成员。不填默认为0。 | 如果添加为机构学生，会显示在 eeo.cn 的学生管理处；如果添加为机构老师，会显示在 eeo.cn 的老师管理处 | 是否加为机构成员（老师、学生） |
|　└customColumn | 否 | 1-50字符，超过会自动截取为50字 | 用户自定义标识 | 不为空则原样返回，为空则不返回该字段|


## 响应参数

| 参数名 | 类型 | 示例值 | 含义|
|-----|---- | ---- |-----|
| data | array |  | 注册的用户对象列表|
|　└   | object |  | 注册后会返回用户的信息|
|　　└ data | number | 1283830 | 注册成功的用户 UID|
|　　└ telephone | string | 13800000000 | 注册的手机号码|
|　　└ customColumn | string | 08cbe7986a2da0975ef0e538790b9987 | 返回用户传入的自定义字段|
|　　└ errno | number | 1 | 错误代码|
|　　└ error | string | "程序正常执行" | 错误详情|
| error_info | 	object |	|	返回信息对象|
|　└ errno |	number |	1	 | 错误代码|
|　└ error |	string | "程序正常执行" |	错误详情|

## 示例

- userJson说明

```json
userJson:[
		{"telephone":"xxxx","nickname":"xxxx","password":"xxxx"},
		{"telephone":"xxxx","nickname":"xxxx","password":"xxxx"}
	]
```

- HTTP 请求

```http
POST /partner/api/course.api.php?action=registerMultiple HTTP/1.1
Host: root_url
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache

SID=2339736&safeKey=5458edceccc78c6698de624e94364285&timeStamp=1493026245&userJson=[{"telephone":18516900101,"password":123456,"addToSchoolMember":1},{"telephone":18516900102,"password":123456,"addToSchoolMember":1}]
```

- Shell cURL 模拟请求指令

```bash
curl -H "Content-Type: application/x-www-form-urlencoded" -X "POST" \
        -d "SID=1234567"\ 
        -d "safeKey=0f7781b3033527a8cc2b1abbf45a5fd2"\ 
        -d "timeStamp=1484719085"\ 
        -d 'userJson=
          [ \
            {\
              "telephone": 18516900101,\
              "password": 123456,\
              "addToSchoolMember": 1\
            }, 
            {
               "telephone": 18516900102,\
               "password": 123456,\
               "addToSchoolMember": 1\
            }\
          ]'\
        "https://root_url/partner/api/course.api.php?action=registerMultiple"
```




## 响应示例（正常时返回的 `json` 数据包示例）

```json
{
    "data": [
        {
            "data": 19820374,
            "telephone": "13800000000",
            "errno": 1,
            "error": "程序正常执行"
        }
    ],
    "error_info": {
        "errno": 1,
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
| 155 | 表示数据数组长度不可为空
| 224 | 表示上传图片类型错误
| 288 |	表示此号码段不合法
| 450 | 表示数量超出限制（一次最多注册10名）
| 461 | 表示邮箱已注册(同时会返回用户UID)
| 820 | 表示注册成功，加为机构学生失败
| 821 | 表示注册成功，加为机构老师失败
| 845 | 表示超出机构老师最大启用数量
| 101003002	|  重复请求（请勿在5s内发送相同参数的请求）
