import pygame
import time
import math
import random as rd
import Ranking
from monsters import Monster
from players import Player
from images_handler import Images
from special_items import SpecialItem
from barriers import Barrier

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

class Map():

    def __init__(self):
        self.barriersExist = False
        self.monsters = []
        self.bullets = []
        self.barriers = []
        self.lives = []
        self.level = None
        self.quant = 0
        self.playersSelected = False
        self.scenarioSelected = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.images = Images()
        self.inGame = True
        self.win = False
        self.windowClosed = False
        self.initialScreen = True
        self.selectScreen = False
        self.instructionsScreen = False
        self.showGuiLevel = True
        self.ranking = []
        self.setRank = True
        self.start_time = time.time()
        self.backgroundIndex = 0
        self.winBackgroundImage = pygame.image.load('Images/Menus/you_win.jpg')
        self.instructionBackgroundImage = pygame.image.load('Images/Menus/instructionsScreen.png')
        self.gameOverBackgroundImage = pygame.image.load('Images/Menus/game_over.jpg')
        self.initialBackgroundImage = pygame.image.load('Images/Menus/initAll.jpg')
        self.playerAndMapImage = pygame.image.load('Images/Menus/playerAndMap.jpg')
        self.muteIcon = pygame.image.load('Images/Util/muteIcon.png')
        self.soundIcon = pygame.image.load('Images/Util/soundIcon.png')
        self.scenario = None

    def spawnMonsters(self, amount, image, life):
        for i in range(amount):
            self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(-(70+(30*amount)), -70)), image, life))

    def spawnBarrier(self,image,position):
        self.barriers.append(Barrier(self,image,position))            

    def generateBarriers(self):
        if(self.barriersExist == False):
            if(self.scenario == 'ringue'):
                self.generateRandomBarriers(1, 2, self.images.getChair())
                self.generateRandomBarriers(1, 2, self.images.getBelt())
                
            elif self.scenario == 'floresta':
                self.generateRandomBarriers(1, 3, self.images.getTrunk())
                self.generateRandomBarriers(1, 3, self.images.getTree())
                self.generateRandomBarriers(1, 3, self.images.getLake())

            elif self.scenario == 'deserto':
                self.generateRandomBarriers(2, 4, self.images.getSand())
                self.generateRandomBarriers(2, 4, self.images.getCactus())
                self.generateRandomBarriers(2, 4, self.images.getRock())

    def generateRandomBarriers(self, floor, roof, image):
        random = rd.randint(floor, roof)
        for a in range(random):
            self.spawnBarrier(image, (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30)))
        self.barriersExist = True

    def generateMonsters(self):
        if self.scenario == 'ringue':
            if(self.quant <= 2): 
                randomAmount1 = rd.randint(1, 3)
                self.spawnMonsters(randomAmount1, self.images.getJoaoLourao(), 1)
                randomAmount2 = rd.randint(1, 3)
                self.spawnMonsters(randomAmount2, self.images.getMikeTyson(), 1)
                self.quant += (randomAmount1 + randomAmount2)
        elif self.scenario == 'floresta':
            if(self.quant <= 3): 
                randomAmount1 = rd.randint(1, 4)
                self.spawnMonsters(randomAmount1, self.images.getJaguar(), 1)
                randomAmount2 = rd.randint(1, 4)
                self.spawnMonsters(randomAmount2, self.images.getSnake(), 1)
                self.quant += (randomAmount1 + randomAmount2)
        elif self.scenario == 'deserto':
            if(self.quant <= 4): 
                randomAmount1 = rd.randint(1, 5)
                self.spawnMonsters(randomAmount1, self.images.getScorpion(), 1)
                randomAmount2 = rd.randint(1, 5)
                self.spawnMonsters(randomAmount2, self.images.getMummy(), 1)
                self.quant += (randomAmount1 + randomAmount2)
     
    def spawnBullets(self, amount):
        for i in range(amount):
            self.bullets.append(SpecialItem())
            self.lives.append(SpecialItem())

    def showPlayerInfos(self):
        self.screen.blit(self.player.img, self.player.position)
        self.player.showLife(self.screen)
        self.player.showScore(self.screen)
        self.player.showAmmoAmount(self.screen)
        self.showGuiLevel = True
        self.start_time = time.time()

    def blitBackgroundMap(self):
        self.screen.blit(pygame.image.load('Images/Scenarios/' + self.scenario + '.png'), (0, 0))

    def barriersInteractions(self):
        for barrier in self.barriers:
            barrier.drawBarrier(self.screen)
            # if self.player.is_collided_with(barrier):
            #     print(self.player.position)
                # self.player.position = list(self.player.position)
                # self.player.position[0] -= 10 
                # self.player.position[1] -= 10
                # self.player.position = tuple(self.player.position)
                
    def monstersInteractions(self):
        for monster in self.monsters:
            monster.move(self.player)
            monster.drawMonster(self.screen)
            if self.player.is_collided_with(monster):
                monster.damageAudio.play()
                self.player.damagePlayer()
                self.monsters.remove(monster)
                if(self.player.isPlayerDead()):
                    self.inGame = False

            else:
                for shot in self.player.shots:
                    if shot.is_collided_with(monster):
                        monster.damageMonster(1)
                        if monster.isDead():
                            self.monsters.remove(monster)
                            self.player.addScore(100)
                            self.quant-=1
                        self.player.shots.remove(shot)

    def bulletsInteractions(self):
        for bullet in self.bullets:
            self.screen.blit(bullet.ammoImg, bullet.position)
            if self.player.is_collided_with(bullet):
                bullet.reloadAudio.play()
                self.player.addAmmo(5)
                self.bullets.remove(bullet)
                if len(self.bullets) == 0:
                    self.player.canSpawnBullets = True

    def lifeInteractions(self):
        for life in self.lives:
            self.screen.blit(life.lifeImg, life.position)
            if self.player.is_collided_with(life):
                life.healAudio.play()
                self.player.addLife()
                self.lives.remove(life)
                if len(self.bullets) == 0:
                    self.player.canSpawnBullets = True

    def shotsInteractions(self):
        for shot in self.player.shots:
            shot.move()
            self.screen.blit(shot.img, shot.position)
            if shot.position[0] > SCREEN_WIDTH or shot.position[0] < 0:
                self.player.shots.remove(shot)
            elif shot.position[1] > SCREEN_HEIGHT or shot.position[1] < 0:
                self.player.shots.remove(shot)

    def checkEvents(self):
        velocity = 7
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            for barrier in self.barriers:
                if not self.player.is_collided_with(barrier):
                    self.player.setVelocityUp(velocity)
                    self.player.grau = 0
                    self.player.moveUp()
                else:
                    print("colidiu")
                    self.player.setVelocityLeft(velocity)
                    self.player.setVelocityRight(velocity)
                    self.player.setVelocityDown(velocity)
                    self.player.setVelocityUp(0)
                    self.player.moveUp()
                    print("Velocidade UP:",self.player.getVelocityUp())
                    print("Velocidade Down:",self.player.getVelocityDown())
                    print("Velocidade Left:",self.player.getVelocityLeft())
                    print("Velocidade Right:",self.player.getVelocityRight())

        elif keys[pygame.K_DOWN]:
            for barrier in self.barriers:
                if not self.player.is_collided_with(barrier):
                    self.player.setVelocityDown(velocity)
                    self.player.grau = 180
                    self.player.moveDown()
                else:
                    print("colidiu")
                    self.player.setVelocityLeft(velocity)
                    self.player.setVelocityRight(velocity)
                    self.player.setVelocityDown(0)
                    self.player.setVelocityUp(velocity)
                    self.player.moveDown()
                    print("Velocidade UP:",self.player.getVelocityUp())
                    print("Velocidade Down:",self.player.getVelocityDown())
                    print("Velocidade Left:",self.player.getVelocityLeft())
                    print("Velocidade Right:",self.player.getVelocityRight())

        elif keys[pygame.K_RIGHT]:
            for barrier in self.barriers:
                if not self.player.is_collided_with(barrier):
                    self.player.setVelocityRight(velocity)
                    self.player.grau = 90
                    self.player.moveRight()
                else:
                    print("colidiu")
                    self.player.setVelocityLeft(velocity)
                    self.player.setVelocityRight(0)
                    self.player.setVelocityDown(velocity)
                    self.player.setVelocityUp(velocity)
                    self.player.moveRight()
                    print("Velocidade UP:",self.player.getVelocityUp())
                    print("Velocidade Down:",self.player.getVelocityDown())
                    print("Velocidade Left:",self.player.getVelocityLeft())
                    print("Velocidade Right:",self.player.getVelocityRight())

        elif keys[pygame.K_LEFT]:
            for barrier in self.barriers:
                if not self.player.is_collided_with(barrier):
                    self.player.setVelocityLeft(velocity)
                    self.player.grau = 270
                    self.player.moveLeft()
                else:
                    print("colidiu")
                    self.player.setVelocityLeft(0)
                    self.player.setVelocityRight(velocity)
                    self.player.setVelocityDown(velocity)
                    self.player.setVelocityUp(velocity)
                    self.player.moveLeft()
                    print("Velocidade UP:",self.player.getVelocityUp())
                    print("Velocidade Down:",self.player.getVelocityDown())
                    print("Velocidade Left:",self.player.getVelocityLeft())
                    print("Velocidade Right:",self.player.getVelocityRight())
                    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot(self)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

    def endOfGame(self):
        if self.win:
            self.screen.blit(self.winBackgroundImage, (0, 0))
        else: 
            self.screen.blit(self.gameOverBackgroundImage, (0, 0))

        if self.setRank:    
            Ranking.SetRank(self.player.score, self.level, Ranking.GetUsername())
            Ranking.LoadRanking()
            self.ranking = Ranking.GetRanking()
            self.setRank = False

        count = 1
        for score in self.ranking:
            self.screen.blit(pygame.font.SysFont('arial', 45).render(str(count) + ". " + score[1] + " Level: " + score[2] + " Score: " + score[3] , True, (255, 255, 255)), (50, 170 + (70*count)))
            count += 1
            if count > 5: break

        pygame.display.update()

    def initalScreen(self):
        self.screen.blit(self.initialBackgroundImage, (0, 0))
        
        if(pygame.mixer.music.get_volume() > 0):
            self.screen.blit(self.soundIcon,(850,5))
        else:
            self.screen.blit(self.muteIcon,(850,5))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_map.inGame = False
                game_map.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                if(pos[0] >= 862 and pos[0] <= 893 and pos[1] >= 15 and pos[1] <= 47):
                    if(pygame.mixer.music.get_volume() > 0):
                        print("Mute")
                        # self.screen.blit(self.muteIcon,(850,5))
                        pygame.mixer.music.set_volume(0)
                    else:
                        print("sound")
                        # self.screen.blit(self.soundIcon,(850,5))
                        pygame.mixer.music.set_volume(0.1)

                if(pos[0] >= 306 and pos[0] <= 620 and pos[1] >= 444 and pos[1] <= 496):
                    self.initialScreen = False
                    self.selectScreen = True
                elif(pos[0] >= 227 and pos[0] <= 700 and pos[1] >= 530 and pos[1] <= 580):
                    self.initialScreen = False
                    self.instructionsScreen = True

    def instructionScreen(self):
        self.screen.blit(self.instructionBackgroundImage,(0,0))
        if(pygame.mixer.music.get_volume() > 0):
            self.screen.blit(self.soundIcon,(850,5))
        else:
            self.screen.blit(self.muteIcon,(850,5))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()   
                print(pos)
                if(pos[0] >= 862 and pos[0] <= 893 and pos[1] >= 15 and pos[1] <= 47):
                    if(pygame.mixer.music.get_volume() > 0):
                        print("Mute")
                    # self.screen.blit(self.muteIcon,(850,5))
                        pygame.mixer.music.set_volume(0)
                    else:
                        print("sound")
                        # self.screen.blit(self.soundIcon,(850,5))
                        pygame.mixer.music.set_volume(0.1)
                if(pos[0] >= 234 and pos[0] <= 726 and pos[1] >= 481 and pos[1] <= 554):
                    self.initialScreen = True
                    self.instructionsScreen = False
                 
    def playerAndMapScreen(self):
        self.screen.blit(self.playerAndMapImage, (0, 0))
        if(pygame.mixer.music.get_volume() > 0):
            self.screen.blit(self.soundIcon,(850,5))
        else:
            self.screen.blit(self.muteIcon,(850,5))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()            
                #escolhendo os personagens
                if(pos[0] >= 862 and pos[0] <= 893 and pos[1] >= 15 and pos[1] <= 47):
                    if(pygame.mixer.music.get_volume() > 0):
                        print("Mute")
                    # self.screen.blit(self.muteIcon,(850,5))
                        pygame.mixer.music.set_volume(0)
                    else:
                        print("sound")
                        # self.screen.blit(self.soundIcon,(850,5))
                        pygame.mixer.music.set_volume(0.1)
                if(pos[0] >= 7 and pos[0] <= 202 and pos[1] >= 148 and pos[1] <= 286):
                    self.definePlayer('farmer', 'farmer-shot', 5)
                elif(pos[0] >= 220 and pos[0] <= 422 and pos[1] >= 148 and pos[1] <= 286):
                    self.definePlayer('hooligan', 'hooligan-shot', 6)
                elif(pos[0] >= 452 and pos[0] <= 647 and pos[1] >= 148 and pos[1] <= 286):
                    self.definePlayer('alien', 'alien-shot', 4)
                elif(pos[0] >= 668 and pos[0] <= 862 and pos[1] >= 148 and pos[1] <= 286):
                    self.definePlayer('r0b07', 'r0b07-shot', 3)

                #escolhendo o mapa
                if(pos[0] >= 21 and pos[0] <= 254 and pos[1] >= 382 and pos[1] <= 486):
                    self.defineScenario('ringue', 'facil')
                elif(pos[0] >= 337 and pos[0] <= 542 and pos[1] >= 382 and pos[1] <= 486):
                    self.defineScenario('floresta', 'medio')
                elif(pos[0] >= 628 and pos[0] <= 848 and pos[1] >= 382 and pos[1] <= 486):
                    self.defineScenario('deserto', 'dificil')

                #se tiver selecionado os dois personagens e o mapa, pode continuar
                if self.playersSelected and self.scenarioSelected:
                    #se clicar em iniciar, avance
                    if(pos[0] >= 306 and pos[0] <= 618 and pos[1] >= 534 and pos[1] <= 584):
                        self.inGame = True
                        self.selectScreen = False

    def definePlayer(self, imageName, shotName, life):
        self.player = Player((100, 100), pygame.image.load('Images/Characters/' + imageName + '0.png'), imageName, shotName, life)
        self.playersSelected = True

    def defineScenario(self, scenario, difficulty):
        self.scenario = scenario
        self.level = difficulty
        self.scenarioSelected = True