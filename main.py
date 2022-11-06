from cmu_112_graphics import *
from background import *
from player import *
from wind_enemy import *
from earth_enemy import *
from water_enemy import *
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
    app.winImage = app.loadImage('./assets/winScreen.png')

    # Sound and music loads
    # https://stackoverflow.com/questions/22227684/pygame-error-mixer-system-not-initialized
    # Not initialized error fix citation
    pygame.mixer.init()
    # https://xdeviruchi.itch.io/8-bit-fantasy-adventure-music-pack
    app.mainMusic = Sound('./assets/audio/backgroundMusic.mp3')
    app.startMusic = Sound('./assets/audio/startAudio.mp3')
    app.endMusic = Sound('./assets/audio/endAudio.mp3')

    app.startMusic.start(loops=-1)

    # Main game load
    app.background = Background(app)
    app.player = Player(app)
    app.windLvl1 = WindEnemy(app, 1)
    app.earthLvl1 = EarthEnemy(app, 1)
    app.waterLvl1 = WaterEnemy(app, 1)

    app.windLvl2 = WindEnemy(app, 2)
    app.earthLvl2 = EarthEnemy(app, 2)
    app.waterLvl2 = WaterEnemy(app, 2)

    app.windLvl3 = WindEnemy(app, 3)
    app.earthLvl3 = EarthEnemy(app, 3)
    app.waterLvl3 = WaterEnemy(app, 3)

    app.windEnemies = [app.windLvl1, app.windLvl2, app.windLvl3]
    app.earthEnemies = [app.earthLvl1, app.earthLvl2, app.earthLvl3]
    app.waterEnemies = [app.waterLvl1, app.waterLvl2, app.waterLvl3]

    app.timerDelay = 1
    app.currentLevel = 0

# Main Game Logic
def mainGame_timerFired(app):
    app.background.timerFired(app)
    app.player.timerFired(app)

    if app.currentLevel in [0, 3, 6]:
        i = (app.currentLevel)//3
        app.windEnemies[i].timerFired(app)
        if app.player.state != 'death':
            checkInteractions(app.player, app.windEnemies[i])
    
        if app.windEnemies[i].callNextLevel == True:
            app.currentLevel += 1
            app.player.hp = app.player.maxHP
            app.background.transition(app)
            app.player.state = 'walk'
    
    elif app.currentLevel in [1, 4, 7]:
        i = (app.currentLevel)//3
        app.earthEnemies[i].timerFired(app)
        if app.player.state != 'death':
            checkInteractions(app.player, app.earthEnemies[i])
    
        if app.earthEnemies[i].callNextLevel == True:
            app.currentLevel += 1
            app.player.hp = app.player.maxHP
            app.background.transition(app)
            app.player.state = 'walk'

    elif app.currentLevel in [2, 5, 8]:
        i = (app.currentLevel)//3
        app.waterEnemies[i].timerFired(app)
        if app.player.state != 'death':
            checkInteractions(app.player, app.waterEnemies[i])
    
        if app.waterEnemies[i].callNextLevel == True:
            app.currentLevel += 1
            app.player.hp = app.player.maxHP
            app.background.transition(app)
            app.player.state = 'walk'

    elif app.currentLevel >= 9:
        app.mode = 'win'

    if app.player.callGameOver:
        app.mainMusic.stop()
        app.endMusic.start(loops=-1)
        app.mode = 'gameOver'

def mainGame_keyPressed(app, event):
    app.player.keyPressed(app, event)

def mainGame_redrawAll(app, canvas):
    app.background.redraw(app, canvas)
    app.player.redraw(app, canvas)

    if app.currentLevel in [0, 3, 6]:
        i = app.currentLevel // 3
        app.windEnemies[i].redraw(app, canvas)
    elif app.currentLevel in [1, 4, 7]:
        i = app.currentLevel // 3
        app.earthEnemies[i].redraw(app, canvas)
    elif app.currentLevel in [2, 5, 8]:
        i = app.currentLevel // 3
        app.waterEnemies[i].redraw(app, canvas)
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
        app.earthLvl1 = EarthEnemy(app, 1)
        app.waterLvl1 = WaterEnemy(app, 1)

        app.windLvl2 = WindEnemy(app, 2)
        app.earthLvl2 = EarthEnemy(app, 2)
        app.waterLvl2 = WaterEnemy(app, 2)

        app.windLvl3 = WindEnemy(app, 3)
        app.earthLvl3 = EarthEnemy(app, 3)
        app.waterLvl3 = WaterEnemy(app, 3)

        app.windEnemies = [app.windLvl1, app.windLvl2, app.windLvl3]
        app.earthEnemies = [app.earthLvl1, app.earthLvl2, app.earthLvl3]
        app.waterEnemies = [app.waterLvl1, app.waterLvl2, app.waterLvl3]

        app.timerDelay = 1
        app.currentLevel = 0
        app.mode = 'mainGame'


# Win Screen
def win_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
    image=ImageTk.PhotoImage(app.winImage))

def win_keyPressed(app, event):
    if event.key == 'd':
        app.endMusic.stop()
        app.mainMusic.start(loops=-1)
        app.background = Background(app)
        app.player = Player(app)
        app.windLvl1 = WindEnemy(app, 1)
        app.earthLvl1 = EarthEnemy(app, 1)
        app.waterLvl1 = WaterEnemy(app, 1)

        app.windLvl2 = WindEnemy(app, 2)
        app.earthLvl2 = EarthEnemy(app, 2)
        app.waterLvl2 = WaterEnemy(app, 2)

        app.windLvl3 = WindEnemy(app, 3)
        app.earthLvl3 = EarthEnemy(app, 3)
        app.waterLvl3 = WaterEnemy(app, 3)

        app.windEnemies = [app.windLvl1, app.windLvl2, app.windLvl3]
        app.earthEnemies = [app.earthLvl1, app.earthLvl2, app.earthLvl3]
        app.waterEnemies = [app.waterLvl1, app.waterLvl2, app.waterLvl3]

        app.timerDelay = 1
        app.currentLevel = 0
        app.mode = 'mainGame'


runApp(width=960, height=540)
