import os
import yaml

class GetRenameLabels:
    def __init__(self):
        if os.name == "nt":
            self.slash_type = "\\"
        elif os.name == "posix":
            self.slash_type = "/"
        self.coco_names = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorbike', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'sofa', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv monitor', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair dryer', 79: 'toothbrush'}
        self.conf_path = f"{os.path.join('workspace', 'configuration')}{self.slash_type}configuration.yaml"
        try:
            with open(self.conf_path, "r") as file:
                self.config = yaml.safe_load(file)
        except Exception as e:
            pass
    
    def get_rename_labels_from_yaml(self):
        rename_labels_status = 1
        get_label = self.config.get("LABELS")
        get_rename_labels = self.config.get("RENAME_LABELS")
        try:
            if len(get_label) != len(get_rename_labels):
                rename_labels_status = 0
        except Exception as e:
            print(e)

        return rename_labels_status, get_label, get_rename_labels
    
    def txt(self):
        rename_labels_status, get_label, get_rename_labels = self.get_rename_labels_from_yaml()
        
        class_names = []
        class_items = {}
        
        for class_id in get_label:
            for key, value in self.coco_names.items():
                if key == class_id:
                    class_names.append(value)
        
        for element in range(len(class_names)):
            class_items[element] = class_names[element]
            
        return rename_labels_status, get_rename_labels, class_items
    
    def json_xml(self):
        rename_labels_status, get_label, get_rename_labels = self.get_rename_labels_from_yaml()
        
        class_names = []
        class_items = {}
        
        for class_id in get_label:
            for key, value in self.coco_names.items():
                if key == class_id:
                    class_names.append(value)
        
        for id, element in enumerate(get_rename_labels):
            class_items[element] = class_names[id]
        
        return rename_labels_status, class_items
        