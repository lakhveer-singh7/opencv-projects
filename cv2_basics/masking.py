import cv2 as cv

img1 = cv.imread("l.png")
img2 = cv.imread("yo.jpg")
img1 = cv.resize(img1,(img2.shape[1],img2.shape[0]),interpolation=cv.INTER_CUBIC)
cv.imshow("im1",img1)
cv.imshow("im2",img2)
im = cv.bitwise_and(img1,img2)
cv.imshow("im",im)
cv.waitKey(0)
cv.destroyAllWindows()