import os
import pygame
import sys
import util
import classes
import random

levelBg = ["bg-araignee.png","bg-chateau.png","bg-chateau.png","bg-chateau.png","bg-plaine.png","bg-plaine.png","bg-grotte.png","bg-grotte.png","bg-grotte.png"]
projectiles = ["projectile_boss/toile.png","projectile_boss/dent.png","projectile_boss/feu.png","projectile_boss/os.png","projectile_boss/massue.png","projectile_boss/feu_blue.png","projectile_boss/sang.png","projectile_boss/feu.png","projectile_boss/feu.png"]
mobSpawnTime = [50,40,30,20,10,5,5,4,3]
tabVitesseTir = [0,70,65,60,55,50,45,40,30,25,20]

def play(screen,varOptions):
	jeu = 1
	pygame.init()
# Background + Zone ---------------------------------------------------------------------
	background = util.load_sprite("background.png")
	niveauActuel = 0
	bg = util.load_sprite(levelBg[niveauActuel])
	bg.rect = [0,31]
# Creation Classes Boss+Hero ------------------------------------------------------------
	cBoss = classes.Enemy(classes.bosses[niveauActuel])
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

	timerMobSpawn = 50
	mob_rects = []

	timerBossAttack = 50
	EnemyBullets_rects = []

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
		timerMobSpawn-=1
		timerBossAttack-=1
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
				timerTir=tabVitesseTir[cHero.vitesseTir]
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
# Spawn des mobs ------------------------------------------------------------------------
		if timerMobSpawn<=0:
			tm = classes.Enemy(classes.mobs[niveauActuel])
			tm.sprite.rect.centery = 31+(tm.sprite.rect.height/2)
			tm.sprite.rect.centerx = random.randint(50,750)
			mob_rects.append(tm)
			timerMobSpawn = mobSpawnTime[niveauActuel]
# Gestion une fois mort + Affichage menu etc ---------------------------------------------
		if keys[pygame.K_y]: # A VIRER DES QUE FINI
			cHero.vieCourante-=1


		if cHero.vieCourante<=0:
			cHero = util.upgrades(screen,cHero)
			if cHero.vieCourante<=0:
				jeu=0
			else:
				timerMenu=50
				niveauActuel=0
				cBoss = classes.Enemy(classes.bosses[niveauActuel])
				bg =  util.load_sprite(levelBg[niveauActuel])
				bg.rect = [0,31]
				mob_rects = []
				EnemyBullets_rects = []
# Gestion si boss mort ---------------------------------------------------------------------
		if cBoss.vieCourante<=0:
			niveauActuel+=1
			cHero.gold+=cBoss.argent
			bg = util.load_sprite(levelBg[niveauActuel])
			bg.rect = [0,31]
			cBoss = classes.Enemy(classes.bosses[niveauActuel])
			mob_rects = []
			EnemyBullets_rects = []
# Gestion des projectiles boss -------------------------------------------------------------
		if timerBossAttack<=0:
			if niveauActuel==0:
				EnemyBullets_rects.append(classes.Projectile(projectiles[niveauActuel],(cBoss.sprite.rect.left+230),(cBoss.sprite.rect.top+200),(cBoss.sprite.rect.left+130),600,1))
				EnemyBullets_rects.append(classes.Projectile(projectiles[niveauActuel],(cBoss.sprite.rect.left+250),(cBoss.sprite.rect.top+200),(cBoss.sprite.rect.left+350),600,1))
				timerBossAttack=200
# Blit du background + zone de combat ---------------------------------------------------
		screen.blit(background.image,background.rect)
		screen.blit(bg.image,bg.rect)
# Blit des projectiles boss -----------------------------------------------------------------
		ebullet_vdb = 0
		for i in EnemyBullets_rects:
			if i.sprite.rect.bottom>536 or i.sprite.rect.left>800 or i.sprite.rect.right<0:
				EnemyBullets_rects.pop(ebullet_vdb)
			if pygame.sprite.collide_mask(cHero.sprite,i.sprite):
				cHero.vieCourante-=cBoss.puissance
				EnemyBullets_rects.pop(ebullet_vdb)
			else:
				bullet_vdb = 0
				for u in bullet_rects:
					if pygame.sprite.collide_mask(u,i.sprite):
						bullet_rects.pop(bullet_vdb)
						EnemyBullets_rects.pop(ebullet_vdb)
					bullet_vdb+=1
				if i.x2==0 and i.y2==0: #Si tir autoguide
					i.x2 = cHero.sprite.rect.centerx
					i.y2 = cHero.sprite.rect.centery

				steps_number = max( abs(i.sprite.rect.centerx-i.x2), abs(i.sprite.rect.centery-i.y2) )

				stepx = float(i.x2-i.sprite.rect.centerx)/steps_number
				stepy = float(i.y2-i.sprite.rect.centery)/steps_number

				i.sprite.rect = i.sprite.rect.move(stepx,stepy)

				if i.x2==cHero.sprite.rect.centerx and i.y2==cHero.sprite.rect.centery:
					i.x2=0
					i.y2=0
				screen.blit(i.sprite.image,i.sprite.rect)
			ebullet_vdb+=1

# Blit des projectiles joueur ----------------------------------------------------------------
		bullet_vdb = 0
		for i in bullet_rects:
			if i.rect.top<35:
				bullet_rects.pop(bullet_vdb)
			if pygame.sprite.collide_mask(cBoss.sprite,i):
				cBoss.vieCourante-=cHero.puissance
				bullet_rects.pop(bullet_vdb)
			else:
				i.rect.top = i.rect.top-10
				screen.blit(i.image,i.rect)
			bullet_vdb+=1
# Affichage mobs --------------------------------------------------------------------------
		mobs_vdb = 0
		for k in mob_rects:
			if pygame.sprite.collide_mask(k.sprite,cHero.sprite):
				mob_rects.pop(mobs_vdb)
				cHero.vieCourante-=k.puissance
			elif k.sprite.rect.bottom>536:
				mob_rects.pop(mobs_vdb)
			else:
				bullet_vdb = 0
				for u in bullet_rects:
					if pygame.sprite.collide_mask(k.sprite,u):
						bullet_rects.pop(bullet_vdb)
						k.vieCourante-=cHero.puissance
						if k.vieCourante<=0:
							mob_rects.pop(mobs_vdb)
							cHero.gold+=k.argent
					bullet_vdb+=1
			mobs_vdb+=1
		for k in mob_rects:
			k.sprite.rect = k.sprite.rect.move(0,k.vitesse)
			screen.blit(k.sprite.image,k.sprite.rect)
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
