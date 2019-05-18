import pygame
import random as rd
#from maps import Map
from images_handler import Images

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
position1= (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30))
position2 = (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30))
position3 = (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30))

class Barrier():
    def __init__(self,maps,img,position):
        self.images = Images()
        self.position = position
        

        def drawBarrier(self, screen):
            screen.blit(img,position)

            # if self.direction:
            #     screen.blit(self.img_right[self.index], self.position)
            # else:
            #     screen.blit(self.img_left[self.index], self.position)
            # self.index += 1
            # if self.index == self.animationFrames:
            #     self.index = 0
       
        # if maps.scenario == 'ringue':
        #     maps.screen.blit(self.images.getChair(), (position1))
        #     maps.screen.blit(self.images.getBelt(), (position2))
        #     maps.barriersExist = True
        # elif maps.scenario == 'floresta':
        #     maps.screen.blit(self.images.getTrunk(), (position1))
        #     maps.screen.blit(self.images.getTree(), (position2))
        #     maps.screen.blit(self.images.getLake(), (position3))
        #     maps.barriersExist = True
        # elif maps.scenario == 'deserto':
        #     maps.screen.blit(self.images.getSand(), (position1))
        #     maps.screen.blit(self.images.getCactus(), (position2))
        #     maps.screen.blit(self.images.getRock(), (position3))
        #     maps.barriersExist = True
