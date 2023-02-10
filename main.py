import pygame,sys
pygame.init()
pygame.font.init()
from settings import *
from level import Level


screen = pygame.display.set_mode((width,height ))
pygame.display.set_caption("platformer")
clock = pygame.time.Clock()
level = Level()
level.setup_level(LEVELS[CURENT_LEVEL])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BG_COLOR)
    if not level.run():
        del level
        CURENT_LEVEL += 1
        level = Level()
        level.setup_level(LEVELS[CURENT_LEVEL])
    level.run()

    pygame.display.update()
    clock.tick(60)
