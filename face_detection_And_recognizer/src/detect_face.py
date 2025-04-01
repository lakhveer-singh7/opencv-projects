import cv2 as cv
import numpy as np
img1 = cv.imread("photos/photo.png")
cv.imshow("ima",img1)

img = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
cv.imshow("gray",img)

haar_cas = cv.CascadeClassifier('face_detect.xml')

facs_rec = haar_cas.detectMultiScale(img,scaleFactor=1.1,minNeighbors=6)

print(len(facs_rec))
bkn = np.zeros(img1.shape[:2],dtype="uint8")
bkn = cv.bitwise_not(bkn)
cv.imshow("bkl",bkn)
for (x,y,w,h) in facs_rec:
    cv.rectangle(bkn,(x,y),(x+w,y+h),0,-1)
    # cv.rectangle(img1,(x,y),(x+w,y+h),0,1)
im = cv.bitwise_or(img,bkn)
cv.imshow("gray",img1)
cv.imshow("deceted faces",im)
cv.waitKey(0)
cv.destroyAllWindows()