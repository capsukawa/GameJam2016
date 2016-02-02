import sys
import pygame
import os

class Hero:
	viePleine = 20
	vieCourante = 20
	puissance = 1
	vitesseTir = 1
	vitesseDepl = 2
	nbProjectiles = 1

class Level:
	def __init__(self,background):
		self.bg = background
		#self.boss = Enemy()
		#self.mob = Enemy()
