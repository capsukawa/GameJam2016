import os
import pygame
import sys
import util

def play(screen):
	jeu = 1

	pygame.init()

	background = util.load_image("background.png")
	background_position = [0,0]

	while jeu==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_ESCAPE]:
			jeu=0

		screen.blit(background,background_position)

		pygame.display.flip()
		screen.blit
		pygame.time.wait(10)
