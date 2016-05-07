import pygame
import sys
from pygame.locals import *


class Light:
    grey = (100, 100, 100)
    radius = 55

    def __init__(self, pos, colour):
        self.pos = pos
        self.colour = colour
        self.off()

    def off(self):
        pygame.draw.circle(TrafficLight.screen, self.grey, self.pos, self.radius)

    def on(self):
        pygame.draw.circle(TrafficLight.screen, self.colour, self.pos, self.radius)

    def update(self, state):
        if state == 1:
            self.on()
        elif state == 0:
            self.off()
        else:
            raise Exception('Invalid light state')


class TrafficLight:
    width = 150
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Traffic Light")
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()

    def __init__(self):
        self.done = False
        self.red = Light((self.width//2, self.height//6), (255, 0, 0))
        self.amber = Light((self.width//2, self.height//2), (255, 155, 0))
        self.green = Light((self.width//2, self.height - self.height//6), (0, 255, 0))

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        self.event_loop()
        pygame.display.update()


def output(colour, state):
    colours = {'red': traffic_light.red,
               'amber': traffic_light.amber,
               'green': traffic_light.green}
    colours[colour].update(state)
    traffic_light.run()


pygame.init()
traffic_light = TrafficLight()

