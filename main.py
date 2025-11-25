import sys
import pygame

from shot import Shot
from player import Player
from asteroid import  Asteroid
from constants import SCREEN_WIDTH ,SCREEN_HEIGHT,PLAYER_SHOOT_SPEED
from logger import log_state
from asteroidfield import AsteroidField
from logger import log_event


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers =(updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    player = Player(x,y)
    asteroidField = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():  #for the GUI x button to exit
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        # cheak if any of asteroids collide with player
        for a in asteroids:
            if player.collides_with(a):
                log_event("player_hit")
                print("Game Over!")
                sys.exit() #to exit
            for shot in shots:
                if a.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    a.split()



        #sceen
        for d in drawable:
            d.draw(screen)


        pygame.display.flip() # rendering method
        dt = clock.tick(60) /1000


if __name__ == "__main__":
    main()
