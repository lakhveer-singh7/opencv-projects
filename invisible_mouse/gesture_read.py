import cv2 as cv
import mediapipe as md
import bkl
import pyautogui as pgi

mphands = md.solutions.hands
hands = mphands.Hands(
    static_image_mode = False,
    model_complexity = 1,
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7,
    max_num_hands = 1
)

        
def main():
    cap = cv.VideoCapture(0)
    draw = md.solutions.drawing_utils


    while True:
        ret,frame = cap.read()
        screen = frame.shape
        # print(screen)
        # time.sleep(.02)
        frame = cv.flip(frame , 1)
        framergb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        processed = hands.process(framergb)
        landmarks_list = []
        
        if processed.multi_hand_landmarks:
            
            hand_landmarks = processed.multi_hand_landmarks[0]
            draw.draw_landmarks(frame,hand_landmarks,mphands.HAND_CONNECTIONS)
            for lm in hand_landmarks.landmark:
                landmarks_list.append((lm.x,lm.y))
         
        bkl.move_mouse(landmarks_list)
        
        # if len(landmarks_list)==21:  
        #     index = landmarks_list[4]
        #     x1  = int(landmarks_list[4][0]*screen[1])
        #     y1 = int(landmarks_list[4][1]*screen[0])  
        #     cv.circle(frame,(x1,y1),6,(255,0,255),2)
        #     x2  = int(landmarks_list[8][0]*screen[1])
        #     y2 = int(landmarks_list[8][1]*screen[0])  
        #     cv.circle(frame,(x2,y2),6,(255,0,255),2)
        #     cv.line(frame,(x1,y1),(x2,y2),(255,0,255),2)
        #     if(bkl.distance(landmarks_list[4],landmarks_list[8],"volume")>.05):
        #         pgi.press("volumeup")
        #     else:
        #         pgi.press("volumedown")
            
        cv.imshow("cam",frame)
        # print(landmarks_list)
    
        if cv.waitKey(2) & 0xff == ord('d'):
            break
        
    cv.destroyAllWindows()
    
if __name__ == '__main__':
    main()