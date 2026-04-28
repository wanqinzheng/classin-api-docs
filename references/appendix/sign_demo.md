## 签名算法代码实例
为了帮助理解签名规则，这里提供了部分语言的签名算法实现以供参考。目前支持三种语言：Python、Go和PHP。  
入参payload为需要签名的数据字典。请求的json里第一层参数和值的组合。 理论上应该仅包含参与计算的kv，但是程序也做了过滤。

其他参数请根据实际情况替换

### Python


```python
import json
import time
import hashlib
import requests


def create_headers(payload):
    """
    创建验签所需信息
    :param payload: 需要签名的数据字典，其中不应包含列表、字典或长于1024个字符的字符串。
    :return:
    """
    sid = 123456
    secret = 'XXXXXX'
    time_stamp = int(time.time())

    # 过滤掉列表、字典或过长的字符串和数值
    filtered_data = {k: v for k, v in payload.items() if not isinstance(v, (list, dict)) and len(str(v)) <= 1024}
    filtered_data['sid'] = sid
    filtered_data['timeStamp'] = time_stamp

    sorted_items = sorted(filtered_data.items())  # 将字典项排序
    sign_string = "&".join(f"{key}={value}" for key, value in sorted_items)   # 构建用于签名的字符串

    # 拼接签名密钥
    sign_string += "&key={}".format(secret)
    sign = hashlib.md5(sign_string.encode('utf-8')).hexdigest()

    headers = {
        'X-EEO-SIGN': sign,
        'X-EEO-UID': f'{sid}',
        'X-EEO-TS': f'{time_stamp}',
        'Content-Type': 'application/json'
    }
    print(f'headers: {headers}')
    return headers  

```

### Go


```Go
import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func createHeaders(payload map[string]interface{}) map[string]string {
	sid := 123456
	secret := "XXXXXX"
	timeStamp := strconv.FormatInt(time.Now().Unix(), 10)

	// 过滤掉列表、字典或过长的字符串和数值
	var filteredData []string
	for k, v := range payload {
		switch v.(type) {
		case []interface{}, map[string]interface{}, string:
			if str, ok := v.(string); ok && len(str) <= 1024 {
				filteredData = append(filteredData, fmt.Sprintf("%s=%v", k, v))
			}
		default:
			if num, ok := v.(int); ok {
				filteredData = append(filteredData, fmt.Sprintf("%s=%d", k, num))
			}
		}
	}

	// 添加 sid 和 timeStamp
	filteredData = append(filteredData, "sid="+strconv.Itoa(sid))
	filteredData = append(filteredData, "timeStamp="+timeStamp)

	// 将字典项排序
	sort.Strings(filteredData)

	// 构建用于签名的字符串
	signString := strings.Join(filteredData, "&")
	signString += "&key=" + secret
	fmt.Printf("signString: %s\n", signString)
	// 使用MD5算法生成签名
	hash := md5.Sum([]byte(signString))
	sign := hex.EncodeToString(hash[:])

	headers := map[string]string{
		"X-EEO-SIGN":   sign,
		"X-EEO-UID":    strconv.Itoa(sid),
		"X-EEO-TS":     timeStamp,
		"Content-Type": "application/json",
	}

	return headers
}
```
### PHP


```PHP
<?php
function sign($body=[]){
    $eeoUId = $body['sid'];
    $secret = $body['secret'];
    $eeoTs = time();
    if(isset($body['secret'])){
        unset($body['secret']);
    }
    foreach($body as $key => $value){
        if(!is_array($value) && strlen($value) < 1024){
            $signParams[$key] = $value;
        }
    }
    $signParams['timeStamp'] = $eeoTs;
    ksort($signParams);
    $signString = '';
    foreach ($signParams as $key=>$value) {
        $signString .= $key . '=' . $value . '&';
    }
    $signString .= "key=".$secret;
    $sign = md5($signString);
    if(isset($body['sid'])){
        unset($body['sid']);
    }
    $headers = [
        'X-EEO-SIGN:'   .   $sign,
        'X-EEO-UID:'    .   $eeoUId,
        'X-EEO-TS:'     .   $eeoTs,
        'Content-Type:application/json'
    ];
    return $body = [
        'headers'    => $headers,
        'body'       => json_encode($body),
    ];
}

function curlPost($url,$params=[],$headers=[]){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_TIMEOUT, 15);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS,$params);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_POST,1);
    $result = curl_exec($ch);
    curl_close($ch);
    return json_decode($result, true);
}

//创建课堂示例
function createClass(){
    $url    = 'https://api.eeo.cn/lms/activity/createClass';
    $body   = [
        'sid'       =>  xxx, // SID
        'secret'    =>  'xxx', // SECRET
        'courseId'  =>  xxx,   // 课程ID
        'unitId'    =>  xxx,   // 单元ID
        'name'      =>  '课节名称', // 编辑单元50字，客户端100字
        'teacherUid'    =>  "老师UID",
        'startTime'     =>  开课时间,
        'endTime'       =>  结束时间
    ];
    $signParams = sign($body);
    $result = curlPost($url, $signParams['body'], $signParams['headers']);
    return $result;
}
createClass();

?>
```