# Virtual_painter

## Overview
This is a code for a virtual painter that uses AI to draw over the webcam feed in realtime. In this program I have used the hand tracking module of mediapipe library to identify and track the various hand landmarks, and openCV library is used for all the image processing. Hands module of mediapipe library is an extremely efficient tool to detect and track the hand landmarks. It track twenty palm landmarks, as shown in the figure below. 
![Computer Vision](https://github.com/AbhinavArya1990/Virtual_painter/blob/main/hands%20mediapipe.JPG)

The information gathered from the landmarks is used to identify the hand's exact location and gesture and using OpenCV and drawing utilities of mediapipe, drawing can be done on the live feed from the webcam as shown below.
