import os
import yaml

class GetLabel:
    def __init__(self):
        self.user_label_list = []
        self.model_label_dict = {0: 'toaster', 1: 'person', 2: 'bike', 3: 'car', 4: 'motor', 5: 'airplane', 6: 'bus', 7: 'train', 8: 'truck', 9: 'boat', 10: 'light', 11: 'hydrant', 12: 'sign', 13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'dog', 18: 'cat', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear', 24: 'zebra', 25: 'giraffe', 26: 'hat', 27: 'backpack', 28: 'umbrella', 29: 'shoe', 30: 'eye glasses', 31: 'handbag', 32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard', 37: 'skateboard', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove', 41: 'sports ball', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle', 45: 'plate', 46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon', 51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange', 56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut', 61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed', 66: 'mirror', 67: 'dining table', 68: 'window', 69: 'desk', 70: 'toilet', 71: 'door', 72: 'tv', 73: 'stroller', 74: 'mouse', 75: 'remote', 76: 'keyboard', 77: 'scooter', 78: 'microwave', 79: 'other vehicle'}
        if os.name == "nt":
            self.slash_type = "\\"
        elif os.name == "posix":
            self.slash_type = "/"
        try:
            conf_path = f"{os.path.join('workspace', 'configuration')}{self.slash_type}configuration.yaml"
            with open(conf_path, "r") as file:
                self.config = yaml.safe_load(file)
        except Exception as e:
            print(f"Config file could not be opened. Error message:\n{e}")
    
    def get_label_from_yaml(self):
        label_status = 1
        labels = self.config.get("LABELS")
        
        for label in labels:
            if label in self.model_label_dict.keys():
                self.user_label_list.append(label)
            elif label == None:
                pass
            else:
                label_status = 0
                print(f"Incorrectly entered class name: {label}\nPlease make sure that you have entered the class parameters correctly in the variable named labels in the configuration.yaml file.")
        
        if len(self.user_label_list) == 0:
            label_status = 0
    
        return label_status, self.user_label_list