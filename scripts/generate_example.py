#!/usr/bin/env python3
"""
generate_example.py - 为指定的 ClassIn API 接口生成多语言调用示例代码

用法：
    python scripts/generate_example.py --api <api_name> --lang <python|java|nodejs|php|go>

示例：
    python scripts/generate_example.py --api create_classroom --lang python
    python scripts/generate_example.py --api auth_signature --lang nodejs
"""

import argparse
import sys

# 支持的 API 示例配置
API_TEMPLATES = {
    "create_classroom": {
        "name": "创建课堂",
        "method": "POST",
        "url": "/v1/classroom/create",
        "params": {
            "name": "高中数学第一课",
            "startTime": 1713751200,
            "endTime": 1713754800,
            "teacherId": "teacher_001",
            "maxStudents": 30
        }
    },
    "auth_signature": {
        "name": "签名鉴权",
        "method": "POST",
        "url": "/v1/classroom/create",
        "params": {
            "name": "测试课堂"
        }
    },
    "get_join_url": {
        "name": "获取入课链接",
        "method": "GET",
        "url": "/v1/classroom/join_url",
        "params": {
            "classroomId": "cls_abc123",
            "userId": "student_001",
            "role": "student"
        }
    }
}

TEMPLATES = {
    "python": """import hashlib
import hmac
import time
import random
import string
import requests
import json

APP_KEY = "your_app_key"
APP_SECRET = "your_app_secret"
BASE_URL = "https://api.eeo.cn"

def generate_signature(params: dict) -> dict:
    \"\"\"生成 ClassIn API 签名\"\"\"
    timestamp = str(int(time.time()))
    nonce = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    
    sign_params = {{**params, 'appKey': APP_KEY, 'timestamp': timestamp, 'nonce': nonce}}
    sorted_keys = sorted(sign_params.keys())
    sign_str = '&'.join(f'{{k}}={{sign_params[k]}}' for k in sorted_keys)
    
    signature = hmac.new(
        APP_SECRET.encode('utf-8'),
        sign_str.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    return {{
        **params,
        'appKey': APP_KEY,
        'timestamp': timestamp,
        'nonce': nonce,
        'signature': signature
    }}

# {api_name} - {description}
def call_api():
    params = {params}
    signed_params = generate_signature(params)
    
    response = requests.post(
        BASE_URL + "{url}",
        json=signed_params,
        headers={{'Content-Type': 'application/json'}}
    )
    result = response.json()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result

if __name__ == '__main__':
    call_api()
""",

    "nodejs": """const crypto = require('crypto');
const axios = require('axios');

const APP_KEY = 'your_app_key';
const APP_SECRET = 'your_app_secret';
const BASE_URL = 'https://api.eeo.cn';

function generateSignature(params) {{
  const timestamp = Math.floor(Date.now() / 1000).toString();
  const nonce = Math.random().toString(36).substring(2, 18);
  
  const signParams = {{ ...params, appKey: APP_KEY, timestamp, nonce }};
  const sortedKeys = Object.keys(signParams).sort();
  const signStr = sortedKeys.map(k => `${{k}}=${{signParams[k]}}`).join('&');
  
  const signature = crypto
    .createHmac('sha256', APP_SECRET)
    .update(signStr)
    .digest('hex');
  
  return {{ ...signParams, signature }};
}}

// {api_name} - {description}
async function callApi() {{
  const params = {params};
  const signedParams = generateSignature(params);
  
  const response = await axios.post(BASE_URL + '{url}', signedParams);
  console.log(JSON.stringify(response.data, null, 2));
  return response.data;
}}

callApi().catch(console.error);
""",

    "java": """import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.net.http.*;
import java.net.URI;

public class ClassInApiExample {{
    private static final String APP_KEY = "your_app_key";
    private static final String APP_SECRET = "your_app_secret";
    private static final String BASE_URL = "https://api.eeo.cn";

    public static String generateSignature(Map<String, String> params) throws Exception {{
        long timestamp = System.currentTimeMillis() / 1000;
        String nonce = UUID.randomUUID().toString().replace("-", "").substring(0, 16);
        
        Map<String, String> signParams = new TreeMap<>(params);
        signParams.put("appKey", APP_KEY);
        signParams.put("timestamp", String.valueOf(timestamp));
        signParams.put("nonce", nonce);
        
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, String> entry : signParams.entrySet()) {{
            if (sb.length() > 0) sb.append("&");
            sb.append(entry.getKey()).append("=").append(entry.getValue());
        }}
        
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(APP_SECRET.getBytes(StandardCharsets.UTF_8), "HmacSHA256"));
        byte[] bytes = mac.doFinal(sb.toString().getBytes(StandardCharsets.UTF_8));
        StringBuilder hex = new StringBuilder();
        for (byte b : bytes) hex.append(String.format("%02x", b));
        
        return hex.toString();
    }}
    
    // {api_name} - {description}
    public static void main(String[] args) throws Exception {{
        Map<String, String> params = new LinkedHashMap<>();
        // 填入请求参数
        {params_java}
        
        String signature = generateSignature(params);
        System.out.println("Signature: " + signature);
        // 将 signature 等鉴权字段加入请求体后发起请求
    }}
}}
""",

    "php": """<?php
$APP_KEY = 'your_app_key';
$APP_SECRET = 'your_app_secret';
$BASE_URL = 'https://api.eeo.cn';

function generateSignature($params, $appKey, $appSecret) {{
    $timestamp = time();
    $nonce = bin2hex(random_bytes(8));
    
    $signParams = array_merge($params, [
        'appKey' => $appKey,
        'timestamp' => (string)$timestamp,
        'nonce' => $nonce
    ]);
    ksort($signParams);
    
    $signStr = implode('&', array_map(
        fn($k, $v) => "$k=$v",
        array_keys($signParams),
        array_values($signParams)
    ));
    
    $signature = hash_hmac('sha256', $signStr, $appSecret);
    return array_merge($signParams, ['signature' => $signature]);
}}

// {api_name} - {description}
$params = {params_php};
$signedParams = generateSignature($params, $APP_KEY, $APP_SECRET);

$ch = curl_init($BASE_URL . '{url}');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($signedParams));
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

echo json_decode($response, true);
?>
""",

    "go": """package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"sort"
	"strings"
	"time"
	"math/rand"
	"bytes"
	"net/http"
)

const (
	AppKey    = "your_app_key"
	AppSecret = "your_app_secret"
	BaseURL   = "https://api.eeo.cn"
)

func generateSignature(params map[string]string) map[string]string {{
	timestamp := fmt.Sprintf("%d", time.Now().Unix())
	nonce := fmt.Sprintf("%016x", rand.Int63())
	
	signParams := make(map[string]string)
	for k, v := range params {{
		signParams[k] = v
	}}
	signParams["appKey"] = AppKey
	signParams["timestamp"] = timestamp
	signParams["nonce"] = nonce
	
	keys := make([]string, 0, len(signParams))
	for k := range signParams {{
		keys = append(keys, k)
	}}
	sort.Strings(keys)
	
	parts := make([]string, 0, len(keys))
	for _, k := range keys {{
		parts = append(parts, k+"="+signParams[k])
	}}
	signStr := strings.Join(parts, "&")
	
	mac := hmac.New(sha256.New, []byte(AppSecret))
	mac.Write([]byte(signStr))
	signParams["signature"] = hex.EncodeToString(mac.Sum(nil))
	
	return signParams
}}

// {api_name} - {description}
func main() {{
	params := map[string]string{{
		{params_go}
	}}
	
	signedParams := generateSignature(params)
	body, _ := json.Marshal(signedParams)
	
	resp, err := http.Post(BaseURL+"{url}", "application/json", bytes.NewBuffer(body))
	if err != nil {{
		panic(err)
	}}
	defer resp.Body.Close()
	
	var result map[string]interface{{}}
	json.NewDecoder(resp.Body).Decode(&result)
	output, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(output))
}}
"""
}


