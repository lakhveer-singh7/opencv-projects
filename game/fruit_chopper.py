import pygame as pgm
import random as rd
import cv2 as cv
import numpy as np
import mediapipe as mp
import time


pgm.mixer.init()
bg = pgm.mixer.Sound("bg music.mp3")
cut =  pgm.mixer.Sound("cut.mp3")
pgm.mixer.Sound.set_volume(bg,0.4)
bg.play()

score_list = []
bomb_list = []
fruits=[]
fps=60
score = [0,None,0,True]
score_file=open("highest_score.txt","r+")
score[1]=int(score_file.read())
# img=cv.imread("watermalon.png")
# img=cv.resize(img,(150,120),interpolation=cv.INTER_AREA)
# cv.imwrite("watermalon.png",img)

# fruits movement code
def move():   
    # print(len(fruits))
    for i in fruits:
    #   i["image"] = images_rect[fruits.index(i)]
      #im =images[fruits.index(i)].get_rect()
    #   print("image = " ,images_rect.index(i["image"]))
      if i["x"]>=width or i["x"]<=-100:
        #   i["x"]=rd.randint(10,width-100)
        #   i["y"]=height+500
        #   if i["x"]>=width/2:
        #      i["dir_x"]=1
        #   else:
        #      i["dir_x"]=0
        fruits.pop(fruits.index(i))
        continue
      if i["y"]>=height and i["dir_y"]==1 :
        #   i["y"]=height+200
        #   i["dir_y"]=0
        #   i["x"]=rd.randint(10,width-100)
        
        fruits.pop(fruits.index(i))
        continue
        
      if (i["y"]-rd.randint(0,5)*20)/10<=1:
         i["dir_y"]=1
      if i["dir_x"]==0:
         i["x"]+=10
      else:
        i["x"]-=10
      if  i["dir_y"]==0:
        i["y"]-=int(i["y"]/(15))
      else:
        i["y"]+=int(i["y"]/(15))

      i["image"].center = i["x"],i["y"]
      window.blit(images[images_rect.index(i["image"])],i["image"])    
      #window.blit(i["image"],(i["x"],i["y"]))


linemade = []
# fruit cutting code
def cut(land_marklist,score):
   if len(land_marklist)>10:
    x=land_marklist[8][0]*width
    y=land_marklist[8][1]*height
    if len(linemade)<=5:
       linemade.append((x,y))
    else:
       linemade.append((x,y))
       linemade.pop(0)
    for i in  range(0,len(linemade)-1):
     pgm.draw.line(window,(255,0,0),linemade[i],linemade[i+1],5)
    font = pgm.font.Font(None,50)
    text = font.render("+10",True,(0,255,0))
    for j in score_list:
        j[1]-=10
        if(j[1]<0):
           score_list.pop(score_list.index(j))
        else:
           window.blit(text,(j[0],j[1]))
    for j in bomb_list:
        j[1] -=5
        if(j[1]<0):
           bomb_list.pop(bomb_list.index(j))
        else:
           window.blit(j[2],(j[0],j[1]))   
    rect = pgm.Rect(x-5,y-5,10,10)
    pgm.draw.rect(window,(0,0,255),rect)
    for i in fruits:
       if(i["image"].clipline(linemade[0],linemade[len(linemade)-1])):
            if images_rect.index(i["image"]) == 2 :
                bomb_sound = pgm.mixer.Sound("bomb.mp3")
                pgm.mixer.Sound.set_volume(bomb_sound,2)
                bomb_sound.play()
                font = pgm.font.Font(None,100)
                if score[0]>=50:
                    score[0] -= 50
                    txt = font.render("-50",True,(255,0,0))
                    bomb_list.append([75,60,txt])
                else :
                    x = 50 - score[0]
                    x = x/10
                    score[2] = x
                    txt_score = font.render(f"-{score[0]}",True,(255,0,0))
                    txt_timer = font.render(f"+{x}",True,(255,0,0))
                    bomb_list.append([75,60,txt_score])
                    bomb_list.append([width-75,60,txt_timer])
                    score[0] = 0
                fruits.pop(fruits.index(i))
            elif images_rect.index(i["image"]) == 11 :
                  clock_sound = pgm.mixer.Sound("clock_sound.mp3")
                  pgm.mixer.Sound.set_volume(clock_sound,2)
                  clock_sound.play()
                  font = pgm.font.Font(None,100)
                  
                  score[2] = -3
                  txt_timer = font.render("-3",True,(0,255,0))
                  bomb_list.append([width-75,60,txt_timer])
                  fruits.pop(fruits.index(i))
            else :
                cut =  pgm.mixer.Sound("cut.mp3")
                pgm.mixer.Sound.set_volume(cut,0.5)
                cut.play()
                score[0]+=10
            #     i["x"]=rd.randint(10,width-100)
            #     i["y"]=height+200
            #     i["dir_y"]=0
            # # fruits[i]["x"]=rd.randint(10,width-100)
            # if i["x"]>=width/2:
            #    i["dir_x"]=1
            # else:
            #    i["dir_x"]=0
                fruits.pop(fruits.index(i))
                score_list.append([x,y])
    #    pgm.mixer.music.stop()     
       
    # pgm.draw.polygon(window,(255,255,255),((x-10,y),(x,y-2),(x,y+2),(x+10,y)))
   
  
