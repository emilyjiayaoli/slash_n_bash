import cv2
import mediapipe as mp


class PoseTracking():
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_pose = mp.solutions.pose #mp_pose class

        #pose object of mp_pose class
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) 
    
    def get_kpts_list(self, img, draw_keypoints=True): #per frame
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        results = self.pose.process(img_rgb) #get results
        
        # Restructuring the keypoints for easy access
        keypoints_list = []
        if results.pose_landmarks:
            poselm = results.pose_landmarks
            #for poselm in results.pose_landmarks:
            for id, joint_lm in enumerate(poselm.landmark):
                if draw_keypoints:
                    self.mp_drawing.draw_landmarks(img, poselm, 
                            self.mp_pose.POSE_CONNECTIONS)
                h, w, c = img.shape
                cx, cy = int(joint_lm.x * w), int(joint_lm.y * h)
                keypoints_list.append([id, cx, cy])

                #draws the wrists
                if id == 15:
                    cv2.circle(img, (cx,cy), 20, (255,0,0),3)
                if id == 16:
                    cv2.circle(img, (cx,cy), 20, (255,0,0),3)

            #print("id, x, y", keypoints_list[0])
        return keypoints_list 
    
    def get_joint_kpts(self, keypoints_list, id):
        if keypoints_list == []:
            return None, None
        else:
            x, y = keypoints_list[id][1], keypoints_list[id][2]
            assert id == keypoints_list[id][0], print("joint id not matched keypoints_list")
            return x, y
