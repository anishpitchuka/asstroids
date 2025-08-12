import pygame
from circleshape import CircleShape

class Asteroid(CircleShape, pygame.sprite.Sprite):
    image = None  # shared between all asteroids

    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

        # Load image only once
        if Asteroid.image is None:
            Asteroid.image = pygame.image.load("booty.png").convert_alpha()

        # Scale image to asteroid's size
        self.image = pygame.transform.scale(Asteroid.image, (radius*2, radius*2))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, surface):
        self.rect.center = (self.position.x, self.position.y)
        surface.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt
