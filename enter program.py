import numpy as np
import cv2
import time
from py2 import PressKey,ReleaseKey,W,S,A,D,C,Enter
import keyboard
from PIL import ImageGrab
#time.sleep(2)
th1 = cv2.imread('matchimage1.png')
#th1 = cv2.Canny(newimg,threshold1 =200,threshold2 = 300)
#th1 =cv2.cvtColor(newimg, cv2.COLOR_BGR2RGB)
i = 0
#cv2.imshow('abc',th1)
global start_timer
start_timer = time.time()
while True:
    i = i + 1
    if keyboard.is_pressed('esc'):
        
        elapsed = time.time() - start_timer
        print((elapsed/60)/60,"Hour")
        print(elapsed/60,"Min")
        print(elapsed,"Sec")
        break

    #time.sleep(0)
    Print_Screen = ImageGrab.grab()
    Print_Numpy = np.array(Print_Screen)
    x,y,w,h = bbox = (600, 460, 650, 150)
    croped = Print_Numpy[y:y+h, x:x+w]
    #th2 = cv2.Canny(croped,threshold1 =200,threshold2 = 300)
    th2 = cv2.cvtColor(croped, cv2.COLOR_BGR2RGB)
    #cv2.imshow('abc1',th2)
    iar = np.array(th1)
    iar2 = np.array(th2)
    matched_arrays = 0
    x = 0      
    while (x < 150):
        y = 0
        while (y < 650 ):   
            if (iar[x][y] == iar2[x][y]).all():
                #print ("match")
                matched_arrays = matched_arrays + 1
            y  = y + 1
        x = x + 1
        if x == iar.size:
            break
    percent = (matched_arrays / 97500) * 100
    if percent > 70:
        PressKey(Enter)
        print(percent)
        print("Matched")
        time.sleep(3)
print(i)


