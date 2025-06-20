import cv2 as cv


capture = cv.VideoCapture("test.mp4")

def changeres(w,h):
    capture.set(4,w)
    capture.set(3,h)
    
def resccale(frame , scale = .25):
    w = int(frame.shape[1]*scale)
    h = int(frame.shape[0]*scale)
    demi = (w,h)
    return cv.resize(frame,demi,interpolation=cv.INTER_AREA)


while True :
    isTrue, frame = capture.read()
    
    cv.imshow("video",resccale(frame))
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()