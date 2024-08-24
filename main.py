import pygame
from classes import *


pygame.init()
HEIGHT = 900
WIDTH = 800
bg_img = pygame.image.load("/home/vincentd007/Desktop/Space_Shooter/—Pngtree—space game earth star background_1592602.png")
background = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()
asteroid = AsteroidLevel1()
ship = Ship()

def main():
    play_game = True
    while play_game:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(background, (0, 0))
        ship.move(SCREEN)
        asteroid.move(SCREEN)
        pygame.display.update()
    pygame.quit()



main()
