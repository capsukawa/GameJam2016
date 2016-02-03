import sys
import pygame
import os
import util

boss1 = [10,1,"boss/araignee.png"]

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
