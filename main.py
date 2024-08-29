import pygame
from classes import *

pygame.init()
HEIGHT = 900
WIDTH = 800
bg_img = pygame.image.load("images/Space_Background.png")
background = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
NEXT_LVL = pygame.event.Event(pygame.USEREVENT + 1)
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()


def check_collision(SHIP, asteroids_list):
    for bullet in SHIP.bullets:
        for asteroid in asteroids_list:
            if pygame.Rect.colliderect(bullet, asteroid):
                SHIP.bullets.remove(bullet)
                asteroid.health -= 1
                if asteroid.health == 0:
                    asteroids_list.remove(asteroid)


lvl = 1
Ship = Ship()


def main(level_value):
    asteroids = []
    play_game = True
    SCREEN.blit(background, (0, 0))
    SCREEN.blit(level_text[level_value - 1], (235, 150))
    Ship.fill_health()
    Ship.update(SCREEN)
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.time.set_timer(NEXT_LVL, 30000)

    while play_game:
        clock.tick(60)
        print(asteroids)
        fire_bullet = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fire_bullet = True
            if event == NEXT_LVL:
                global lvl
                lvl += 1
                main(lvl)

        SCREEN.fill((0, 0, 0))
        SCREEN.blit(background, (0, 0))
        if fire_bullet:
            Ship.shoot()
        if len(asteroids) < 5:
            asteroids.append(Asteroid(level_value))
        for asteroid in asteroids: 
            if asteroid.rect.y + asteroid.velocity >= 900:
                asteroids.remove(asteroid)
                Ship.health.pop()
            else:
               asteroid.move(SCREEN) 
        Ship.update(SCREEN)
        check_collision(Ship, asteroids)
        pygame.display.update()
    pygame.quit()
    


main(lvl)
