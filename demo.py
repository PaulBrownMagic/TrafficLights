from traffic_light import output
from time import sleep
red = 'red'
amber = 'amber'
green = 'green'

while True:
    # red ON
    # amber OFF
    # green OFF
    output(red, 1)
    output(amber, 0)  # included here because of loop
    sleep(2)

    # red ON
    # amber ON
    # green OFF
    output(amber, 1)
    sleep(1)

    # red OFF
    # amber OFF
    # green ON
    output(red, 0)
    output(amber, 0)
    output(green, 1)
    sleep(2)

    # red OFF
    # amber ON
    # green OFF
    output(green, 0)
    output(amber, 1)
    sleep(1)
