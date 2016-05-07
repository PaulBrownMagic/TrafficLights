from traffic_light import output
from time import sleep
red = 'red'
amber = 'amber'
green = 'green'

while True:
    output(red, 1)
    sleep(2)
    output(amber, 1)
    sleep(1)
    output(red, 0)
    output(amber, 0)
    output(green, 1)
    sleep(2)
    output(green, 0)
    output(amber, 1)
    sleep(1)
    output(amber, 0)
