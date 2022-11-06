class ActionGestures:
    def __init__(self, keypoints):
        self.kpts = keypoints

    def isBlock(self):
        pass

    def isDown(self):
        #print(len(self.kpts))
        if self.kpts[13][2] < self.kpts[11][2]:
            #print("hi")
            return True
        else: return False

    def isSide(self):
        pass