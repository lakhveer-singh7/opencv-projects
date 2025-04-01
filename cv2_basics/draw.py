import cv2 as cv
import numpy as np

bl = np.zeros((500,500,3),dtype = 'uint8')
#cv.imshow("bla",bl)
#1. PAINT AN IMAGE

bl[:] = 255,0,0
cv.rectangle(bl,(5,5),(200,200),(0,255,0),thickness=-1)
cv.circle(bl,(200,200),100,(0,0,233),thickness= -1)
cv.line(bl,(10,10),(100,100),(0,255,255),thickness=5)
cv.putText(bl,"opencv",(150,450),cv.FONT_HERSHEY_SCRIPT_COMPLEX,3,(100,200,100),2)
cv.imshow("bla=",bl)
cv.waitKey(0)
cv.destroyAllWindows()