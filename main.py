import pygame
import sys
import random

pygame.init()

background_colour = (100, 100, 100)  # rgb colors - this is dark gray
(width, height) = (1280, 720)  # resolution of game window
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)  # creates screen
screen.fill(background_colour)  # puts color onto screen
pygame.display.flip()  # updates display settings
clock = pygame.time.Clock()
pygame.display.set_caption("Komasawaski II")
Icon = pygame.image.load("assets/pistol_icon.png")
pygame.display.set_icon(Icon)


TILE_SIZE = 32
GRAVITY = pygame.math.Vector2(0, 0.3)
kFont = pygame.font.Font("assets/font/5x5.ttf", 30)
bigkFont = pygame.font.Font("assets/font/5x5.ttf", 80)

coinCount = 0

lives = 5
scorecount = 0
deflevel = 1
pistolAmmo = 25
akAmmo = 5

def gameBegin():
    running = True
    while running:  # game loop
        clock.tick(100)  # set the FPS to 100
        #print("FPS:", int(clock.get_fps())) # print the FPS to the logs

        screen.fill((0,0,0))  # fills background color every frame
        startScreen = pygame.image.load("assets/start.png")
        screen.blit(startScreen, (0, 0))
        startText = bigkFont.render("KOMASAWASKI II", True, (255, 255, 255))
        screen.blit(startText, (330, 60))
        enterToContinue = kFont.render("Press Enter to Begin", True, (255, 255, 255))
        screen.blit(enterToContinue, (485, 670))

        pygame.display.update()

        keys = pygame.key.get_pressed()  # pygame keyboard handler
        if keys[pygame.K_RETURN]:
            return
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        for event in pygame.event.get():  # quits the game if the x button is pushed
            if event.type == pygame.QUIT:
                sys.exit()

def gameOver():
    global deflevel
    global lives
    global scorecount
    global pistolAmmo
    global akAmmo
    global coinCount

    running = True
    while running:  # game loop
        clock.tick(100)  # set the FPS to 100
        #print("FPS:", int(clock.get_fps())) # print the FPS to the logs

        screen.fill((0,0,0))  # fills background color every frame
        gameOver = bigkFont.render("GAME OVER", True, (255, 255, 255))
        screen.blit(gameOver, (440, 300))
        enterToContinue = kFont.render("Press Enter to Continue", True, (255, 255, 255))
        screen.blit(enterToContinue, (450, 620))

        pygame.display.update()

        keys = pygame.key.get_pressed()  # pygame keyboard handler
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if keys[pygame.K_RETURN]:
            coinCount = 0
            lives = 5
            scorecount = 0
            deflevel = 1
            pistolAmmo = 25
            akAmmo = 5

            main()

        for event in pygame.event.get():  # quits the game if the x button is pushed
            if event.type == pygame.QUIT:
                sys.exit()

def victory():
    global deflevel
    global lives
    global scorecount
    global pistolAmmo
    global akAmmo
    global coinCount

    running = True
    while running:  # game loop
        clock.tick(100)  # set the FPS to 100
        # print("FPS:", int(clock.get_fps())) # print the FPS to the logs

        screen.fill((0,0,0))  # fills background color
        victory = bigkFont.render("CONGRATS! You Win!", True, (255, 255, 255))
        screen.blit(victory, (280, 300))
        playAgain = kFont.render("Press Enter to Continue", True, (255, 255, 255))
        screen.blit(playAgain, (430, 620))

        pygame.display.update()

        keys = pygame.key.get_pressed()  # pygame keyboard handler
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if keys[pygame.K_RETURN]:
            deflevel += 1
            pistolAmmo = 25
            akAmmo = 5
            main()

        for event in pygame.event.get():  # quits the game if the x button is pushed
            if event.type == pygame.QUIT:
                sys.exit()

def credits():
    running = True
    while running:  # game loop
        clock.tick(100)  # set the FPS to 100
        # print("FPS:", int(clock.get_fps())) # print the FPS to the logs

        screen.fill((0,0,0))  # fills background color

        startText = bigkFont.render("KOMASAWASKI II", True, (255, 255, 255))
        screen.blit(startText, (330, 60))

        end = kFont.render("Created by William F. Cunnion and Jonas B. Huff", True, (255, 255, 255))
        screen.blit(end, (280, 300))

        trial = kFont.render("This is a trial version", True, (255, 255, 255))
        screen.blit(trial, (430, 420))

        trial = kFont.render("More levels coming soon", True, (255, 255, 255))
        screen.blit(trial, (423, 470))

        pygame.display.update()

        keys = pygame.key.get_pressed()  # pygame keyboard handler
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        for event in pygame.event.get():  # quits the game if the x button is pushed
            if event.type == pygame.QUIT:
                sys.exit()


