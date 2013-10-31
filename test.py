import pygame, sys
from pygame.locals import *

WINDOWSURF = pygame.display.set_mode((400,300),0, 32)
pygame.display.set_caption('hello world')
WHITE = (255, 255, 255)
BLACK = (0,0,0)
pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
speed = 10
direction = 'right'

if __name__ == '__main__':

    while True:
        WINDOWSURF.fill(BLACK)
        if direction == 'right':
            catx += speed
            if catx >= 280:
                direction = 'down'
        if direction == 'down':
            caty += speed
            if caty >= 220:
                direction = 'left'
        if direction == 'left':
            catx -= speed
            if catx <= 10:
                direction = 'up'
        if direction == 'up':
            caty -= speed
            if caty <= 10:
                direction = 'right'
        for msg in pygame.event.get():
            if msg == QUIT:
                pygame.quit()
                sys.exit()
        WINDOWSURF.blit(catImg, (catx, caty))
        pygame.display.update()
        fpsClock.tick(FPS)
