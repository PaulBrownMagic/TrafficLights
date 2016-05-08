from traffic_light import output
from traffic_light import TrafficLight
from time import sleep

while True:
    output('green', True)
    if TrafficLight.button_pressed:
        sleep(0.5)
        output('green', False)
        output('amber', True)
        sleep(1)
        output('amber', False)
        output('red', True)
        sleep(2)
        output('amber', True)
        sleep(1)
        output('red', False)
        output('amber', False)
        TrafficLight.button_pressed = False
