import cv2 as cv
import numpy as np

img1 = cv.imread("l.png")
img1 =cv.resize(img1,(800,560),interpolation=cv.INTER_CUBIC)
cv.imshow("img0",img1)
bla = np.zeros(img1.shape,'uint8')
cv.imshow("bka",bla)
img = cv.GaussianBlur(img1,(7,7),cv.BORDER_DEFAULT)
cv.imshow("img1",img)

img = cv.Canny(img1,100,100)
cv.imshow("img2",img)
ret, img = cv.threshold(img,125,255,cv.THRESH_BINARY)
contours,hierarchies = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(bla,contours,-1,(0,0,255),2)
cv.imshow("co",bla)

bil  = cv.bilateralFilter(img1,5,5,5)
cv.imshow("bil",bil)
cv.waitKey(0)


cv.destroyAllWindows()