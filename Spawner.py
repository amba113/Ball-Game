import pygame, sys, math, random
from Ball import *

class Spawner():
    def __init__(self, pos = [25,25]):
        self.image = pygame.image.load("Images/tiles/Spawner.png")
        self.rect = self.image.get_rect(center = pos)
        
        self.spawnerSound = pygame.mixer.Sound("Sounds/Spawn.wav")
        
        self.counter = 0
        self.counterMax = 60*3
        
        self.kind = "spawner"
        
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            return True
        return False
        
    def spawn(self):
        if self.counter == 0:
            self.counter += 1
            self.spawnerSound.play()
            return Ball([random.randint(-7,7), random.randint(-7,7)], 
                        [random.randint(100,750), random.randint(100,600)])
                    
        
    def update(self, size):
        if self.counter > 0:
            self.counter += 1
            if self.counter > self.counterMax:
                self.counter = 0
