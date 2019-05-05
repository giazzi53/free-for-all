import pygame

class Images():

    def __init__(self):
        #--------------------Enemies--------------------
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

        #--------------------Barriers--------------------
        self.chair = pygame.image.load('Images/Barriers/cadeira-ringue.png')

        self.belt = pygame.image.load('Images/Barriers/cinturao-ringue.png')

        self.bush = pygame.image.load('Images/Barriers/arbusto-floresta.png')

        self.tree = pygame.image.load('Images/Barriers/arvore-floresta.png')

        self.trunk = pygame.image.load('Images/Barriers/tronco-floresta.png')

        self.lake = pygame.image.load('Images/Barriers/lago-floresta.png')

        self.sand = pygame.image.load('Images/Barriers/morroAreia-deserto.png')

        self.rock = pygame.image.load('Images/Barriers/pedra-deserto.png')

        self.cactus = pygame.image.load('Images/Barriers/cacto-deserto.png')

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

    def getChair(self):
        return self.chair

    def getBelt(self):
        return self.belt

    def getBush(self):
        return self.bush

    def getTrunk(self):
        return self.trunk

    def getTree(self):
        return self.tree

    def getLake(self):
        return self.lake

    def getSand(self):
        return self.sand

    def getRock(self):
        return self.rock

    def getCactus(self):
        return self.cactus

    '''
    def changeImagesSize(self, images, size):
        return [[pygame.transform.scale(images[0][i], size) for i in range(len(images[0]))], [pygame.transform.scale(images[1][i], size) for i in range(len(images[1]))]]
    '''