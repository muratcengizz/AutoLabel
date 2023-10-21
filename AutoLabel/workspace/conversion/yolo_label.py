import os
import cv2
import uuid
import numpy as np
from workspace.utils.process import Process
from workspace.utils.get_rename_labels import GetRenameLabels

class YoloFormatAutoLabel():
    def __init__(self):
        self.coco_names = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorbike', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'sofa', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv monitor', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair dryer', 79: 'toothbrush'}
        self.conf = Process()
        self.rename_labels = GetRenameLabels()
        if os.name == "nt":
            self.slash_type = "\\"
        elif os.name == "posix":
            self.slash_type = "/"
        try:
            self.USER_LABEL_LIST, self.USER_LABEL_FORMAT, self.ROOT_DIR, self.IMAGES_LABELS_PATH = self.conf.process()
        except Exception as e:
            print("deneme yolo",e)

        
        
        
    def generateUniqueName(self):
        unique_name = uuid.uuid1()
        return unique_name
    
    
    def process(self, frame, class_list):
        img_height, img_width = frame.shape[:2]
        try:
            unique_name = self.generateUniqueName()
        except Exception as e:
            message = f"Unique variable creation error. Error message:\n{e}"
            return message
        
        try:
            folder_path = os.path.join(self.IMAGES_LABELS_PATH)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        except Exception as e:
            message = f"Could not create collected_images folder. Error message:\n{e}"
            return message
        
        try:
            images_path = os.path.join(self.IMAGES_LABELS_PATH)
            cv2.imwrite(filename=f"{images_path}{self.slash_type}{unique_name}.jpg", img=frame)
        except Exception as e:
            message = f"The frame could not be written to the folder. Error message:\n{e}"
            return message
        
        try:
            rename_labels_status, rename_labels, class_items = self.rename_labels.txt()
            labels_path = os.path.join(self.IMAGES_LABELS_PATH)
            with open(f"{labels_path}{self.slash_type}{unique_name}.txt", "w") as f:
                if rename_labels_status == 0:
                    for class_name, x, y, w, h in class_list:
                        for key, value in self.coco_names.items():
                            if value == class_name:
                                class_id = key
                                x, y, w, h = x/img_width, y/img_height, w/img_width, h/img_height
                                f.write(f"{class_id} {x} {y} {w} {h}\n")
                elif rename_labels_status == 1:
                    for class_name, x, y, w, h in class_list:
                        for key, value in class_items.items():
                            if class_name == value:
                                x, y, w, h = x/img_width, y/img_height, w/img_width, h/img_height
                                f.write(f"{key} {x} {y} {w} {h}\n")
        except Exception as e:
            message = f"Coordinated could not be written to txt file. Error message:\n{e}"
            return message