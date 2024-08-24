import pygame
import random


class Ship:
    def __init__(self) -> None:
        image = pygame.image.load("/home/vincentd007/Desktop/Space_Shooter/yct20hubfk061.webp")
        self.image = pygame.transform.scale(image, (200, 200))
        self.rect = pygame.Surface.get_rect(self.image)
        self.rect.y = 700
        self.rect.x = 300


    def move(self, screen):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= 8
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.x += 8
        screen.blit(self.image, (self.rect.x, self.rect.y))


class AsteroidLevel1:
    def __init__(self) -> None:
        image = pygame.image.load("/home/vincentd007/Desktop/Space_Shooter/meteor_asteroid_icon_149797.png")
        self.asteroid_image = pygame.transform.rotate(pygame.transform.scale(image, (100, 100)), 45)
        self.velocity = 5
        self.rect = pygame.Surface.get_rect(self.asteroid_image)
        self.rect.x = random.randint(0, 700)
        self.y = -100
        
    
    def move(self, screen):
        self.rect.y += 5
        screen.blit(self.asteroid_image, (self.rect.x, self.rect.y))
        pass
