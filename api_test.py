#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的API测试脚本
"""

import requests
import time
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# DeepSeek API 配置
API_KEY = os.getenv('DEEPSEEK_API_KEY')
BASE_URL = os.getenv('DEEPSEEK_BASE_URL', 'https://api.deepseek.com/v1/chat/completions')

if not API_KEY:
    raise ValueError("请在.env文件中设置DEEPSEEK_API_KEY环境变量")

def test_api():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": "请简单介绍一下你自己，不超过100字。"
            }
        ],
        "max_tokens": 200,
        "temperature": 0.7
    }
    
    try:
        print("正在测试API连接...")
        response = requests.post(
            BASE_URL,
            headers=headers,
            json=payload,
            timeout=(10, 60)  # 连接超时10s，读取超时60s
        )
        
        if response.status_code == 200:
            result = response.json()
            print("API连接成功！")
            print("回复内容：", result['choices'][0]['message']['content'])
            return True
        else:
            print(f"API调用失败，状态码：{response.status_code}")
            print(f"错误信息：{response.text}")
            return False
            
    except Exception as e:
        print(f"API测试失败：{e}")
        return False

if __name__ == "__main__":
    success = test_api()
    if success:
        print("\nAPI测试通过，可以运行完整脚本")
    else:
        print("\nAPI测试失败，请检查网络连接或API密钥")
