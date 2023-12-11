import pygame
import sys
import os
from pygame.locals import *

class ScrollingBackground:

    def __init__(self, screenheight, imagefile):

        self.img = pygame.image.load(imagefile)

        self.coord = [0, 0]

        self.coord2 = [0, -screenheight]

        self.y_original = self.coord[1]

        self.y2_original = self.coord2[1]
        

    def Show(self, surface):

        surface.blit(self.img, self.coord)

        surface.blit(self.img, self.coord2)
        

    def UpdateCoords(self, speed_y, time):

        distance_y = speed_y * time

        self.coord[1] += distance_y

        self.coord2[1] += distance_y

        if self.coord2[1] >= 0:

            self.coord[1] = self.y_original

            self.coord2[1] = self.y2_original

class HeroShip:

    def __init__(self, screenheight, screenwidth, imagefile):

        self.shape = pygame.image.load(imagefile)

        self.top = screenheight - self.shape.get_height()/1.5

        self.left = screenwidth/2 - self.shape.get_width()/4


    def Show(self, surface):

        surface.blit(self.shape, (self.left, self.top))


    def UpdateCoords(self, x):

        self.left = x-self.shape.get_width()/2
        
            
pygame.init()

clock = pygame.time.Clock()

screenwidth, screenheight = (1920, 1080)

screen = pygame.display.set_mode((screenwidth, screenheight))

framerate = 60

bg_speed = 100

StarField = ScrollingBackground(screenheight, "spacebg.jpg")

Hero = HeroShip(screenheight, screenwidth, "ufo.png")

pygame.mouse.set_visible(0)

pygame.display.set_caption('Space Arena')

while True:

    time = clock.tick(framerate)/1000.0

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

    StarField.UpdateCoords(bg_speed, time)

    StarField.Show(screen)
    
    Hero.UpdateCoords(x)

    Hero.Show(screen)
    
    pygame.display.update()


