#!/usr/bin/env python3

import sys
import pygame
from pygame.locals import *
from random import seed
from random import random
from random import randint

seed(1)

FPS = 120
SIZE = 480

pygame.init()

screen = pygame.display.set_mode((SIZE, SIZE))

class Ant:
    def __init__(self, x, y, dir, max_age, c):
        self.x = x
        self.y = y
        # 0 - left | 1 - up |  2 - right | 3 - down
        self.dir = dir; 
        self.age = 0
        self.max_age = max_age
        self.alive = True
        self.color = c

    def turn(self, t):
        if t:
            self.dir = (self.dir + 1) % 4
        else:
            self.dir = (self.dir - 1) % 4

    def update(self):
        global SIZE
        
        self.age = self.age + 1
        if self.age >= self.max_age:
            pass #self.alive = False

        if random() <= 0.5:
            if random() <= 0.5:
                self.turn(True)
            else:
                self.turn(False)

        if self.dir == 0:
            self.x = (self.x - 1) % SIZE
        elif self.dir == 1:
            self.y = (self.y - 1) % SIZE
        elif self.dir == 2:
            self.x = (self.x + 1) % SIZE
        elif self.dir == 3:
            self.y = (self.y + 1) % SIZE
        else:
            print("invalid direction")
            sys.exit(-1)

    def look(self):
        global SIZE
        global screen
        if self.dir == 0:
            return screen.get_at(((self.x - 1) %  SIZE, self.y))
        elif self.dir == 1:
            return screen.get_at((self.x, (self.y - 1) % SIZE))
        elif self.dir == 2:
            return screen.get_at(((self.x + 1) %  SIZE, self.y))
        elif self.dir == 3:
            return screen.get_at((self.x, (self.y + 1) % SIZE))
        else:
            print("invalid direction")
            sys.exit(-1)


def rand_ant(x, y):
    global behaviours
    global SIZE
    dir = randint(0, 3)
    max_age = randint(100, 10000)
    c = Color(randint(0, 255), randint(0, 255), randint(0, 255))
    return Ant(x, y, dir, max_age, c)

ants = []
START_ANTS = 10000

for x in range(START_ANTS):
    ants.append(rand_ant(randint(0, SIZE - 1), randint(0, SIZE - 1)))

def update():
    global screen
    global ants

    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONUP:
            (x, y) = pygame.mouse.get_pos()
            ants.append(rand_ant(x, y))

    for ant in ants:
        ant.update()

    ants = [ant for ant in ants if ant.alive]

    for ant in ants:
        screen.set_at((ant.x, ant.y), ant.color)
    return True
 

def main():
    fpsClock = pygame.time.Clock()
 
    # Game loop.
    while True:
        if not update(): break
        pygame.display.flip()
        fpsClock.tick(FPS)
    pygame.quit()
    sys.exit()


main()