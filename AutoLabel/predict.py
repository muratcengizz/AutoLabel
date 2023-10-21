# from ultralytics import YOLO
# import cv2
# import os 
# from workspace.utils.get_label import GetLabel
# from workspace.utils.get_train_test_split import GetTrainTestSplit
# from workspace.processing import Processing
# from workspace.utils.get_rename_labels import GetRenameLabels
# class Predict:
#     def __init__(self):
#         if os.name == "nt":
#             self.slash_type = "\\"
#         elif os.name == "posix":
#             self.slash_type = "/"
#         self.model = YOLO(f"{os.path.join('workspace', 'models')}{self.slash_type}yolov8n.pt")
#         self.get_label = GetLabel()
#         self.processing = Processing()
#         self.get_rename_labels = GetRenameLabels()
#     def predict(self):
#         video = cv2.VideoCapture(0)
        
#         while True:
#             retval, frame = video.read()
#             if not retval: break
#             frame = cv2.flip(src=frame, flipCode=1)
            
#             _, label_list = self.get_label.get_label_from_yaml()
#             predict = self.model.predict(frame, classes=label_list)
#             for result in predict:
#                 boxes = result.boxes.cpu().numpy()
#                 class_list = []
#                 for box in boxes:
#                     x, y, w, h = box.xyxy[0].astype(int)
#                     #print(x1, y1, w1, h1)
#                     names = result.names[int(box.cls[0])]
                    
#                     class_list.append([names,x,y,w,h])
                    
#                     #message = self.processing.process(frame=frame, class_list=class_list)
#                     #print(message)
                    
#                     #self.get_rename_labels.json()
                    
#                     #cv2.rectangle(img=frame, pt1=(x1,y1), pt2=(w1,h1), color=(0, 0, 255), thickness=2)
#                     #cv2.putText(img=frame, text=names, org=(x1, y1-20), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 100), thickness=2)
#             cv2.imshow(winname="Prediction", mat=frame)
#             if cv2.waitKey(1) == ord("q"): break
        
        

# p1 = Predict()
# p1.predict()


# message = GetTrainTestSplit().get_train_test_split_from_yaml()
# print(message)