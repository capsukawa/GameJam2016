import os
import pygame
import sys
import util
import classes

levelBg = ["bg-araignee.png","bg-chateau.png","bg-chateau.png","bg-chateau.png","bg-plaine.png","bg-plaine.png","bg-grotte.png","bg-grotte.png"]

def play(screen,varOptions):
	jeu = 1
	pygame.init()
# Background + Zone ---------------------------------------------------------------------
	background = util.load_sprite("background.png")
	niveauActuel = 0
	bg = util.load_sprite(levelBg[niveauActuel])
	bg.rect = [0,31]
# Creation Classes Boss+Hero ------------------------------------------------------------
	cBoss = classes.Enemy(classes.boss6)
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
# Variables ---------------------------------------------------------------------------------
	timerPas = 0
	marche = 20
	pas=1

	timerTir=0
	bullet_rects = []

	timerMenu = 20

	vie = util.load_sprite("vie.png")
# Boucle du jeu ##############################################
	while jeu==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
# Mise a jour des timers --------------------------------------------------------------------
		marche-=1
		timerPas-=1
		timerTir-=1
		timerMenu-=1
# Gestion des touches clavier --------------------------------------------------------------
		keys = pygame.key.get_pressed()

		if keys[pygame.K_ESCAPE] and timerMenu<=0:
			jeu=0

		if keys[pygame.K_UP] and cHero.sprite.rect.bottom>350:
			cHero.sprite.rect = cHero.sprite.rect.move(0,-(cHero.vitesseDepl))
			marche=5
		if keys[pygame.K_DOWN] and cHero.sprite.rect.bottom<530:
			cHero.sprite.rect = cHero.sprite.rect.move(0,cHero.vitesseDepl)
			marche=5
		if keys[pygame.K_LEFT] and cHero.sprite.rect.left>5:
			cHero.sprite.rect = cHero.sprite.rect.move(-(cHero.vitesseDepl),0)
			marche=5
		if keys[pygame.K_RIGHT] and cHero.sprite.rect.right<795:
			cHero.sprite.rect = cHero.sprite.rect.move(cHero.vitesseDepl,0)
			marche=5

		if keys[pygame.K_SPACE] or varOptions[2]==1:
			if timerTir<=0:
				timerTir=30*(1/cHero.vitesseTir)
				tb = util.load_sprite("armes/rock.png")
				tb.rect.left = (cHero.sprite.rect.right+cHero.sprite.rect.left)/2
				tb.rect.top = cHero.sprite.rect.top-2
				bullet_rects.append(tb)
			if marche>0:
				if pas==1:
					cHero.sprite.image = heroPasGA
				else:
					cHero.sprite.image = heroPasDA
				if timerPas<=0:
					pas = abs(pas-1)
					timerPas=20
			else:
				 cHero.sprite.image = heroDebA
		else:
			if marche>0:
				if pas==1:
					cHero.sprite.image = heroPasG
				else:
					cHero.sprite.image = heroPasD
				if timerPas<=0:
					pas = abs(pas-1)
					timerPas=20
			else:
				 cHero.sprite.image = heroDeb
# Gestion une fois mort + Affichage menu etc ---------------------------------------------
		if keys[pygame.K_y]: # A VIRER DES QUE FINI
			cHero.vieCourante-=1


		if cHero.vieCourante<=0:
			cHero = util.upgrades(screen,cHero)
			if cHero.vieCourante<=0:
				jeu=0
			else:
				timerMenu=50
# Blit du background + zone de combat ---------------------------------------------------
		screen.blit(background.image,background.rect)
		screen.blit(bg.image,bg.rect)
# Blit des projectiles -----------------------------------------------------------------------
		bullet_vdb = 0
		for i in bullet_rects:
			if i.rect.top<35:
				bullet_rects.pop(bullet_vdb)
			if pygame.sprite.collide_mask(cBoss.sprite,i):
				cBoss.vieCourante-=cHero.puissance
				bullet_rects.pop(bullet_vdb)
			i.rect.top = i.rect.top-10
			screen.blit(i.image,i.rect)
			bullet_vdb+=1
#-------------------------------------------------------------------------------------------
		screen.blit(cHero.sprite.image,cHero.sprite.rect)
		screen.blit(cBoss.sprite.image,cBoss.sprite.rect)
# Blit de la barre de vie du heros ----------------------------------------------------------
		for i in range(1,((cHero.vieCourante*50)/cHero.viePleine)+1):
			vie.rect.centery = 579
			vie.rect.left = 296+i*4
			screen.blit(vie.image,vie.rect)
# Blit de la barre de vie du boss -----------------------------------------------------------
		for i in range(1,((cBoss.vieCourante*125)/cBoss.viePleine)+1):
			vie.rect.centery = 15
			vie.rect.left = 284+i*4
			screen.blit(vie.image,vie.rect)
#-------------------------------------------------------------------------------------------
		pygame.display.flip()
		screen.blit
		pygame.time.wait(10)
########################################################
