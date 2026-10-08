import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")
player_image = pygame.image.load("bullet.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (100, 100))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(player_image, (350, 250))
    pygame.display.flip()
pygame.quit()
