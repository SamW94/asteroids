import pygame
from constants import *
from player import *

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
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT /2))
    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        for sprite in updatable:
            sprite.update(dt)
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
