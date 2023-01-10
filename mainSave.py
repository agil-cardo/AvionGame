import pygame
from avion import Avion

# generer la fenetre du jeu
pygame.display.set_caption("Avion")

# taille de la fenetre
width  = 1280
height = 720

screen = pygame.display.set_mode((width, height))

background = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background,( width, height))

avion = Avion()

running = True

# boucle de jeu
while running:

    screen.blit(background, (0, 0))

    screen.blit(avion.image, (avion.rect.x, avion.rect.y))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()