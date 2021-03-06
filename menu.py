import sys
import pygame
import os
import game,util

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

background = util.load_sprite("menu.png")

menuPos = [98,199,300,401,502]

select = util.load_sprite("select.png")
select.rect.right = 520
select.rect.centery = menuPos[0]

pygame.mixer.music.load("menutheme.mp3")
pygame.mixer.music.play(1000)

choix = 0
timer = 0
timerMenu = 0

varOptions = [1,0,0]
	# 0:(optSon) 0 = Mute / 1 = Play
	# 1:(optGD) 0 = Droitier / 1 = Gaucher
	# 2:(optTir) 0 = Manuel / 1 = Automatique

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	#Gestion du clavier
	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP]:
		if timer<=0:
			timer=10
			if choix==0:
				choix=4
			else:
				choix-=1

	if keys[pygame.K_DOWN]:
		if timer<=0:
			timer=10
			if choix==4:
				choix=0
			else:
				choix+=1

	if keys[pygame.K_SPACE] and timerMenu<=0:
		if choix==0:
			game.play(screen,varOptions)
			timerMenu=50
		elif choix==1:
			util.regles(screen)
		elif choix==2:
			varOptions = util.options(screen,varOptions)
		elif choix==3:
			util.credits(screen)
		elif choix==4:
			sys.exit()


	timer-=1
	timerMenu-=1

	screen.blit(background.image,background.rect)
	select.rect.centery = menuPos[choix]
	screen.blit(select.image,select.rect)

	pygame.display.flip()
	screen.blit

	pygame.time.wait(10)
