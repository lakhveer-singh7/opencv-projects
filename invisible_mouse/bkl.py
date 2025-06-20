import cv2 as cv
import mediapipe as md
import pyautogui as pgi
import numpy as np
import math

pgi.FAILSAFE = False
screen_w,screen_h = pgi.size()
def calcAngle(a,b,c):
    line1Y1 = a[1]
    line1X1 = a[0]
    line1Y2 = b[1]
    line1X2 = b[0]

    line2Y1 = b[1]
    line2X1 = b[0]
    line2Y2 = c[1]
    line2X2 =c[0]

    #calculate angle between pairs of lines
    angle1 = math.atan2(line1Y1-line1Y2,line1X1-line1X2)
    angle2 = math.atan2(line2Y1-line2Y2,line2X1-line2X2)
    angleDegrees = (angle1-angle2) * 360 / (2*math.pi)
    # print(angleDegrees)
    return angleDegrees


def distance(a,b,c):
    dis =  math.dist(a,b)
    # print(dis,c)
    return dis



def move_mouse(landmarks_list):
    if len(landmarks_list)==21:
        if(distance(landmarks_list[4],landmarks_list[9],"mouse")>0.065 and distance(landmarks_list[8],landmarks_list[5],"hello")>0.10 and calcAngle(landmarks_list[16],landmarks_list[14],landmarks_list[13])>100 and calcAngle(landmarks_list[12],landmarks_list[10],landmarks_list[9])>100 and calcAngle(landmarks_list[20],landmarks_list[18],landmarks_list[17])>100):
            index = landmarks_list[8]
            if(index[0]>0.3 and index[0] <0.8 and index[1]>0.2 and index[1] <0.7 ):
                x  = int((index[0]-0.3)*screen_w*2)
                y = int((index[1]-0.2)*screen_h*2)  
                pgi.moveTo(x,y)

        
        
        if(distance(landmarks_list[4],landmarks_list[9],"first")<0.065 and distance(landmarks_list[7],landmarks_list[5],"seocnd")<0.12 and calcAngle(landmarks_list[8],landmarks_list[6],landmarks_list[5])>100 and calcAngle(landmarks_list[12],landmarks_list[10],landmarks_list[9])>100 and calcAngle(landmarks_list[20],landmarks_list[18],landmarks_list[17])>100 and calcAngle(landmarks_list[16],landmarks_list[14],landmarks_list[13])>100):
            pgi.leftClick()
        if(distance(landmarks_list[4],landmarks_list[9],"first")>0.065 and distance(landmarks_list[7],landmarks_list[5],"seocnd")<0.12 and calcAngle(landmarks_list[8],landmarks_list[6],landmarks_list[5])>100 and calcAngle(landmarks_list[12],landmarks_list[10],landmarks_list[9])<20 and calcAngle(landmarks_list[20],landmarks_list[18],landmarks_list[17])>100 and calcAngle(landmarks_list[16],landmarks_list[14],landmarks_list[13])>100):
            pgi.rightClick()
            
        if(distance(landmarks_list[4],landmarks_list[9],"first")<0.08 and calcAngle(landmarks_list[8],landmarks_list[6],landmarks_list[5]) <20  and calcAngle(landmarks_list[12],landmarks_list[10],landmarks_list[9])<20 and calcAngle(landmarks_list[20],landmarks_list[18],landmarks_list[17])>100 and calcAngle(landmarks_list[16],landmarks_list[14],landmarks_list[13])>100):
            index = landmarks_list[8]
            x  = int(index[0]*screen_w)
            y = int(index[1]*screen_h) 
            pgi.mouseDown(button="left")
            pgi.moveTo(x,y)
            
        
        if(landmarks_list[4][1]<landmarks_list[8][1] and landmarks_list[8][1]<landmarks_list[12][1] and landmarks_list[12][1]<landmarks_list[16][1] and landmarks_list[16][1]<landmarks_list[20][1] and calcAngle(landmarks_list[20],landmarks_list[18],landmarks_list[17])>100):
            pgi.scroll(-100)
        if(landmarks_list[4][1]>landmarks_list[8][1] and landmarks_list[8][1]>landmarks_list[12][1] and landmarks_list[12][1]>landmarks_list[16][1] and landmarks_list[16][1]>landmarks_list[20][1] and calcAngle(landmarks_list[20],landmarks_list[18],landmarks_list[17])>100):
            pgi.scroll(100)
            
        if(distance(landmarks_list[4],landmarks_list[9],"first")<0.065 and calcAngle(landmarks_list[8],landmarks_list[6],landmarks_list[5])<20 and calcAngle(landmarks_list[16],landmarks_list[14],landmarks_list[13])>100 and calcAngle(landmarks_list[12],landmarks_list[10],landmarks_list[9])>100 and calcAngle(landmarks_list[20],landmarks_list[18],landmarks_list[17])<20) :
            pgi.screenshot("photos/screenshot.png") 
            img = cv.imread("photos/screenshot.png")
            img = cv.resize(img,(700,500)) 
            cv.imshow("screensht",img)
            cv.waitKey(1000) 
            cv.destroyAllWindows()
        

        
        if(distance(landmarks_list[4],landmarks_list[9],"first")<0.065  and landmarks_list[5][0]<landmarks_list[9][0] and landmarks_list[9][0]<landmarks_list[13][0] and landmarks_list[13][0]<landmarks_list[17][0] and calcAngle(landmarks_list[20],landmarks_list[18],landmarks_list[17])<20 and calcAngle(landmarks_list[8],landmarks_list[6],landmarks_list[5])>100 and calcAngle(landmarks_list[12],landmarks_list[10],landmarks_list[9])>100 and calcAngle(landmarks_list[16],landmarks_list[14],landmarks_list[13])>100):
            pgi.press("volumeup")
        if(distance(landmarks_list[4],landmarks_list[9],"first")>0.065 and landmarks_list[5][0]<landmarks_list[9][0] and landmarks_list[9][0]<landmarks_list[13][0] and landmarks_list[13][0]<landmarks_list[17][0] and calcAngle(landmarks_list[20],landmarks_list[18],landmarks_list[17])<20 and calcAngle(landmarks_list[8],landmarks_list[6],landmarks_list[5])>100 and calcAngle(landmarks_list[12],landmarks_list[10],landmarks_list[9])>100 and calcAngle(landmarks_list[16],landmarks_list[14],landmarks_list[13])>100):
            pgi.press("volumedown")
    