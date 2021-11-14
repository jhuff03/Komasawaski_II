import pygame
import sys

background_colour = (0, 0, 100)  # rgb colors - this is dark blue
(width, height) = (1280, 720)  # resolution of game window
screen = pygame.display.set_mode((width, height))  # creates screen
screen.fill(background_colour)  # puts color onto screen
pygame.display.flip()  # updates display settings
clock = pygame.time.Clock()

TILE_SIZE = 32
GRAVITY = pygame.math.Vector2(0, 0.3)

coinCount = 0

def main():  # main game
    bulletCooldown = 80

    # list represents level
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                          P",
        "P           |          R                 | P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P   |    R   |                             P",
        "P    PPPPPPPP                              P",
        "P                                          P",
        "P                   S      PPPPPPP         P",
        "P                 PPPPPP                   P",
        "P           ***                            P",
        "P         PPPPPPP                          P",
        "P                          E               P",
        "P                         PP               P",
        "P                     PPPPPP               P",
        "P                                          P",
        "P                                          P",
        "P               ***                        P",
        "P              PPPPP                       P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]

    level_width = len(level[0]) * TILE_SIZE
    level_height = len(level) * TILE_SIZE

    entities = pygame.sprite.Group()  # creates entities group which can be tracked
    players = pygame.sprite.Group()  # creates players group which can be tracked
    platforms = pygame.sprite.Group()  # creates platforms group which can be tracked
    enemies = pygame.sprite.Group()
    hasCollidePhysics = pygame.sprite.Group()
    smartEnemies = pygame.sprite.Group()
    smartEnemyTurnTriggers = pygame.sprite.Group()
    playerKillers = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # build the level
    for row in range(0, len(level)):  # traverse 2d array, put platforms at P and spawns the player at S
        for col in range(0, len(level[0])):
            if level[row][col] == "S":
                Player((col * TILE_SIZE, row * TILE_SIZE), players)
            if level[row][col] == "P":
                Platform((col * TILE_SIZE, row * TILE_SIZE), entities, platforms)
            if level[row][col] == "E":
                Enemy((col * TILE_SIZE, row * TILE_SIZE), entities, enemies, hasCollidePhysics, playerKillers)
            if level[row][col] == "R":
                SmartEnemy((col * TILE_SIZE, row * TILE_SIZE), entities, smartEnemies, playerKillers)
            if level[row][col] == "|":
                SmartEnemyTurnTrigger((col * TILE_SIZE, row * TILE_SIZE), entities, smartEnemyTurnTriggers)
            if level[row][col] == "*":
                Coin((col * TILE_SIZE + 16, row * TILE_SIZE + 16), entities, coins)

    for player in players:
        scroll = [(width / 2) -player.rect.x, (height / 2) - player.rect.y]
        for entity in entities:
            entity.rect.x += scroll[0]
            entity.rect.y += scroll[1]
        player.rect.x = width / 2
        player.rect.y = height / 2

    def killPlayer():
        main()

    running = True
    while running:  # game loop
        clock.tick(100)
        #print("FPS:", int(clock.get_fps()))

        screen.fill(background_colour)  # fills background color every frame

        entities.draw(screen)  # draws every entity every frame
        entities.update()  # updates every entity every frame

        players.draw(screen)  # draws the player every frame
        players.update()  # updates the player every frame

        pygame.display.update()  # updates the screen every frame

        for event in pygame.event.get():  # quits the game if the x button is pushed
            if event.type == pygame.QUIT:
                sys.exit()

        bulletCooldown -= 1


        for player in players:
            scroll = [-int(player.vel.x), -int(player.vel.y)]
            for entity in entities:
                entity.rect.x += scroll[0]
                entity.rect.y += scroll[1]

        for enemy in enemies:
            for platform in platforms:
                if platform.rect.colliderect(enemy.rect.x + 2 * enemy.vel.x, enemy.rect.y, TILE_SIZE,
                                             TILE_SIZE):  # X Collisions
                    if enemy.direction == "left":
                        enemy.direction = "right"
                    else:
                        enemy.direction = "left"

        for collider in hasCollidePhysics:
            for platform in platforms:
                if platform.rect.colliderect(collider.rect.x + 2 * collider.vel.x, collider.rect.y, TILE_SIZE, TILE_SIZE):  # X Collisions
                    collider.vel.x = 0
                if platform.rect.colliderect(collider.rect.x, collider.rect.y + 1.3 * collider.vel.y, TILE_SIZE, TILE_SIZE):  # Y collisions
                    if collider.vel.y >= 0:
                        collider.vel.y = 0

        for smartEnemy in smartEnemies:
            for smartEnemyTurnTrigger in smartEnemyTurnTriggers:
                if smartEnemyTurnTrigger.rect.colliderect(smartEnemy.rect.x, smartEnemy.rect.y + 1.3 * smartEnemy.vel.y, TILE_SIZE, TILE_SIZE):  # Y collisions
                    if smartEnemy.direction == "left":
                        smartEnemy.direction = "right"
                    else:
                        smartEnemy.direction = "left"

        for bullet in bullets:
            if level_width * 5 < bullet.rect.x < 0 - level_width * 5:
                bullet.kill()

        global coinCount
        for player in players:
            for coin in coins:
                if coin.rect.colliderect(player.rect):
                    coinCount += 1
                    coin.kill()
                    #print(coinCount)

        for player in players:
            for playerKiller in playerKillers:
                if playerKiller.rect.colliderect(player.rect):  # Example of general, clipping collisions. This is great for coin or powerup pickups, bullet collisions, or death
                    killPlayer()

            for enemy in enemies:
                if enemy.rect.y == player.rect.y:
                    if(bulletCooldown <= 0):
                        Bullet((enemy.rect.x + 16, enemy.rect.y + 16), enemy.direction, entities, bullets, playerKillers)
                        bulletCooldown = 80

            for platform in platforms:
                for bullet in bullets:
                    if bullet.rect.colliderect(platform.rect):
                        bullet.kill()
                if platform.rect.colliderect(player.rect.x + 2 * player.vel.x, player.rect.y, player.image.get_width(), player.image.get_height()):  # X Collisions
                    player.vel.x = 0
                if platform.rect.colliderect(player.rect.x, player.rect.y + 1.3 * player.vel.y, player.image.get_width(), player.image.get_height()):  # Y collisions
                    if player.vel.y >= 0:
                        player.vel.y = 0
                        player.onGround = True

                    if player.vel.y < 0:
                        player.vel.y = 0
                        player.onGround = False


