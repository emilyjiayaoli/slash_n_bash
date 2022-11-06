from cmu_112_graphics import *
from player import *
from wind_enemy import *

# https://www.cs.cmu.edu/~112/notes/notes-oop-part1.html#oopExample
# Citation ^ 9. Example: Animation with OOP

def appStarted(app):
    app.player = Player(app)
    app.windLvl1 = WindEnemy(app, 1)

def timerFired(app):
    app.player.timerFired(app)
    app.windLvl1.timerFired(app)

def keyPressed(app, event):
    app.player.keyPressed(app, event)

def keyReleased(app, event):
    app.player.keyReleased(app, event)

def redrawAll(app, canvas):
    app.player.redraw(app, canvas)
    app.windLvl1.redraw(app, canvas)

runApp(width=1920, height=1080)