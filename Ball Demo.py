import pygame, sys, math, random, os
from LevelLoader import *
from Wall import *
from Ball import *
from PlayerBall import *
from Hud import *
from Spawner import *
from Laser import *

pygame.init()
pygame.mixer.init()
if not pygame.font: print('Warning, fonts disabled')

clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode(size)

counter = 0



score = Hud("Score: ", [0, 0])
timer = Hud("Time: ", [900-150, 0])
win = Hud("Congrats! You have beat the game! :D", [150, 700/2])
levName = Hud("Level ", [900/2 - 75, 0])

level = 1

tiles = loadLevel("levels/"+ str(level) + ".lvl")
walls = tiles[0]
spawners = tiles[1]
player = PlayerBall(4, tiles[2])
balls = [player]
lasers = []

end = False

kills = 0
time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("up")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("down")
            PlayerBall.getDir(player)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")
            PlayerBall.getDir(player)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                lasers += [player.shoot()]
    
    #----------Spawn Balls--------------     
    time += 1
    counter += 1
    if counter >= 100:
        counter = 0
        balls += [Ball([random.randint(-7,7), random.randint(-7,7)], 
                    [random.randint(100,750), random.randint(100,600)])
                ]
        for ball in balls:
            if balls[-1].ballCollide(ball):
                balls.remove(balls[-1])
                break
        for wall in walls:
            if balls[-1].wallTileCollide(wall):
                balls.remove(balls[-1])
                break
                
    #----------Updates--------------         
    for ball in balls:
        ball.update(size)
        
    for laser in lasers:
        laser.update(size)
        
    timer.update(int(time/60))
    score.update(kills)
    levName.update(level)
    win.update("")
    
    #----------Collisions-------------- 
    for hittingBall in balls:
        for hitBall in balls:
            if hittingBall.ballCollide(hitBall):
                if hittingBall.kind == "player" and hitBall.kind != "laser":
                    balls.remove(hitBall)
                    kills += 1
                    hitBall.die(hittingBall.kind)
                if hittingBall.kind == "laser" and hitBall.kind != "player":
                    balls.remove(hitBall)
                    hitBall.die(hittingBall.kind)
        for wall in walls:
            hittingBall.wallTileCollide(wall)
            
        for laser in lasers:
            if hittingBall.kind != "player":
                hittingBall.laserCollide(laser)
                laser.collide(hittingBall)
            for wall in walls:
                laser.wallTileCollide(wall)
            
    for spawner in spawners:
        spawner.update(size)
        if spawner.ballCollide(player):
            ball = spawner.spawn()
            if ball != None:
                balls += [ball]
                for ball in balls:
                    if balls[-1].ballCollide(ball):
                        balls.remove(balls[-1])
                        break
                for wall in walls:
                    if balls[-1].wallTileCollide(wall):
                        balls.remove(balls[-1])
                        break
    
    #----------Check end level-------------- 
    if kills > 50:
        level += 1
        maxLevel = len(os.listdir("levels"))
        if level <= maxLevel: 
            tiles = loadLevel("levels/"+ str(level) + ".lvl")
            walls = tiles[0]
            spawners = tiles[1]
            player = PlayerBall(4, tiles[2])
            balls = [player]
            kills = 0
            end = False
        elif level > maxLevel:
            tiles = loadLevel("end.lvl")
            end = True
            

    
                        
    #----------Remove Balls-------------- 
    for ball in balls:
        if ball.living == False:
            balls.remove(ball)
            kills += 2
            
    for laser in lasers:
        if laser.living == False:
            lasers.remove(laser)
    
    #----------Draw-------------- 
    if end == True:
        screen.fill((178, 251, 226))
        screen.blit(win.image, win.rect)
    else:
        screen.fill((250, 175, 225))
        for spawner in spawners:
            screen.blit(spawner.image, spawner.rect)
        for laser in lasers:
            screen.blit(laser.image, laser.rect)
        for ball in balls:
            screen.blit(ball.image, ball.rect)
        for wall in walls:
            screen.blit(wall.image, wall.rect)
        screen.blit(score.image, score.rect)
        screen.blit(timer.image, timer.rect)
        screen.blit(levName.image, levName.rect)
    pygame.display.flip()
    clock.tick(60)
