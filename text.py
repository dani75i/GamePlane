import pygame
from constantes import *

messages = {
    "begin": "TAPE SUR S",
    "win": "YOU WIN",
    "lose": "GAME OVER !",
    "reolad": "Pour relancer tape sur r "
}

colors = {
    "green": (0, 255, 0),
    "blue": (0, 0, 128),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

positions = {
    "topleft": (20, 40),
    "toplright": (SIZE_FENETRE_X - 100, 40),
    "center": (SIZE_FENETRE_X // 2 - 150, SIZE_FENETRE_Y // 2 - 100),
    "bottomcenter": (SIZE_FENETRE_X // 2 - 230, SIZE_FENETRE_Y // 2 + 50),
    "topcenter": (SIZE_FENETRE_X // 2 - 150, 50),
}


class Text:

    def __init__(self, message=None, position=positions["topleft"]):
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.position = position
        self.message = message
        self.text = self.font.render(self.message, True, colors["green"], None)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.position

    def display_message(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, colors["black"], None)
        return self.text

    def set_position_message(self, position):
        self.position = position
        return self.position
