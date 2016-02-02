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
	# Sprites du heros
	heroDeb = util.load_image("hero.png")
	heroPasG = util.load_image("heroPasG.png")
	heroPasD = util.load_image("heroPasD.png")
	if varOptions[1]==0:
		heroDebA = util.load_image("heroDebAD.png")
		heroPasDA = util.load_image("heroPasDAD.png")
		heroPasGA = util.load_image("heroPasGAD.png")
	else:
		heroDebA = util.load_image("heroDebAG.png")
		heroPasDA = util.load_image("heroPasDAG.png")
		heroPasGA = util.load_image("heroPasGAG.png")
	hero = heroDeb

	timerPas = 0
	marche = 20
	pas=1
	timerBullet=0
	hero_rect = hero.get_rect()
	hero_rect.centerx = 400
	hero_rect.centery = 500

	while jeu==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_ESCAPE]:
			jeu=0

		marche-=1
		timerPas-=1
		if keys[pygame.K_UP] and hero_rect.bottom>350:
			hero_rect = hero_rect.move(0,-(cHero.vitesseDepl))
			marche=5
		if keys[pygame.K_DOWN] and hero_rect.bottom<530:
			hero_rect = hero_rect.move(0,cHero.vitesseDepl)
			marche=5
		if keys[pygame.K_LEFT] and hero_rect.left>5:
			hero_rect = hero_rect.move(-(cHero.vitesseDepl),0)
			marche=5
		if keys[pygame.K_RIGHT] and hero_rect.right<795:
			hero_rect = hero_rect.move(cHero.vitesseDepl,0)
			marche=5

		if keys[pygame.K_SPACE] or varOptions[2]==1:
			if marche>0:
				if pas==1:
					hero = heroPasGA
				else:
					hero = heroPasDA
				if timerPas<=0:
					pas = abs(pas-1)
					timerPas=20
			else:
				 hero = heroDebA
		else:
			if marche>0:
				if pas==1:
					hero = heroPasG
				else:
					hero = heroPasD
				if timerPas<=0:
					pas = abs(pas-1)
					timerPas=20
			else:
				 hero = heroDeb

		screen.blit(background,background_position)
		screen.blit(hero,hero_rect)

		pygame.display.flip()
		screen.blit
		pygame.time.wait(10)
