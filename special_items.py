import pygame
import random as rd

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

class SpecialItem():

    def __init__(self):
        self.position = (rd.randint(0, SCREEN_WIDTH-30), rd.randint(0, SCREEN_HEIGHT-30))
        self.ammoImg = pygame.image.load('Images/Special items/arma.png')
        self.rect = pygame.Rect(self.position[0], self.position[1], self.ammoImg.get_width(), self.ammoImg.get_height())
        self.reloadAudio = pygame.mixer.Sound('Audio/reload.wav')
        self.lifeImg = pygame.image.load('Images/Special items/heart.png')
        self.healAudio = pygame.mixer.Sound('Audio/heal.wav')
        
