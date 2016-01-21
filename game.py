import sys
import pygame
import os,inspect

def load_image(name):
    name = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+name
    image = pygame.image.load(name)
    return image

pygame.init()

background_image = load_image("/tutos/les_evenements/background.jpg")
background_position = [0, 0]

os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

speed = [1, 1]
bspeed = [0,-5]
invader = load_image("/tutos/les_evenements/InvaderA_00.png")
invader_rect = invader.get_rect()
my_hero = load_image("/tutos/les_evenements/InvaderB_00.png")
my_hero_rect = my_hero.get_rect()
bstack1 = []
bstack2 = []

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	invader_rect = invader_rect.move(speed)

	if invader_rect.left < 0 or invader_rect.right > width:
		speed[0] = -speed[0]

	if invader_rect.top < 0 or invader_rect.bottom > height:
		speed[1] = -speed[1]

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and my_hero_rect.left > 0:
		my_hero_rect = my_hero_rect.move(-5, 0)

	if keys[pygame.K_RIGHT] and my_hero_rect.right < width:
		my_hero_rect = my_hero_rect.move(5, 0)

	if keys[pygame.K_UP] and my_hero_rect.top > 0:
		my_hero_rect = my_hero_rect.move(0, -5)

	if keys[pygame.K_DOWN] and my_hero_rect.bottom < height:
		my_hero_rect = my_hero_rect.move(0, 5)

	if keys[pygame.K_SPACE]:
		bstack1.append(load_image("/bullet.png"))
		if bstack1:
			bstack2.append(bstack1[len(bstack1)-1].get_rect())
			bstack2[len(bstack2)-1] = my_hero_rect
			print(bstack2)
			for item in bstack2:
				item = item.move(0,-5)

	screen.blit(background_image, background_position)
	screen.blit(invader, invader_rect)
	screen.blit(my_hero, my_hero_rect)
	for item in bstack2:
		screen.blit(bstack1[0],item)

	pygame.display.flip()
	screen.blit

	pygame.time.wait(10)
