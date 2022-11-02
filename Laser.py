import pygame, sys, math, random
from Ball import *

class Laser(Ball):
    def __init__(self, speed, startPos = [0,0]):
        Ball.__init__(self, [0,0], startPos)
        
        self.imagesLaser1 = [pygame.image.load("Images\Laser\Laser1.png")]
        
        self.image = self.imagesLaser1[0]

        self.kind = "laser"
        
        self.rect = self.rect.move(speed)
        self.living = True
        
        self.laserSound = pygame.mixer.Sound("Sounds/LaserShot.wav")
        
        self.laserSound.play()
        
    def collision(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.living = False
                        return True
        return False
