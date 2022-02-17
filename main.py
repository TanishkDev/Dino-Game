import pygame
from setting import *
from support import *
import sys
from random import choice

#ground_pixels = 2400


class Game:
    def __init__(self):
        self.WHITE = (255, 255, 255)

        self.ground = import_image("assets/ground.png")
        self.ground_x = 0
        self.playing = True
        self.world_shift = 5
        dino = Dino()
        self.dino = pygame.sprite.GroupSingle(dino)
        self.catuses = pygame.sprite.Group()

    def ground_draw(self):
        self.ground_x -= self.world_shift
        screen.blit(self.ground, (self.ground_x, 500))
        screen.blit(self.ground, (self.ground_x+2400, 500))

    def run(self):
        while self.playing:
            screen.fill(self.WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.playing = False
                    sys.exit()
                if event.type == SWAPCACTUS:
                    cactus = Cactus()
                    self.catuses.add(cactus)

            if self.ground_x < -2400:
                self.ground_x = 0

            self.dino.draw(screen)
            self.catuses.draw(screen)
            print("scuess")
            self.catuses.draw(screen)
            screen.blit(draw_fps(), (10, 10))
            self.ground_draw()
            self.catuses.update(self.world_shift)
            pygame.display.flip()
            clock.tick(120)


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.catuses = [import_image("assets/cactuses_small_3.png"), import_image("assets/cactuses_small_2.png"), import_image("assets/cactuses_small_1.png"),
                        import_image("assets/cactuses_big_3.png"), import_image("assets/cactuses_big_2.png"), import_image("assets/cactuses_big_1.png")]
        self.image = choice(self.catuses)
        self.offset = self.image.get_size()[1]-70
        self.rect = self.image.get_rect(topleft=(900, 500-self.offset))

    def update(self, shift):
        self.rect.x -= shift


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.idle = import_image("assets/dino-idle.png")
        self.run = sprite_sheet("assets/dino-run.png")
        self.hurt = import_image("assets/dino-hurt.png")
        self.down = sprite_sheet("assets/dino-down.png")
        self.state = "idle"
        self.frames = {"idle": self.idle, "run": self.run,
                       "hurt": self.hurt, "down": self.down}
        self.frame = 0
        self.image = self.frames["idle"]
        self.rect = self.image.get_rect(topleft=(50, 450))


def draw_fps():
    fps = str(int(clock.get_fps()))
    fps_txt = font.render(fps, True, (0, 0, 0))
    return fps_txt


pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 16)

SWAPCACTUS = pygame.USEREVENT

game = Game()
game_state = "run"
cactus_spawn_time = 1200
pygame.time.set_timer(SWAPCACTUS, cactus_spawn_time)

# FIXME LAG
# ditch the class game
while True:
    if game_state == "run":
        game.run()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    clock.tick(60)
    print(clock.get_fps())

sys.exit()