class Player(pygame.sprite.Sprite):  # player class
    def __init__(self, pos, *groups):  # constructor: uses position and however many groups to construct player
        super().__init__(*groups)  # initializes every single group by adding player to each group
        self.image = pygame.Surface((16, 32))  # creates player as a 16x32 surface
        self.image.fill((255, 255, 255))  # makes the player white
        self.rect = self.image.get_rect(topleft=pos)  # sets the location of the player to the top left corner of the surface

        self.vel = pygame.math.Vector2(0, 0)

        self.speed = 1  # gives speed variable to player
        self.speedMax = 5
        self.onGround = False
        self.jumpStrength = 10

    def update(self):  # keyboard inputs for player
        self.vel += GRAVITY

        keys = pygame.key.get_pressed()  # pygame keyboard handler
        if keys[pygame.K_a]:
            self.vel.x -= self.speed
        if keys[pygame.K_d]:
            self.vel.x += self.speed

        if keys[pygame.K_LSHIFT]:
            self.speedMax = 7
        else:
            self.speedMax = 5

        if keys[pygame.K_SPACE] and self.onGround and self.speedMax == 5:
            self.vel.y -= self.jumpStrength
            self.onGround = False

        if (self.vel.x > self.speedMax):
            self.vel.x = self.speedMax

        if (self.vel.x < -self.speedMax):
            self.vel.x = -self.speedMax

        if (self.vel.y > self.speedMax):
            self.vel.y = self.speedMax

        # FRICTION:
        self.vel.x = (self.vel.x / 1.1)

        # self.rect.x += self.vel.x
        # self.rect.y += self.vel.y


class Platform(pygame.sprite.Sprite):  # similar to player class but for platforms
    def __init__(self, pos, *groups):  # constructs platforms
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))  # platforms are 32x32 and only to be placed every 32 pixels.
        self.image.fill((255, 0, 0))  # red
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 69, 0))
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left

        self.speed = 1
        self.vel = pygame.math.Vector2(0, 0)
        self.direction = "left"

        if (self.direction == "right"):
            self.rect.x += 32

    def update(self):
        self.vel += GRAVITY
        if (self.direction == "left"):
            self.vel.x = -3
        else:
            self.vel.x = 3

        self.rect.x += self.vel.x
        self.rect.y += self.vel.y


class SmartEnemy(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 200, 0))
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left

        self.speed = 1
        self.vel = pygame.math.Vector2(0, 0)
        self.direction = "left"

    def update(self):

        if (self.direction == "left"):
            self.vel.x = -3
        else:
            self.vel.x = 3

        self.rect.x += self.vel.x
        self.rect.y += self.vel.y


class SmartEnemyTurnTrigger(pygame.sprite.Sprite):  # These allow the level builder to place triggers to turn around the smart enemies wherever they want
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)  # SRCALPHA allows for the tile to be transparent
        self.image.fill((0, 0, 0, 0))  # The last zero is the transparency
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((8, 8))  # coins are 8x8 and only to be placed every 32 pixels.
        self.image.fill((255, 255, 0))  # yellow
        self.rect = self.image.get_rect(center=pos)  # coords assigned to center

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((8, 8))
        self.image.fill((200, 200, 200))  # gray
        self.rect = self.image.get_rect(center=pos)  # coords assigned to center

        self.speed = 10
        self.vel = pygame.math.Vector2(0, 0)

        if(direction == "right"):
            self.vel.x = self.speed
        if (direction == "left"):
            self.vel.x = -self.speed

        if (direction == "up"):
            self.vel.y = -self.speed
        if (direction == "down"):
            self.vel.x = self.speed

    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y


main()
