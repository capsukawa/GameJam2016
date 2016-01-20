import sys
import pygame
import os
import inspect

pygame.init()

background_image = pygame.image.load(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"/tutos/les_evenements/background.jpg")
background_position = [0, 0]

os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
    screen.blit(background_image, background_position)
    pygame.display.flip()
    screen.blit
    pygame.time.wait(10)
