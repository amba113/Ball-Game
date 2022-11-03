import pygame, sys, math
from Ball import *
from Laser import *

class PlayerBall(Ball):
    def __init__(self, maxSpeed = 4, startPos = [0,0]):
        Ball.__init__(self, [0,0], startPos)
        scale = [100, 100]
        self.images0 = [pygame.transform.scale(pygame.image.load("Images/Player Ball/playerBall-0.png"), scale)]
        self.images45 = [pygame.transform.scale(pygame.image.load("Images/Player Ball/playerBall-45.png"), scale)]
        self.images90 = [pygame.transform.scale(pygame.image.load("Images/Player Ball/playerBall-90.png"), scale)]
        self.images135 = [pygame.transform.scale(pygame.image.load("Images/Player Ball/playerBall-135.png"), scale)]
        self.images180 = [pygame.transform.scale(pygame.image.load("Images/Player Ball/playerBall-180.png"), scale)]
        self.images225 = [pygame.transform.scale(pygame.image.load("Images/Player Ball/playerBall-225.png"), scale)]
        self.images270 = [pygame.transform.scale(pygame.image.load("Images/Player Ball/playerBall-270.png"), scale)]
        self.images315 = [pygame.transform.scale(pygame.image.load("Images/Player Ball/playerBall-315.png"), scale)]
        self.imagesStop = [pygame.transform.scale(pygame.image.load("Images/Player Ball/playerBall-stop.png"), scale)]

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
     
    def shoot(self):
        speed = [0,0]
        if self.speedx > 0:
            speed[0] = 8
            if self.speedy > 0:
                speed[1] = 8
            elif self.speedy < 0:
                speed[1] = -8
            elif self.speedy == 0:
                speed[1] = 0
        elif self.speedx < 0:
            speed[0] = -8
            if self.speedy > 0:
                speed[1] = 8
            elif self.speedy < 0:
                speed[1] = -8
            elif self.speedy == 0:
                speed[1] = 0
        elif self.speedx == 0:
            speed[0] = 0
            if self.speedy > 0:
                speed[1] = 8
            elif self.speedy < 0:
                speed[1] = -8
            else:
                while speed == [0, 0]:
                    speed[0] = random.randint(-1, 1) * 8
                    speed[1] = random.randint(-1, 1) * 8
                    
        return Laser(speed, self.rect.center)
                
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
                        xDist = abs(self.rect.centerx - other.rect.centerx)
                        yDist = abs(self.rect.centery - other.rect.centery)
                        self.move()
                        if xDist < yDist:
                            self.speedx = 0
                            self.speedy = -self.speedy
                        if yDist < xDist:
                            self.speedx = -self.speedx
                            self.speedy = 0
                        return True
        return False
