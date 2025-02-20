import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill(0)
        player.draw(screen)
        pygame.display.flip()
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()