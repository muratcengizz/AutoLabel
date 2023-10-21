import os
import yaml
import shutil

class GetTrainTestSplit:
    def __init__(self):
        try:
            if os.name == "nt":
                self.slash_type = "\\"
            elif os.name == "posix":
                self.slash_type = "/"
            conf_path = f"{os.path.join('workspace', 'configuration')}{self.slash_type}configuration.yaml"
            with open(conf_path, "r") as file:
                self.config = yaml.safe_load(file)
            self.root_dir = self.config.get("ROOT_DIR")[0]
        except Exception as e:
            print(f"\n{e}")
    
    def get_train_test_split_from_yaml(self):
        try:
            data_path = self.config.get("IMAGES_LABELS_PATH")
            data_path = data_path[0]
            root_dir = self.config.get("ROOT_DIR")[0]
            
            tts = self.config.get("TRAIN_TEST_SPLIT")
            if tts != None:
                tts = dict(tts[0])
                train_ratio = tts.get("train") / 100
                
                data_path_split = data_path.split(f"{self.slash_type}")
                main_path = ""
                for element in data_path_split[:-1]:
                    main_path += element + f"{self.slash_type}"
                
                train_data_path = main_path + "train"
                test_data_path = main_path + "test"

                
                image_list, label_list = [], []
                list_dir = os.listdir(data_path)
                for element in list_dir:
                    if element.endswith(".jpg"):
                        image_list.append(element)
                    elif element.endswith("txt") or element.endswith("xml") or element.endswith("json"):
                        label_list.append(element)
                
                

                
                train_list, test_list = image_list[:int(len(image_list) * train_ratio)], image_list[int(len(image_list)* train_ratio):]
                train_list += label_list[:int(len(label_list) * train_ratio)]
                test_list += label_list[int(len(label_list) * train_ratio):]
                
                for element in train_list:
                    fromm = f"{root_dir}{self.slash_type}dataset{self.slash_type}collected_images{self.slash_type}{element}"
                    too = f"{root_dir}{self.slash_type}dataset{self.slash_type}train{self.slash_type}{element}"
                    shutil.copy(fromm, too)
                
                for element in test_list:
                    fromm = f"{root_dir}{self.slash_type}dataset{self.slash_type}collected_images{self.slash_type}{element}"
                    too = f"{root_dir}{self.slash_type}dataset{self.slash_type}test{self.slash_type}{element}"
                    shutil.copy(fromm, too)
                    
                return "Train-Test split process is ok."
        except Exception as e:
            return e