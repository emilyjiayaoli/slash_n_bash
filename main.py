from cmu_112_graphics import *
from background import *
from player import *
from wind_enemy import *
from earth_enemy import *
from interactions import *
from sound import *

# https://www.cs.cmu.edu/~112/notes/notes-oop-part1.html#oopExample
# Citation ^ 9. Example: Animation with OOP

# Main App
def appStarted(app):
    app.mode = 'startScreen'
    # Start, help, and restart screens 
    app.startScreenImage = app.loadImage('./assets/startScreenSheet.png')
    app.helpImage = app.loadImage('./assets/instructions.png')
    app.overImage = app.loadImage('./assets/restart_screen.png')

    # Sound and music loads
    # https://stackoverflow.com/questions/22227684/pygame-error-mixer-system-not-initialized
    # Not initialized error fix citation
    pygame.mixer.init()
    app.mainMusic = Sound('./assets/audio/backgroundMusic.mp3')
    app.startMusic = Sound('./assets/audio/startAudio.mp3')
    app.endMusic = Sound('./assets/audio/endAudio.mp3')

    app.startMusic.start(loops=-1)

    # Main game load
    app.background = Background(app)
    app.player = Player(app)
    app.windLvl1 = WindEnemy(app, 1)
    app.earthLvl1 = EarthEnemy(app, 1)
    app.timerDelay = 1
    app.currentLevel = 0

# Main Game Logic
def mainGame_timerFired(app):
    app.background.timerFired(app)
    app.player.timerFired(app)

    if app.currentLevel == 0:
        app.windLvl1.timerFired(app)
        if app.player.state != 'death':
            checkInteractions(app.player, app.windLvl1)
    
        if app.windLvl1.callNextLevel == True:
            app.currentLevel += 1
            app.player.hp = app.player.maxHP

    if app.player.callGameOver:
        app.mainMusic.stop()
        app.endMusic.start(loops=-1)
        app.mode = 'gameOver'

def mainGame_keyPressed(app, event):
    app.player.keyPressed(app, event)

def mainGame_redrawAll(app, canvas):
    app.background.redraw(app, canvas)
    app.player.redraw(app, canvas)

    if app.currentLevel == 0:
        app.windLvl1.redraw(app, canvas)

# Start Screen

def startScreen_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
    image=ImageTk.PhotoImage(app.startScreenImage))

def startScreen_keyPressed(app, event):
    if event.key == 'd':
        app.startMusic.stop()
        app.mainMusic.start(loops=-1)
        app.mode = 'mainGame'
    elif event.key == 's':
        app.mode = 'help'

# Help Screen
def help_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
    image=ImageTk.PhotoImage(app.helpImage))

def help_keyPressed(app, event):
    if event.key == 'd':
        app.mode = 'startScreen'

# Restart Screen
def gameOver_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
    image=ImageTk.PhotoImage(app.overImage))

def gameOver_keyPressed(app, event):
    if event.key == 'd':
        app.endMusic.stop()
        app.mainMusic.start(loops=-1)
        app.background = Background(app)
        app.player = Player(app)
        app.windLvl1 = WindEnemy(app, 1)
        app.timerDelay = 1
        app.currentLevel = 0
        app.mode = 'mainGame'

runApp(width=960, height=540)