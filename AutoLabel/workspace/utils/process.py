from workspace.utils.get_images_labels_path import GetImagesLabelsPath
from workspace.utils.get_label_format import GetLabelFormat
from workspace.utils.get_label import GetLabel
from workspace.utils.get_root_dir import GetRootDir

class Process:
    def __init__(self):
        self.get_label = GetLabel()
        self.get_root_dir = GetRootDir()
        self.get_label_format = GetLabelFormat()
        self.get_images_labels_path = GetImagesLabelsPath()
    
    def process(self):
        
        try:
            label_status, user_label_list = self.get_label.get_label_from_yaml()
            if label_status == 1:
                print("LABELS successfully registered.")
        except Exception as e:
            print(f"Please make sure that you enter the class names correctly and in the correct format. Error message:\n{e}")
        
        
        try:
            label_format_status, label_format = self.get_label_format.get_label_format_from_yaml()
        except Exception as e:
            print(f"The variable named LABEL_FORMAT in the configuration.yaml file could not be read. Error message:\n{e}")
        
        
       
        
        try:
            root_dir_status, root_dir = self.get_root_dir.get_root_dir_from_yaml()
            if root_dir_status == 1:
                print("ROOT_DIR successfully registered.")
                
        except Exception as e:
            print(f"Please enter the main directory of your project correctly. Error message:\n{e}")
        
        
        try:
            image_label_path_status, images_labels_path = self.get_images_labels_path.get_images_labels_path_from_yaml()
            if image_label_path_status == 1:
                print("IMAGES_LABELS_PATH successfully registered.")
        except Exception as e:
            print(f"Please make sure that you enter the correct directory where your data will be saved after the prediction process. Error message:\n{e}")
        
        
        return [user_label_list, label_format[0], root_dir[0], images_labels_path[0]]
        
            