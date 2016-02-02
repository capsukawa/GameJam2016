import sys
import pygame
import os,inspect

def load_image(name):
    name = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+'/images/'+name
    image = pygame.image.load(name)
    return image

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
