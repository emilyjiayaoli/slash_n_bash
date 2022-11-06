# Citation: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
# #playingSoundsWithPygame
import pygame

class Sound(object):
    def __init__(self, path):
        self.path = path
        self.loops = 1
        self.Sound = pygame.mixer.Sound(path)

    # Returns True if the sound is currently playing
    def isPlaying(self):
        return bool(pygame.mixer.music.get_busy())

    # Loops = number of times to loop the sound.
    # If loops = 1 or 1, play it once.
    # If loops > 1, play it loops + 1 times.
    # If loops = -1, loop forever.
    def start(self, loops=1):
        self.loops = loops
        self.Sound.play(loops=loops)
        # pygame.mixer.music.play(loops=loops)

    # Stops the current sound from playing
    def stop(self):
        self.Sound.fadeout(2000)