def reset(t,timer):
  b,c=t,timer
  if score[1]<score[0]:
      score_file.seek(0)
      score_file.truncate()
      score_file.write(str(score[0]))
      score[1]=score[0]
  
  fruits.clear()
  a = rd.randint(0,len(images))
  for i in range(0,a):
    b  = rd.randint(0,len(images)-1)
    # print("initialize list ",a,b)
    img = fru_dic.copy()
    img["image"] = images_rect[b]
    img["x"] = rd.randint(10,width-10)
    img["y"] = height+rd.randint(100,800)
    if img["x"]>=width/2:
        img["dir_x"]=1
    else:
        img["dir_x"]=0
    fruits.append(img)

  pgm.mouse.set_visible(True)
  window.blit(bg_img,(0,0))
  font = pgm.font.Font(None,60)
  font2 = pgm.font.Font(None,60)
  text1 = font.render("TIME UP",True,(0,255,0))
  text2 = font.render(f"YOUR SCORE : {score[0]}",True,(0,255,0))
  text_max_score = font.render(f"HIGHEST SCORE : {score[1]}",True,(0,255,0))
  text3=font2.render("PLAY",True,(255,255,255))
  text4=font2.render("QUIT",True,(255,255,255))
  #text5=font2.render("SETTINGS",True,(255,255,255))
  if not score[3]:
    window.blit(text1,(width/2-70,height/2-280))
    window.blit(text2,(width/2-150,height/2-230))
    window.blit(text_max_score,(width/2-180,height/2-180))
  #play rect

  rect_play=pgm.Rect((width/2-70,height/2-50,180,40))
  rect_play_bdr=pgm.Rect((width/2-73,height/2-53,186,46))
  pgm.draw.rect(window,(255,255,255),rect_play_bdr,2,2,2,2)
  pgm.draw.rect(window,(255,153,51),rect_play)
  window.blit(text3,(rect_play.centerx-53,rect_play.centery-18))
  #quit rect
  rect_quit=pgm.Rect((width/2-70,height/2+50,180,40))
  rect_quit_bdr=pgm.Rect((width/2-73,height/2+47,186,46))
  pgm.draw.rect(window,(255,255,255),rect_quit_bdr,2,2,2,2)
  pgm.draw.rect(window,(255,153,51),rect_quit)
  window.blit(text4,(rect_quit.centerx-53,rect_quit.centery-18))
  # #settings rectangle
  # rect_settings=pgm.Rect((width/2-90,height/2+150,240,40))
  # rect_settings_bdr=pgm.Rect((width/2-93,height/2+147,246,46))
  # pgm.draw.rect(window,(255,255,255),rect_settings_bdr,2,2,2,2)
  # pgm.draw.rect(window,(255,153,51),rect_settings)
  # window.blit(text5,(rect_settings.centerx-105,rect_settings.centery-18))

  if(rect_play.collidepoint(pgm.mouse.get_pos())):
           rect_play.inflate_ip((50,50))
           #pgm.draw.rect(window,(255,153,51),rect_play,4)
           #system_cursor = pgm.cursors.compile(pgm.cursors.ball)
           # Set the cursor
           #cursor_size = (16, 16)  # Standard size for system cursors
           #hotspot = (0, 0)  # Hotspot at top-left corner for hand cursor
           #pgm.mouse.set_cursor(cursor_size,hotspot,SYSTEM_CURSOR_HAND)

           for ev in pgm.event.get():
            if ev.type==pgm.MOUSEBUTTONDOWN:
               score[0]=0
               b=time.perf_counter()
               score[3] = False
               c=0
  if(rect_quit.collidepoint(pgm.mouse.get_pos())):
           rect_quit.inflate_ip((10,10))
           #system_cursor = pgm.cursors.compile(pgm.cursors.ball)
           # Set the cursor
           #cursor_size = (16, 16)  # Standard size for system cursors
           #hotspot = (0, 0)  # Hotspot at top-left corner for hand cursor
           #pgm.mouse.set_cursor(cursor_size,hotspot,SYSTEM_CURSOR_HAND)
           for ev in pgm.event.get():
            if ev.type==pgm.MOUSEBUTTONDOWN:
               pgm.quit()

  # if(rect_settings.collidepoint(pgm.mouse.get_pos())):
            #rect_settings.inflate_ip((10,10))
           #system_cursor = pgm.cursors.compile(pgm.cursors.ball)
           # Set the cursor
           #cursor_size = (16, 16)  # Standard size for system cursors
           #hotspot = (0, 0)  # Hotspot at top-left corner for hand cursor
           #pgm.mouse.set_cursor(cursor_size,hotspot,SYSTEM_CURSOR_HAND) 
           #for ev in pgm.event.get():
             #if ev.type==pgm.MOUSEBUTTONDOWN:
               
  pgm.display.update()
  return (b,c)
