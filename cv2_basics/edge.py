import cv2 as cv
import numpy as np
img1 = cv.imread("l.png")

gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

cv.imshow("gray1",gray)
#using laplasian method
lap = cv.Laplacian(gray,cv.CV_64F)
print(lap)
lab = np.uint8(np.absolute(lap))

cv.imshow("gray",lap)


# # using sobal
# sob = cv.Sobel()

cv.waitKey(0)
cv.destroyAllWindows()