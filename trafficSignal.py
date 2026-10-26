import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

CHANGE_CAR_COLOR = pygame.USEREVENT + 1
CHANGE_SIGNAL_COLOR = pygame.USEREVENT + 2

WHITE = pygame.Color('white')
GRAY = pygame.Color('gray25')
YELLOW = pygame.Color('yellow')
RED = pygame.Color('red')
GREEN = pygame.Color('green')

CAR_COLORS = [pygame.Color('blue'), pygame.Color('magenta'), pygame.Color('orange'), pygame.Color('cyan')]
signal_color = RED

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80, 40))
        self.image.fill(random.choice(CAR_COLORS))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300
        self.velocity_x = 5

    def update(self):
        self.rect.move_ip(self.velocity_x, 0)
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.velocity_x = -self.velocity_x
            pygame.event.post(pygame.event.Event(CHANGE_CAR_COLOR))
            pygame.event.post(pygame.event.Event(CHANGE_SIGNAL_COLOR))

    def change_color(self):
        self.image.fill(random.choice(CAR_COLORS))

all_sprites = pygame.sprite.Group()
player_car = Car()
all_sprites.add(player_car)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_CAR_COLOR:
            player_car.change_color()
        elif event.type == CHANGE_SIGNAL_COLOR:
            signal_color = GREEN if signal_color == RED else RED

    all_sprites.update()

    screen.fill(GRAY)
    pygame.draw.rect(screen, YELLOW, (0, SCREEN_HEIGHT // 2 - 5, SCREEN_WIDTH, 10))
    
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 25, 40, 50, 90))
    pygame.draw.circle(screen, RED if signal_color == RED else pygame.Color('darkred'), (SCREEN_WIDTH // 2, 65), 15)
    pygame.draw.circle(screen, GREEN if signal_color == GREEN else pygame.Color('darkgreen'), (SCREEN_WIDTH // 2, 105), 15)

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
