import pygame

asteroid_h1 = pygame.transform.scale(pygame.image.load("images/Asteroid_Health1.png"), (70, 15))
asteroid_h2 = pygame.transform.scale(pygame.image.load("images/Asteroid_Health2.png"), (70, 15))
asteroid_h3 = pygame.transform.scale(pygame.image.load("images/Asteroid_Health3.png"), (70, 15))

asteroid_image_lvl1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/asteroid1.png"), (80, 80)), 45)
asteroid_image_lvl2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/asteroid2.png"), (80, 80)), 45)
asteroid_image_lvl3 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/asteroid3.png"), (80, 80)), 45)

heart_image = pygame.transform.scale(pygame.image.load("images/heart.png"), (25, 25))