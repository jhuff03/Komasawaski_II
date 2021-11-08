import pygame

background_colour = (0, 0, 100)
(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
pygame.display.flip()


def main():
    running = True

    entities = pygame.sprite.Group()
    player = Player((0,0), entities)

    while running:
        screen.fill(background_colour)

        entities.draw(screen)
        entities.update()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos)

        self.speed = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

main()