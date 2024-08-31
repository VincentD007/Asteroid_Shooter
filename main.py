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

# Checks if the bullet/asteroid has gone off screen, and if a bullet has collided with an asteroid
def check_collision(SHIP, asteroids_list):
    for asteroid in asteroids_list:
        if asteroid.rect.y >= HEIGHT:
            asteroids_list.remove(asteroid)
            SHIP.health.pop()
    for bullet in SHIP.bullets:
        if  bullet.y <= -30:
            Ship.bullets.remove(bullet)
        else:
            for asteroid in asteroids_list:
                if pygame.Rect.colliderect(bullet, asteroid):
                    SHIP.bullets.remove(bullet)
                    asteroid.health -= 1
                    if asteroid.health == 0:
                        asteroids_list.remove(asteroid)
                    break
                


lvl = 5
Ship = Ship()


def main(level_value):
    max_level = 4
    asteroids = []
    play_game = True
    SCREEN.blit(background, (0, 0))

    # Checks if final level has passed
    if level_value > max_level:
        SCREEN.blit(game_win, (200, 150))
        play_game = False

    # Displays which level the play is on at the beginning of the level
    if play_game:
        SCREEN.blit(level_text_font.render(f"Level {level_value}", 1, (255, 255, 255)), (240, 150))
    Ship.fill_health()
    Ship.update(SCREEN)
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.time.set_timer(NEXT_LVL, 30000)

    # Game loop
    while play_game:
        clock.tick(60)
        # fire_bullet variable becomes true if the space_bar event is posted which represents the player shooting
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
        # Limits the amount of asteroids being spawned
        if len(asteroids) < level_value + 4:
            if level_value == max_level:
                asteroids.append(Asteroid(random.randint(1, max_level)))
            else:
                asteroids.append(Asteroid(level_value))
        # Updates the postion of the asteroids
        for asteroid in asteroids:
            asteroid.move(SCREEN)
        if fire_bullet:
            Ship.shoot()
        check_collision(Ship, asteroids)
        # Updates both the ship position, and bullet position on screen
        Ship.update(SCREEN)
        # Wnds the game if the player runs out of health
        if len(Ship.health) == 0:
            SCREEN.blit(game_loose, (150, 150))
            play_game = False
            pygame.display.update()
            pygame.time.delay(5000)
        pygame.display.update()

    pygame.quit()
    


main(lvl)
