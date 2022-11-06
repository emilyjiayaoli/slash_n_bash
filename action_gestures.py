class ActionGestures:
    def __init__(self, keypoints):
        self.kpts = keypoints
        if self.kpts != []:
            self.l_wrist = self.kpts[16]
            self.r_wrist = self.kpts[15]
            self.l_shoulder = self.kpts[12]
            self.r_shoulder = self.kpts[11]
            self.l_hip = self.kpts[24]
            self.r_hip = self.kpts[23]

    def isSide(self):
        if (self.l_wrist[1] < self.l_shoulder[1]) and (self.l_wrist[1] < self.l_hip[1]):
            if (self.r_wrist[1] < self.r_shoulder[1]) and (self.r_wrist[1] < self.r_hip[1]):
                if abs(self.kpts[15][1]-self.kpts[16][1]) < \
                    0.5*abs(self.kpts[12][1]-self.kpts[11][1]):
                        if not self.r_wrist[1] > self.r_shoulder[1]:
                            return True
        return False

    def isBlock(self):
        if self.l_shoulder[1] > self.r_shoulder[1]:
            return True
        return False

    def isDown(self):
        if (self.l_wrist[2] < self.l_shoulder[2]) and (self.r_wrist[2] < self.r_shoulder[2]):
            if abs(self.kpts[15][1]-self.kpts[16][1]) < 0.5*abs(self.kpts[12][1]-self.kpts[11][1]):
                return True
        return False