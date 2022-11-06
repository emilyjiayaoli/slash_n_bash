# from the mediaipe website for pose

import cv2
import mediapipe as mp
import body_tracking_module as btm
import action_gestures as ag
import pyautogui as p

body = btm.PoseTracking() #takes in image
# later could call body.getkeypts()

#pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

def checkGestures(gestures):
    # if gestures.isBlock():
    #     p.press("w")
    if gestures.isDown():
        p.press("d")
        print("down")
    # elif gestures.isSide():
    #     p.press("d")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame!")
        continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    keypoints = body.get_kpts_list(image, True)
    #x, y = body.get_joint_kpts(keypoints_list=keypoints, id=0)
    
    gestures = ag.ActionGestures(keypoints) #gesture object, 

    if keypoints != []:
        checkGestures(gestures)

    #display image
    cv2.imshow('Pose Estimation!', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()