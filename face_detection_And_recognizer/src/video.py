import cv2 as cv
import numpy as np
import os
haar_cas = cv.CascadeClassifier('face_detect.xml')
people = []
for i in os.listdir(r'C:\Users\Lakhv\Desktop\projects\mouse\faces') :
    people.append(i)

print(people)
features  = np.load('C:\Users\Lakhv\Desktop\projects\mouse\src\features.npy',allow_pickle=True)
labels = np.load('labels.npy')

face_recongnizer = cv.face.LBPHFaceRecognizer_create()
face_recongnizer.read('faces_trained.yml')



def live_face_rec(frame) :
    img = frame
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    face_rec = haar_cas.detectMultiScale(gray,1.1,3)

    for (x,y,w,h) in face_rec:
        face_roi = gray[y:y+h,x:x+w]
        label,confidence = face_recongnizer.predict(face_roi)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
        print(people[label] ," with  a confidence of ",confidence)
        cv.putText(img,f"{people[label]}",(x,y-10),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

        # cv.imshow("imd",img)
        return img


video = cv.VideoCapture(0)
while True:
    ret,frame  = video.read()
    frame = cv.flip(frame,1)
    frame = live_face_rec(frame)
    cv.imshow("cam",frame)
    if cv.waitKey(1) & 0xff == ord('d') :
        break

  
cv.destroyAllWindows()   