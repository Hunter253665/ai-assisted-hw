import streamlit as st
import cv2
import numpy as np
from PIL import Image
from src.face_utils import detect_faces, get_face_encodings, recognize_faces

# 示例已知人脸库（可替换为自己的图片）
# known_image = face_recognition.load_image_file("known_person.jpg")
# known_encoding = face_recognition.face_encodings(known_image)[0]
# known_encodings = [known_encoding]
# known_names = ["Known Person"]

st.title("🧑 Face Detection & Recognition Demo")

# 上传或选择示例图片
uploaded_file = st.file_uploader("上传图片", type=["jpg", "jpeg", "png"])
example = st.selectbox("或选择示例图片", ["None", "Example 1", "Example 2"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
elif example != "None":
    # 可加载本地示例图片
    img_array = cv2.imread(f"examples/{example}.jpg")
else:
    st.info("请上传或选择示例图片")
    st.stop()

# 检测人脸
face_locations = detect_faces(img_array)
face_encodings = get_face_encodings(img_array)

# 绘制人脸框
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(img_array, (left, top), (right, bottom), (0, 255, 0), 2)

# 显示结果
st.image(img_array, channels="BGR", caption="检测到的人脸位置")
st.write(f"检测到 {len(face_locations)} 张人脸")
st.write(f"每张人脸特征编码维度：{len(face_encodings[0]) if face_encodings else 0}")

# 可选：人脸识别
# if known_encodings:
#     names = recognize_faces(face_encodings, known_encodings, known_names)
#     st.write("识别结果：", names)