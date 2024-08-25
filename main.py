import pygame
from classes import *

pygame.init()
HEIGHT = 900
WIDTH = 800
bg_img = pygame.image.load("images/Space_Background.png")
background = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()
asteroid = AsteroidLevel1()
ship = Ship(SCREEN)

def main( ):
    play_game = True
    while play_game:
        clock.tick(60)
        fire_bullet = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fire_bullet = True

        SCREEN.fill((0, 0, 0))
        SCREEN.blit(background, (0, 0))
        if fire_bullet:
            ship.shoot()
        ship.update()
        asteroid.move(SCREEN) 
        pygame.display.update()
    pygame.quit()  



main()
