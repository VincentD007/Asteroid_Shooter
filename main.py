import pygame
from classes import *
from images.icons import *

pygame.init()
HEIGHT = 900
WIDTH = 800
background = pygame.transform.scale(pygame.image.load("images/Space_Background.png"), (WIDTH, HEIGHT))
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
NEXT_LVL = pygame.event.Event(pygame.USEREVENT + 1)
RESUME_LEVEL = pygame.event.Event(pygame.USEREVENT + 2)
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

# Checks if the bullet/asteroid has gone off screen, and if a bullet has collided with an asteroid
def check_collision(ship, asteroids, score):
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
                        score[0] += asteroid.level
                    break
                    

def main():
    level = 0
    max_level = 5
    score = [0]
    player_ship = Ship()
    asteroids_list = []
    play_game = True
    player_died = False
    pause_level = False

    pygame.event.post(NEXT_LVL)


    # Game loop
    while play_game:
        clock.tick(60)
        for event in pygame.event.get():
            if len(player_ship.health) == 0 or level > max_level:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL:
                    main()
            if event.type == pygame.QUIT:
                play_game = False
            if event == NEXT_LVL and player_died == False:
                pause_level = True
                player_ship.fill_health()
                level += 1
                asteroids_list.clear()
                if not level > max_level:
                    pygame.time.set_timer(RESUME_LEVEL, 3500, 1)
            if event == RESUME_LEVEL and player_died == False:
                pause_level = False
                pygame.time.set_timer(NEXT_LVL, 40000, 1)

        SCREEN.fill((0, 0, 0))
        SCREEN.blit(background, (0, 0))
        if not pause_level:
            if len(asteroids_list) < level + 3:
                if level == 5:
                    asteroids_list.append(Asteroid(random.randint(1, 4)))
                else:
                    asteroids_list.append(Asteroid(level))
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                player_ship.shoot()
        else:
            if level > max_level:
                SCREEN.blit(game_win, (140, 150))
                SCREEN.blit(final_score_font.render(f"Score: {score[0]}", 1, (255, 255, 255)), (200, 300))
                SCREEN.blit(play_again, (220, HEIGHT - 300))
            elif not player_died:
                SCREEN.blit(level_text_font.render(f"Level {level}", 1, (255, 255, 255)), (240, 150))
        for asteroid in asteroids_list:
            asteroid.move(SCREEN)
        # Checks for all possible collisions while also updating the player score accordingly
        check_collision(player_ship, asteroids_list, score)
        player_ship.update(SCREEN)
        SCREEN.blit(score_font.render(f"Score: {score}", 1, (255, 255, 255)), (650, 25))
        # Checks if the player has lost
        if len(player_ship.health) == 0:
            pause_level = True
            player_died = True
            asteroids_list.clear()
            SCREEN.blit(game_loose, (150, 150))
            SCREEN.blit(final_score_font.render(f"Score: {score[0]}", 1, (255, 255, 255)), (200, 300))
            SCREEN.blit(play_again, (220, HEIGHT - 300))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
