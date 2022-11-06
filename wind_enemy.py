from cmu_112_graphics import *
from helpers import *
from sound import *
# getYs and cutSpritesheet from helpers.py 

# https://www.cs.cmu.edu/~112/notes/notes-oop-part1.html#oopExample
# Citation ^ 9. Example: Animation with OOPclass Enemy
 
class WindEnemy:
    def __init__(self, app, level):
        self.level = level
        self.animationCounter = 0

        if level == 1:
            self.hp = 120
            self.maxHP = 120     
            self.state = 'walk'
            self.walkX = 0
            self.moveDeath = 0
            self.timeAfterDeath = 0
            self.callNextLevel = False

            self.behavior = ['idle', 'slash', 'idle', 'block', 'idle', 'slash', 
            'block', 'slash', 'block', 'air']
            self.behaviorIndex = 0
            self.combatTuple = (0, 0, 'vulnerable')
            spritesheet = app.loadImage('./assets/windSheet.png')
            self.icon = app.loadImage('./assets/wind_hashashin.png')
            xWidth = 288
            startX = 0

            self.deathSound = Sound('./assets/audio/deathAudio.mp3')

        if level == 2:
            self.hp = 140
            self.maxHP = 140
            self.state = 'walk'
            self.walkX = 0
            self.moveDeath = 0
            self.timeAfterDeath = 0
            self.callNextLevel = False

            self.behavior = ['block','block','block','block','block',
            'slash','slash','block','block','block','air','idle','idle','idle',
            'block','block','spec']



            self.behaviorIndex = 0
            self.combatTuple = (0, 0, 'vulnerable')
            spritesheet = app.loadImage('./assets/windSheet.png')
            self.icon = app.loadImage('./assets/wind_hashashin.png')
            xWidth = 288
            startX = 0

            self.deathSound = Sound('./assets/audio/deathAudio.mp3')

        if level == 3:
            self.hp = 160
            self.maxHP = 160
            self.state = 'walk'
            self.walkX = 0
            self.moveDeath = 0
            self.timeAfterDeath = 0
            self.callNextLevel = False

            self.behavior = ['block','block','spec','block','block','block',
            'slash','slash','block','block','spec','block',
            'air','idle','idle','idle',
            'block','block','spec']



            self.behaviorIndex = 0
            self.combatTuple = (0, 0, 'vulnerable')
            spritesheet = app.loadImage('./assets/windSheet.png')
            self.icon = app.loadImage('./assets/wind_hashashin.png')
            xWidth = 288
            startX = 0

            self.deathSound = Sound('./assets/audio/deathAudio.mp3')


        # Load special attack
        self.spec = []
        for i in range(5):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(5,10):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 1, 
                'invulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(10,11):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(11,12):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 8, 0, 
                'vulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(12,16):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 1, 
                'invulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(16, 17):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(17,18):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 8, 0, 
                'vulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(18,19):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 1, 
                'invulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(19,20):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 8, 0, 
                'invulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(20,24):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(24,29):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 1, 
                'invulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))
        for i in range(29,30):
            (startY, endY) = getYs(9)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.spec.append((img, dmg, blockEff, vulnerability))



        # Load idle animation
        self.idle = []
        for i in range(8):
            (startY, endY) = getYs(0)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.idle.append((img, dmg, blockEff, vulnerability))

        # Load slash
        self.slash = []
        # load slash windup
        for i in range(7,2,-1):
            (startY, endY) = getYs(6)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.slash.append((img, dmg, blockEff, vulnerability))
        # load slash attack
        for i in [2]:
            (startY, endY) = getYs(6)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 3, 0, 
                'vulnerable')
            self.slash.append((img, dmg, blockEff, vulnerability))

        # Load air attack
        self.air = []
        # Load windup
        for i in range(17,13,-1):
            (startY, endY) = getYs(7)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.air.append((img, dmg, blockEff, vulnerability))        
        # Load attack
        for i in range(7,12,1):
            (startY, endY) = getYs(7)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 2, 0, 
                'vulnerable')
            self.air.append((img, dmg, blockEff, vulnerability)) 
        # Load reset
        for i in range(12,18):
            (startY, endY) = getYs(7)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.air.append((img, dmg, blockEff, vulnerability)) 

        # Load block
        self.block = []
        for i in range(7):
            (startY, endY) = getYs(10)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 1, 
                'counterdamage')
            self.block.append((img, dmg, blockEff, vulnerability)) 

        # Load death
        self.death = []
        for i in range(18):
            (startY, endY) = getYs(12)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'invulnerable')
            self.death.append((img, dmg, blockEff, vulnerability)) 

        # Load hit
        self.hit = []
        for i in range(5):
            (startY, endY) = getYs(11)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i < 4:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'invulnerable')
            else:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.hit.append((img, dmg, blockEff, vulnerability)) 

        # Load walk
        self.walk = []
        for i in range(7):
            (startY, endY) = getYs(1)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.walk.append((img, dmg, blockEff, vulnerability)) 


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
        if self.state == 'slash':
            animation = self.slash[self.animationCounter][0]
        elif self.state == 'air':
            animation = self.air[self.animationCounter][0]
        elif self.state == 'block':
            animation = self.block[self.animationCounter][0]
        elif self.state == 'death':
            animation = self.death[self.animationCounter][0]
        elif self.state == 'hit':
            animation = self.hit[self.animationCounter][0]
        elif self.state == 'walk':
            animation = self.walk[self.animationCounter][0]
        elif self.state == 'spec':
            animation = self.spec[self.animationCounter][0]
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

        elif self.state == 'slash':
            self.combatTuple = createCombatTuple(self.slash[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.slash):
                self.animationCounter = 0
                self.changeBehavior()

        elif self.state == 'air':
            self.combatTuple = createCombatTuple(self.air[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.air):
                self.animationCounter = 0
                self.changeBehavior()
        
        elif self.state == 'spec':
            self.combatTuple = createCombatTuple(self.spec[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.spec):
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