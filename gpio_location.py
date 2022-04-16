import Rpi.GPIO as GPIO

gpio_locs = {}

for i in gpio_pins:
    print(f"GPIO Pin {i}")
    GPIO.output(i,ON)
    x = input(f"    X co-ord->")
    y = input(f"    Y co-ord->")
    gpio_locs[i] = {'x':x, 'y':y}
    GPIO.out(i, OFF)

for  key, value in gpio_locs:
    print(f"{key}: x:{value['x']}, y:{value['y']}")