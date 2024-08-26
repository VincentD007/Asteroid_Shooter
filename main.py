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
game_level = 1
ship = Ship()
asteroids = []


def check_collision(ship, asteroids_list):
    for bullet in ship.bullets:
        for asteroid in asteroids_list:
            if pygame.Rect.colliderect(bullet, asteroid):
                ship.bullets.remove(bullet)
                asteroid.health -= 1
                if asteroid.health == 0:
                    asteroids_list.remove(asteroid)


def main( ):
    play_game = True
    ship.fill_health()
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
        if len(asteroids) < 5:
            asteroids.append(Asteroid(game_level))
        for asteroid in asteroids: 
            if asteroid.rect.y + asteroid.velocity < 900:
                asteroid.move(SCREEN)
            else:
                asteroids.remove(asteroid)
                ship.health.pop()
        ship.update(SCREEN)
        check_collision(ship, asteroids)
        pygame.display.update()
    pygame.quit()  



main()
