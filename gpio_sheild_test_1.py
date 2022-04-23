import RPi.GPIO as GPIO
import time

gpio_pins = [ 3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18,
              19, 21, 22, 23, 24, 26, 29, 31,
              32, 33, 35, 36, 37, 38, 40]

led_squares = [3,16,8,11,
5,15,10,12,
7,99,18,19, # note 99 is reserved
40,99,22,21, # note 99 is reserved
13,32,29,23,
33,38,31,24,
37,35,36,26]

GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)

# setup
for i in gpio_pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, 0)

GPIO.output(8, True)

# for i in range(10):
#     for i in gpio_pins:
#         GPIO.output(i, True)
#         time.sleep(0.1)
#         
#     for i in gpio_pins:
#         GPIO.output(i, False)
#         time.sleep(0.1)

for i in led_squares:
    if i == 99:
        continue
    else:
        GPIO.output(i, True)
        time.sleep(0.25)
        x = input('wait')
        GPIO.output(i, False)
        time.sleep(0.1)
#         
#     for i in gpio_pins:
#         GPIO.output(i, False)
#         time.sleep(0.1)
    

x = input('wait')
# Reset the GPIO pins (turns off motors too)
GPIO.cleanup()