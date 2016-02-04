import sys
import pygame
import os,inspect
import math

def load_image(name):
	name = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+'/images/'+name
	image = pygame.image.load(name).convert_alpha()
	return image

def load_sprite(name):
	sprite = pygame.sprite.Sprite()
	sprite.image = load_image(name)
	sprite.rect = sprite.image.get_rect()
	sprite.mask = pygame.mask.from_surface(sprite.image)
	return sprite

def gameOver(screen):
	gameOver=1
	pygame.init()
	bgGameOver = load_sprite("gameover.png")

	while gameOver==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			keys = pygame.key.get_pressed()

			if keys[pygame.K_ESCAPE]:
				gameOver=0

		screen.blit(bgGameOver.image,bgGameOver.rect)
		pygame.display.flip()
		screen.blit
		pygame.time.wait(10)

def win(screen):
	aGagne=1
	pygame.init()
	bgGagne = load_sprite("youwin.png")

	while aGagne==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			keys = pygame.key.get_pressed()

			if keys[pygame.K_ESCAPE]:
				aGagne=0
		screen.blit(bgGagne.image, bgGagne.rect)
		pygame.display.flip()
		screen.blit
		pygame.time.wait(10)

def upgrades(screen,hero):
	menuUpgrades=1
	pygame.init()
	if hero.gold < 100:
		gameOver(screen)
	else:
		bgUpgrades = load_sprite("upgrades.png")

		select = load_sprite("select.png")
		select.rect.right = 125
		select.rect.centery = 170

		# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
		myfont = pygame.font.SysFont("monospace", 30)
		myfont.set_bold(1)

		tabPrixVital = [0,0,42,80,120,200,235,285,400,470,550,635,720,800,880,965,1050,1130,1215,1300,1380,1460,1540,1620,1700,1780,1860,1940,2020,2100,2180,2260,2340,2420,2500,2580,2660,2740,2820,2900,2980,3060,3140,3220,3300,3380,3460,3540,3620,3700,3780]
		tabPrixPuiss = [0,69,80,120,200,235,285,400,470,550,635,720,800,880,965,1050,1130,1215,1300,1380,1460,1540,1620,1700,1780,1860,1940,2020,2100,2180,2260,2340,2420,2500,2580,2660,2740,2820,2900,2980,3060,3140,3220,3300,3380,3460,3540,3620,3700,3780]
		tabPrixVitTir = [0,80,150,190,260,320,490,580,690,800]
		tabPrixVitDep = [0,80,190,320,500]

		choix = 0
		timer = 0
		timerAchat = 50
		selectPos = [225,275,325,375,465,505]
		hero.gold-=100


		while menuUpgrades==1:

			if (hero.viePleine < 50):
				prixVital = myfont.render(str(tabPrixVital[hero.viePleine]), 1, (0,0,0))
			else:
				prixVital = myfont.render("-", 1, (0,0,0))

			if(hero.puissance < 50):
				prixPuiss = myfont.render(str(tabPrixPuiss[hero.puissance]), 1, (0,0,0))
			else:
				prixPuiss = myfont.render("-", 1, (0,0,0))

			if(hero.vitesseTir < 10):
				prixVitTir = myfont.render(str(tabPrixVitTir[hero.vitesseTir]), 1, (0,0,0))
			else:
				prixVitTir = myfont.render("-", 1, (0,0,0))

			if(hero.vitesseDepl < 10):
				prixVitesse = myfont.render(str(tabPrixVitDep[hero.vitesseDepl]), 1, (0,0,0))
			else:
				prixVitesse = myfont.render("-", 1, (0,0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			timer-=1
			timerAchat-=1

			keys = pygame.key.get_pressed()

			if keys[pygame.K_ESCAPE]:
				menuUpgrades=0

			if keys[pygame.K_UP]:
				if timer<=0:
					timer=20
					if choix==0:
						choix=5
					else:
						choix-=1
			if keys[pygame.K_DOWN]:
				if timer<=0:
					timer=20
					if choix==5:
						choix=0
					else:
						choix+=1
			if keys[pygame.K_SPACE] and timerAchat<=0:
					timerAchat=30
					if choix==0:
						#Ameliorer la vitalite du joueur
						if(hero.viePleine < 50 and hero.gold >= tabPrixVital[hero.viePleine]):
							hero.gold-=tabPrixVital[hero.viePleine]
							hero.viePleine+=1
						else:
							print("achat impossible")
					if choix==1:
						#Ameliorer la puissance du joueur
						if(hero.puissance < 50 and hero.gold >= tabPrixPuiss[hero.puissance]):
							hero.gold-=tabPrixPuiss[hero.puissance]
							hero.puissance+=1
						else:
							print("achat impossible")
					if choix==2:
						#Ameliorer la vitesse de tir du joueur
						if(hero.vitesseTir < 10 and hero.gold >= tabPrixVitTir[hero.vitesseTir]):
							hero.gold-=tabPrixVitTir[hero.vitesseTir]
							hero.vitesseTir+=1
						else:
							print("achat impossible")
					if choix==3:
						#Ameliorer la vitesse de deplacement du joueur
						if(hero.vitesseDepl < 5 and hero.gold >= tabPrixVitDep[hero.vitesseDepl]):
							hero.gold-=tabPrixVitDep[hero.vitesseDepl]
							hero.vitesseDepl+=1
						else:
							print("achat impossible")
					if choix==4:
						menuUpgrades=0
						hero.vieCourante = hero.viePleine
					if choix==5:
						menuUpgrades=0

			screen.blit(bgUpgrades.image,bgUpgrades.rect)
			select.rect.centery = selectPos[choix]
			screen.blit(select.image,select.rect)

			aRes = hero.viePleine-2
			i=0
			while aRes>0:
				if aRes>=3:
					s = load_sprite("case_full.PNG")
					s.rect.top = 207
					s.rect.left = 420+i*14
					screen.blit(s.image,s.rect)
					aRes-=3
					i+=1
				elif aRes==2:
					s = load_sprite("case_2tiers.png")
					s.rect.top = 207
					s.rect.left = 420+i*14
					screen.blit(s.image,s.rect)
					aRes-=2
					i+=1
				elif aRes==1:
					s = load_sprite("case_1tier.png")
					s.rect.top = 207
					s.rect.left = 420+i*14
					screen.blit(s.image,s.rect)
					aRes-=1
					i+=1
			aRes = hero.puissance-2
			i=0
			while aRes>0:
				if aRes>=3:
					s = load_sprite("case_full.PNG")
					s.rect.top = 255
					s.rect.left = 420+i*14
					screen.blit(s.image,s.rect)
					aRes-=3
					i+=1
				elif aRes==2:
					s = load_sprite("case_2tiers.png")
					s.rect.top = 255
					s.rect.left = 420+i*14
					screen.blit(s.image,s.rect)
					aRes-=2
					i+=1
				elif aRes==1:
					s = load_sprite("case_1tier.png")
					s.rect.top = 255
					s.rect.left = 420+i*14
					screen.blit(s.image,s.rect)
					aRes-=1
					i+=1
			aRes = hero.vitesseTir-1
			i=0
			while aRes>0:
				s = load_sprite("case_full.PNG")
				s.rect.top = 305
				s.rect.left = 519+i*14
				screen.blit(s.image,s.rect)
				aRes-=1
				i+=1

			aRes = hero.vitesseDepl-1
			i=0
			while aRes>0:
				s = load_sprite("case_full.PNG")
				s.rect.top = 355
				s.rect.left = 519+i*14
				screen.blit(s.image,s.rect)
				aRes-=1
				i+=1

			# render text
			label = myfont.render(str(hero.gold), 1, (0,0,0))
			screen.blit(label, (490, 144))
			screen.blit(prixVital, (675,206))
			screen.blit(prixPuiss, (675,254))
			screen.blit(prixVitTir, (675,299))
			screen.blit(prixVitesse, (675,354))
			pygame.display.flip()
			screen.blit

			pygame.time.wait(10)

	return hero

def credits(screen):
	menuCredits = 1
	pygame.init()
	bgCredits = load_image("credits.png")
	bgCredits_position = [0,0]
	while menuCredits==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			menuCredits=0
		screen.blit(bgCredits,bgCredits_position)
		pygame.display.flip()
		screen.blit
		pygame.time.wait(10)

def regles(screen):
	menuRegles = 1
	pygame.init()
	bgRegles = load_image("regles.png")
	bgRegles_position = [0,0]
	while menuRegles==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			menuRegles=0
		screen.blit(bgRegles,bgRegles_position)
		pygame.display.flip()
		screen.blit
		pygame.time.wait(10)

def options(screen,varOptions):
	menuOptions = 1

	pygame.init()

	bgOptions = load_image("bgOptions.png")
	bgOptions_position = [0,0]

	select = load_image("select.png")
	select_rect = select.get_rect()
	select_rect.right = 235
	select_rect.centery = 195

	checked = load_image("checked.png")

	timer = 0
	timer2 = 10
	choix = 0
	selectPos = [195,295,395]

	while menuOptions==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			menuOptions=0

		if keys[pygame.K_UP]:
			if timer<=0:
				timer=10
				if choix==0:
					choix=2
				else:
					choix-=1

		if keys[pygame.K_DOWN]:
			if timer<=0:
				timer=10
				if choix==2:
					choix=0
				else:
					choix+=1

		if keys[pygame.K_SPACE]:
			if timer2<=0:
				if choix==0:
					if varOptions[0]==0:
						varOptions[0]=1
						pygame.mixer.music.unpause()
					else:
						varOptions[0]=0
						pygame.mixer.music.pause()
				elif choix==1:
					if varOptions[1]==0:
						varOptions[1]=1
					else:
						varOptions[1]=0
				elif choix==2:
					if varOptions[2]==0:
						varOptions[2]=1
					else:
						varOptions[2]=0
				timer2=20


		timer-=1
		timer2-=1
		screen.blit(bgOptions,bgOptions_position)
		select_rect.centery=selectPos[choix]
		screen.blit(select,select_rect)
		if varOptions[0]==1:
			checked_rect1 = checked.get_rect()
			checked_rect1.centerx = 522
			checked_rect1.centery = 195
			screen.blit(checked,checked_rect1)
		if varOptions[1]==1:
			checked_rect2 = checked.get_rect()
			checked_rect2.centerx = 522
			checked_rect2.centery = 293
			screen.blit(checked,checked_rect2)
		if varOptions[2]==1:
			checked_rect3 = checked.get_rect()
			checked_rect3.centerx = 522
			checked_rect3.centery = 392
			screen.blit(checked,checked_rect3)


		pygame.display.flip()
		screen.blit
		pygame.time.wait(10)

	return varOptions
