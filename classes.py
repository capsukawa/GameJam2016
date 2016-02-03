import sys
import pygame
import os
import util

#boss : vie, puissance, vitesse, drop d'argent, image
boss1 = [50,1,0,100,"boss/araignee.png"] #ok
boss2 = [100,1,0,150,"boss/rat.png"] #ok
boss3 = [150,2,0,300,"boss/fantome.png"]
boss4 = [300,2,0,400,"boss/squelette.png"]
boss5 = [1000,4,0,600,"boss/troll.png"]
boss6 = [700,5,0,700,"boss/mage.png"] #ok
boss7 = [1000,10,0,800,"boss/vampire.png"]
boss8 = [1500,15,0,900,"boss/dragon1.png"] #ok
boss9 = [2000,20,0,1000,"boss/dragon3.png"] #ok

bosses = []
bosses.append(boss1)
bosses.append(boss2)
bosses.append(boss3)
bosses.append(boss4)
bosses.append(boss5)
bosses.append(boss6)
bosses.append(boss7)
bosses.append(boss8)
bosses.append(boss9)

# Mobs : vie, puissance, vitesse, drop argent, image
mob1 = [1,1,15,5,"mob/araignee.png"]
mob2 = [1,0.5,20,10,"mob/rat.png"] #ok
mob3 = [2,2,15,30,"mob/fantome.png"]
mob4 = [4,2,15,40,"mob/squelette.png"]
mob5 = [10,3,10,75,"mob/troll.png"]
mob6 = [7,3,17,50,"mob/mage.png"]
mob7 = [6,5,20,80,"mob/chauvesouris.png"] #ok
mob8 = [10,10,15,120,"mob/dragon.png"] #ok

class Hero():
	def __init__(self):
		self.viePleine = 2
		self.vieCourante = 2
		self.puissance = 5
		self.vitesseTir = 1
		self.vitesseDepl = 2
		self.nbProjectiles = 1
		self.sprite = util.load_sprite("hero.png")
		self.sprite.rect.centerx = 400
		self.sprite.rect.centery = 500

class Enemy():
	def __init__(self,infos):
		self.viePleine = infos[0]
		self.vieCourante = infos[0]
		self.puissance = infos[1]
		self.vitesse = infos[2]
		self.argent = infos[3]
		self.sprite = util.load_sprite(infos[4])
		self.sprite.rect.centerx = 400
		self.sprite.rect.top = 31
