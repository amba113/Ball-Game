import pygame, sys, math
from Wall import *
from Spawner import *
from PlayerBall import *

def loadLevel(lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()
    
    size = 50
    offset = size/2
    tiles = []
    walls = []
    spawners = []
    playerLoc = []
    
    newLines = []
    for line in lines:
        newLine = ""
        for c in line:
            if c != "\n":
                newLine += c
        newLines += [newLine]
    lines = newLines
    
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                walls += [Wall([x*size + offset, y*size + offset])]
            if c == "X":
                spawners += [Spawner([x*size + offset, y*size + offset])]
            if c == "$":
                playerLoc = [x*size + offset, y*size + offset]
                
    tiles = [walls, 
             spawners,
             playerLoc]
    return tiles
    
# ~ loadLevel("levels/1.lvl")
