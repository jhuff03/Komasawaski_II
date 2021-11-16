import pygame
import sys

background_colour = (50, 50, 50)  # rgb colors - this is dark blue
(width, height) = (1280, 720)  # resolution of game window
screen = pygame.display.set_mode((width, height))  # creates screen
screen.fill(background_colour)  # puts color onto screen
pygame.display.flip()  # updates display settings
clock = pygame.time.Clock()

TILE_SIZE = 32
GRAVITY = pygame.math.Vector2(0, 0.3)

coinCount = 0


def main():  # main game
    global coinCount
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
        "P                                 J        P",
        "P                                          P",
        "P                                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]

    level_width = len(level[0]) * TILE_SIZE
    level_height = len(level) * TILE_SIZE

    entities = pygame.sprite.Group()  # creates entities group which can be tracked
    players = pygame.sprite.Group()  # creates players group which can be tracked
    platforms = pygame.sprite.Group()  # creates platforms group which can be tracked
    enemies = pygame.sprite.Group()  # the rest of these should be self-explanatory
    hasCollidePhysics = pygame.sprite.Group()
    smartEnemies = pygame.sprite.Group()
    smartEnemyTurnTriggers = pygame.sprite.Group()
    playerKillers = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    playerKillables = pygame.sprite.Group()  # list of all things that can have their health lowered by the player firing bullets at them
    playerBullets = pygame.sprite.Group()
    miniBosses = pygame.sprite.Group()

    # build the level
    for row in range(0, len(level)):  # traverse 2d array, put platforms at P and spawns the player at S
        for col in range(0, len(level[0])):
            if level[row][col] == "S":
                Player((col * TILE_SIZE, row * TILE_SIZE), players)
            if level[row][col] == "P":
                Platform((col * TILE_SIZE, row * TILE_SIZE), entities, platforms)
            if level[row][col] == "E":
                Enemy((col * TILE_SIZE, row * TILE_SIZE), entities, enemies, hasCollidePhysics, playerKillers, playerKillables)
            if level[row][col] == "R":
                SmartEnemy((col * TILE_SIZE, row * TILE_SIZE), entities, smartEnemies, playerKillers, playerKillables)
            if level[row][col] == "|":
                SmartEnemyTurnTrigger((col * TILE_SIZE, row * TILE_SIZE), entities, smartEnemyTurnTriggers)
            if level[row][col] == "*":
                Coin((col * TILE_SIZE + 16, row * TILE_SIZE + 16), entities, coins)
            if level[row][col] == "J":
                MiniBoss((col * TILE_SIZE + 16, row * TILE_SIZE + 16), entities, enemies, hasCollidePhysics, miniBosses, playerKillers, playerKillables)

    for player in players:
        scroll = [(width / 2) - player.rect.x, (height / 2) - player.rect.y]  # set the initial offset of the level before the game loop
        for entity in entities:
            entity.rect.x += scroll[0]  # move everything to be aligned with the offset
            entity.rect.y += scroll[1]
        player.rect.x = width / 2  # center the player in the screen
        player.rect.y = height / 2

    def killPlayer():
        main()

    running = True
    while running:  # game loop
        clock.tick(100)  # set the FPS to 100
        # print("FPS:", int(clock.get_fps())) # print the FPS to the logs

        screen.fill(background_colour)  # fills background color every frame

        entities.draw(screen)  # draws every entity every frame
        entities.update()  # updates every entity every frame

        players.draw(screen)  # draws the player every frame
        players.update()  # updates the player every frame

        pygame.display.update()  # updates the screen every frame

        for event in pygame.event.get():  # quits the game if the x button is pushed
            if event.type == pygame.QUIT:
                sys.exit()

        bulletCooldown -= 1  # each frame of the game, lower the cooldown of the enemy being able to shoot again

        """
        Below is the scrolling code and technically the movement code of the player. Instead of moving the player around 
        within the level, everything else in the level is moved instead to give the illusion of player movement.
        """
        for player in players:  # access the player's "velocity" even though the player never really moves
            scroll = [-int(player.vel.x), -int(player.vel.y)]
            for entity in entities:
                entity.rect.x += scroll[0]  # move everything other than the player by that velocity
                entity.rect.y += scroll[1]

        for enemy in enemies:  # handle enemy / platform collisions for enemy turnaround
            for platform in platforms:
                if platform.rect.colliderect(enemy.rect.x + 2 * enemy.vel.x, enemy.rect.y, enemy.rect.width, enemy.rect.height):  # X Collisions
                    if enemy.direction == "left":
                        enemy.direction = "right"
                        enemy.vel.x = 0
                    else:
                        enemy.direction = "left"
                        enemy.vel.x = 0

        for collider in hasCollidePhysics:  # handle non-player collisions. Any entity in the hasCollidePhysics group will collide with floors and walls
            for platform in platforms:
                if platform.rect.colliderect(collider.rect.x + 2 * collider.vel.x, collider.rect.y, collider.rect.width, collider.rect.height):  # X Collisions
                    collider.vel.x = 0
                if platform.rect.colliderect(collider.rect.x, collider.rect.y + 1.3 * collider.vel.y, collider.rect.width, collider.rect.height):  # Y collisions
                    if collider.vel.y >= 0:
                        collider.vel.y = 0

                    if collider.vel.y < 0:
                        collider.vel.y = 0

        for smartEnemy in smartEnemies:  # make sure that smartEnemies turn around when they encounter the invisible turn around flag
            for smartEnemyTurnTrigger in smartEnemyTurnTriggers:
                if smartEnemyTurnTrigger.rect.colliderect(smartEnemy.rect.x, smartEnemy.rect.y + 1.3 * smartEnemy.vel.y, TILE_SIZE, TILE_SIZE):  # Y collisions
                    if smartEnemy.direction == "left":
                        smartEnemy.direction = "right"
                    else:
                        smartEnemy.direction = "left"

        for bullet in bullets:  # bullet overflow protection
            if level_width * 5 < bullet.rect.x < 0 - level_width * 5:
                bullet.kill()

        for playerBullet in playerBullets:
            for playerKillable in playerKillables:
                if playerBullet.rect.colliderect(playerKillable.rect):  # Everything that can be killed by the player MUST have a health variable even if it is just 1
                    playerKillable.health -= 1
                    playerBullet.kill()
                if playerKillable.health <= 0:
                    playerKillable.kill()

        """
        All of the player's interactions should be handled below
        """
        for player in players:
            for coin in coins:
                if coin.rect.colliderect(player.rect):
                    coinCount += 1
                    coin.kill()
                    # print(coinCount)
            if pygame.mouse.get_pressed() == (True, False, False) and player.shotCooldown <= 0:  # Shoot on right click and only right click. True False False represents only right click out of the three mouse buttons
                Bullet((player.rect.x + 8, player.rect.y + 16), player.direction, not pygame.key.get_pressed()[pygame.K_w], entities, bullets, playerBullets)
                player.shotCooldown = 20

            for playerKiller in playerKillers:
                if playerKiller.rect.colliderect(player.rect):  # Example of general, clipping collisions. This is great for coin or powerup pickups, bullet collisions, or death
                    killPlayer()

            for enemy in enemies:  # Handle when enemies fire
                if enemy.rect.y == player.rect.y:
                    if bulletCooldown <= 0:
                        Bullet((enemy.rect.x + 16, enemy.rect.y + 16), enemy.direction, True, entities, bullets, playerKillers)  # spawn new bullet at the enemy's center, going in the enemy's direction
                        bulletCooldown = 80

            for platform in platforms:  # Destroy bullets on contact with platforms
                for bullet in bullets:
                    if bullet.rect.colliderect(platform.rect):
                        bullet.kill()
                """
                Here is where all of the player's collisions are handled. If the player attempts to move into another
                platform (A platform is a group that keeps track of anything that should have collisions, the player's
                movement his halted in that direction.
                """
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
        self.rect = self.image.get_rect(
            topleft=pos)  # sets the location of the player to the top left corner of the surface

        self.vel = pygame.math.Vector2(0, 0)
        self.onGround = False
        self.direction = "left"
        self.shotCooldown = 20

        self.animationCooldown = 15
        self.animationState = 0

        self.speed = 1  # gives speed variable to player
        self.speedMax = 5
        self.jumpStrength = 10.2

    def update(self):  # keyboard inputs for player
        self.shotCooldown -= 1

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

        if keys[pygame.K_SPACE] and self.onGround:
            self.vel.y -= self.jumpStrength
            self.onGround = False

        if self.vel.x > self.speedMax:
            self.vel.x = self.speedMax

        if self.vel.x < -self.speedMax:
            self.vel.x = -self.speedMax

        if self.vel.y > self.speedMax:
            self.vel.y = self.speedMax

        if self.vel.x > 0:
            self.direction = "right"
        if self.vel.x < 0:
            self.direction = "left"

        # FRICTION:
        self.vel.x = (self.vel.x / 1.1)  # Apply friction to the movement of the player by slowly lowering it's velocity

        self.animate()

    def animate(self):
        if int(self.vel.x) == 0:
            self.image = pygame.image.load('assets/player.png')
        elif self.direction == "right":
            self.animationCooldown -= 1

            if self.animationCooldown <= 0:
                self.animationState += 1
                self.animationCooldown = 15

            if self.animationState == 0:
                self.image = pygame.image.load('assets/player_run_1.png')
            if self.animationState == 1:
                self.image = pygame.image.load('assets/player_run_2.png')
            if self.animationState == 2:
                self.image = pygame.image.load('assets/player_run_3.png')
            if self.animationState == 3:
                self.image = pygame.image.load('assets/player_run_2.png')
                self.animationState = 0
        elif self.direction == "left":
            self.animationCooldown -= 1

            if self.animationCooldown <= 0:
                self.animationState += 1
                self.animationCooldown = 15

            if self.animationState == 0:
                self.image = pygame.transform.flip(pygame.image.load('assets/player_run_1.png'), True, False)
            if self.animationState == 1:
                self.image = pygame.transform.flip(pygame.image.load('assets/player_run_2.png'), True, False)
            if self.animationState == 2:
                self.image = pygame.transform.flip(pygame.image.load('assets/player_run_3.png'), True, False)
            if self.animationState == 3:
                self.image = pygame.transform.flip(pygame.image.load('assets/player_run_2.png'), True, False)
                self.animationState = 0


