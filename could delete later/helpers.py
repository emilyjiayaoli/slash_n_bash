from cmu_112_graphics import *

def cutSpritesheet(startX, adjW, w, startY, endY, spritesheet, app):
    animation = spritesheet.crop((startX+adjW, startY, (w-startX)+adjW, endY))
    return app.scaleImage(animation, (((7/8)*app.height)//128))

def cutWindEnemySheet(startX, adjW, w, startY, endY, spritesheet, app):
    animation = spritesheet.crop((startX+adjW, startY, (w-startX)+adjW, endY))
    # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#flipImage
    # Using transpose to flip an image
    animation = animation.transpose(Image.FLIP_LEFT_RIGHT)
    return app.scaleImage(animation, ((1.2*app.height)//128))

def getYs(row):
    return (128*row, 128*(row+1))