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
        #self.allies = []
        self.bullets = []
        self.barriers = []
        self.lives = []
        self.level = 1
        self.quant = 0
        self.clicks = 0
        self.playersSelected = False
        self.scenarioSelected = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.images = Images()
        self.bossTime = True
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
        self.scenario = None

    def spawnMonsters(self, amount, image, life, isBoss):
        
        for i in range(amount):
            #monsters spawn at left side
            #self.monsters.append(Monster((rd.randint(-(70+(30*amount)), -70), rd.randint(0, 700)), image, life, isBoss))
            #monsters spawn at top side
            self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(-(70+(30*amount)), -70)), image, life, isBoss))
            #monsters spawn at right side
            #self.monsters.append(Monster((rd.randint(1070, 1070+(30*amount)), rd.randint(0, 700)), image, life, isBoss))
            #monsters spawn at bot side
            #self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(770, 770+(30*amount))), image, life, isBoss))

    def spawnBarrier(self,image,position):
        self.barriers.append(Barrier(self,image,position))            

    def generateBarriers(self):
        if(self.barriersExist == False):
            if(self.scenario == 'ringue'):
                print("Ringue")
                self.spawnBarrier(self.images.getChair(),(rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30)))
                self.spawnBarrier(self.images.getBelt(), (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30)))
                self.barriersExist = True
                
            elif self.scenario == 'floresta':
                self.spawnBarrier(self.images.getTrunk(), (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30)))
                self.spawnBarrier(self.images.getTree(), (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30)))
                self.spawnBarrier(self.images.getLake(), (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30)))
                self.barriersExist = True

            elif self.scenario == 'deserto':
                self.spawnBarrier(self.images.getSand(), (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30)))
                self.spawnBarrier(self.images.getCactus(), (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30)))
                self.spawnBarrier(self.images.getRock(), (rd.randint(0,SCREEN_WIDTH-30), rd.randint(0,SCREEN_HEIGHT-30)))
                self.barriersExist = True
            

    def generateMonsters(self):
        if self.scenario == 'ringue':
            if(self.quant <= 2): 
                randomAmount1 = rd.randint(1, 3)
                self.spawnMonsters(randomAmount1, self.images.getJoaoLourao(), 1, False)
                randomAmount2 = rd.randint(1, 3)
                self.spawnMonsters(randomAmount2, self.images.getMikeTyson(), 1, False)
                self.quant += (randomAmount1 + randomAmount2)
        elif self.scenario == 'floresta':
            if(self.quant <= 3): 
                randomAmount1 = rd.randint(1, 4)
                self.spawnMonsters(randomAmount1, self.images.getJaguar(), 1, False)
                randomAmount2 = rd.randint(1, 4)
                self.spawnMonsters(randomAmount2, self.images.getSnake(), 1, False)
                self.quant += (randomAmount1 + randomAmount2)
        elif self.scenario == 'deserto':
            if(self.quant <= 4): 
                randomAmount1 = rd.randint(1, 5)
                self.spawnMonsters(randomAmount1, self.images.getScorpion(), 1, False)
                randomAmount2 = rd.randint(1, 5)
                self.spawnMonsters(randomAmount2, self.images.getMummy(), 1, False)
                self.quant += (randomAmount1 + randomAmount2)
      #for i in range(3):
            #del self.monsters[rd.randint(0, len(self.monsters)-1)]
        #self.monsters[0].changeMonsterVelocity(3)

    def spawnBullets(self, amount):
        for i in range(amount):
            self.bullets.append(SpecialItem())
            self.lives.append(SpecialItem())

    def showPlayerInfos(self):
        self.screen.blit(self.player1.img, self.player1.position)
        self.player1.showLife(self.screen)
        self.player1.showScore(self.screen)
        self.player1.showAmmoAmount(self.screen)
        self.showGuiLevel = True
        self.start_time = time.time()

    def blitBackgroundMap(self):
        self.screen.blit(pygame.image.load('Images/Scenarios/' + self.scenario + '.png'), (0, 0))

    def barriersInteractions(self):
        for barrier in self.barriers:
            barrier.drawBarrier(self.screen)
            if self.player1.is_collided_with(barrier):
                print(self.player1.position)
                self.player1.position = list(self.player1.position)
                self.player1.position[0] -= 10 
                self.player1.position[1] -= 10
                self.player1.position = tuple(self.player1.position)

                print(self.player1.position)


    def monstersInteractions(self):
        for monster in self.monsters:
            monster.move(self.player1)
            monster.drawMonster(self.screen)
            if self.player1.is_collided_with(monster):
                monster.damageAudio.play()
                if monster.isBoss:
                    self.player1.damagePlayer(5)
                else:
                    self.player1.damagePlayer(1)
                self.monsters.remove(monster)
                if(self.player1.isPlayerDead()):
                    self.inGame = False

                

            else:
                for shot in self.player1.shots:
                    if shot.is_collided_with(monster):
                        monster.damageMonster(1)
                        if monster.isDead():
                            self.monsters.remove(monster)
                            self.player1.addScore(100)
                            self.quant-=1
                        self.player1.shots.remove(shot)

            

    def bulletsInteractions(self):
        for bullet in self.bullets:
            self.screen.blit(bullet.ammoImg, bullet.position)
            if self.player1.is_collided_with(bullet):
                bullet.reloadAudio.play()
                self.player1.addAmmo(5)
                self.bullets.remove(bullet)
                if len(self.bullets) == 0:
                    self.player1.canSpawnBullets = True

    def lifeInteractions(self):
        for life in self.lives:
            self.screen.blit(life.lifeImg, life.position)
            if self.player1.is_collided_with(life):
                life.healAudio.play()
                self.player1.addLife()
                self.lives.remove(life)
                if len(self.bullets) == 0:
                    self.player1.canSpawnBullets = True

    def shotsInteractions(self):
        for shot in self.player1.shots:
            shot.move()
            self.screen.blit(shot.img, shot.position)
            if shot.position[0] > SCREEN_WIDTH or shot.position[0] < 0:
                self.player1.shots.remove(shot)
            elif shot.position[1] > SCREEN_HEIGHT or shot.position[1] < 0:
                self.player1.shots.remove(shot)

    def checkEvents(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player1.grau = 0
            self.player1.moveUp()
            self.player1.passo += 1
        elif keys[pygame.K_DOWN]:
            self.player1.grau = 180
            self.player1.moveDown()
            self.player1.passo += 1
        elif keys[pygame.K_RIGHT]:
            self.player1.grau = 90
            self.player1.moveRight()
            self.player1.passo += 1
        elif keys[pygame.K_LEFT]:
            self.player1.grau = 270
            self.player1.moveLeft()
            self.player1.passo += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player1.shoot(self)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

    def endOfGame(self):
        if self.win:
            self.screen.blit(self.winBackgroundImage, (0, 0))
        else: 
            self.screen.blit(self.gameOverBackgroundImage, (0, 0))

        if self.setRank:    
            Ranking.SetRank(self.player1.score, self.level, Ranking.GetUsername())
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
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_map.inGame = False
                game_map.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0] >= 306 and pos[0] <= 620 and pos[1] >= 444 and pos[1] <= 496):
                    self.initialScreen = False
                    self.selectScreen = True
                elif(pos[0] >= 227 and pos[0] <= 700 and pos[1] >= 530 and pos[1] <= 580):
                    self.initialScreen = False
                    self.instructionsScreen = True

    def instructionScreen(self):
        self.screen.blit(self.instructionBackgroundImage,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()   
                print(pos)
                if(pos[0] >= 234 and pos[0] <= 726 and pos[1] >= 481 and pos[1] <= 554):
                    self.initialScreen = True
                    self.instructionsScreen = False
                    print("Voltar")
                 
    def playerAndMapScreen(self):
        self.screen.blit(self.playerAndMapImage, (0, 0))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()            
                #escolhendo os personagens
                if(pos[0] >= 7 and pos[0] <= 202 and pos[1] >= 148 and pos[1] <= 286):
                    self.definePlayer('farmer', 'farmer-shot')
                elif(pos[0] >= 220 and pos[0] <= 422 and pos[1] >= 148 and pos[1] <= 286):
                    self.definePlayer('hooligan', 'hooligan-shot')
                elif(pos[0] >= 452 and pos[0] <= 647 and pos[1] >= 148 and pos[1] <= 286):
                    self.definePlayer('alien', 'alien-shot')
                elif(pos[0] >= 668 and pos[0] <= 862 and pos[1] >= 148 and pos[1] <= 286):
                    self.definePlayer('r0b07', 'r0b07-shot')

                #escolhendo o mapa
                if(pos[0] >= 21 and pos[0] <= 254 and pos[1] >= 382 and pos[1] <= 486):
                    self.defineScenario('ringue')
                elif(pos[0] >= 337 and pos[0] <= 542 and pos[1] >= 382 and pos[1] <= 486):
                    self.defineScenario('floresta')
                elif(pos[0] >= 628 and pos[0] <= 848 and pos[1] >= 382 and pos[1] <= 486):
                    self.defineScenario('deserto')

                #se tiver selecionado os dois personagens e o mapa, pode continuar
                if self.playersSelected and self.scenarioSelected:
                    #se clicar em iniciar, avance
                    if(pos[0] >= 306 and pos[0] <= 618 and pos[1] >= 534 and pos[1] <= 584):
                        self.inGame = True
                        self.selectScreen = False

    def definePlayer(self, imageName, shotName):
        self.player1 = Player((100, 100), pygame.image.load('Images/Characters/' + imageName + '0.png'), imageName, shotName)
        self.playersSelected = True

    def defineScenario(self, scenario):
        self.scenario = scenario
        self.scenarioSelected = True
   
    
            
            

                
                    