def main():  # main game
    global coinCount
    global scorecount
    global lives
    global deflevel
    global pistolAmmo
    global akAmmo

    ammoGeneration = 500

    # list represents level
    if deflevel == 1:
        level = [
            "      =    =   =                                =                                                                                                                                                     ",
            "      =    =   =                                =                                                                                                                                                     ",
            "      =    =   =                                =       =                                                                                                                                             ",
            "      =    =   =                                =       =                                                                                                                                             ",
            "      =    =   =                                =       =                                                                                                                                             ",
            "      =    =   =                                =       =               = =                                                                                                                           ",
            "      =    =   =                                =       =               = =                                                                                                                           ",
            "      =    =   =                                =       =               = =                                                                                                                           ",
            "      =    =   =                                =       =               = =                                                                                                                           ",
            "      =    =   =                                =       =               = =                                                                                                                           ",
            "]     =    =   =                                =       =               = =                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP        ",
            "]     =    =|  =       R                 |      =       =               = =                                                                | =               =   =     =    =   =            P        ",
            "]     =    =   =                                =       =               = =                                                                | =               =   =     =    =   =            P        ",
            "]     =    =   =                                =       =               = =                                                                | =               =   =     =    =   =            P        ",
            "]     =    =   =                                =       =               = =                                                                | =               =   =     =    =   =            P        ",
            "]     =    =   =                                =       =               = =                                                                | =               =   =     =    =   =            P        ",
            "]   | =R > = | =                                =       =               = =                                                                | =               =   =     =    =   =            P        ",
            "]    PPPPPPPP  =                                =       =               = =                                                                | =               =***=     =    =   =            P        ",
            "]          =   =                                =       =               = =                                                                | =              PPPPPPP    = ** =   =            P        ",
            "]          =   =    S>                       |  =  R    =               = =                  |                                             | =               =   =     PPPPPP   =            P        ",
            "]          =   =  PPPPPP                        =       =               = =                                                                | =               =   =              =            P        ",
            "]          =***=  =    =                        =       =               = =                                                                | =               =   =              =            P        ",
            "]         PPPPPPP =    =                        =       =               = =                                                 <              | =               =   =              =            P        ",
            "]                 =    =   E                    =       =               = =                                               PPPPP            | =               =   =             PPP           P        ",
            "]                 =    =  CC                    =       =               = =                                 **>**          = =             | =               =   =                           P        ",
            "]                 =   PPPPPP                    =       =         |     =>=           R       |           PPPPPPPPP        = =             | =               =   =                           P        ",
            "]                 =    =  =                     =       =              PPPPP          <                    =     =         = =             | =               =   =      PPPP                 P        ",
            "]                 =    =  =               <     =       =               = =         |*R*|                  =     =    >    = =             | =              PPPPPPP     =  =      J          P        ",
            "]                >=    =  =             PPPPP   =       =               = =          PPP                   =     =   PPP   =>=             | =                          =  =                 P        ",
            "]              PPPPP   =  =              = =    =       =               = =           =                    =     =    =   PPPPP            | =                          =  =                 PPPPPPPPP",
            "]               = =    =  =              = =    =       =            PPPPPPPPP        =                   PPPPPPPPP   =    = =         C   | =     PPP                  =  =         *        ;      P",
            "]               = =    =  =              = =    =     * P *                           =                    =     =    =    = =        CC   | =    C =                   =  =        *C        ;      P",
            "]               = = >  =  =              PPP    =     P P P                        C  =        E           =     =    =    = =       CCC   | =   CC =                   =  =       CCCC       ;  ^   P",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  PPP   PPPPPPP|       -           |PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]

    elif deflevel == 2:
        level = [
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                       PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                              ",
            "                                                                                                                                       P                                                    P                              ",
            "                                                                                                                                       P                                                    P                              ",
            "                                                                                                                                       P                                                    P                              ",
            "]                                                                                                                                      P                                                    P                              ",
            "]                                                                                                                                      P                         * ^ *                      P                              ",
            "]                                                                                                                                      P                      PPPPPPPPPPP                   P                              ",
            "]                                                                                                                                      P                      ; =     = ;                   P                              ",
            "]                                            |                    R                     |                                              P                      ; =     = ;                   P                              ",
            "]                                                                                                                                      P                      ; =     = ;                   P                              ",
            "]                                                                                                                                      PPPPPPPPPPPPPPPPPPPPPPPPPP     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "]                                                                                                                                        =                                       |              =  =                      P",
            "]                                                                                                                                        =                                       |              =  =                      P",
            "]                                                               S    C >                                                                 =                       PPPPP           |              =  =                      P",
            "]                                                            PPPPPPPPPPPPP                                                               =                        = =            |              =  =                      P",
            "]                                                             =         =         *****                                                  =                        = =            |              =  =       *              P",
            "]                                                             =         =       PPPPPPPPP                                                =                 *CC    = =            |              =  =C     PPP             P",
            "]                                                             =         =        =     =         ******                                  =                PPPPP   = =            |            PPPPPPPP    = =             P",
            "]                                                             =         =        =     =        PPPPPPPP                                 =                  =     = =            |              =  =      = =             P",
            "]                                                             =         =        =     =         =    =       >                          =                  =     = =            |              =  =      = =   J         P",
            "]                                                             =         =        =     =         =    =      PPP                         =                  =     =>=            |              =  =      =*=             P",
            "]      |    R                                        |        =    >R   =        =     =      R  =    =       =    |                     =                  =    PPPPP           |              =  =     PPPPP            P",
            "]                                                            PPPPPPPPPPPPP       =     =         =    =       =                          =                  =     = =            |              =  =      = =             P",
            "]                                                             =         =        =     =        PPPPPPPP      =                          =                 PPP    = =            |              =  =      = =             P",
            "]                                                             =         =       PPPPPPPPP        =    =       =                          =                  =     = =      C     |     PPP      PPPP      = =             P",
            "]    *                                         C              =         =        =     =         =    =       =                       C  =                  =     = =     CC     |      =                 = =             P",
            "]  <*<*<                                      CC       E      =         =        =     =    >    =    =       =         E            CCC =         E     C  =  >  = =    CCC     |      =                 = =             P",
            "PPPPPPPPPP|       -                        |PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]

    elif deflevel == 3:
        level = [
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "                                                                                                                                                                                                                           ",
            "]                                                         =   =                                                                                                                                                           ]",
            "]                                                         =   =                                                                                                                                                           ]",
            "]                                                         =   =                                                                                                                                                           ]",
            "]                                                         =   =                                                                                                                                                           ]",
            "]                                                         =   =                                                                                                                                                           ]",
            "]                                                      |  =   =                                                                                                                                                           ]",
            "]                                                      |  =   =                                                                                                                                                           ]",
            "]                                                      |  =   =                                                                                                                                                           ]",
            "]                                                      |  =   =                                                                                                                                                           ]",
            "]                                                      |  =   =                                         *                                                                   <                                             ]",
            "]                                                      |  =   =                                      > *** >                                                              PPPPP                                           ]",
            "]                       ***                            |  =   =                                     PPPPPPPPP                                                              = =                                            ]",
            "]                     PPPPPPP                          |  =   =                                      =     =                                                               = =                                            ]",
            "]   | R                =   =                           |  =   =                                      =     =                                                               =>= *******                                    ]",
            "]                      =   =                           |  =   =                                   >**=     =**>                                                           PPPPPPPPPPPPP                                   ]",
            "]                      =***=         J                 |  =   =                                   PPPPP   PPPPP                                                            =         =                                    ]",
            "]                 PPPPPPPPPPP                          |  =   =                |R                  = =     = =                  R|                                ****     =         =                                    ]",
            "]                  =   =   =                           |  =   =                                    = =     = =                                                   PPPPPP    =         =                                    ]",
            "]       ****       =   =   =               *           |  =***=                     ***            =*=  S  =*=                      |     R              <        =  =     =   |     =           *******                  ]",
            "]      PPPPPP      =   =   =              PPP          | PPPPPPP                  PPPPPPP         PPPPPPPPPPPPP                                        PPPPP      =  =     =         =          PPPPPPPPP                 ]",
            "]       =  =       =   =   =               =           |            C              =   =          ;           ;                     *                   = =       =  =     =         =           =     =                  ]",
            "]       =  =       =   =   =               =           |            CC             =   =          ;           ;                    *C*                  = =       =  =     =         =           =     =                  ]",
            "]       =  =       =***=***=               =           |            CCC            =   =       C  ; *E* ^ * * ;  C                *CCC*    E     E   C  = =  E    =  =     =    C    =           =     =       E          ]",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP|-            |PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]

    else:
        credits()

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
    playerPistolBullets = pygame.sprite.Group()
    playerAKBullets = pygame.sprite.Group()
    miniBosses = pygame.sprite.Group()
    smartPlatforms = pygame.sprite.Group()
    tt30AmmoPickups = pygame.sprite.Group()
    akAmmoPickups = pygame.sprite.Group()
    blueKeyCards = pygame.sprite.Group()
    turners = pygame.sprite.Group()
    blueDoors = pygame.sprite.Group()
    trophies = pygame.sprite.Group()


    # build the level
    for row in range(0, len(level)):  # traverse 2d array, put platforms at P and spawns the player at S
        for col in range(0, len(level[0])):
            if level[row][col] == "S":
                Player((col * TILE_SIZE, row * TILE_SIZE), players)
            if level[row][col] == "P":
                Platform((col * TILE_SIZE, row * TILE_SIZE), entities, platforms)
            if level[row][col] == "C":
                Crate((col * TILE_SIZE, row * TILE_SIZE), entities, platforms)
            if level[row][col] == "]":
                Barrier((col * TILE_SIZE, row * TILE_SIZE), entities, platforms)
            if level[row][col] == "E":
                Enemy((col * TILE_SIZE, row * TILE_SIZE), entities, enemies, turners, hasCollidePhysics, playerKillers, playerKillables)
            if level[row][col] == "R":
                SmartEnemy((col * TILE_SIZE, row * TILE_SIZE), entities, smartEnemies, playerKillers, playerKillables)
            if level[row][col] == "|":
                SmartEnemyTurnTrigger((col * TILE_SIZE, row * TILE_SIZE), entities, smartEnemyTurnTriggers)
            if level[row][col] == "*":
                Coin((col * TILE_SIZE + 16, row * TILE_SIZE + 16), entities, coins)
            if level[row][col] == "J":
                MiniBoss((col * TILE_SIZE + 16, row * TILE_SIZE + 16), entities, hasCollidePhysics, miniBosses, playerKillers, playerKillables, turners)
            if level[row][col] == "=":
                Support((col * TILE_SIZE, row * TILE_SIZE), entities)
            if level[row][col] == ">":
                Ammo((col * TILE_SIZE, row * TILE_SIZE), entities, tt30AmmoPickups)
            if level[row][col] == "<":
                AKAmmo((col * TILE_SIZE, row * TILE_SIZE), entities, akAmmoPickups)
            if level[row][col] == "-":
                MovingPlatform((col * TILE_SIZE, row * TILE_SIZE), entities, smartEnemies, platforms, smartPlatforms)
            if level[row][col] == ";":
                BlueDoor((col * TILE_SIZE, row * TILE_SIZE), entities, platforms, blueDoors)
            if level[row][col] == "^":
                Trophy((col * TILE_SIZE, row * TILE_SIZE), entities, trophies)

    for player in players:
        totalYScroll = player.rect.y
        scroll = [(width / 2) - player.rect.x, (height / 2) - player.rect.y]  # set the initial offset of the level before the game loop
        for entity in entities:
            entity.rect.x += scroll[0]  # move everything to be aligned with the offset
            entity.rect.y += scroll[1]
        player.rect.x = width / 2  # center the player in the screen
        player.rect.y = height / 2

    def printthehud():
        levelcounter = "LEVEL: " + str(deflevel)
        lifecounter = "LIVES: " + str(lives)
        coincounter = "COINS: " + str(coinCount)
        scorecounter = "SCORE: " + str(scorecount)
        level_text = kFont.render(levelcounter + "        " + lifecounter + "         " + coincounter + "         " + scorecounter, True, (255, 255, 255))
        screen.blit(level_text, (10, 0))

        if pistolAmmo <= 10:
            ttColor = (150, 0, 0)
        else:
            ttColor = (255, 255, 255)

        if akAmmo <= 10:
            akColor = (150, 0, 0)
        else:
            akColor = (255, 255, 255)

        for player in players:
            if player.activeWeapon == 1:
                pistolAmmoText1 = kFont.render("TT-30", True, (255, 255, 255))
                pistolAmmoText2 = kFont.render("AMMO: " + str(pistolAmmo), True, ttColor)
                pistol = pygame.image.load('assets/pistol_icon.png')
                screen.blit(pistol, (10, 40))
                screen.blit(pistolAmmoText1, (50, 40))
                screen.blit(pistolAmmoText2, (10, 70))

            if player.activeWeapon == 2:
                akAmmoText1 = kFont.render("AK-47", True, (255, 255, 255))
                akAmmoText2 = kFont.render("AMMO: " + str(akAmmo), True, akColor)
                ak = pygame.image.load('assets/ak_icon.png')
                screen.blit(ak, (10, 40))
                screen.blit(akAmmoText1, (50, 40))
                screen.blit(akAmmoText2, (10, 70))

            if player.keys[0]:
                bk = pygame.image.load('assets/blue_key.png')
                screen.blit(bk, (width - (10 + 32), 40))

    def killPlayer():
        global pistolAmmo
        global akAmmo
        global lives
        lives -= 1
        pistolAmmo = 25
        akAmmo = 5

        if lives <= 0:
            gameOver()
        else:
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
        printthehud()

        pygame.display.update()  # updates the screen every frame

        for event in pygame.event.get():  # quits the game if the x button is pushed
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()  # pygame keyboard handler
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        """
        Below is the scrolling code and technically the movement code of the player. Instead of moving the player around 
        within the level, everything else in the level is moved instead to give the illusion of player movement.
        """
        for player in players:  # access the player's "velocity" even though the player never really moves
            scroll = [-int(player.vel.x), -int(player.vel.y)]
            totalYScroll -= scroll[1]
            for entity in entities:
                entity.rect.x += scroll[0]  # move everything other than the player by that velocity
                entity.rect.y += scroll[1]

        for turner in turners:  # handle enemy / platform collisions for enemy turnaround
            for platform in platforms:
                    if platform.rect.colliderect(turner.rect.x + 3 * turner.vel.x, turner.rect.y - turner.vel.y, turner.rect.width, turner.rect.height):  # X Collisions
                        if turner.direction == "left":
                            turner.direction = "right"
                            turner.vel.x = 0
                        else:
                            turner.direction = "left"
                            turner.vel.x = 0

        for collider in hasCollidePhysics:  # handle non-player collisions. Any entity in the hasCollidePhysics group will collide with floors and walls
            for platform in platforms:
                if platform.rect.colliderect(collider.rect):  # X Collisions
                    # if collider.vel.x > 0:
                    #     collider.direction = "left"
                    #
                    # if collider.vel.x < 0:
                    #     collider.direction = "right"

                    if collider.vel.y > 0:
                        collider.rect.bottom = platform.rect.top
                        collider.onGround = True
                        collider.yvel = 0
                    if collider.vel.y < 0:
                        collider.rect.top = platform.rect.bottom
                    if collider.rect.top == platform.rect.bottom:
                        collider.vel.y = 0
                    if collider.onGround:
                        collider.vel.y = 0


        for miniBoss in miniBosses:
            for smartEnemyTurnTrigger in smartEnemyTurnTriggers:
                if smartEnemyTurnTrigger.rect.colliderect(miniBoss.rect.x + 2 * miniBoss.vel.x, miniBoss.rect.y, miniBoss.rect.width, miniBoss.rect.height):  # X Collisions
                    miniBoss.vel.x = 0
                    if miniBoss.direction == "left":
                        miniBoss.direction = "right"
                    else:
                        miniBoss.direction = "left"
            miniBoss.bulletCooldown -= 1  # each frame of the game, lower the cooldown of the enemy being able to shoot again
            if miniBoss.bulletCooldown <= 0:
                miniBoss.shooting = True
                if miniBoss.direction == "left":
                    Laser((miniBoss.rect.x - 100, miniBoss.rect.y + 64), miniBoss.direction, True, True, entities, playerKillers, bullets)  # spawn new bullet at the enemy's center, going in the enemy's direction
                else:
                    Laser((miniBoss.rect.x + 64, miniBoss.rect.y + 64), miniBoss.direction, True, True, entities, playerKillers, bullets)  # spawn new bullet at the enemy's center, going in the enemy's direction
                miniBoss.bulletCooldown = 80

        for enemy in enemies:  # Handle when enemies fire
            enemy.bulletCooldown -= 1  # each frame of the game, lower the cooldown of the enemy being able to shoot again
            if enemy.bulletCooldown <= 0:
                Bullet((enemy.rect.x + 16, enemy.rect.y + 16), enemy.direction, True, True, entities, bullets,
                       playerKillers)  # spawn new bullet at the enemy's center, going in the enemy's direction
                enemy.bulletCooldown = 80

        for smartEnemy in smartEnemies:  # make sure that smartEnemies turn around when they encounter the invisible turn around flag
            for smartEnemyTurnTrigger in smartEnemyTurnTriggers:
                if smartEnemy.rect.colliderect(smartEnemyTurnTrigger.rect):  # Y collisions
                    if smartEnemy.direction == "left":
                        smartEnemy.vel.x *= -1
                        smartEnemy.direction = "right"
                    else:
                        smartEnemy.vel.x *= -1
                        smartEnemy.direction = "left"

        for bullet in bullets:  # bullet overflow protection
            if level_width * 5 < bullet.rect.x < 0 - level_width * 5:
                bullet.kill()

        for playerKillable in playerKillables:
            for playerPistolBullet in playerPistolBullets:
                if playerPistolBullet.rect.colliderect(playerKillable.rect):  # Everything that can be killed by the player MUST have a health variable even if it is just 1
                    playerKillable.health -= 1
                    playerPistolBullet.kill()
                    scorecount += 10
                if playerKillable.health <= 0:
                    scorecount += 100
                    if isinstance(playerKillable, MiniBoss):  # On the death of something that is killable by a player, check to see if it is a miniboss
                        BlueKey((playerKillable.rect.x + (playerKillable.rect.width / 2), playerKillable.rect.y + (playerKillable.rect.height / 2)), entities, blueKeyCards)  # If it is the miniboss, spawn the blue keycard at it's center before killing it
                    playerKillable.kill()  # If not... just kill anyway

            for playerAKBullet in playerAKBullets:
                if playerAKBullet.rect.colliderect(playerKillable.rect):
                    playerKillable.health -= 10  # AK Bullets do 10x the damage of a regular bullet
                    playerAKBullet.kill()
                    scorecount += 10
                if playerKillable.health <= 0:
                    scorecount += 100
                    if isinstance(playerKillable, MiniBoss):  # On the death of something that is killable by a player, check to see if it is a miniboss
                        BlueKey((playerKillable.rect.x + (playerKillable.rect.width / 2), playerKillable.rect.y + (playerKillable.rect.height / 2)), entities, blueKeyCards)  # If it is the miniboss, spawn the blue keycard at it's center before killing it
                    playerKillable.kill()  # If not... just kill anyway

        ammoGeneration -= 1
        if ammoGeneration <= 0 and pistolAmmo < 10:  # Give the player one bullet every 5 seconds while the player is low on pistol ammo
            pistolAmmo += 1
            ammoGeneration = 500

        """
        All of the player's interactions should be handled below
        """
        for player in players:
            if totalYScroll > level_height:
                killPlayer()

            for smartPlatform in smartPlatforms:
                if smartPlatform.rect.colliderect(player.rect.x, player.rect.y + 1.3 * player.vel.y, player.image.get_width(), player.image.get_height()):
                    player.frictional = False
                    player.vel.x = smartPlatform.vel.x * 1.3
                else:
                    player.frictional = True

            for coin in coins:
                if coin.rect.colliderect(player.rect):
                    coinCount += 1
                    coin.kill()
                    scorecount += 10

            for tt30AmmoPickup in tt30AmmoPickups:
                if tt30AmmoPickup.rect.colliderect(player.rect):
                    pistolAmmo += 25
                    tt30AmmoPickup.kill()

            for akAmmoPickup in akAmmoPickups:
                if akAmmoPickup.rect.colliderect(player.rect):
                    akAmmo += 5
                    akAmmoPickup.kill()

            for blueKeyCard in blueKeyCards:
                if blueKeyCard.rect.colliderect(player.rect):
                    player.keys[0] = True
                    blueKeyCard.kill()


            for blueDoor in blueDoors:  # Handle when enemies fire
                if player.keys[0] == True:
                    blueDoor.kill()

            for trophy in trophies:
                if trophy.rect.colliderect(player.rect):
                    running = False
                    victory()

            if player.activeWeapon == 1:
                if pygame.mouse.get_pressed() == (True, False, False) and player.shotCooldown <= 0 and pistolAmmo > 0:  # Shoot on right click and only right click. True False False represents only right click out of the three mouse buttons
                    Bullet((player.rect.x + 8, player.rect.y + 16), player.direction, not pygame.key.get_pressed()[pygame.K_w], not pygame.key.get_pressed()[pygame.K_s], entities, bullets, playerPistolBullets)
                    player.shotCooldown = 30
                    player.shooting = True
                    pistolAmmo -= 1

            if player.activeWeapon == 2:
                if pygame.mouse.get_pressed() == (True, False, False) and player.shotCooldown <= 0 and akAmmo > 0:  # Shoot on right click and only right click. True False False represents only right click out of the three mouse buttons
                    Bullet((player.rect.x + 8, player.rect.y + 16), player.direction, not pygame.key.get_pressed()[pygame.K_w], not pygame.key.get_pressed()[pygame.K_s], entities, bullets, playerAKBullets)
                    player.shotCooldown = 10
                    player.shooting = True
                    akAmmo -= 1

            for playerKiller in playerKillers:
                if playerKiller.rect.colliderect(player.rect):  # Example of general, clipping collisions. This is great for coin or powerup pickups, bullet collisions, or death
                    killPlayer()

            for miniBoss in miniBosses: # Handle miniboss attacks
                if abs(player.rect.x - miniBoss.rect.x) < 200:
                    if player.rect.x < miniBoss.rect.x:
                        player.vel.x += .3
                    if player.rect.x > miniBoss.rect.x:
                        player.vel.x -= .3

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
        self.rect = self.image.get_rect(topleft=pos)  # sets the location of the player to the top left corner of the surface

        self.frictional = True
        self.vel = pygame.math.Vector2(0, 0)
        self.onGround = False
        self.direction = "left"
        self.shotCooldown = 30

        self.moving = False
        self.shooting = False
        self.shootingCooldown = 30

        self.activeWeapon = 1

        self.animationCooldown = 15
        self.animationState = 0

        self.speed = 1  # gives speed variable to player
        self.speedMax = 5
        self.jumpStrength = 10.2

        self.keys = [False, False, False]  # blue green red

    def update(self):  # keyboard inputs for player
        self.shotCooldown -= 1

        self.vel += GRAVITY

        keys = pygame.key.get_pressed()  # pygame keyboard handler
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.vel.x -= self.speed
            self.direction = "left"
            self.moving = True

        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.vel.x += self.speed
            self.direction = "right"
            self.moving = True
        else:
            self.moving = False

        if keys[pygame.K_LSHIFT]:
            self.speedMax = 7
        else:
            self.speedMax = 5

        if keys[pygame.K_SPACE] and self.onGround:
            self.vel.y -= self.jumpStrength
            self.onGround = False

        if keys[pygame.K_1]:
            self.activeWeapon = 1
        if keys[pygame.K_2]:
            self.activeWeapon = 2

        if self.vel.x > self.speedMax:
            self.vel.x = self.speedMax

        if self.vel.x < -self.speedMax:
            self.vel.x = -self.speedMax

        if self.vel.y > self.speedMax:
            self.vel.y = self.speedMax

        # FRICTION:
        if self.frictional:
            self.vel.x = (self.vel.x / 1.1)  # Apply friction to the movement of the player by slowly lowering it's velocity

        self.animate()

    def animate(self):
        if not self.moving:
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

        if self.shooting:
            self.shootingCooldown -= 1
            if self.direction == "right":
                if self.activeWeapon == 1:
                    gun = pygame.image.load("assets/pistol.png")
                elif self.activeWeapon == 2:
                    gun = pygame.image.load("assets/ak.png")
            else:
                if self.activeWeapon == 1:
                    gun = pygame.transform.flip(pygame.image.load('assets/pistol.png'), True, False)
                if self.activeWeapon == 2:
                    gun = pygame.transform.flip(pygame.image.load('assets/ak.png'), True, False)
            if self.activeWeapon == 1:
                screen.blit(gun, (self.rect))
            if self.activeWeapon == 2:
                if self.direction == "right":
                    screen.blit(gun, (self.rect))
                if self.direction == "left":
                    screen.blit(gun, (self.rect.x - 6, self.rect.y))
            if not self.moving:
                if self.direction == "right":
                    self.image = pygame.image.load('assets/player_run_2.png')
                elif self.direction == "left":
                    self.image = pygame.transform.flip(pygame.image.load('assets/player_run_2.png'), True, False)
        if self.shootingCooldown <= 0:
            self.shootingCooldown = 30
            self.shooting = False


