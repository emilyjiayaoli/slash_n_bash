from cmu_112_graphics import *
import decimal

#copied from 15-112 hw9
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#!change n to change how fast the screen moves
def rotateList(L, n=2):
    return L[n:] + L[0:n]

def resizeBckg(app):
    app.bckgImage = app.loadImage('./assets/forest_background.png')
    imgWidth, imgHeight = app.bckgImage.size
    app.scaledBckgImage = app.scaleImage(app.bckgImage, app.width/imgWidth, app.height/imgHeight)

def slicingBckg(app):
    if app.paused == False:
        app.bckgSlices = []
        
        #!100 to be changed later
        for i in range(100):
            bckgSlice = app.scaledBckgImage.crop((i*roundHalfUp(app.width/100), 0, (i+1)*roundHalfUp(app.width/100), app.height))
            app.bckgSlices.append(bckgSlice)

def appStarted(app):
    app.paused = False
    resizeBckg(app)
    slicingBckg(app)

def keyPressed(app, event):
    if event.key == 'p':
        app.paused = not app.paused

def timerFired(app):
    resizeBckg(app)
    if app.paused == False:
        app.bckgSlices = rotateList(app.bckgSlices)
    
def redrawAll(app, canvas):
    
    for i in range(100):
        canvas.create_image(i*(roundHalfUp(app.width/100)), 0, image=ImageTk.PhotoImage(app.bckgSlices[i]), anchor = 'nw')

runApp(width=800, height=450) #16:9