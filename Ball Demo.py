import pygame, sys, math, random
from Ball import *
from PlayerBall import *

pygame.init()
clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode(size)




counter = 0

player = PlayerBall(4, [900/2, 700/2])
balls = [player]

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
            
    counter += 1
    if counter >= 10:
        counter = 0
        balls += [Ball([random.randint(-7,7), random.randint(-7,7)], 
                    [random.randint(100,750), random.randint(100,600)])
                ]
        for ball in balls:
            if balls[-1].ballCollide(ball):
                balls.remove(balls[-1])
                break
            
    for ball in balls:
        ball.update(size)
    
    for hittingBall in balls:
        for hitBall in balls:
            if hittingBall.ballCollide(hitBall):
                if hittingBall.kind == "player":
                    balls.remove(hitBall)
        

    screen.fill((250, 175, 225))
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    clock.tick(60)
    # ~ print(clock.get_fps())