# initialising pygame
pgm.init()
# creating window
width,height=1450,740
window=pgm.display.set_mode((width,height))
pgm.display.set_caption("fruit-chopper")

# initializing fps
clock=pgm.time.Clock()

# creating fruit's dectionaries
# lis =['bomb.png']
# for i in lis:
#  img = cv.imread(i)
#  img=cv.resize(img,(130,130),interpolation=cv.INTER_AREA)
#  cv.imwrite(i,img)

# image load
images=(pgm.image.load('apple.png'),pgm.image.load('banana.png').convert_alpha(),pgm.image.load('bomb.png').convert_alpha(),pgm.image.load('broccli.png').convert_alpha(),pgm.image.load('Dragon-fruit.png').convert_alpha(),pgm.image.load('grapes.png').convert_alpha(),pgm.image.load('loki.png').convert_alpha(),pgm.image.load('mango.png').convert_alpha(),pgm.image.load('orange.png').convert_alpha(),pgm.image.load('pinapple.png').convert_alpha(),pgm.image.load('strobery.png').convert_alpha(),pgm.image.load('timer.png').convert_alpha(),pgm.image.load('tomato.png').convert_alpha(),pgm.image.load('watermalon.png').convert_alpha())
images_rect=(pgm.image.load('apple.png').convert_alpha().get_rect(),pgm.image.load('banana.png').convert_alpha().get_rect(),pgm.image.load('bomb.png').convert_alpha().get_rect(),pgm.image.load('broccli.png').convert_alpha().get_rect(),pgm.image.load('Dragon-fruit.png').convert_alpha().get_rect(),pgm.image.load('grapes.png').convert_alpha().get_rect(),pgm.image.load('loki.png').convert_alpha().get_rect(),pgm.image.load('mango.png').convert_alpha().get_rect(),pgm.image.load('orange.png').convert_alpha().get_rect(),pgm.image.load('pinapple.png').convert_alpha().get_rect(),pgm.image.load('strobery.png').convert_alpha().get_rect(),pgm.image.load('timer.png').convert_alpha().get_rect(),pgm.image.load('tomato.png').convert_alpha().get_rect(),pgm.image.load('watermalon.png').convert_alpha().get_rect())
# initialise x and y coordinates of fruits


