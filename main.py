from cmu_112_graphics import *
from background import *
from player import *
from wind_enemy import *
from interactions import *

# https://www.cs.cmu.edu/~112/notes/notes-oop-part1.html#oopExample
# Citation ^ 9. Example: Animation with OOP

def appStarted(app):
    app.background = Background(app)
    app.player = Player(app)
    app.windLvl1 = WindEnemy(app, 1)
    app.timerDelay = 1
    app.currentLevel = 0

def timerFired(app):
    app.background.timerFired(app)
    app.player.timerFired(app)

    if app.currentLevel == 0:
        app.windLvl1.timerFired(app)
        checkInteractions(app.player, app.windLvl1)
    
        if app.windLvl1.callNextLevel == True:
            app.currentLevel += 1
            app.player.hp = app.player.maxHP

def keyPressed(app, event):
    app.player.keyPressed(app, event)

def redrawAll(app, canvas):
    app.background.redraw(app, canvas)
    app.player.redraw(app, canvas)

    if app.currentLevel == 0:
        app.windLvl1.redraw(app, canvas)

runApp(width=960, height=540)