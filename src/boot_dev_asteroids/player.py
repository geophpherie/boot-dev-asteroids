import pygame

from boot_dev_asteroids import constants
from boot_dev_asteroids.circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)

        # self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(
            surface=screen, color="white", points=self.triangle(), width=2
        )

    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-1 * dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shot_timer > 0:
            return

        shot = Shot(self.position.x, self.position.y)
        shot.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
        )

        self.shot_timer = constants.PLAYER_SHOOT_COOLDOWN


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)

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
