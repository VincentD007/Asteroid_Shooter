import pygame
import random

class Ship:
    def __init__(self, screen) -> None:
        self.screen = screen
        image = pygame.image.load("images/fighter_ship1.webp")
        self.image = pygame.transform.scale(image, (200, 200))
        self.rect = pygame.Surface.get_rect(self.image)
        self.bullets = []
        self.rect.x = 300
        self.rect.y = 700


    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= 8
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.x += 8
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            if bullet.y - 7 > -30:
                bullet.y -= 7
                pygame.draw.rect(self.screen, (255, 255, 255), bullet)
            elif bullet.y == -28:
                self.bullets.remove(bullet)
   

    def shoot(self):
        new_bullet = pygame.Rect(self.rect.x + 95, self.rect.y, 10, 30)
        if len(self.bullets) < 6:
            self.bullets.append(new_bullet)

  



class AsteroidLevel1:
    def __init__(self) -> None:
        image = pygame.image.load("images/asteroid1.png")
        self.asteroid_image = pygame.transform.rotate(pygame.transform.scale(image, (100, 100)), 45)
        self.velocity = 5
        self.health = 3
        self.rect = pygame.Surface.get_rect(self.asteroid_image)
        self.rect.x = random.randint(0, 700)
        self.y = -100
        
    
    def move(self, screen):
        self.rect.y += self.velocity
        screen.blit(self.asteroid_image, (self.rect.x, self.rect.y))
        pass
