import sys
import pygame
import os
import util

boss1 = [50,1,"boss/araignee.png"]
boss2 = [100,1,"boss/rat.png"]
boss3 = [150,2,"boss/fantome.png"]
boss4 = [300,2,"boss/squelette.png"]
boss5 = [1000,4,"boss/troll.png"]
boss6 = [700,5,"boss/mage.png"]
boss7 = [1000,10,"boss/vampire.png"]
boss8 = [1500,15,"boss/dragon1.png"]
boss9 = [2000,20,"boss/dragon3.png"]

class Hero():
	def __init__(self):
		self.viePleine = 2
		self.vieCourante = 2
		self.puissance = 1
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
		self.sprite = util.load_sprite(infos[2])
		self.sprite.rect.centerx = 400
		self.sprite.rect.top = 31
