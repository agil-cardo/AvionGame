import pygame
from avion import Avion
from weapon import Weapon
import time

pygame.display.set_caption("Avion")

pygame.init()
width = 1280
height = 720
#frams par seconde
screen = pygame.display.set_mode((width, height))

background = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background, (width, height))
#instance de weapon
weapon - Weapon("fusi")
avion = Avion()

running = True

while running:

    #on regle l'img par seconde
    clock - pygame.time.clock()

    screen.blit(background, (0, 0))

    screen.blit(avion.image, (avion.rect.x, avion.rect.y))

    avion.update_pv(screen)

    if avion.keyboard.get(pygame.K_RIGHT) and (avion.rect.x + avion.rect.width) < screen.get_width():
        avion.move_right()
    elif avion.keyboard.get(pygame.K_LEFT) and avion.rect.x > 0:
        avion.move_left()

    if avion.keyboard.get(pygame.K_DOWN) and (avion.rect.y + avion.rect.height) < screen.get_height():
        avion.move_down()
    elif avion.keyboard.get(pygame.K_UP) and avion.rect.y > 0:
        avion.move_up()  

    pygame.display.flip()

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            avion.keyboard[event.key] = True
        elif event.type == pygame.KEYUP:
            avion.keyboard[event.key] = False
        
