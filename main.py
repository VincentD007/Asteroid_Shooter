import pygame
from classes import *
from images.icons import *

pygame.init()
HEIGHT = 900
WIDTH = 800
bg_img = pygame.image.load("images/Space_Background.png")
background = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
NEXT_LVL = pygame.event.Event(pygame.USEREVENT + 1)
RESUME_LEVEL = pygame.event.Event(pygame.USEREVENT + 2)
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

# Checks if the bullet/asteroid has gone off screen, and if a bullet has collided with an asteroid
def check_collision(ship, asteroids):
    score_increase = 0
    for asteroid in asteroids:
        if asteroid.rect.y >= HEIGHT:
            asteroids.remove(asteroid)
            ship.health.pop()
    for bullet in ship.bullets:
        if  bullet.y <= -30:
            ship.bullets.remove(bullet)
        else:
            for asteroid in asteroids:
                if pygame.Rect.colliderect(bullet, asteroid):
                    ship.bullets.remove(bullet)
                    asteroid.health -= 1
                    if asteroid.health == 0:
                        asteroids.remove(asteroid)
                        score_increase += asteroid.level
                    break
    return score_increase
                

def main():
    level = 0
    max_level = 5
    score = 0
    player_ship = Ship()
    asteroids_list = []
    play_game = True
    pause_level = False
    pygame.event.post(NEXT_LVL)

    # Game loop
    while play_game:
        clock.tick(60)
        fire_bullet = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
            if event == NEXT_LVL:
                pause_level = True
                player_ship.fill_health()
                level += 1
                asteroids_list.clear()
                if not level > max_level:
                    pygame.time.set_timer(RESUME_LEVEL, 3500, 1)
            if event == RESUME_LEVEL:
                pause_level = False
                pygame.time.set_timer(NEXT_LVL, 20000, 1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not pause_level:
                        fire_bullet = True
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(background, (0, 0))

        if not pause_level:
            if len(asteroids_list) < level + 3:
                if level == 5:
                    asteroids_list.append(Asteroid(random.randint(1, 4)))
                else:
                    asteroids_list.append(Asteroid(level))
            if fire_bullet:
                player_ship.shoot()
        else:
            if level > max_level:
                SCREEN.blit(game_win, (150, 150))
                SCREEN.blit(final_score_font.render(f"Score: {score}", 1, (255, 255, 255)), (200, 300))
            elif not level > max_level:
                SCREEN.blit(level_text_font.render(f"Level {level}", 1, (255, 255, 255)), (240, 150))
        for asteroid in asteroids_list:
            asteroid.move(SCREEN)
                        # Checks for all possible collisions and returns a score increase value based on how many asteroids were destroyed.
        score_increase = check_collision(player_ship, asteroids_list)
        score += score_increase
        player_ship.update(SCREEN)
        SCREEN.blit(score_font.render(f"Score: {score}", 1, (255, 255, 255)), (665, 25))

        if len(player_ship.health) == 0:
            SCREEN.blit(game_loose, (150, 150))
            play_game = False
            pygame.display.update()
            pygame.time.delay(5000)
        pygame.display.update()

    pygame.quit()


main()
