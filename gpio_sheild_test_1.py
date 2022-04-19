import RPi.GPIO as GPIO
import time

gpio_pins = [ 3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18,
              19, 21, 22, 23, 24, 26, 29, 31,
              32, 33, 35, 36, 37, 38, 40]

GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)

# setup
for i in gpio_pins:
    GPIO.setup(i, GPIO.OUT)

GPIO.output(7, True)

# for i in range(10):
#     for i in gpio_pins:
#         GPIO.output(i, True)
#         time.sleep(0.1)
#         
#     for i in gpio_pins:
#         GPIO.output(i, False)
#         time.sleep(0.1)
x = input('wait')
# Reset the GPIO pins (turns off motors too)
GPIO.cleanup()