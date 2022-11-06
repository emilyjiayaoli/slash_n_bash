from cmu_112_graphics import *
from helpers import *
from sound import *
# getYs and cutSpritesheet from helpers.py 

# https://www.cs.cmu.edu/~112/notes/notes-oop-part1.html#oopExample
# Citation ^ 9. Example: Animation with OOP
class Player:
    def __init__(self, app):
        self.hp = 100
        self.maxHP = 100
        self.actions = {} 
        self.state = 'walk'
        self.startWalkIn = True
        self.animationCounter = 0
        self.timeAfterDeath = 0
        self.walkX = 0
        self.combatTuple = (0, 0, 'vulnerable')
        self.callGameOver = False
        spritesheet = app.loadImage('./assets/playerSheet.png')
        self.icon = app.loadImage('./assets/fire_knight.png')

        # Load sounds
        self.downAudio = Sound('./assets/audio/downAudio.mp3')
        self.sideAudio = Sound('./assets/audio/slashAudio.mp3')
        self.blockAudio = Sound('./assets/audio/blockAudio.mp3')

        # https://chierit.itch.io/elementals-fire-knight
        xWidth = 288
        startX = 0

        # Citation for all loads & redraw...
        # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#
        # spritesheetsWithCropping
        # Load idle 
        self.idle = []
        for i in range(8):
            (startY, endY) = getYs(0)
            animation = cutSpritesheet(startX, xWidth*i, xWidth, startY, endY, 
            spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.idle.append((img, dmg, blockEff, vulnerability))

        # Load walk
        self.walk = []
        for i in range(8):
            (startY, endY) = getYs(1)
            animation = cutSpritesheet(startX, xWidth*i, xWidth, startY, endY, 
            spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.walk.append((img, dmg, blockEff, vulnerability))

        # Load side
        self.side = []
        for i in [0, 14, 15, 0]:
            (startY, endY) = getYs(8)
            animation = cutSpritesheet(startX, xWidth*i, xWidth, startY, endY, 
            spritesheet, app)
            if i == 0:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')                              
            else:
                (img, dmg, blockEff, vulnerability) = (animation, 10, 0, 
                'vulnerable')
            self.side.append((img, dmg, blockEff, vulnerability))

        # Load down
        self.down = []
        for i in range(11):
            (startY, endY) = getYs(7)
            animation = cutSpritesheet(startX, xWidth*i, xWidth, startY, endY, 
            spritesheet, app)
            if i == 4:
                (img, dmg, blockEff, vulnerability) = (animation, 25, 0, 
                'vulnerable')
            elif i == 5:
                (img, dmg, blockEff, vulnerability) = (animation, 5, 0, 
                'vulnerable')                                
            else:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.down.append((img, dmg, blockEff, vulnerability))

        # Load block
        self.block = []
        for i in [0, 1, 2, 2, 2, 2, 8, 9]:
            (startY, endY) = getYs(11)
            animation = cutSpritesheet(startX, xWidth*i, xWidth, startY, endY, 
            spritesheet, app)
            if i == 2:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 1, 
                'invulnerable')
            else:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')

            self.block.append((img, dmg, blockEff, vulnerability))

        # Load hit
        self.hit = []
        for i in range(6):
            (startY, endY) = getYs(12)
            animation = cutSpritesheet(startX, xWidth*i, xWidth, startY, endY, 
            spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 1, 
                'invulnerable')
            self.hit.append((img, dmg, blockEff, vulnerability))

        # Load death
        self.death = []
        for i in range(12):
            (startY, endY) = getYs(13)
            animation = cutSpritesheet(startX, xWidth*i, xWidth, startY, endY, 
            spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'invulnerable')
            self.death.append((img, dmg, blockEff, vulnerability))

    def drawIcon(self, app, canvas):
        canvas.create_image(app.width//50, app.height//50, image=ImageTk.PhotoImage(self.icon), anchor = 'nw')
 
    def drawMaxHP(self, app, canvas):
        self.maxHPBarLength = (app.width//25)*10 - (app.width//25)*2 
        canvas.create_rectangle((app.width//25)*2, app.width//50, 
                                    (app.width//25)*10, (app.width//50)*3, width = 5)
 
    def drawCurrentHP(self, app, canvas):
        hpSliceLength = self.hp/self.maxHP * self.maxHPBarLength
        if self.hp > 0:
            canvas.create_rectangle((app.width//25)*2, app.width//50, 
                    hpSliceLength + (app.width//25)*2, (app.width//50)*3, fill = 'blue')

    def redraw(self, app, canvas):
        self.drawIcon(app, canvas)
        self.drawMaxHP(app, canvas)
        self.drawCurrentHP(app, canvas)

        # Change animation set (self.___) depending on state
        if self.state == 'down':
            animation = self.down[self.animationCounter][0]
        elif self.state == 'walk':
            animation = self.walk[self.animationCounter][0]
        elif self.state == 'side':
            animation = self.side[self.animationCounter][0]
        elif self.state == 'hit':
            animation = self.hit[self.animationCounter][0]
        elif self.state == 'death':
            animation = self.death[self.animationCounter][0]
        elif self.state == 'block':
            animation = self.block[self.animationCounter][0]
        else:
            animation = self.idle[self.animationCounter][0]

        if self.state == 'walk' and self.startWalkIn:
            canvas.create_image(self.walkX, app.height//2 
            - app.height//5, image=ImageTk.PhotoImage(animation))
        else:
            canvas.create_image(app.width//2 - app.width//9, app.height//2 
            - app.height//5, image=ImageTk.PhotoImage(animation))

    def timerFired(self, app):
        if self.hp <= 0:
            if self.state != 'death':
                self.animationCounter = 0
            self.state = 'death'
        # Define behaviors depending on state
        if self.state == 'down':
            self.combatTuple = createCombatTuple(self.down[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)
            if self.animationCounter >= len(self.down):
                self.animationCounter = 0
                self.state = 'idle'

        elif self.state == 'side':
            self.combatTuple = createCombatTuple(self.side[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)
            if self.animationCounter >= len(self.side):
                self.animationCounter = 0
                self.state = 'idle'

        elif self.state == 'walk' and self.startWalkIn:
            self.combatTuple = createCombatTuple(self.walk[self.animationCounter])
            self.animationCounter = ((1 + self.animationCounter) % 
            len(self.walk))
            self.walkX += 10
            if self.walkX >= app.width//2 - app.width//9 - 20:
                self.startWalkIn = False
                self.animationCounter = 0
                self.state = 'idle'
    
        elif self.state == 'walk' and self.startWalkIn != True:
            pass

        elif self.state == 'hit':
            self.combatTuple = createCombatTuple(self.hit[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)
            if self.animationCounter >= len(self.hit):
                self.animationCounter = 0
                self.state = 'idle'

        elif self.state == 'block':
            self.combatTuple = createCombatTuple(self.block[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)
            if self.animationCounter >= len(self.block):
                self.animationCounter = 0
                self.state = 'idle'
                
        elif self.state == 'death':
            self.combatTuple = createCombatTuple(self.death[self.animationCounter])
            if self.animationCounter < len(self.death) - 1:
                self.animationCounter += 1
                self.timeAfterDeath += 1
            else:
                self.timeAfterDeath += 1
            
            if self.timeAfterDeath > 30:
                self.callGameOver = True

        else: # idle animation
            self.combatTuple = createCombatTuple(self.idle[self.animationCounter])
            self.animationCounter = ((1 + self.animationCounter) % 
            len(self.idle))

    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#events
    # Part 3. Events
    def keyPressed(self, app, event):
        if event.key == 's' and self.state == 'idle':
            self.downAudio.start(1)
            self.state = 'down'
            self.animationCounter = 0

        elif event.key == 'd' and self.state == 'idle':
            self.sideAudio.start(1)
            self.state = 'side'
            self.animationCounter = 0

        elif (event.key == 'a' and self.state == 'idle'):
            self.blockAudio.start(1)
            self.state = 'block'
            self.animationCounter = 0

# Block auto releases after key pressed on Macbook Pro 16 (M1), but works on 
# Macbook Pro 16 non M1