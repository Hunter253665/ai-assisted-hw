 1. 运行环境
操作系统：Windows 10/11
Python 版本：Python 3.10 及以上
硬件需求：显卡显存 ≥ 8GB
本地模型：Qwen-7B（通过 Ollama 运行）
2. 依赖安装
由于使用本地 Ollama 服务，只需安装 requests 即可：
运行
pip install requests
 3. API Key 说明（本地模型无需真实 Key）
本项目使用 本地 Ollama 服务，因此不需要 OpenAI / 火山方舟 API Key。
仅需满足以下条件即可运行：
已安装 Ollama
已拉取 Qwen-7B 模型：ollama pull qwen:7b 
4. 运行命令
启动 Ollama 服务（后台运行）：
bash
运行
ollama serve
运行聊天脚本：
bash
运行
python chatbot.py
5. 示例输入 / 输出
plaintext
✅ 本地 Qwen-7B Chatbot 已启动（输入 'quit' 退出）

你: 介绍一下生成式AI大模型结合知识库与AI Agent的知识挖掘方案
AI: 生成式AI大模型结合知识库与AI Agent的知识挖掘方案，主要围绕“检索-生成”流程展开。其核心思路是将外部知识库向量化，通过检索相关上下文增强大模型的回答能力，有效减少幻觉并提升信息准确性。

你: quit
👋 再见！

运行成功截图：<img width="10" height="7" alt="image" src="https://github.com/user-attachments/assets/9a7f7f14-e702-4887-9b02-2c7dbf19f281" />

