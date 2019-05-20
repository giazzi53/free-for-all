import pygame
import time
import Ranking
from maps import Map

Ranking.SetUsername()

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)
pygame.mixer.music.load('Audio/background_music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

game_map = Map()

while not game_map.windowClosed:
    pygame.time.Clock().tick(30)
    game_map.screen.fill((255, 255, 255))

    if game_map.initialScreen:
        game_map.initalScreen()

    elif game_map.selectScreen:
        game_map.playerAndMapScreen()

    elif game_map.instructionsScreen:
        game_map.instructionScreen()

    elif game_map.inGame:
        game_map.blitBackgroundMap()   
        game_map.player.animatePlayerSprite()
        game_map.shotsInteractions()
        game_map.bulletsInteractions()
        game_map.lifeInteractions()
        game_map.monstersInteractions()
        game_map.generateMonsters()
        game_map.generateBarriers()
        game_map.barriersInteractions()
        game_map.showPlayerInfos()
        pygame.display.update()
   
    else:
        game_map.endOfGame()

    game_map.checkEvents()
