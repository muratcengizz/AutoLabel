import os
import yaml

class GetLabelFormat:
    def __init__(self):
        self.label_format_list = ["xml", "json", "txt"]
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
    
    def get_label_format_from_yaml(self):
        label_format_status = 1
        label_format = self.config.get("LABEL_FORMAT", "")
        if label_format not in self.label_format_list:
            label_format_status = 0
        
        return label_format_status, label_format[0]