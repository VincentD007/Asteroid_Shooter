import pygame
import random
from images.icons import *

class Ship:
    def __init__(self) -> None:
        image = pygame.image.load("images/fighter_ship1.webp")
        self.image = pygame.transform.scale(image, (200, 200))
        self.rect = pygame.Surface.get_rect(self.image)
        self.health = []
        self.bullets = []
        self.rect.x = 300
        self.rect.y = 700

    # updates the position of the ship and it's bullets.
    def update(self, screen):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and self.rect.x - 8 > -50:
            self.rect.x -= 8
        if pressed_keys[pygame.K_RIGHT] and self.rect.x + 8 < 650:
            self.rect.x += 8
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            bullet.y -= 7
            pygame.draw.rect(screen, (255, 255, 255), bullet)
        for heart in self.health:
            screen.blit(heart_image, (heart.x, heart.y))
    # Controls automatic fire to create bullet spacing
    def shoot(self):
        new_bullet = pygame.Rect(self.rect.x + 95, self.rect.y, 10, 30)
        if len(self.bullets) < 6:
            if len(self.bullets) == 0:
                self.bullets.append(new_bullet)
            else:  
                if self.bullets[-1].y < 650:
                    self.bullets.append(new_bullet)

    
    def fill_health(self):
        x, y = 750, 500
        self.health = []
        for _ in range(4):
            self.health.append(pygame.Rect(x, y, 25, 25))
            y -= 30
  

class Asteroid:
    def __init__(self, level) -> None:
        self.level = level
        self.health = level
        if level == 5:
            self.velocity = random.randint(3, 6)
        else:
            self.velocity = random.randint(2, level + 1)
        self.rect = pygame.Surface.get_rect(asteroid_images[level - 1])
        self.rect.x = random.randint(0, 700)
        self.rect.y = random.randint(-1200, -400)
        
    
    def move(self, screen):
        self.rect.y += self.velocity
        if self.level == self.health:
            screen.blit(asteroid_health_image[0], (self.rect.x + 21, self.rect.y - 15))
        elif self.level == 2:
            if self.health == 1:
                screen.blit(asteroid_health_image[3], (self.rect.x + 21, self.rect.y - 15))
        elif self.level == 3:
            if self.health == 2:
                screen.blit(asteroid_health_image[1], (self.rect.x + 21, self.rect.y - 15))
            elif self.health == 1:
                screen.blit(asteroid_health_image[3], (self.rect.x + 21, self.rect.y - 15))
        elif self.level == 4:
            if self.health == 3:
                screen.blit(asteroid_health_image[2], (self.rect.x + 21, self.rect.y - 15))
            elif self.health == 2:
                screen.blit(asteroid_health_image[3], (self.rect.x + 21, self.rect.y - 15))
            elif self.health == 1:
                screen.blit(asteroid_health_image[3], (self.rect.x + 21, self.rect.y - 15))

        screen.blit(asteroid_images[self.level-1], (self.rect.x, self.rect.y))
