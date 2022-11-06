from cmu_112_graphics import *
from helpers import *
from sound import *
# getYs and cutSpritesheet from helpers.py 

# https://www.cs.cmu.edu/~112/notes/notes-oop-part1.html#oopExample
# Citation ^ 9. Example: Animation with OOPclass Enemy
 
class WaterEnemy:
    def __init__(self, app, level):
        self.level = level
        self.animationCounter = 0

        if level == 1:
            self.hp = 115
            self.maxHP = 115
            self.state = 'walk'
            self.walkX = 0
            self.moveDeath = 0
            self.timeAfterDeath = 0
            self.callNextLevel = False

            self.behavior = ['idle', 'magic', 'block', 'idle', 'stab', 'combo',
            'block', 'stab']
            self.behaviorIndex = 0
            self.combatTuple = (0, 0, 'vulnerable')
            # https://chierit.itch.io/elementals-water-priestess
            spritesheet = app.loadImage('./assets/waterSheet.png')
            self.icon = app.loadImage('./assets/water_priestess.png')
            xWidth = 288
            startX = 0

            # https://pixabay.com/sound-effects/medieval-bell-d3-90290/
            self.deathSound = Sound('./assets/audio/deathAudio.mp3')

        elif level == 2:
            self.hp = 130
            self.maxHP = 130
            self.state = 'walk'
            self.walkX = 0
            self.moveDeath = 0
            self.timeAfterDeath = 0
            self.callNextLevel = False

            self.behavior = ['block', 'stab', 'block', 'idle', 'stab', 'stab', 'block',
            'combo', 'idle', 'stab', 'block', 'stab']
            self.behaviorIndex = 0
            self.combatTuple = (0, 0, 'vulnerable')
            spritesheet = app.loadImage('./assets/waterSheet.png')
            self.icon = app.loadImage('./assets/water_priestess.png')
            xWidth = 288
            startX = 0

            self.deathSound = Sound('./assets/audio/deathAudio.mp3')

        elif level == 3:
            self.hp = 150
            self.maxHP = 150
            self.state = 'walk'
            self.walkX = 0
            self.moveDeath = 0
            self.timeAfterDeath = 0
            self.callNextLevel = False

            self.behavior = ['magic', 'stab', 'idle', 'stab', 'stab', 'idle',
            'combo', 'idle', 'magic', 'combo', 'idle', 'stab', 'idle','combo']
            self.behaviorIndex = 0
            self.combatTuple = (0, 0, 'vulnerable')
            spritesheet = app.loadImage('./assets/waterSheet.png')
            self.icon = app.loadImage('./assets/water_priestess.png')
            xWidth = 288
            startX = 0

            self.deathSound = Sound('./assets/audio/deathAudio.mp3')

        # Load idle animation
        self.idle = []
        for i in range(7):
            (startY, endY) = getYs(0)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.idle.append((img, dmg, blockEff, vulnerability))

        # Load walk animation
        self.walk = []
        for i in range(7):
            (startY, endY) = getYs(2)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.walk.append((img, dmg, blockEff, vulnerability))

        # Load stab animation
        self.stab = []
        for i in range(6):
            (startY, endY) = getYs(7)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i not in [2, 3]:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            else:
                (img, dmg, blockEff, vulnerability) = (animation, 7, 0, 
                'vulnerable')
            self.stab.append((img, dmg, blockEff, vulnerability))

        # Load stab animation
        self.combo = []
        for i in range(12, 26):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i in [12, 13, 18, 24, 25, 26]:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            elif i in range(14, 18):
                (img, dmg, blockEff, vulnerability) = (animation, 3, 0, 
                'vulnerable') 
            elif i in range(19, 23):
                (img, dmg, blockEff, vulnerability) = (animation, 3, 0, 
                'vulnerable')
            self.combo.append((img, dmg, blockEff, vulnerability))

        # Load magic
        self.magic = []
        for i in range(31):
            (startY, endY) = getYs(10)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i in range(0, 2) or i in [11, 30]:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0.2, 
                'invulnerable')
            elif i in range(2, 11):
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            elif i in range(12, 17):
                (img, dmg, blockEff, vulnerability) = (animation, 5, 0, 
                'vulnerable') 
            elif i in range(17, 21):
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0.8, 
                'vulnerable') 
            elif i in range(21, 30):
                (img, dmg, blockEff, vulnerability) = (animation, 3, 0, 
                'vulnerable') 

            self.magic.append((img, dmg, blockEff, vulnerability))

        # Load block
        self.block = []
        for i in range(11):
            (startY, endY) = getYs(12)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i == 0:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            elif i in range(1, 8):
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0.6, 
                'counterhit')
            elif i in range(8, 12):
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0.4, 
                'vulnerable')
            self.block.append((img, dmg, blockEff, vulnerability)) 

        # Load hit
        self.hit = []
        for i in range(6):
            (startY, endY) = getYs(12)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i < 2:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'invulnerable')
            else:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.hit.append((img, dmg, blockEff, vulnerability)) 

        # Load death
        self.death = []
        for i in range(15):
            (startY, endY) = getYs(13)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.death.append((img, dmg, blockEff, vulnerability)) 

    # Specified behavior to jump to hit, death, run in
    def changeBehavior(self, specifiedBehavior=None):
        if specifiedBehavior == None:
            self.behaviorIndex = ((1 + self.behaviorIndex) % 
            len(self.behavior))
            self.state = self.behavior[self.behaviorIndex]
        else:
            pass

    def drawIcon(self, app, canvas):
        canvas.create_image(app.width//50, app.height/7.5, image=ImageTk.PhotoImage(self.icon), anchor = 'nw')
 
    def drawMaxHP(self, app, canvas):
        self.maxHPBarLength = (app.width//25)*10 - (app.width//25)*2 
        canvas.create_rectangle((app.width//25)*2, app.width//12.5, 
                                    (app.width//25)*10, (app.width//50)*6, width = 5)
 
    def drawCurrentHP(self, app, canvas):
        hpSliceLength = self.hp/self.maxHP * self.maxHPBarLength
        if self.hp > 0:
            canvas.create_rectangle((app.width//25)*2, app.width//12.5, 
                    hpSliceLength + (app.width//25)*2, (app.width//50)*6, fill = 'red')

    def redraw(self, app, canvas):

        self.drawIcon(app, canvas)
        self.drawMaxHP(app, canvas)
        self.drawCurrentHP(app, canvas)
        if self.state == 'stab':
            animation = self.stab[self.animationCounter][0]
        elif self.state == 'combo':
            animation = self.combo[self.animationCounter][0]
        elif self.state == 'magic':
            animation = self.magic[self.animationCounter][0]
        elif self.state == 'block':
            animation = self.block[self.animationCounter][0]
        elif self.state == 'death':
            animation = self.death[self.animationCounter][0]
        elif self.state == 'hit':
            animation = self.hit[self.animationCounter][0]
        elif self.state == 'walk':
            animation = self.walk[self.animationCounter][0]
        else:
            animation = self.idle[self.animationCounter][0]
            
        if self.state == 'walk':
            canvas.create_image(app.width - self.walkX, app.height//12, 
            image=ImageTk.PhotoImage(animation))
        else:
            canvas.create_image(app.width//2 + app.width//9 - self.moveDeath, 
            app.height//12, image=ImageTk.PhotoImage(animation))
 
    def timerFired(self, app):
        if self.hp <= 0:
            if self.state != 'death':
                self.deathSound.start()
                self.animationCounter = 0
            self.state = 'death'
        if self.state == 'idle':
            self.combatTuple = createCombatTuple(self.idle[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.idle):
                self.animationCounter = 0
                self.changeBehavior()

        elif self.state == 'stab':
            self.combatTuple = createCombatTuple(self.stab[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.stab):
                self.animationCounter = 0
                self.changeBehavior()

        elif self.state == 'combo':
            self.combatTuple = createCombatTuple(self.combo[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.combo):
                self.animationCounter = 0
                self.changeBehavior()

        elif self.state == 'magic':
            self.combatTuple = createCombatTuple(self.magic[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.magic):
                self.animationCounter = 0
                self.changeBehavior()

        elif self.state == 'block':
            self.combatTuple = createCombatTuple(self.block[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.block):
                self.animationCounter = 0
                self.changeBehavior() 

        elif self.state == 'hit':
            self.combatTuple = createCombatTuple(self.hit[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.hit):
                self.animationCounter = 0
                self.changeBehavior() 

        elif self.state == 'walk':
            self.combatTuple = createCombatTuple(self.walk[self.animationCounter])
            self.animationCounter = ((1 + self.animationCounter) % 
            len(self.walk))
            self.walkX += 8
            if app.width - self.walkX <= app.width//2 + app.width//9 + 20:
                self.animationCounter = 0
                self.state = 'idle'

        elif self.state == 'death':
            self.combatTuple = createCombatTuple(self.death[self.animationCounter])
            if self.animationCounter < len(self.death) - 1:
                self.animationCounter += 1
                self.timeAfterDeath += 1
            elif self.timeAfterDeath < 20:
                self.timeAfterDeath += 1
            else:
                self.moveDeath += 30
                self.timeAfterDeath += 1
            
            if self.timeAfterDeath > 40:
                self.callNextLevel = True
