import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1100, 600))

pygame.display.set_caption("byt namn")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

