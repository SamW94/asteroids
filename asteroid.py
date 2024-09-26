import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            vector2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            smaller_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, smaller_asteroids_radius)
            split2 = Asteroid(self.position.x, self.position.y, smaller_asteroids_radius)
            split1.velocity = vector1 * 1.2
            split2.velocity = vector2 * 1.2
            return split1, split2 