class Platform(pygame.sprite.Sprite):  # similar to player class but for platforms
    def __init__(self, pos, *groups):  # constructs platforms
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))  # platforms are 32x32 and only to be placed every 32 pixels.
        self.image = pygame.image.load('assets/tile.png')
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left


class Crate(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load('assets/crate.png')
        self.rect = self.image.get_rect(topleft=pos)


class Support(pygame.sprite.Sprite):  # see platform class
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))  # supports are 32x32 and only to be placed every 32 pixels.
        self.image = pygame.image.load('assets/support.png')
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left


class Barrier(pygame.sprite.Sprite):  # Invisible barriers to prevent the player from going out of bounds
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)  # SRCALPHA allows for the tile to be transparent
        self.image.fill((0, 0, 0, 0))  # The last zero is the transparency
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 69, 0))
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left

        self.health = 1

        self.bulletCooldown = random.randrange(0, 80)

        self.animationCooldown = 15
        self.animationState = 0

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

        self.animate()

    def animate(self):
        self.animationCooldown -= 1

        if self.animationCooldown <= 0:
            self.animationState += 1
            self.animationCooldown = 15

        if self.direction == "right":

            if self.animationState == 0:
                self.image = pygame.image.load('assets/enemy.png')
            elif self.animationState == 1:
                self.image = pygame.image.load('assets/enemy2.png')
            elif self.animationState == 2:
                self.image = pygame.image.load('assets/enemy3.png')
            else:
                self.animationState = 0
        elif self.direction == "left":

            if self.animationState == 0:
                self.image = pygame.transform.flip(pygame.image.load('assets/enemy.png'), True, False)
            elif self.animationState == 1:
                self.image = pygame.transform.flip(pygame.image.load('assets/enemy2.png'), True, False)
            elif self.animationState == 2:
                self.image = pygame.transform.flip(pygame.image.load('assets/enemy3.png'), True, False)
            else:
                self.animationState = 0


