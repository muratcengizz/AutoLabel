import os
import yaml


class GetRootDir:
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
            
    def get_root_dir_from_yaml(self):
        root_dir_status = 1
        root_dir = self.config.get("ROOT_DIR", "")
        if os.path.exists(root_dir[0]):
            pass
        else:
            root_dir_status = 0
            print("File path not found.\nPlease make sure that the path you provided in the variable named ROOT_DIR in the configuration.yaml file is entered correctly.")
        
        return root_dir_status, root_dir