import pygame
import time
import Ranking
from maps import Map

Ranking.SetUsername()

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)
pygame.mixer.music.load('audio/background_music.mp3')
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
    
    elif game_map.inGame:
        game_map.blitBackgroundMap()   
        
        game_map.player1.animatePlayerSprite()

        game_map.player2.animatePlayerSprite()

        game_map.shotsInteractions()

        game_map.bulletsInteractions()
        
        game_map.monstersInteractions()

        game_map.generateMonsters()
                    
        game_map.showPlayerInfos()

        pygame.display.update()
   
    else:
        game_map.endOfGame()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_map.inGame = False
                game_map.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0] >= 380 and pos[0] <= 600 and pos[1] >= 630 and pos[1] <= 690):
                    game_map = Map()
                    game_map.spawnAllies(1, game_map.images.getAngelingImages(), 1)
                    game_map.spawnMonsters(1, game_map.images.getPoringImages(), 1, False)

    game_map.checkEvents()