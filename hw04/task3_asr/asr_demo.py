import whisper
import os

# ---------------------- 核心自动路径处理（永远不会报错） ----------------------
# 获取当前 .py 文件所在的目录路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 拼接音频文件路径（自动找到当前目录下的 1.m4a）
# 这一步彻底解决了路径找不到、中文路径解码失败的问题
audio_file = os.path.join(script_dir, "1.m4a")

# 检查文件是否真的存在（防止误传）
if not os.path.exists(audio_file):
    print(f"❌ 错误：请确保 1.m4a 文件在这个路径下: {script_dir}")
    exit()

# ---------------------- 语音识别核心逻辑 ----------------------
try:
    print("🚀 正在加载模型...")
    # 加载基础模型（速度快，适合作业）
    model = whisper.load_model("base")
    
    print(f"🎙️  正在识别文件: {audio_file}")
    # 执行识别，指定语言为中文
    result = model.transcribe(audio_file, language="zh")
    
    # ---------------------- 输出与保存结果 ----------------------
    print("\n=== 📝 语音识别结果 ===")
    print(result["text"])
    
    # 自动保存识别结果到 result.txt（和音频同目录）
    output_file = os.path.join(script_dir, "result.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"\n✅ 任务三完成！识别结果已保存至: {output_file}")

except Exception as e:
    print(f"❌ 运行出错: {e}")
    print("💡 建议检查：1.m4a 是否在当前文件夹内？")