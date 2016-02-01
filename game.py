import sys
import pygame
import os,inspect

def load_image(name):
    name = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+'/'+name
    image = pygame.image.load(name)
    return image

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

background = load_image("background.png")
background_position = [0,0]

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.blit(background,background_position)

	pygame.display.flip()
	screen.blit

	pygame.time.wait(10)
