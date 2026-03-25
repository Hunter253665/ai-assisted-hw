
## 功能说明
1. **人脸检测**：基于 `face_recognition` 定位图片中所有人脸位置并框选。
2. **特征编码**：提取每张人脸的 128 维特征向量。
3. **可选：人脸识别**：通过比对已知人脸库的特征编码，实现身份识别。

## 运行说明
1. 安装依赖：`pip install -r requirements.txt`
2. 启动服务：`streamlit run app.py`
3. 访问：浏览器打开 `http://localhost:8501`

## 人脸库准备（可选）
1. 收集已知人物的清晰人脸图片。
2. 提取每张图片的特征编码，存入 `known_encodings` 列表。
3. 对应人物姓名存入 `known_names` 列表。