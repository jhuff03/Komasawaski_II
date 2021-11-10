import pygame

GRAVITY = pygame.math.Vector2(0, 0.3)

background_colour = (0, 0, 100) # rgb colors - this is dark blue
(width, height) = (1280, 720) # resolution of game window
screen = pygame.display.set_mode((width, height)) # creates screen
screen.fill(background_colour) # puts color onto screen
pygame.display.flip() # updates display settings

TILE_SIZE = 32
clock = pygame.time.Clock()


def main(): # main game

# list represents level
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P    PPPPPPPP                              P",
        "P                     S                    P",
        "P                          PPPPPPP         P",
        "P                 PPPPPP                   P",
        "P                                          P",
        "P         PPPPPPP                          P",
        "P                                          P",
        "P                         PP               P",
        "P                     PPPPPP               P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P              PPPPP                       P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]

    level_width = len(level[0]) * TILE_SIZE
    level_height = len(level) * TILE_SIZE

    entities = pygame.sprite.Group()  # creates entities group which can be tracked
    players = pygame.sprite.Group() # creates players group which can be tracked
    platforms = pygame.sprite.Group() # creates platforms group which can be tracked

    # build the level
    for row in range(0, len(level)): # traverse 2d array, put platforms at P and spawns the player at S
        for col in range(0, len(level[0])):
            if level[row][col] == "S":
                Player((col * TILE_SIZE, row * TILE_SIZE), entities, players)
            if level[row][col] == "P":
                Platform((col * TILE_SIZE, row * TILE_SIZE), entities, platforms)

    running = True

    while running: # game loop
        clock.tick(100)
        print("FPS:", int(clock.get_fps()))

        screen.fill(background_colour) # fills background color every frame

        entities.draw(screen) # draws every entity every frame
        entities.update() # updates every entity every frame

        pygame.display.update() # updates the screen every frame

        for event in pygame.event.get(): # quits the game if the x button is pushed
            if event.type == pygame.QUIT:
                running = False



        for player in players:
            for platform in platforms:
                if platform.rect.colliderect(player.rect.x + 2 * player.vel.x, player.rect.y, TILE_SIZE, TILE_SIZE): #X Collisions
                    player.vel.x = 0
                if platform.rect.colliderect(player.rect.x, player.rect.y + 1.3 * player.vel.y, TILE_SIZE, TILE_SIZE): #Y collisions
                    if player.vel.y >= 0:
                        player.vel.y = 0
                        player.onGround = True

                    if player.vel.y < 0:
                        player.vel.y = 0
                        player.onGround = False









class Player(pygame.sprite.Sprite): # player class
    def __init__(self, pos, *groups): # constructor: uses position and however many groups to construct player
        super().__init__(*groups) # initializes every single group by adding player to each group
        self.image = pygame.Surface((32, 32)) # creates player as a 32x32 surface
        self.image.fill((255, 255, 255)) # makes the player white
        self.rect = self.image.get_rect(topleft=pos) # sets the location of the player to the top left corner of the surface


        self.vel = pygame.math.Vector2(0, 0)


        self.speed = 1 # gives speed variable to player
        self.speedMax = 5
        self.onGround = False
        self.jumpStrength = 10

    def update(self): # keyboard inputs for player
        self.vel += GRAVITY

        keys = pygame.key.get_pressed() # pygame keyboard handler
        if keys[pygame.K_a]:
            self.vel.x -= self.speed
        if keys[pygame.K_d]:
            self.vel.x += self.speed

        if keys[pygame.K_LCTRL]:
            self.speedMax = 7
        else:
            self.speedMax = 5


        if keys[pygame.K_SPACE] and self.onGround and self.speedMax == 5:
            self.vel.y -= self.jumpStrength
            self.onGround = False

        if (self.vel.x > self.speedMax):
            self.vel.x = self.speedMax

        if(self.vel.x < -self.speedMax):
            self.vel.x = -self.speedMax

        if (self.vel.y > self.speedMax):
            self.vel.y = self.speedMax

        # if (self.vel.y < -self.speedMax):
        #     self.vel.y = -self.speedMax

        # FRICTION:
        self.vel.x = (self.vel.x / 1.1)

        self.rect.x += int(self.vel.x)
        self.rect.y += int(self.vel.y)




class Platform(pygame.sprite.Sprite): # similar to player class but for platforms
    def __init__(self, pos, *groups): # constructs platforms
        super().__init__(*groups) # initializes groups
        self.image = pygame.Surface((32, 32)) # platforms are 32x32 and only to be placed every 32 pixels.
        self.image.fill((255, 0, 0)) # red
        self.rect = self.image.get_rect(topleft=pos) # coords assigned to top left


main()