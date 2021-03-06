import pygame
from shots import Shot

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

class Player():

    def __init__(self, position, img, imageName, shotName, life, speed):
        self.position = position
        self.img = img
        self.imageName = imageName
        self.shotName = shotName
        self.rect = pygame.Rect(position[0]+8, position[1]+5, img.get_width()-16, img.get_height()-10)
        self.grau = 0
        self.speed = speed
        self.oldSpeed = self.speed
        self.life = life
        self.heartText = pygame.font.SysFont('arial', 30).render("Life: ", True, (0, 0, 0))
        self.heartImage = pygame.image.load('Images/Special items/heart.png')
        self.shots = []
        self.ammo = 10
        self.ammoImage = pygame.image.load('Images/Special items/ammo_amount.png')
        self.ammoText = pygame.font.SysFont('arial', 21).render("Ammo:", True, (0, 0, 0))
        self.canSpawnBullets = True
        self.score = 0
        self.scoreText = pygame.font.SysFont('arial', 30).render("Score: " + str(self.score), True, (0, 0, 0))
        self.shotAudio = pygame.mixer.Sound('Audio/shot.wav')
  
    def setPosition(self, position):
        self.position = position

    def setImage(self, image):
        self.img = image

    def setRect(self, rect):
        self.rect = rect

    def animatePlayerSprite(self):
        if self.grau >= 360:
            self.grau = 0
        if self.grau < 0:
            self.grau = 360 + self.grau
        image = pygame.image.load('Images/Characters/' + self.imageName + str(self.grau) + '.png') 
        self.setImage(image)

    def makeSlower(self):
        self.speed -= 5
        
    def returnNormalSpeed(self):
        self.speed = self.oldSpeed
    
    def moveUp(self):
        if self.position[1] > 0:
            self.setPosition((self.position[0], self.position[1] - self.speed))
            self.rect.y -= self.speed
        
    def moveDown(self):
        if self.position[1] < SCREEN_HEIGHT - self.img.get_height():
            self.setPosition((self.position[0], self.position[1] + self.speed))
            self.rect.y += self.speed

    def moveRight(self):
        if self.position[0] < SCREEN_WIDTH - self.img.get_width():
            self.setPosition((self.position[0] + self.speed, self.position[1]))
            self.rect.x += self.speed

    def moveLeft(self):
        if self.position[0] > 0:
            self.setPosition((self.position[0] - self.speed, self.position[1]))
            self.rect.x -= self.speed

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def damagePlayer(self):
        self.life -= 1

    def isPlayerDead(self):
        return self.life <= 0

    def showLife(self, screen):
        screen.blit(self.heartText, (7, 7))
        for i in range(1, self.life+1):
            screen.blit(self.heartImage, (20 + 40*i, 10))

    def shoot(self, game_map):
        if self.ammo > 0:
            self.shotAudio.play()
            self.ammo -= 1
            if self.grau == 0:
                self.shots.append(Shot((self.position[0]+40, self.position[1]), 'y', -1, self.shotName + str(self.grau)))
            elif self.grau == 180:
                self.shots.append(Shot((self.position[0]+20, self.position[1]+40), 'y',  1, self.shotName + str(self.grau))) 
            elif self.grau == 90:
                self.shots.append(Shot((self.position[0]+40, self.position[1]+40), 'x',  1, self.shotName + str(self.grau)))
            else:
                self.shots.append(Shot((self.position[0], self.position[1]+20), 'x', -1, self.shotName + str(self.grau)))
            if self.ammo == 0 and self.canSpawnBullets:
                game_map.spawnBullets(4)
                self.canSpawnBullets = False

    def showAmmoAmount(self, screen):
        screen.blit(self.ammoText, (7, 50))
        for i in range(self.ammo):
            screen.blit(self.ammoImage, (60 + (20*i), 50))

    def addAmmo(self, amount):
        self.ammo += amount

    def addLife(self):
        self.life += 1

    def addScore(self, amount):
        self.score += amount
        self.scoreText = pygame.font.SysFont('arial', 30).render("Score: " + str(self.score), True, (0, 0, 0))

    def showScore(self, screen):
        screen.blit(self.scoreText, (780 , 7))
