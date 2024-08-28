import pygame
pygame.font.init()
asteroid_h1 = pygame.transform.scale(pygame.image.load("images/Asteroid_Health1.png"), (70, 15))
asteroid_h2 = pygame.transform.scale(pygame.image.load("images/Asteroid_Health2.png"), (70, 15))
asteroid_h3 = pygame.transform.scale(pygame.image.load("images/Asteroid_Health3.png"), (70, 15))
asteroid_h4 = pygame.transform.scale(pygame.image.load("images/Asteroid_Health4.png"), (70, 15))
asteroid_health_image = [asteroid_h1, asteroid_h2, asteroid_h3, asteroid_h4]

asteroid_image_lvl1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/asteroid1.png"), (80, 80)), 45)
asteroid_image_lvl2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/asteroid2.png"), (80, 80)), 55)
asteroid_image_lvl3 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/asteroid3.png"), (80, 80)), 60)
asteroid_images = [asteroid_image_lvl1, asteroid_image_lvl2, asteroid_image_lvl3]

level_text_font = pygame.font.SysFont("Comic Sans", 150, False, False)
level1_text = level_text_font.render("Level 1", 1, (255, 255, 255))
level2_text = level_text_font.render("Level 2", 1, (255, 255, 255))
level3_text = level_text_font.render("Level 3", 1, (255, 255, 255))
level_text = [level1_text, level2_text, level3_text]

heart_image = pygame.transform.scale(pygame.image.load("images/heart.png"), (25, 25))

level_text_font = pygame.font.SysFont("Comic Sans", 150, False, False)
