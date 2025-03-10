import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from bullets import Bullet


def main():
    pygame.init()
    dt = 0
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Bullet.containers = (updatable, drawable, bullets)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0)
        
        for item in updatable:
            item.update(dt)
        
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        
        for item in asteroids:
            if player.crush(item):
                print("Game over!")
                quit()
            for shot in bullets:
                if item.crush(shot):
                    item.split()
                    shot.kill()
        
        dt = fps.tick(60) / 1000



if __name__ == "__main__":
    main()