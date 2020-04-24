import pygame
import random

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 3
        self.posx = random.randint(900, 1100)
        self.posy = random.randint(50, 600)
        self.image = pygame.image.load("images/asteroide.png")
        self.size = random.randint(50, 80)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = self.posx
        self.rect.y = self.posy
        self.origine_image = self.image
        self.angle = random.randint(0, 90)

    def move_forward(self):
        self.rect.x -= self.velocity
        self.rotate()

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
