from cmu_112_graphics import *
from helpers import *
from sound import *
# getYs and cutSpritesheet from helpers.py 

# https://www.cs.cmu.edu/~112/notes/notes-oop-part1.html#oopExample
# Citation ^ 9. Example: Animation with OOPclass Enemy
 
class EarthEnemy:
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
 
            self.behavior = ['idle', 'kick', 'block', 'punch', 'idle', 'kick',
            'punch', 'punch', 'idle', 'block', 'combo']
            self.behaviorIndex = 0
            self.combatTuple = (0, 0, 'vulnerable')
            spritesheet = app.loadImage('./assets/earthSheet.png')
            self.icon = app.loadImage('./assets/ground_monk.png')
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
 
            self.behavior = ['block','block','idle','block','punch', 'kick', 
            'block', 'punch', 'idle', 'kick',
            'punch', 'punch', 'idle', 'block', 'combo']
            self.behaviorIndex = 0
            self.combatTuple = (0, 0, 'vulnerable')
            spritesheet = app.loadImage('./assets/earthSheet.png')
            self.icon = app.loadImage('./assets/ground_monk.png')
            xWidth = 288
            startX = 0
 
            self.deathSound = Sound('./assets/audio/deathAudio.mp3')
 
        if level == 3:
            self.hp = 200
            self.maxHP = 200  
            self.state = 'walk'
            self.walkX = 0
            self.moveDeath = 0
            self.timeAfterDeath = 0
            self.callNextLevel = False
 
            self.behavior = ['block','block','block','block','punch', 'kick', 
            'block', 'punch', 'idle', 'kick',
            'punch', 'punch', 'idle', 'block', 'combo','block','idle','idle']
            self.behaviorIndex = 0
            self.combatTuple = (0, 0, 'vulnerable')
            spritesheet = app.loadImage('./assets/earthSheet.png')
            self.icon = app.loadImage('./assets/ground_monk.png')
            xWidth = 288
            startX = 0
 
            self.deathSound = Sound('./assets/audio/deathAudio.mp3')
 
        # Load idle animation
        self.idle = []
        for i in range(6):
            (startY, endY) = getYs(0)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.idle.append((img, dmg, blockEff, vulnerability))

        # Load walk
        self.walk = []
        for i in range(7):
            (startY, endY) = getYs(1)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.walk.append((img, dmg, blockEff, vulnerability))

        # Load kick attack
        self.kick = []
        for i in range(6):
            (startY, endY) = getYs(4)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i in [0,2]:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            elif i == 3:
                (img, dmg, blockEff, vulnerability) = (animation, 15, 0, 
                'vulnerable')
            elif i == 4:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 1, 
                'invulnerable')
            elif i == 5:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.kick.append((img, dmg, blockEff, vulnerability))

        # Load combo attack
        self.combo = []
        for i in range(22):
            (startY, endY) = getYs(7)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i in [0,1,7,9,10,11,12,13,14,15,22]:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            elif i == 2:
                (img, dmg, blockEff, vulnerability) = (animation, 4, 0, 
                'vulnerable')
            elif i in [4, 5]:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 1, 
                'invulnerable')
            elif i == 6:
                (img, dmg, blockEff, vulnerability) = (animation, 4, 0, 
                'vulnerable')
            elif i in range(16, 22):
                (img, dmg, blockEff, vulnerability) = (animation, 5, 0, 
                'invulnerable')   

            self.combo.append((img, dmg, blockEff, vulnerability))

        # Load punch attack
        self.punch = []
        for i in range(5):
            (startY, endY) = getYs(5)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i not in [1, 2]:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            elif i in [1, 2]:
                (img, dmg, blockEff, vulnerability) = (animation, 5, 0, 
                'vulnerable')
            self.punch.append((img, dmg, blockEff, vulnerability))

        # Load death
        self.death = []
        for i in range(17):
            (startY, endY) = getYs(13)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'invulnerable')
            self.death.append((img, dmg, blockEff, vulnerability)) 

        # Load hit
        self.hit = []
        for i in range(5):
            (startY, endY) = getYs(12)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i < 4:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'invulnerable')
            else:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            self.hit.append((img, dmg, blockEff, vulnerability)) 

        # Load block
        self.block = []
        for i in range(12):
            (startY, endY) = getYs(11)
            animation = cutEnemySheet(startX, xWidth*i, xWidth, startY, 
            endY, spritesheet, app)
            if i in [0, 1, 10, 11]:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 0, 
                'vulnerable')
            else:
                (img, dmg, blockEff, vulnerability) = (animation, 0, 1, 
                'counterhit') 
            self.block.append((img, dmg, blockEff, vulnerability)) 


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
        if self.state == 'kick':
            animation = self.kick[self.animationCounter][0]
        elif self.state == 'punch':
            animation = self.punch[self.animationCounter][0]
        elif self.state == 'combo':
            animation = self.combo[self.animationCounter][0]
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
            canvas.create_image(app.width - self.walkX, app.height//8, 
            image=ImageTk.PhotoImage(animation))
        else:
            canvas.create_image(app.width//2 + app.width//9 - self.moveDeath, 
            app.height//8, image=ImageTk.PhotoImage(animation))
 
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

        elif self.state == 'punch':
            self.combatTuple = createCombatTuple(self.punch[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.punch):
                self.animationCounter = 0
                self.changeBehavior()

        elif self.state == 'kick':
            self.combatTuple = createCombatTuple(self.kick[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.kick):
                self.animationCounter = 0
                self.changeBehavior()

        elif self.state == 'combo':
            self.combatTuple = createCombatTuple(self.combo[self.animationCounter])
            self.animationCounter = (1 + self.animationCounter)

            if self.animationCounter >= len(self.combo):
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