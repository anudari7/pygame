import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Jumper")

clock = pygame.time.Clock()

test_font = pygame.font.Font("pygame/Pixeltype (1).ttf", 50)

sky_surface = pygame.image.load('pygame/Sky.png').convert()
ground_surface = pygame.image.load('pygame/ground.png').convert()

surfacetext = "Press W"
text_surface = test_font.render(surfacetext, False, "black")
text_rect = text_surface.get_rect(center=(400, 50))
move = False

snail_surf = pygame.image.load('pygame/snail1.png').convert_alpha()
snail_rectangle = snail_surf.get_rect(bottomright=(600, 300))  #300 för att groundsurfen är 300

player_surface = pygame.image.load('pygame/player_walk_1 (1).png').convert_alpha()
player_rect = player_surface.get_rect(midbottom= (80, 300))

player_gravity = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -22
                move = True
                surfacetext = "Jumper"
                text_surface = test_font.render(surfacetext, False, "black")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player_rect.bottom >= 300:
                player_gravity = -22
                move = True
                surfacetext = "Jumper"
                text_surface = test_font.render(surfacetext, False, "black")
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))  #alltså den
    screen.blit(text_surface, text_rect)
    screen.blit(snail_surf, snail_rectangle)

    if move == True:
        snail_rectangle.x -= 5  # det hur snailen går.
    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800  #om snigeln går ur från skärmen kommer den komma tillbaks till sin första  plats.
    screen.blit(snail_surf, snail_rectangle)

    #player
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300: player_rect.bottom = 300
    screen.blit(player_surface, player_rect)

    if snail_rectangle.colliderect(player_rect):
        surfacetext = "Game over"
        text_surface = test_font.render(surfacetext, False, "black")
        move = False


    pygame.display.update()
    clock.tick(100)  #allt kommer flytta med såhär speed.