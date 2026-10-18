import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")

x, y = 375, 275
w, h = 50, 50
speed = 5
color = (0, 255, 0)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    x = max(0, min(x, 800 - w))
    y = max(0, min(y, 600 - h))

    if x <= 0:
        color = (255, 0, 0)
    elif x >= 800 - w:
        color = (0, 0, 255)
    elif y <= 0:
        color = (255, 255, 0)
    elif y >= 600 - h:
        color = (255, 165, 0)
    else:
        color = (0, 255, 0)

    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (0, 0, 0), (200, 150), 40, 0)
    pygame.draw.circle(screen, (0, 0, 0), (600, 150), 40, 3)
    
    pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
