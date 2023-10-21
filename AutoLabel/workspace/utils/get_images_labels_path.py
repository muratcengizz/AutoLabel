import os 
import yaml

class GetImagesLabelsPath:
    def __init__(self):
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
            

    def get_images_labels_path_from_yaml(self):
        images_labels_path_status = 1
        images_labels_path = self.config.get("IMAGES_LABELS_PATH", "")
        if os.path.exists(images_labels_path[0]):
            pass
        else:
            images_labels_path_status = 0
            print("File path not found.\nPlease make sure that the path you provided in the variable named IMAGES_LABELS_PATH in the configuration.yaml file is entered correctly.")
        
        return images_labels_path_status, images_labels_path