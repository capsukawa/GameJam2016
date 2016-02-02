import os
import pygame
import sys
import util
import classes

levelBg = ["bg-araignee.png","bg-chateau.png","bg-chateau.png","bg-chateau.png","bg-plaine.png","bg-plaine.png","bg-grotte.png","bg-grotte.png"]

def play(screen,varOptions):
	jeu = 1

	pygame.init()

	background = util.load_image("background.png")
	background_position = [0,0]

	cHero = classes.Hero()
# Sprites du heros -------------------------------------------------------------------------
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
	hero_rect = hero.get_rect()
	hero_rect.centerx = 400
	hero_rect.centery = 500
# Variables ---------------------------------------------------------------------------------
	timerPas = 0
	marche = 20
	pas=1

	timerTir=0
	bullet = util.load_image("armes/rock.png")
	bullet_rects = []

	vie = util.load_image("vie.png")

	niveauActuel = 0
	bg = util.load_image(levelBg[niveauActuel])
	bg_position = [0,31]
# Boucle du jeu ##############################################
	while jeu==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
# Mise a jour des timers --------------------------------------------------------------------
		marche-=1
		timerPas-=1
		timerTir-=1
# Gestion des touches clavier --------------------------------------------------------------
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			jeu=0
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
			if timerTir<=0:
				timerTir=30*(1/cHero.vitesseTir)
				tb = bullet.get_rect()
				tb.left = (hero_rect.right+hero_rect.left)/2
				tb.top = hero_rect.top-2
				bullet_rects.append(tb)
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
# Gestion une fois mort + Affichage menu etc ---------------------------------------------
		if cHero.vieCourante<=0:
			print("blbl")
# Blit du background + zone de combat ---------------------------------------------------
		screen.blit(background,background_position)
		screen.blit(bg,bg_position)
# Blit des projectiles -----------------------------------------------------------------------
		bullet_vdb = 0
		for i in bullet_rects:
			if i.top<35:
				bullet_rects.pop(bullet_vdb)
			i.top = i.top-10
			screen.blit(bullet,i)
			bullet_vdb+=1
#-------------------------------------------------------------------------------------------
		screen.blit(hero,hero_rect)
# Blit de la barre de vie du heros ----------------------------------------------------------
		for i in range(1,((cHero.vieCourante*50)/cHero.viePleine)+1):
			vie_rect = vie.get_rect()
			vie_rect.centery = 579
			vie_rect.left = 296+i*4
			screen.blit(vie,vie_rect)
#-------------------------------------------------------------------------------------------
		pygame.display.flip()
		screen.blit
		pygame.time.wait(10)
########################################################