# bomb_img = pgm.image.load("bomb.jpg").convert_alpha()
# bomb_img = bomb_img.get_rect()

fru_dic = {"image":None,"x":None,"y":None,"dir_y":0,"dir_x":0}

a = rd.randint(0,6)
for i in range(0,a):
    b  = rd.randint(0,6)
    print("initialize list ",a,b)
    img = fru_dic.copy()
    img["image"] = images_rect[b]
    img["x"] = rd.randint(10,width-10)
    img["y"] = height+rd.randint(100,800)
    if img["x"]>=width/2:
        img["dir_x"]=1
    else:
        img["dir_x"]=0
    fruits.append(img)

#  setting size of background image
img=cv.imread("bg_chopper.webp")
img=cv.resize(img,(width,height),interpolation=cv.INTER_AREA)
cv.imwrite("bg_chopper.webp",img)
bg_img_reset=pgm.image.load("bg_chopper.webp").convert()

#setting background image
bg_img=pgm.image.load("game_fruit_backgr.jpg").convert()
check=True
timer = 0
# opencv integration
mphands=mp.solutions.hands
hands=mphands.Hands( 
    static_image_mode=False, 
    model_complexity=1, 
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5, 
    max_num_hands=1)

drawingModule = mp.solutions.drawing_utils

cam=cv.VideoCapture(0)
# pre game display
window.blit(bg_img_reset,(0,0))
pgm.display.update()
time.sleep(1.5)

# loop start
t = time.perf_counter()
while check:
    frame_check,frame=cam.read()
    if(not frame_check):
        break
    else:
     for i in pgm.event.get():
        if i.type==pgm.QUIT:
            check=False
            pgm.quit()
    
# logic
     frame=cv.flip(frame,1)
     frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
     detection_result=hands.process(frame)
     landmarks_list = []
     if detection_result.multi_hand_landmarks:
            for i in detection_result.multi_hand_landmarks:
            #   drawingModule.draw_landmarks(bg_img, i, mphands.HAND_CONNECTIONS)  
                for id, lm in enumerate(i.landmark):
                    landmarks_list.append((lm.x, lm.y))
                # print(landmarks_list)
     window.blit(bg_img,(0,0))
     #pgm.draw.rect(window,(255,255,255),(0,0,width,height))
     st = pgm.font.Font(None,50)
     tst = st.render(f"score : {score[0]}", True,(255,255,255))
     timer = int(time.perf_counter()-t) + score[2]
     score[2] =0
     if score[3] :
         timer = 35
     if timer >30:
        t,timer = reset(t,timer)
        # window.blit(bg_img,(0,0))
        # font = pgm.font.Font(None,100)
        # text1 = font.render("TIME UP",True,(0,255,0))
        # text2 = font.render(f"YOUR SCORE IS : {score[0]}",True,(0,255,0))
        # window.blit(text1,(width/2-120,height/2-100))
        # window.blit(text2,(width/2-300,height/2))
        # pgm.display.update()
        # pgm.quit()
     else:
        pgm.mouse.set_visible(False)
        timetxt = st.render(f"time : {timer}",True,(255,255,255))
        window.blit(tst,(50,50))
        window.blit(timetxt,(width-200,50))
        move()
        # fruit list generation
        r = rd.randint(0,20)
        if r==10:
                b  = rd.randint(0,len(images)-1)
                img = fru_dic.copy()
                img["image"] = images_rect[b]
                img["x"] = rd.randint(10,width-10)
                img["y"] = height+rd.randint(100,200)
                img["dir_y"]=0
                if img["x"]>=width/2:
                    img["dir_x"]=1
                else:
                    img["dir_x"]=0
                fruits.append(img) 
        cut(landmarks_list,score)
# display update
        pgm.display.update()

# fps set
        clock.tick(fps)


