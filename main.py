import pygame

background_colour = (0, 0, 100) # rgb colors - this is dark blue
(width, height) = (1280, 720) # resolution of game window
screen = pygame.display.set_mode((width, height)) # creates screen
screen.fill(background_colour) # puts color onto screen
pygame.display.flip() # updates display settings

TILE_SIZE = 32

def main(): # main game


    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                    PPPPPPPPPPP           P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P    PPPPPPPP                              P",
        "P                                          P",
        "P                          PPPPPPP         P",
        "P                 PPPPPP                   P",
        "P                                          P",
        "P         PPPPPPP                          P",
        "P                                          P",
        "P                     PPPPPP               P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "PS                                         P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]

    level_width = len(level[0]) * TILE_SIZE
    level_height = len(level) * TILE_SIZE

    entities = pygame.sprite.Group()  # creates entities group which can be tracked
    players = pygame.sprite.Group()
    platforms = pygame.sprite.Group()

    # build the level
    for row in range(0, len(level)):
        for col in range(0, len(level[0])):
            if level[row][col] == "S":
                Player((col * TILE_SIZE, row * TILE_SIZE), entities, players)  # player (0,0 is the spawn location, entities is the group it is in)
            if level[row][col] == "P":
                Platform((col * TILE_SIZE, row * TILE_SIZE), entities, platforms)

    running = True

    while running: # game loop
        screen.fill(background_colour) # fills background color every frame

        entities.draw(screen) # draws every entity every frame
        entities.update() # updates every entity every frame

        pygame.display.update() # updates the screen every frame

        for event in pygame.event.get(): # quits the game if the x button is pushed
            if event.type == pygame.QUIT:
                running = False


class Player(pygame.sprite.Sprite): # player class
    def __init__(self, pos, *groups): # constructor: uses position and however many groups to construct player
        super().__init__(*groups) # initializes every single group by adding player to each group
        self.image = pygame.Surface((32, 32)) # creates player as a 32x32 surface
        self.image.fill((255, 255, 255)) # makes the player white
        self.rect = self.image.get_rect(topleft=pos) # sets the location of the player to the top left corner of the surface

        self.speed = 1 # gives speed variable to player

    def update(self): # keyboard inputs for player
        keys = pygame.key.get_pressed() # pygame keyboard handler
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        # these if statements adjust the coordinates of the player based on WASD movements
        # 1 pixel per frame per speed setting (default speed is 1)

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)


main()