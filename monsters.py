import pygame
import random as rd

class Monster():

    def __init__(self, position, img, life):
        self.position = position
        self.img_left = img[0]
        self.img_right = img[1]
        self.img_width = self.img_right[0].get_width()
        self.img_height = self.img_right[0].get_height()
        self.rect = pygame.Rect(position[0]+5, position[1]+5, self.img_width-10, self.img_height-10)
        self.vel = rd.randint(1, 3)
        self.direction = 1
        self.index = rd.randint(0, len(self.img_right)-1)
        self.animationFrames = len(self.img_right)
        self.life = life
        self.initialLife = life
        self.dieAudio = pygame.mixer.Sound('Audio/enemy_hurt.wav')
        self.damageAudio = pygame.mixer.Sound('Audio/player_hurt.wav')
        
    def move(self, player):
        if player.position[0]+player.img.get_width()/2 > self.position[0]+self.img_width/2:
            self.position = (self.position[0]+self.vel, self.position[1])
            self.rect.x += self.vel
            self.direction = 0
        if player.position[0]+player.img.get_width()/2 < self.position[0]+self.img_width/2:
            self.position = (self.position[0]-self.vel, self.position[1])
            self.rect.x -= self.vel
            self.direction = 1
        if player.position[1]+player.img.get_height()/2 > self.position[1]+self.img_height/2:
            self.position = (self.position[0], self.position[1]+self.vel)
            self.rect.y += self.vel
        if player.position[1]+player.img.get_height()/2 < self.position[1]+self.img_height/2:
            self.position = (self.position[0], self.position[1]-self.vel)
            self.rect.y -= self.vel

    def drawMonster(self, screen):
        if self.direction:
            screen.blit(self.img_right[self.index], self.position)
        else:
            screen.blit(self.img_left[self.index], self.position)
        self.index += 1
        if self.index == self.animationFrames:
            self.index = 0

    def changeMonsterVelocity(self, newVel):
        self.vel = newVel

    def damageMonster(self, amount):
        self.life -= amount
    def isDead(self):
        if self.life <= 0:
            self.dieAudio.play()
            return True
        return False
