import RPi.GPIO as GPIO
ON = True
OFF = False


gpio_locs = {}

gpio_pins = [ 3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18,
              19, 21, 22, 23, 24, 26, 29, 31,
              32, 33, 35, 36, 37, 38, 40]

GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)

# setup
for i in gpio_pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, OFF)

for i in gpio_pins:
    print(f"GPIO Pin {i}")
    GPIO.output(i,ON)
    x = input(f"    X co-ord->")
    y = input(f"    Y co-ord->")
    name = input(f"    name->")
    gpio_locs[i] = {'x':x, 'y':y, 'name':name}
    GPIO.output(i, OFF)

for  key, value in gpio_locs.items():
    print(f"{key}: x:{value['x']}, y:{value['y']}, name:{value['name']}")