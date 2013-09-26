import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('hello')

WHITE = (255,255,255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
FPS = 3
fpsClock = pygame.time.Clock()


fontObj = pygame.font.Font('freesansbold.ttf',32)
textSurfaceObj = fontObj.render('Hello ugly world', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
while True:
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	print textRectObj
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(FPS)
