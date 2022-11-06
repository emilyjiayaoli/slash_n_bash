# from the mediaipe website for pose

import cv2
import mediapipe as mp
import body_tracking_module as btm
import action_gestures as ag
import pyautogui as p

from cmu_112_graphics import *

# referenced mediapipe documentation https://google.github.io/mediapipe/solutions/pose.html
#            pyautogui documentation for p.press("key") https://pyautogui.readthedocs.io/en/latest/keyboard.html
body = btm.PoseTracking() #takes in image

cap = cv2.VideoCapture(0)

slash = 0
block = 0
down = 0

def checkGestures(gestures, slash, block, down):   
    # checks if gestures are activated
    # if so, call the corresponding keypressed using pyautogui 
    if gestures.isDown():
        down += 1
        if down >= 3:
            p.press("s")
            down = 0
            print("Down!")
    elif gestures.isSide():
        slash += 1
        if slash >= 3:
            p.press("d")
            slash = 0
            print("Side Slash!")
    elif gestures.isBlock():
        block += 1
        if block >= 2:
            p.press("a")
            block = 0
            print("Block!!")
    return slash, block, down

while cap.isOpened():
    # reads image from webcam
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame!")
        continue

    # optionally mark the image as not writeable to pass by inference
    image.flags.writeable = False

    keypoints = body.get_kpts_list(image, True) #processes keypoints
    gestures = ag.ActionGestures(keypoints) #gesture object

    if keypoints != []:
        slash, block, down = checkGestures(gestures, slash, block, down)

    # display image
    cv2.imshow('Pose Estimation!', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()