# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:03:23 2021
@author: Abhinav
This program uses openCV and mediapipe libraries to detect hand landmarks and use them for to write 
and draw realtime of the screen
"""
#!pip install HandDetectorModule
#!pip install mediapipe --user
import cv2
import mediapipe as mp
import time
import math
import numpy as np

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.9)           #high confidence index to reduce noice
mpDraw = mp.solutions.drawing_utils
imgCanvas = np.zeros((720,1280,3), np.uint8 )  # Canvas for drawing
pTime = 0
cTime = 0
x1,y1 = 0,0 

cap =cv2.VideoCapture(0)                      # Capture webcam feed
cap.set(3,1280)
cap.set(4,720)

while True:
    lms_list = []                               #this list holds the position information of each landmark
    _,frame = cap.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)     # Mediapipe works with RGB images
    results = hands.process(imgRGB)  
   # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h,w,c =frame.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                lms_list.append((id,cx,cy))
                if len(lms_list)>20:
                    x4,y4 = lms_list[4][1:]
                    x8,y8 = lms_list[8][1:]
                    x12,y12 = lms_list[12][1:]
                    dist4_12 = math.dist((x12,y12), (x4,y4))              #Distance between thumb and middle finger tip
                    dist8_12 = math.dist((x8,y8),(x12,y12))               #Distance between index and middle finger tip                                 
                    if dist8_12>100 and dist4_12 <200:
                        #Drawing mode
                        cv2.line(imgCanvas, (x1,y1),(x8,y8),(0,0,255), 10)
                    elif dist8_12<40:
                        #Eraser mode
                        cv2.line(imgCanvas, (x1,y1),(x8,y8),(0,0,0), 200)
                    print(dist4_12)
                    
            x1,y1 = x8,y8    
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
            
    cTime =time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    img = cv2.addWeighted(frame, 0.9, imgCanvas,0.1,0) 
    img = cv2.flip(img,1)
    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3,
                (0,0,255), 3)
    cv2.imshow("Feed", img)
    #cv2.imshow("Canvas", cv2.flip(imgCanvas,1))
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

