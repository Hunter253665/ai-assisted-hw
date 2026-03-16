 1. 运行环境
操作系统：Windows 10/11
Python 版本：Python 3.10 及以上（你当前是 3.14 可用）
硬件需求：显卡显存 ≥ 8GB（你的 RTX 5070Ti 完美适配）
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
