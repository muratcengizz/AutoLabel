import os
import cv2
import uuid
import numpy as np
import xml.etree.ElementTree as ET
from workspace.utils.process import Process
from workspace.utils.get_rename_labels import GetRenameLabels

class TensorflowXmlFormatAutoLabel:
    def __init__(self):
        self.coco_names = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorbike', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'sofa', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv monitor', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair dryer', 79: 'toothbrush'}
        self.conf = Process()
        self.rename_labels = GetRenameLabels()
        if os.name == "nt":
            self.slash_type = "\\"
        elif os.name == "posix":
            self.slash_type = "/"
        try:
            self.USER_LABEL_LIST, self.user_label_format, self.ROOT_DIR, self.IMAGES_LABELS_PATH = self.conf.process()
        except Exception as e:
            print("deneme tf",e)
        
        
        
    def generateUniqueName(self):
        unique_name = uuid.uuid1()
        return unique_name
    
   
    def process(self, frame, class_list):
        
        image_height, image_width = frame.shape[:2]
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
            if rename_labels_status == 0:
                folder_name = str(self.IMAGES_LABELS_PATH).split(self.slash_type)[-1]
                labels_path = os.path.join(self.IMAGES_LABELS_PATH)
                
                root = ET.Element("annotation")
            
                folder = ET.Element("folder")
                folder.text = f"{folder_name}"
                root.append(folder)
                
                filename = ET.Element("filaname")
                filename.text = f"{unique_name}.jpg"
                root.append(filename)
                
                path = ET.Element("path")
                path.text = f"{labels_path}{self.slash_type}{unique_name}.jpg"
                root.append(path)
                
                source = ET.Element("source")
                database = ET.Element("database")
                database.text = "Unknown"
                source.append(database)
                root.append(source)
                
                size = ET.Element("size")
                width = ET.Element("width")
                width.text = f"{image_width}"
                height = ET.Element("height")
                height.text = f"{image_height}"
                depth = ET.Element("depth")
                depth.text = "3"
                size.extend([width, height, depth])
                root.append(size)
                
                segmented = ET.Element("segmented")
                segmented.text = "0"
                root.append(segmented)
                for element in class_list:
                    object_element = ET.Element("object")
                    name = ET.Element("name")
                    name.text = f"{element[0]}"
                    object_element.append(name)
                    pose = ET.Element("pose")
                    pose.text = "Unspecified"
                    object_element.append(pose)
                    truncated = ET.Element("truncated")
                    truncated.text = "0"
                    object_element.append(truncated)
                    difficult = ET.Element("difficult")
                    difficult.text = "0"
                    object_element.append(difficult)

                    bndbox = ET.Element("bndbox")
                    xmin = ET.Element("xmin")
                    xmin.text = f"{element[1]}"
                    bndbox.append(xmin)
                    ymin = ET.Element("ymin")
                    ymin.text = f"{element[2]}"
                    bndbox.append(ymin)
                    xmax = ET.Element("xmax")
                    xmax.text = f"{element[3]}"
                    bndbox.append(xmax)
                    ymax = ET.Element("ymax")
                    ymax.text = f"{element[4]}"
                    bndbox.append(ymax)

                    object_element.append(bndbox)

                    root.append(object_element)
                
                tree = ET.ElementTree(root)
                
                
            elif rename_labels_status == 1:
                
                
                folder_name = str(self.IMAGES_LABELS_PATH).split(self.slash_type)[-1]
                labels_path = os.path.join(self.IMAGES_LABELS_PATH)
                
                root = ET.Element("annotation")
            
                folder = ET.Element("folder")
                folder.text = f"{folder_name}"
                root.append(folder)
                
                filename = ET.Element("filaname")
                filename.text = f"{unique_name}.jpg"
                root.append(filename)
                
                path = ET.Element("path")
                path.text = f"{labels_path}{self.slash_type}{unique_name}.jpg"
                root.append(path)
                
                source = ET.Element("source")
                database = ET.Element("database")
                database.text = "Unknown"
                source.append(database)
                root.append(source)
                
                size = ET.Element("size")
                width = ET.Element("width")
                width.text = f"{image_width}"
                height = ET.Element("height")
                height.text = f"{image_height}"
                depth = ET.Element("depth")
                depth.text = "3"
                size.extend([width, height, depth])
                root.append(size)
                
                segmented = ET.Element("segmented")
                segmented.text = "0"
                root.append(segmented)
                for element in class_list:
                    for key, value in class_items.items():
                        if value == element[0]:
                            object_element = ET.Element("object")
                            name = ET.Element("name")
                            name.text = f"{key}"
                            object_element.append(name)
                            pose = ET.Element("pose")
                            pose.text = "Unspecified"
                            object_element.append(pose)
                            truncated = ET.Element("truncated")
                            truncated.text = "0"
                            object_element.append(truncated)
                            difficult = ET.Element("difficult")
                            difficult.text = "0"
                            object_element.append(difficult)

                            bndbox = ET.Element("bndbox")
                            xmin = ET.Element("xmin")
                            xmin.text = f"{element[1]}"
                            bndbox.append(xmin)
                            ymin = ET.Element("ymin")
                            ymin.text = f"{element[2]}"
                            bndbox.append(ymin)
                            xmax = ET.Element("xmax")
                            xmax.text = f"{element[3]}"
                            bndbox.append(xmax)
                            ymax = ET.Element("ymax")
                            ymax.text = f"{element[4]}"
                            bndbox.append(ymax)

                            object_element.append(bndbox)

                            root.append(object_element)
                
                tree = ET.ElementTree(root)
            tree.write(f"{labels_path}{self.slash_type}{unique_name}.xml", encoding="utf-8")
        except Exception as e:
            message = f"Coordinated could not be written to xml file. Error message:\n{e}"
            return message