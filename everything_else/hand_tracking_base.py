# install opencv and mediapipe
# using opencv to use webcam
import cv2 
import mediapipe as mp
#cannot install using pip3, just use pip
import time

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands() #parameters: 

cap = cv2.VideoCapture(0)

cTime = 0
pTime = 0

print('Capturing...') 
while True:
    success, img = cap.read() #reading the image from capture
    #rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converting img from BGR to RBG
    results = hands.process(img) #process the captured rgb_img using mp.solutions.hands.process()
        #results is basically an array with all the keypoints labeled
    
    #print(results.multi_hand_landmarks) #results/multi_hand_landmarks is a list of the x,y,x pixel ratio for the 0-21 keypoints

    if results.multi_hand_landmarks: 
        for handLm in results.multi_hand_landmarks: #handLm are obkects of <class 'mediapipe.framework.formats.landmark_pb2.NormalizedLandmarkList'> for each keypoint
            mpDraw.draw_landmarks(img, handLm, mpHands.HAND_CONNECTIONS) #use mp.solutions.drawing_utils.draw_landmarks to draw individual landmarks
            
            #retrieve the coordinate positions of the actual keypoint labels using height and width
            for id, lm in enumerate(handLm.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 0: #draws circle at the tip of index finger
                    cv2.circle(img, (cx,cy), 15, (255,0,3), 3)

            

    #printing out the fps
    cTime = time.time()
    fps = 1/(cTime -pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (230,0,0), 2)

    cv2.imshow("image", img)
    cv2.waitKey(1)

