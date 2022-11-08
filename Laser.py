import pygame, sys, math, random
from Ball import *

class Laser():
    def __init__(self, speed, startPos = [0,0]):
                
        self.imagesVertical = [pygame.transform.scale(pygame.image.load("Images/Laser/LaserVert.png"), scale)]
        self.imagesHorizontal = [pygame.transform.scale(pygame.image.load("Images/Laser/LaserHori.png"), scale)]
        self.imagesPosSlope = [pygame.transform.scale(pygame.image.load("Images/Laser/LaserInc.png"), scale)]
        self.imagesNegSlope = [pygame.transform.scale(pygame.image.load("Images/Laser/LaserDec.png"), scale)]
        
        self.image = self.imagesLaserVertical[0]

        self.kind = "laser"
        
        self.rect = self.image.get_rect(center = startPos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.living = True
        
        self.laserSound = pygame.mixer.Sound("Sounds/LaserShot.wav")
        
        self.laserSound.play()
        
        self.counter = 0
        self.counterMax = 60*3
        
        
    def update(self, size):
        self.move()
        
        self.didBounceX = False
        self.didBounceY = False
             
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.living = False
                        speed = [0, 0]
                        return True
        return False
        
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.living = False
                        speed = [0, 0]
                        return True
        return False
        
    def getDir(self):
        if self.speedx > 0:
            if self.speedy > 0:
                self.images = self.imagesNegSlope
            elif self.speedy < 0:
                self.images = self.imagesPosSlope
            else:
                self.images = self.imagesHorizontal
        elif self.speedx < 0:
            if self.speedy > 0:
                self.images = self.imagesPosSlope
            elif self.speedy < 0:
                self.images = self.imagesNegSlope
            else:
                self.images = self.imagesHorizontal
        else:
            self.images = self.imagesVertical
