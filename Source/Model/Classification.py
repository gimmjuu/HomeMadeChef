"""
작성자 : 주혜인
작성일 : 23/08/29
내용 : 학습된 Yolov8 모델을 사용하여 입력받은 사진에서 객체를 인식하고 분류하여 결과를 반환합니다.
"""
from ultralytics import YOLO


class Classification:
    __instance__ = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance__, cls):
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def __init__(self):
        self.file_path = r"Temp/"
        # --- temp model
        self.model = YOLO("trained_model.pt", task="detect")

    def classify_obj_from_img(self, t_file: str=None):
        result_list = list()
        predicted_result = self.model.predict(source=fr"{self.file_path}{t_file}", save=False)

        for v_ in predicted_result:
            if v_.boxes:
                box = v_.boxes[0]
                class_id = int(box.cls)
                if class_id:
                    object_name = self.model.names[class_id]
                    result_list.append(object_name)

        print(result_list)
        return result_list


if __name__ == '__main__':
    cf = Classification()
    result_ = cf.classify_obj_from_img("target_240.jpg")