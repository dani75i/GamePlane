import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.velocity = 10
        self.image = pygame.image.load("images/helico.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (130, 70))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.health = 150

        super().__init__()

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
