import pygame

class Images():

    def __init__(self):
        self.joaoLourao = [pygame.image.load('Images/Enemies/joaoLourao-ringue.png'), (60, 60)) for i in range(10)],
        self.mikeTyson = [pygame.image.load('Images/Enemies/mikeTyson-ringue.png'), (60, 60)) for i in range(10)],
        self.cobra = [pygame.image.load('Images/Enemies/cobra-floresta.png'), (60, 60)) for i in range(10)],
        self.onca = [pygame.image.load('Images/Enemies/onca-floresta.png'), (60, 60)) for i in range(10)],
        self.scorpion = [pygame.image.load('Images/Enemies/scorpion-deserto.png'), (60, 60)) for i in range(10)],
        self.mumia = [pygame.image.load('Images/Enemies/mumia-deserto.png'), (60, 60)) for i in range(10)]

    def getJoaoLourao(self):
        return self.joaoLourao

    def getMikeTyson(self):
        return self.mikeTyson

    def changeImagesSize(self, images, size):
        return [[pygame.transform.scale(images[0][i], size) for i in range(len(images[0]))], [pygame.transform.scale(images[1][i], size) for i in range(len(images[1]))]]
