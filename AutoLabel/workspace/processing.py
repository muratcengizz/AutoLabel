from workspace.utils.get_label_format import GetLabelFormat
from workspace.conversion.yolo_label import YoloFormatAutoLabel
from workspace.conversion.tf_xml_label import TensorflowXmlFormatAutoLabel
from workspace.conversion.tf_json_label import TensorflowJsonFormatAutoLabel
class Processing:
    def __init__(self):
        self.label_format = GetLabelFormat()
        self.yolo_format = YoloFormatAutoLabel()
        self.tensorflow_format = TensorflowXmlFormatAutoLabel()
        self.tensorflow_json_format = TensorflowJsonFormatAutoLabel()
        
        
    def process(self, frame, class_list):
        label_format_status, label_format = self.label_format.get_label_format_from_yaml()
        
        if label_format == "txt":
            message = self.yolo_format.process(frame, class_list)
            return message
        
        elif label_format == "xml":
            message = self.tensorflow_format.process(frame, class_list)
            return message
        
        elif label_format == "json":
            message = self.tensorflow_json_format.process(frame, class_list)
            return message
        
