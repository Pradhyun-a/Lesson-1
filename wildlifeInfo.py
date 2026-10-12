import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Wildlife Spotlight: Tiger")

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (500, 500))

tiger_image = pygame.image.load("tiger.png")
tiger_image = pygame.transform.scale(tiger_image, (250, 250))

tiger_rect = tiger_image.get_rect(center=(250, 250))

font = pygame.font.Font(None, 30)
title_surface = font.render("Wildlife Spotlight: Tiger", True, (255, 255, 255))
fact_surface = font.render("Fact: Tigers are the largest wild cats.", True, (255, 255, 255))

title_rect = title_surface.get_rect(center=(250, 50))
fact_rect = fact_surface.get_rect(center=(250, 450))

clock = pygame.time.Clock()

def game_loop():
    while True:
        clock.tick(30) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background_image, (0, 0))
        screen.blit(tiger_image, tiger_rect)
        screen.blit(title_surface, title_rect)
        screen.blit(fact_surface, fact_rect)
        
        pygame.display.flip()

game_loop()
