import cv2

class Test:
    def __init__(self):
        pass
    
    def label_test(self):
        image = cv2.imread(filename="dataset\\collected_images\\0b4e7e90-6b7f-11ee-935a-80fa5b98d551.jpg")
        
        with open(file="dataset\\collected_images\\0b4e7e90-6b7f-11ee-935a-80fa5b98d551.txt", mode="r") as f:
            clas_ids = f.read()
            class_ids = clas_ids.split("\n")
            for element in class_ids:
                
                satir = element.split()
                if len(satir) == 5:
                    class_id, x, y, w, h = satir
                    img_width, img_height = image.shape[:2]
                    x, y, w, h = float(x)*img_width, float(y)*img_height, float(w)*img_width, float(h)*img_height
                    x, y, w, h = int(x), int(y), int(w), int(h)
                    cv2.rectangle(img=image, pt1=(x,y), pt2=(w,h), color=(0, 0, 255), thickness=1)
                    cv2.putText(img=image, text=class_id, org=(x, y-20), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255), thickness=1)
                
        
        cv2.imshow(winname="test", mat=image)
        if cv2.waitKey(0) == ord("q"): cv2.destroyAllWindows()
    
    
p1 = Test()
p1.label_test()