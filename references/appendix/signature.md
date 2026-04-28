# ClassIn API v2签名方式说明
从LMS 系列API 开始，ClassIn API 接口将使用header进行鉴权，不再使用SafeKey参数进行鉴权。

- 加密后的签名值将放在请求的header里，参数为 “X-EEO-SIGN”，加密规则为`sign = md5(’请求串&key=密钥’)`  
- 原学校sid和timeStamp将放到header里，对应“X-EEO-UID” 和 “X-EEO-TS” 参数，body参数中不应包含sid和timeStamp。   
- “X-EEO-TS” 需保证当前调用接口5分钟以内的 Unix Epoch 时间戳，秒级别
- body参数中禁止使用 “key” 作为参数名

## header示例
```json
{
    "X-EEO-SIGN": "sign",  # 参数加密后sign
    "X-EEO-UID": "sid",  # 学校SID
    "X-EEO-TS": "timeStamp",  # 当前调用接口5分钟以内的 Unix Epoch 时间戳，秒级别
    "Content-Type": "application/json"
}
```

## 如何生成请求签名    
   
###  Step 1：排除不参与签名的请求参数
body为json格式，按以下规则，从body中取出参与签名的key/value。 

  1. 数组和字典类参数不参与签名，需剔除；
  2. value字节长度大于1024的参数，不参与签名，需剔除；

###  Step 2：拼接待签名字符串

1. 将sid=XXXXXX以及timeStamp=XXXXXXXX添加进待签名的参数中；
2. 按参数名ASCII码从小到大排序（字典序），使用URL键值对的格式（即key1=value1&key2=value2…）拼接成字符串stringA。
3. 在stringA最后拼接上'&key=秘钥' 

### Step 3：计算待签名字符串的32位小写md5值
计算整个字符串的md5值（32位小写）作为签名值，即sign；




## **示例**

假设一个接口请求如下，密钥：`Mb71234`

```bash
curl --location --request POST '/lms/unit/test' \
--header 'X-EEO-SIGN: 4f97f55addf4921a05c2395617cd8a7b' \
--header 'X-EEO-UID: 1000082' \
--header 'X-EEO-TS: 1721095405' \
--header 'Content-Type: application/json' \
--data-raw '{
    "courseId": 132323,
    "unitJson": [
        {
            "name": "string",
            "content": "string",
            "publishFlag": 0
        }
    ],
}'
```

1. **拼接请求串**
    
    排除不参与签名的请求参数：unitJson（数组）,再加上sid和timeStamp,得到请求参数和值列表如下：
    
    | 参数名 | 参数值 |  
    | --- | --- |  
    | sid | 1000082 |  
    | courseId | 132323 |    
    | timeStamp | 1721095405 |  
    
    将得到的参数按参数名ASCII码从小到大排序（字典序），使用URL键值对的格式（即key1=value1&key2=value2…）拼接成字符串stringA。
    
    在stringA最后拼接上key（密钥），得到待签名字符串。
    
    按以上规则，示例中得到的待签名字符串如下：
    
    ```
    courseId=132323&sid=1000082&timeStamp=1673949471&key=Mb71234
    ```
    
2. **计算签名**
    
    对待签名字符串进行 md5 运算，得到签名值。
    
    此示例计算结果是 `d0d99023aa44549f97dfe9523059f0c3`。

    
    
## 代码实例
[签名算法代码实例](sign_demo.md)
## 签名失败

签名失败相关错误码如下

| 错误码 | 说明 |
| --- | --- |
|101002005|	签名异常（签名没有传或者错误）|
|101002006|	验签时间戳过期（当前时间前后5分钟内）|
|101002008| 时间戳不存在|
|121601030|	参数不全或者错误|
