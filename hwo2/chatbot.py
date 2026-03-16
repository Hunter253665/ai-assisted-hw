# -*- coding: utf-8 -*-
import requests
import json

# Ollama 本地接口（无需 API Key）
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"

def chat_with_qwen(message: str) -> str:
    """调用本地 Qwen-7B 模型，返回对话结果"""
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "qwen:7b",  # 本地 Qwen-7B 模型名
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7
    }
    
    try:
        # 调用本地 Ollama 接口
        response = requests.post(OLLAMA_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()  # 捕获 HTTP 错误
        result = response.json()
        
        # 容错：判断是否有返回结果
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            return f"模型返回异常：{result}"
    
    except requests.exceptions.ConnectionError:
        return "❌ 本地 Ollama 服务未启动，请先安装并启动 Ollama"
    except requests.exceptions.Timeout:
        return "❌ 模型响应超时，请稍后重试"
    except Exception as e:
        return f"❌ 调用失败：{str(e)}"

if __name__ == "__main__":
    print("✅ 本地 Qwen-7B Chatbot 已启动（输入 'quit' 退出）")
    while True:
        user_input = input("\n你: ")
        if user_input.lower() == "quit":
            print("👋 再见！")
            break
        # 调用模型并打印结果
        reply = chat_with_qwen(user_input)
        print(f"AI: {reply}")
