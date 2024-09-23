import random
import pygame

from boot_dev_asteroids import constants
from boot_dev_asteroids.circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            center=self.position,
            radius=self.radius,
            width=2,
            color="white",
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = self.velocity.rotate(angle) * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = self.velocity.rotate(-angle) * 1.2
