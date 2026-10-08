import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text Example")
font = pygame.font.Font(None, 40)
text = font.render("Hello Pygame!", True, (0, 0, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(text, (300, 250))
    pygame.display.flip()
pygame.quit()
