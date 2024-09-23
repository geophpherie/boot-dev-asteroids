import sys

import pygame

from boot_dev_asteroids import constants
from boot_dev_asteroids.asteroid import Asteroid
from boot_dev_asteroids.player import Player, Shot
from boot_dev_asteroids.asteroid_field import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )

    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    _ = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for u in updateable:
            u.update(dt)

        asteroid: Asteroid
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
