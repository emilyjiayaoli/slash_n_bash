#class draft 1

class Player:
    def __init__(self):
        self.hp #quantity   
        self.actions #dictionary of actions mapping to a list of states/frames
        self.action #current action

    def redraw(self, app, canvas):
        pass

    def timerFired(self, app):
        #some way to check interactions (player state and current enemy state)
        #checkInteractions(self, currentEnemy)
        pass


    def keyPressed(self, app, event):
        #{key} starts {action} if not already in an action
        pass

    
class Enemy:
    def __init__(self):
        pass

class currentEnemy(Enemy):
    def __init__(self):
        self.hp
        self.actions
        self.action
        self.behavior #hard coded series of actions to take

