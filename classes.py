import pygame


class Ship:
    def __init__(self) -> None:
        image = pygame.image.load("/home/vincentd007/Desktop/Space_Shooter/fighter_plane_icon_171269.png")
        self.image = pygame.transform.rotate(pygame.transform.scale(image, (120, 120)), 45)
        self.x = 330
        self.y = 780

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.x -= 5
        elif pressed_keys[pygame.K_RIGHT]:
            self.x += 5


class Asteroid1:
    def __init__(self) -> None:
        image = pygame.image.load("/home/vincentd007/Desktop/Space_Shooter/meteor_asteroid_icon_149797.png")
        self.x = image.get_rect()
        self.y = -100
        self.image = pygame.transform.rotate(pygame.transform.scale(image, (100, 100)), 45)


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pass