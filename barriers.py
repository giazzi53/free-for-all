import pygame
import random as rd
#from maps import Map
from images_handler import Images

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

class Barrier():
    def __init__(self,maps):
        self.images = Images()
        self.position = (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30))
        if maps.scenario == 'ringue':
            maps.screen.blit(self.images.getChair(), (position))
            maps.screen.blit(self.images.getBelt(), (position))
        elif maps.scenario == 'floresta':
            maps.screen.blit(self.images.getTrunk(),  )
            maps.screen.blit(self.images.getTree(), position)
            maps.screen.blit(self.images.getLake(), position)
        elif maps.scenario == 'deserto':
            maps.screen.blit(self.images.getSand(), position)
            maps.screen.blit(self.images.getCactus(), position)
            maps.screen.blit(self.images.getRock(), position)
