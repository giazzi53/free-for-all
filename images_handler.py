import pygame

class Images():

    def __init__(self):
        self.joaoLourao = [[pygame.image.load('Images/Enemies/Right/joaoLourao-ringue.png')],
                       [pygame.image.load('Images/Enemies/Left/joaoLourao-ringue.png')]]

        self.mikeTyson = [[pygame.image.load('Images/Enemies/Right/mikeTyson-ringue.png')],
                       [pygame.image.load('Images/Enemies/Left/mikeTyson-ringue.png')]]

        self.snake = [[pygame.image.load('Images/Enemies/Right/cobra-floresta.png')],
                       [pygame.image.load('Images/Enemies/Left/cobra-floresta.png')]]
                       
        self.jaguar = [[pygame.image.load('Images/Enemies/Right/onca-floresta.png')],
                       [pygame.image.load('Images/Enemies/Left/onca-floresta.png')]]

        self.mummy = [[pygame.image.load('Images/Enemies/Right/mumia-deserto.png')],
                       [pygame.image.load('Images/Enemies/Left/mumia-deserto.png')]]

        self.scorpion = [[pygame.image.load('Images/Enemies/Right/scorpion-deserto.png')],
                       [pygame.image.load('Images/Enemies/Left/scorpion-deserto.png')]]

    def getJoaoLourao(self):
        return self.joaoLourao

    def getMikeTyson(self):
        return self.mikeTyson

    def getSnake(self):
        return self.snake

    def getJaguar(self):
        return self.jaguar

    def getMummy(self):
        return self.mummy

    def getScorpion(self):
        return self.scorpion

    def changeImagesSize(self, images, size):
        return [[pygame.transform.scale(images[0][i], size) for i in range(len(images[0]))], [pygame.transform.scale(images[1][i], size) for i in range(len(images[1]))]]
