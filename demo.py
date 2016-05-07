from traffic_light import output
from time import sleep
red = 'red'
amber = 'amber'
green = 'green'

while True:
    # red ON
    # amber OFF
    # green OFF
    output(red, True)
    output(amber, False)  # included here because of loop
    sleep(2)

    # red ON
    # amber ON
    # green OFF
    output(amber, True)
    sleep(1)

    # red OFF
    # amber OFF
    # green ON
    output(red, False)
    output(amber, False)
    output(green, True)
    sleep(2)

    # red OFF
    # amber ON
    # green OFF
    output(green, False)
    output(amber, True)
    sleep(1)
