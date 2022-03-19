
import random

# import pygame modules
import pygame

# import pygame.locals for easier access to key coordinates
from pygame.locals import (
    RLEACCEL,   # render more quickly on non-accelerated displays
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# calls init of all included pygame modules
# provides platform independence
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# setup game clock
clock = pygame.time.Clock()

# player sprite


class Player(pygame.sprite.Sprite):
    # initialise object through super call
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./img/jet.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (70, 50))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.speed = 10

    # update sprite position
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            # print("UP key pressed!")
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_DOWN]:
            # print("DOWN key pressed!")
            self.rect.move_ip(0, self.speed)
        if pressed_keys[K_LEFT]:
            # print("LEFT key pressed!")
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            # print("RIGHT key pressed!")
            self.rect.move_ip(self.speed, 0)

        # keep inside screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# enemy sprite


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("./img/bird.png").convert()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)

    # update sprite position
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.kill()


# cloud object
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("./img/cloud.png").convert()
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# returns surface representing visible parts of window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# create custom event to add enemy
# USEREVENT --> last reserved event by pygame
# set_timer every 250ms sets ADDENEMY event
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# instantiate player
player = Player()

# create sprite groups
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# GAME LOOP
# loop control variable
run = True
# loop body
while run:
    # look event in queue
    for event in pygame.event.get():
        # check if key pressed
        if event.type == KEYDOWN:
            # ESCAPE KEY -> exit
            if event.key == K_ESCAPE:
                run = False
        # check close window button pressed
        elif event.type == QUIT:
            run = False
        # ADDENEMY event
        elif event.type == ADDENEMY:
            # create new enemy
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        # ADDCLOUD event
        elif event.type == ADDCLOUD:
            # create new cloud
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # get all key pressed
    pressed_keys = pygame.key.get_pressed()
    # update player position
    player.update(pressed_keys)
    enemies.update()
    clouds.update()

    # Fill screen white
    screen.fill((135, 206, 250))

    # draw sprites on screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # check collision
    if pygame.sprite.spritecollideany(player, enemies):
        print("Collision !! ")
        player.kill()
        run = False

    # # custom surface object
    # surf = pygame.Surface((50, 50))
    # # color the surface
    # surf.fill((0, 0, 0))
    # rect = surf.get_rect()
    # # draw surface on screen
    # # blit -> block transfer (possible only between surfaces)
    # surf_center = (
    #     (SCREEN_WIDTH-surf.get_width())/2,
    #     (SCREEN_HEIGHT-surf.get_height())/2
    # )
    # screen.blit(surf, surf_center)

    # update the screen
    pygame.display.flip()

    # frame rate --> 30 frames per second
    clock.tick(30)

# Done! quit
pygame.quit()
