import face_recognition
import cv2
import numpy as np

def detect_faces(image: np.ndarray) -> list:
    """检测人脸位置"""
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_image)
    return face_locations

def get_face_encodings(image: np.ndarray) -> list:
    """获取人脸128维特征编码"""
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_encodings = face_recognition.face_encodings(rgb_image)
    return face_encodings

def recognize_faces(unknown_encodings: list, known_encodings: list, known_names: list) -> list:
    """比对已知人脸库进行识别"""
    names = []
    for encoding in unknown_encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_encodings, encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_names[best_match_index]
        names.append(name)
    return names