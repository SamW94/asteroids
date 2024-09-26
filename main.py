import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    # Initialise the game screen
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    dt = 0

    # Puts sprites into the group collection using Pygame
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT /2))
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        for sprite in updatable:
            sprite.update(dt)
        for asteroid in asteroids:
            if CircleShape.check_for_collisions(asteroid, player) == True:
                print("Game over!")
                sys.exit()
            for shot in shots:
                if CircleShape.check_for_collisions(asteroid, shot) == True:
                    pygame.sprite.Sprite.kill(asteroid)
                    pygame.sprite.Sprite.kill(shot)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
