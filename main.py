# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
   
        
    #Create groups for objects.
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Set containers
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable)
    asteroid_field = AsteroidField()

    hero = Player((SCREEN_WIDTH / 2), SCREEN_HEIGHT / 2) #instantiate player, set start pos
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updateable.update(dt) #Calling the update function on the whole group instead of ind. members.

        #Checking for collisions. If found, print "Game Over!" and immediately exit.
        for asteroid in asteroids: #iterate over each object in the 'asteroids' group.
            if hero.collision_detect(asteroid): #Call coll_det method on player object and handle.
                print("Game Over!")
                sys.exit()

        #Loop over ALL objects in the drawable group and .draw() them individually.
        for item in drawable:
            item.draw(screen) #Using item refers to each object in the group as the loop iterates.
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        #Return time elapsed since last frame in seconds.
        


if __name__ == "__main__":
    main()
