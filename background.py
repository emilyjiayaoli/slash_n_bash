from cmu_112_graphics import *
from helpers import *

class Background:
    def __init__(self, app):
        self.image = app.loadImage('./assets/forest_background.png')
        self.image = app.scaleImage(self.image, 1/2)
        self.imgWidth, self.imgHeight = self.image.size
        self.boolScroll = False
        self.scrollingCount = 0
        self.scrollProg = 0
        self.scrollAmt = 0

    def transition(self, app):
        self.boolScroll = True

    def scroll(self, app):
        self.scrollProg += .01
        self.scrollAmt = self.scrollProg*app.width
        if self.scrollProg >= 1:
            self.scrollProg -= 1

    def timerFired(self, app):
        if self.boolScroll and self.scrollingCount < 40:
            self.scroll(app)
            self.scrollingCount += 1
        elif self.scrollingCount >= 40:
            self.boolScroll = False
            self.scrollingCount = 0

    def redraw(self, app, canvas):
        canvas.create_image(0 - self.scrollAmt,0,image=ImageTk.PhotoImage(self.image), 
        anchor = 'nw')
        canvas.create_image(app.width - self.scrollAmt,0,
        image=ImageTk.PhotoImage(self.image), anchor = 'nw')