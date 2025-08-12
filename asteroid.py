import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape, pygame.sprite.Sprite):
    image_original = None

    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

        # Load booty.png once
        if Asteroid.image_original is None:
            Asteroid.image_original = pygame.image.load("booty.png").convert_alpha()

        # Scale image to match radius
        self.image = pygame.transform.scale(
            Asteroid.image_original, (radius * 2, radius * 2)
        )
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, surface):
        self.rect.center = (self.position.x, self.position.y)
        surface.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
