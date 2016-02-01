import sys
import pygame
import os,inspect

def load_image(name):
    name = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+'/'+name
    image = pygame.image.load(name)
    return image

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

background = load_image("background.png")
background_position = [0,0]

hero = load_image("hero.png")
hero_rect = hero.get_rect()
hero_rect.left = 296
hero_rect.top = 430

bullet = load_image("bullet.png")
bullet_rects = []
bullet_time=0

enemy = load_image("enemy.png")
enemy_rects = []
enemy_alive = []
for i in range(0,5):
	te = enemy.get_rect()
	te.left = i*60 + 2
	enemy_rects.append(te)
	enemy_alive.append(1)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# Evenements clavier
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and hero_rect.left > 5:
		hero_rect = hero_rect.move(-3,0)

	if keys[pygame.K_RIGHT] and hero_rect.right < width-5:
		hero_rect = hero_rect.move(3,0)

	if keys[pygame.K_SPACE] and bullet_time<=0:
		bullet_time = 20
		tb = bullet.get_rect()
		tb.left = (hero_rect.right+hero_rect.left)/2
		tb.top = hero_rect.top-2
		bullet_rects.append(tb)

	# Gros bordel
	bullet_time-=1
	screen.blit(background,background_position)
	screen.blit(hero,hero_rect)

	bullet_vdb = 0
	for i in bullet_rects:
		if i.bottom<0:
			bullet_rects.pop(bullet_vdb)
		enemy_vdb = 0
		for y in enemy_rects:
			if i.top<y.bottom and i.centerx<y.right and i.centerx>y.left:
				bullet_rects.pop(bullet_vdb)
				enemy_rects.pop(enemy_vdb)
			enemy_vdb+=1
		i.top = i.top-10
		screen.blit(bullet,i)
		bullet_vdb+=1
	for y in enemy_rects:
		screen.blit(enemy,y)

	pygame.display.flip()
	screen.blit

	pygame.time.wait(10)
