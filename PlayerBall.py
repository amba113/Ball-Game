import pygame, sys, math
from Ball import *

class PlayerBall(Ball):
    def __init__(self, maxSpeed = 4, startPos = [0,0]):
        Ball.__init__(self, [0,0], startPos)
        self.images0 = [pygame.image.load("Images/Player Ball/playerBall-0.png")]
        self.images45 = [pygame.image.load("Images/Player Ball/playerBall-45.png")]
        self.images90 = [pygame.image.load("Images/Player Ball/playerBall-90.png")]
        self.images135 = [pygame.image.load("Images/Player Ball/playerBall-135.png")]
        self.images180 = [pygame.image.load("Images/Player Ball/playerBall-180.png")]
        self.images225 = [pygame.image.load("Images/Player Ball/playerBall-225.png")]
        self.images270 = [pygame.image.load("Images/Player Ball/playerBall-270.png")]
        self.images315 = [pygame.image.load("Images/Player Ball/playerBall-315.png")]
        self.imagesStop = [pygame.image.load("Images/Player Ball/playerBall-stop.png")]

        self.images = self.imagesStop
        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.maxSpeed = maxSpeed
        self.kind = "player"

    def getDir(self):
        if self.speedx > 0:
            if self.speedy > 0:
                self.images = self.images135
            elif self.speedy < 0:
                self.images = self.images45
            else:
                self.images = self.images90
        elif self.speedx < 0:
            if self.speedy > 0:
                self.images = self.images225
            elif self.speedy < 0:
                self.images = self.images315
            else:
                self.images = self.images270
        else:
            if self.speedy > 0:
                self.images = self.images180
            elif self.speedy < 0:
                self.images = self.images0
            else:
                self.images = self.imagesStop

    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "up":
            self.speedy = -self.maxSpeed
        elif direction == "down":
            self.speedy = self.maxSpeed
        elif direction == "sleft":
            if self.speedx < 0:
                self.speedx = 0
        elif direction == "sright":
            if self.speedx > 0:
                self.speedx = 0
        elif direction == "sup":
            if self.speedy < 0:
                self.speedy = 0
        elif direction == "sdown":
            if self.speedy > 0:
                self.speedy = 0
            
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
                self.didBounceY = True
            if self.rect.top < 0:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
                self.didBounceY = True
        if not self.didBounceX:
            if self.rect.right > width:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True
            if self.rect.left < 0:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True
            
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False
    
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.speedx = -self.speedx
                        self.speedy = -self.speedy
                        self.move()
                        self.speedx = 0
                        self.speedy = 0
                        return True
        return False