class Platform(pygame.sprite.Sprite):  # similar to player class but for platforms
    def __init__(self, pos, *groups):  # constructs platforms
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))  # platforms are 32x32 and only to be placed every 32 pixels.
        self.image = pygame.image.load('assets/tile.png')
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 69, 0))
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left

        self.health = 1

        self.speed = 3
        self.vel = pygame.math.Vector2(0, 0)
        self.direction = "left"  # set default direction

    def update(self):
        self.vel += GRAVITY
        if self.direction == "left":
            self.vel.x = -self.speed
        else:
            self.vel.x = self.speed

        self.rect.x += self.vel.x  # apply velocity
        self.rect.y += self.vel.y


class SmartEnemy(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 200, 0))
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left

        self.health = 5

        self.speed = 2
        self.vel = pygame.math.Vector2(0, 0)
        self.direction = "left"

    def update(self):

        if self.direction == "left":
            self.vel.x = -self.speed
        else:
            self.vel.x = self.speed

        self.rect.x += self.vel.x
        self.rect.y += self.vel.y


class SmartEnemyTurnTrigger(pygame.sprite.Sprite):  # These allow the level builder to place triggers to turn around the smart enemies wherever they want. Smart enemies will always turn on contact with these triggers
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)  # SRCALPHA allows for the tile to be transparent
        self.image.fill((0, 0, 0, 0))  # The last zero is the transparency
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((8, 8))  # coins are 8x8 and only to be placed every 32 pixels.
        self.image = pygame.image.load('assets/coin.png')
        self.rect = self.image.get_rect(center=pos)  # coords assigned to center


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, straight, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((8, 8))
        self.image.fill((200, 200, 200))  # gray
        self.rect = self.image.get_rect(center=pos)  # coords assigned to center

        self.speed = 10
        self.vel = pygame.math.Vector2(0, 0)

        if direction == "right":
            self.vel.x = self.speed
        if direction == "left":
            self.vel.x = -self.speed

        if direction == "up":
            self.vel.y = -self.speed
        if direction == "down":
            self.vel.x = self.speed

        if not straight:
            self.vel.y -= self.speed

    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y


class MiniBoss(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):  # constructs miniboss
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((64, 64))  # boss is 64x64
        self.image.fill((255, 0, 0))  # red - placeholder texture
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left

        self.health = 15
        self.jumpStrength = 15
        self.jumpCooldown = 200
        self.speed = 2
        self.vel = pygame.math.Vector2(0, 0)
        self.direction = "left"  # set default direction

    def update(self):
        self.jumpCooldown -= 1
        self.vel += GRAVITY
        if self.jumpCooldown <= 0:
            self.vel.y -= self.jumpStrength
            self.jumpCooldown = 200
        if self.direction == "left":
            self.vel.x = -self.speed
        else:
            self.vel.x = self.speed

        self.rect.x += self.vel.x  # apply velocity
        self.rect.y += self.vel.y


main()  # run the main game loop