class SmartEnemy(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load('assets/ufo.png')
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left

        self.health = 5

        self.speed = 2
        self.vel = pygame.math.Vector2(0, 0)
        self.direction = "left"

    def update(self):

        if self.direction == "left":
            self.image = pygame.image.load('assets/ufo.png')
            self.vel.x = -self.speed
        else:
            self.image = pygame.transform.flip(pygame.image.load('assets/ufo.png'), True, False)
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


class Ammo(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load('assets/ammo_pickup.png')
        self.rect = self.image.get_rect(topleft=pos)


class AKAmmo(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load('assets/ak_ammo_pickup.png')
        self.rect = self.image.get_rect(topleft=pos)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, up, down, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((8, 8))
        self.image = pygame.image.load('assets/bullet.png')
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

        if not up:
            self.vel.y -= self.speed

        if not down:
            self.vel.y = self.speed

    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y


class MiniBoss(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):  # constructs miniboss
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((64, 128))  # boss is 64x128
        self.image = pygame.image.load('assets/miniboss.png')
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left

        self.animationCooldown = 0
        self.animationState = 0

        self.shooting = False
        self.shootingCooldown = 0

        self.health = 60
        self.jumpStrength = 15
        self.jumpCooldown = 200
        self.bulletCooldown = random.randrange(70, 90)
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

        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

        self.animate()
    def animate(self):
        self.animationCooldown -= 1

        if self.animationCooldown <= 0:
            self.animationState += 1
            self.animationCooldown = 15

        if self.direction == "right":

            if self.animationState == 0:
                self.image = pygame.image.load('assets/miniboss_walk_1.png')
            elif self.animationState == 1:
                self.image = pygame.image.load('assets/miniboss1.png')
            elif self.animationState == 2:
                self.image = pygame.image.load('assets/miniboss_walk_2.png')
            elif self.animationState == 3:
                self.image = pygame.image.load('assets/miniboss1.png')
            else:
                self.animationState = 0
        elif self.direction == "left":

            if self.animationState == 0:
                self.image = pygame.transform.flip(pygame.image.load('assets/miniboss_walk_1.png'), True, False)
            elif self.animationState == 1:
                self.image = pygame.transform.flip(pygame.image.load('assets/miniboss1.png'), True, False)
            elif self.animationState == 2:
                self.image = pygame.transform.flip(pygame.image.load('assets/miniboss_walk_2.png'), True, False)
            elif self.animationState == 3:
                self.image = pygame.transform.flip(pygame.image.load('assets/miniboss1.png'), True, False)
            else:
                self.animationState = 0

        if self.shooting:
            self.shootingCooldown -= 1
            if self.direction == "left":
                self.image = pygame.transform.flip(pygame.image.load('assets/miniboss_shoot.png'), True, False)
            else:
                self.image = pygame.image.load('assets/miniboss_shoot.png')
        if self.shootingCooldown <= 0:
            self.shootingCooldown = 30
            self.shooting = False


class MovingPlatform(pygame.sprite.Sprite):  # similar to smart enemy class but for platforms
    def __init__(self, pos, *groups):  # constructs platforms
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((96, 32))
        self.image = pygame.image.load('assets/moving_platform.png')
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left
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


class BlueKey(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load('assets/blue_key.png')
        self.rect = self.image.get_rect(center=pos)


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, direction, up, down, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((100, 12))
        self.image = pygame.image.load('assets/laser.png')
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to center

        self.speed = 10
        self.vel = pygame.math.Vector2(0, 0)

        if direction == "right":
            self.vel.x = self.speed
        if direction == "left":
            self.vel.x = -self.speed


    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

class BlueDoor(pygame.sprite.Sprite):  # similar to player class but for platforms
    def __init__(self, pos, *groups):  # constructs platforms
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))  # platforms are 32x32 and only to be placed every 32 pixels.
        self.image = pygame.image.load('assets/blue_door.png')
        self.rect = self.image.get_rect(topleft=pos)  # coords assigned to top left

class Trophy(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)  # initializes groups
        self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load('assets/trophy.png')
        self.rect = self.image.get_rect(topleft=pos)


gameBegin() # start screen
main()  # run the main game loop
