import cv2 as cv
import os
import numpy as np

people = []
for i in os.listdir(r'C:\Users\Lakhv\Desktop\projects\mouse\faces') :
    people.append(i)
    
haar_cascade = cv.CascadeClassifier('face_detect.xml')
dir  = r'C:\Users\Lakhv\Desktop\projects\mouse\faces'
features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(dir,person)
        label = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_read = cv.imread(img_path)
            img_gray = cv.cvtColor(img_read,cv.COLOR_BGR2GRAY)
            face_rec = haar_cascade.detectMultiScale(img_read,1.1,3)
            
            
            for (x,y,w,h) in face_rec:
                imag_roi = img_gray[y:y+h,x:x+w]
                features.append(imag_roi)
                labels.append(label)
                # print(features)
                
                
create_train()
print("length of features",len(features))
print(len(labels))
features = np.array(features,dtype='object')
labels = np.array(labels)

face_recongnizer = cv.face.LBPHFaceRecognizer_create()

face_recongnizer.train(features,labels)
face_recongnizer.save('faces_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
