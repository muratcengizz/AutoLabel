import os
import cv2
import json
import uuid
from workspace.utils.process import Process
from workspace.utils.get_rename_labels import GetRenameLabels

class TensorflowJsonFormatAutoLabel:
    def __init__(self):
        self.conf = Process()
        self.rename_labels = GetRenameLabels()
        if os.name == "nt":
            self.slash_type = "\\"
        elif os.name == "posix":
            self.slash_type = "/"
        try:
            self.USER_LABEL_LIST, self.LABEL_FORMAT, self.ROOT_DIR, self.IMAGES_LABELS_PATH = self.conf.process()
        except Exception as e:
            print(e)
        
    
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
            rename_labels_status, class_items = self.rename_labels.json_xml()
            detection_list = []
            if rename_labels_status == 0:
                for element in class_list:
                    dictionary = {
                        "image": f"{images_path}{self.slash_type}{unique_name}.jpg",
                        "annotations": [{
                            "label": f"{element[0]}",
                            "coordinates": {
                                "x": f"{element[1]}",
                                "y": f"{element[2]}",
                                "width": f"{element[3]}",
                                "height": f"{element[4]}"
                            }
                        }]
                    }
                    detection_list.append(dictionary)
                    
            elif rename_labels_status == 1:
                for element in class_list:
                    for key, value in class_items.items():
                        if value == element[0]:
                           x, y, w, h = element[1]/img_width, element[2]/img_height, element[3]/img_width, element[4]/img_height
                           dictionary = {
                                "image": f"{images_path}{self.slash_type}{unique_name}.jpg",
                                "annotations": [{
                                    "label": f"{key}",
                                    "coordinates": {
                                        "x": f"{x}",
                                        "y": f"{y}",
                                        "width": f"{w}",
                                        "height": f"{h}"
                                    }
                                }]
                            }
                           detection_list.append(dictionary) 
                        
            label_path = f"{images_path}{self.slash_type}{unique_name}.json"
            with open(label_path, "w") as f:
                json.dump(detection_list, f, indent=4)
        except Exception as e:
            message = f"Coordinated could not be written to json file. Error message:\n{e}"
            return message