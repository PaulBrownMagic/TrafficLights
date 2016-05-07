import pygame
import sys
from pygame.locals import *


class Light:
    """
    Light class is for a single coloured light in the traffic light. It can be turned on and off
    """
    grey = (100, 100, 100)
    colours = {'red': (255, 0, 0),
               'amber': (255, 155, 0),
               'green': (0, 255, 0)}
    radius = 55

    def __init__(self, pos, colour):
        """
        :param pos: position as (x, y) tuple where x and y are the centre of the circle
        :param colour: string, must be either 'red', 'amber' or 'green', describes colour of the light.
        """
        self.pos = pos
        self.colour = self.colours[colour]
        self.off()

    def off(self):
        """
        Sets light to grey
        :return: None
        """
        pygame.draw.circle(TrafficLight.screen, self.grey, self.pos, self.radius)

    def on(self):
        """
        Sets light to it's colour (turns it "on")
        :return: None
        """
        pygame.draw.circle(TrafficLight.screen, self.colour, self.pos, self.radius)

    def update(self, state):
        """
        Function to determine whether to turn the light on or off, depending on state param
        :param state: Can be either a boolean value or 0 or 1. True/1 will turn the light on, the others will turn it off.
        :return: None, calls appropriate function
        """
        if state == 1:
            self.on()
        elif state == 0:
            self.off()
        else:
            raise Exception('Invalid light state')


class TrafficLight:
    """
    Traffic light is the whole pygame window, include clock and exit functions.
    """
    width = 150
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Traffic Light")
    clock = pygame.time.Clock()

    def __init__(self):
        """
        Sets up visual display and fill
        """
        self.screen.fill((0, 0, 0))
        self.red = Light((self.width//2, self.height//6), 'red')
        self.amber = Light((self.width//2, self.height//2), 'amber')
        self.green = Light((self.width//2, self.height - self.height//6), 'green')

    @staticmethod
    def event_loop():
        """
        Enables close window to work, however it is only called when the output function is called.
        :return: None
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        """
        Entry point for output function and updating the traffic light
        :return: None
        """
        self.event_loop()
        pygame.display.update()


def output(colour, state):
    """
    Updates the state of the lights on the traffic light, turning them on or off.
    :param colour: string, must be either 'red', 'amber' or 'green'
    :param state: Can be either a Boolean or 0 or 1
    :return: None
    """
    colours = {'red': traffic_light.red,
               'amber': traffic_light.amber,
               'green': traffic_light.green}
    colours[colour].update(state)
    traffic_light.run()


pygame.init()
traffic_light = TrafficLight()