def build_params_str(params: dict, lang: str) -> str:
    """根据语言生成参数字符串"""
    if lang == "python":
        return str(params)
    elif lang == "nodejs":
        parts = [f"  {k}: {repr(v) if isinstance(v, str) else v}" for k, v in params.items()]
        return "{\n" + ",\n".join(parts) + "\n}"
    elif lang == "java":
        lines = [f'        params.put("{k}", "{v}");' for k, v in params.items()]
        return "\n".join(lines)
    elif lang == "php":
        parts = [f"  '{k}' => '{v}'" for k, v in params.items()]
        return "[\n" + ",\n".join(parts) + "\n]"
    elif lang == "go":
        parts = [f'    "{k}": "{v}",' for k, v in params.items()]
        return "\n".join(parts)
    return str(params)


def main():
    parser = argparse.ArgumentParser(description="生成 ClassIn API 调用示例")
    parser.add_argument("--api", required=True, choices=list(API_TEMPLATES.keys()),
                        help=f"API名称，可选：{', '.join(API_TEMPLATES.keys())}")
    parser.add_argument("--lang", required=True, choices=list(TEMPLATES.keys()),
                        help=f"编程语言，可选：{', '.join(TEMPLATES.keys())}")
    args = parser.parse_args()

    api_cfg = API_TEMPLATES[args.api]
    template = TEMPLATES[args.lang]
    
    params_str = build_params_str(api_cfg["params"], args.lang)

    code = template.format(
        api_name=args.api,
        description=api_cfg["name"],
        url=api_cfg["url"],
        params=params_str,
        params_java=build_params_str(api_cfg["params"], "java"),
        params_php=build_params_str(api_cfg["params"], "php"),
        params_go=build_params_str(api_cfg["params"], "go"),
    )
    
    print(f"# ClassIn API 示例 — {api_cfg['name']} ({args.lang})")
    print("=" * 60)
    print(code)


if __name__ == "__main__":
    main()
