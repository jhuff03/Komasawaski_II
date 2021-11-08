import pygame

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

