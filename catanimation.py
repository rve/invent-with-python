import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400,300),0, 32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255,255)
catImg = pygame.image.load('cat.png')
catx=10
caty=10
direction = 'right'
speed = 10

while True:
	DISPLAYSURF.fill(WHITE)

	if direction == 'right':
		catx += speed
		if catx == 280:
			direction = 'down'
	elif direction == 'down':
		caty += speed
		if caty == 220:
			direction = 'left'
	elif direction == 'left':
		catx -= speed
		if catx == 10:
			direction = 'up'
	elif direction == 'up':
		caty -= speed
		if caty == 10:
			direction = 'right'
	DISPLAYSURF.blit(catImg, (catx, caty))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)
