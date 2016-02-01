import sys
import pygame
import os,inspect

def load_image(name):
    name = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+'/'+name
    image = pygame.image.load(name)
    return image
