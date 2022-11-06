from cmu_112_graphics import *
from helpers import *
# getYs and cutSpritesheet from helpers.py 

# https://www.cs.cmu.edu/~112/notes/notes-oop-part1.html#oopExample
# Citation ^ 9. Example: Animation with OOPclass Enemy
 
class WindEnemy:
    def __init__(self, app, level):
        self.level = level
 
        if level == 1:
            self.hp = 80 #quantity   
            self.actions = {} #dictionary of actions mapping to a list of states/frames
            self.state = 'idle'
            self.animationCounter = 0
            spritesheet = app.loadImage('./assets/windSheet.png')
            xWidth = 288
            startX = 0

        # Load idle animation
        self.idle = []
        for i in range(8):
            (startY, endY) = getYs(0)
            animation = cutWindEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.idle.append((img, dmg, blockEff, vulnerability))
 
    def redraw(self, app, canvas):
        if self.state == 'idle':
            animation = self.idle[self.animationCounter][0]
        else:
            animation = self.idle[self.animationCounter][0]
 
        canvas.create_image(app.width//2 + app.width//10, app.height//12, image=ImageTk.PhotoImage(animation))
 
    def timerFired(self, app):
        if self.state == 'idle':
            self.animationCounter = (1 + self.animationCounter) % len(self.idle)
 
 
