import pygame

from enemy import Enemy
from text import *
from player import Player
from missile import MissilePlayer
from constantes import *

pygame.init()

# Variables
continuer = True
start = False
displayplayer = True
x = 0
y = 0
x2 = SIZE_FENETRE_X
list_missiles = []
list_ennemies = []
score = 0

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((SIZE_FENETRE_X, SIZE_FENETRE_Y))

# Définition du background
background = pygame.image.load("images/ciel.jpg")
background = pygame.transform.scale(background, (SIZE_FENETRE_X, SIZE_FENETRE_Y))

# Instanciation class Text
texte = Text()

# Instanciation class Player
player = Player()


# Fonction pour générer des ennemies
def generate_ennemies(number_ennemies):
    for i in range(number_ennemies):
        enemy = Enemy()
        list_ennemies.append(enemy)


# Générer des ennemies
generate_ennemies(6)

# Intanciation Timer
time_elapsed_since_last_action = TIME_GAME
clock = pygame.time.Clock()

while continuer:

    # Afficher et animer le background
    x -= 2
    x2 -= 2

    fenetre.blit(background, (x, y))
    fenetre.blit(background, (x2, y))

    if -x > SIZE_FENETRE_X:
        x = SIZE_FENETRE_X
    if -x2 > SIZE_FENETRE_X:
        x2 = SIZE_FENETRE_X

    # Afficher le text
    if not start:
        fenetre.blit(texte.display_message(messages["begin"]), texte.set_position_message(positions["center"]))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            continuer = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                start = True

            elif event.key == pygame.K_SPACE:
                missile = MissilePlayer(player.rect.x, player.rect.y)
                list_missiles.append(missile)

    # Commenrcer le jeu
    if start:

        # Afiicher le score
        message = "SCORE : " + str(score)
        fenetre.blit(texte.display_message(message), texte.set_position_message(positions["topcenter"]))

        # Afficher le joueur
        if displayplayer:
            fenetre.blit(player.image, (player.rect.x, player.rect.y))
        else:
            fenetre.blit(texte.display_message(messages["lose"]), texte.set_position_message(positions["center"]))

        # Compte à rebourd
        dt = clock.tick()
        time_elapsed_since_last_action -= dt
        time = int(time_elapsed_since_last_action / 1000)

        if time_elapsed_since_last_action <= 0:
            fenetre.blit(texte.display_message(messages["win"]), texte.set_position_message(positions["center"]))

        else:
            fenetre.blit(texte.display_message(str(time)), texte.set_position_message(positions["toplright"]))

        #####################
        # Missile part
        #####################

        # Afficher les missiles et les animer
        if displayplayer:
            for missile in list_missiles:
                fenetre.blit(missile.image, (missile.rect.x, missile.rect.y))
                missile.launch_missile()

            # Tester une collision entre un missile et un ennemi
            for missile in list_missiles:
                if missile.rect.collidelist(list_ennemies) != -1:
                    index = missile.rect.collidelist(list_ennemies)
                    list_ennemies.remove(list_ennemies[index])
                    list_missiles.remove(missile)
                    score += 1

        #####################
        # Enemy part
        #####################

        # Afficher les ennemies et les animer
        for enemy in list_ennemies:
            fenetre.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
            enemy.move_forward()

        # Supprimer les ennemies de la liste s'ils ne sont plus ds l'écran
        for enemy in list_ennemies:
            if enemy.rect.x <= 0:
                list_ennemies.remove(enemy)

        if len(list_ennemies) <= 3:
            generate_ennemies(6)

        #####################
        # Missile part
        #####################

        # Tester une collision entre le joueur et un ennemi
        if player.rect.collidelist(list_ennemies) != -1:
            displayplayer = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and player.rect.x + player.rect.width < SIZE_FENETRE_X:
            player.move_right()

        elif keys[pygame.K_LEFT] and player.rect.x > 0:
            player.move_left()

        elif keys[pygame.K_UP] and player.rect.y > 0:
            player.move_up()

        elif keys[pygame.K_DOWN] and player.rect.y + player.rect.height < SIZE_FENETRE_Y:
            player.move_down()

    # Rafraichissement
    pygame.display.flip()
