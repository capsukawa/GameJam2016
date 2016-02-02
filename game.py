import os
import pygame
import sys
import util
import classes

def play(screen,varOptions):
	jeu = 1

	pygame.init()

	background = util.load_image("background.png")
	background_position = [0,0]

	cHero = classes.Hero()
	hero = util.load_image("hero.png")
	hero_rect = hero.get_rect()
	hero_rect.centerx = 400
	hero_rect.centery = 300

	while jeu==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_ESCAPE]:
			jeu=0

		screen.blit(background,background_position)
		screen.blit(hero,hero_rect)

		pygame.display.flip()
		screen.blit
		pygame.time.wait(10)
