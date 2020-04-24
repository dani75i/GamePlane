import pygame


class MissilePlayer(pygame.sprite.Sprite):

    def __init__(self, posx, posy):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load("images/missile.png")
        self.image = pygame.transform.scale(self.image, (15, 60))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.x = posx + self.rect.width
        self.rect.y = posy + 55

    def launch_missile(self):
        self.rect.x += self.velocity
