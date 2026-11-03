import pygame
import sys

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))

try:
    bg = pygame.image.load("pet_bg.jpg")
    bg = pygame.transform.scale(bg, (W, H))
except:
    bg = pygame.Surface((W, H))
    bg.fill((40, 40, 40))

font = pygame.font.SysFont("Arial", 50)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, size, color, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self, dx, dy):
        self.rect.x = max(0, min(self.rect.x + dx, W - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + dy, H - self.rect.height))

pet = GameSprite(50, (0, 255, 0), 100, 100)
food = GameSprite(30, (255, 0, 0), 600, 400)

group = pygame.sprite.Group(pet, food)
collected = False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    pet.move(dx, dy)

    if not collected and pet.rect.colliderect(food.rect):
        food.kill()
        collected = True

    screen.blit(bg, (0, 0))
    group.draw(screen)

    if collected:
        txt = font.render("Food Collected!", True, (255, 255, 255))
        screen.blit(txt, ((W - txt.get_width()) // 2, (H - txt.get_height()) // 2))

    pygame.display.flip()
    clock.tick(60)
