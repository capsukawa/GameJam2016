import sys
import pygame
import os,inspect

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

def upgrades(screen,hero):
	menuUpgrades=1
	pygame.init()
	bgUpgrades = load_sprite("upgrades.png")

	select = load_sprite("select.png")
	select.rect.right = 125
	select.rect.centery = 170

	choix = 0
	timer = 0
	timer2 = 10
	selectPos = [180,230,280,330,420,470]

	while menuUpgrades==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		timer-=1
		timer2-=1

		keys = pygame.key.get_pressed()

		if keys[pygame.K_ESCAPE]:
			menuUpgrades=0

		if keys[pygame.K_UP]:
			if timer<=0:
				timer=10
				if choix==0:
					choix=5
				else:
					choix-=1
		if keys[pygame.K_DOWN]:
			if timer<=0:
				timer=10
				if choix==5:
					choix=0
				else:
					choix+=1
		if keys[pygame.K_SPACE]:
			if timer2<=0:
				timer2=10
				if choix==0:
					#Ameliorer la vitalite du joueur
					print("choix")
				if choix==1:
					#Ameliorer la puissance du joueur
					print("choix")
				if choix==2:
					#Ameliorer la vitesse de tir du joueur
					print("choix")
				if choix==3:
					#Ameliorer la vitesse de deplacement du joueur
					print("choix")
				if choix==4:
					menuUpgrades=0
					hero.vieCourante = hero.viePleine
				if choix==5:
					menuUpgrades=0

		screen.blit(bgUpgrades.image,bgUpgrades.rect)
		select.rect.centery = selectPos[choix]
		screen.blit(select.image,select.rect)

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
