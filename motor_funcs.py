# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

def right_motor_fwd():
    GPIO.output(9, 0)
    GPIO.output(10, 1)

def right_motor_back():
    GPIO.output(9, 1)
    GPIO.output(10, 0)
    
def right_motor_off():
    GPIO.output(9, 1)
    GPIO.output(10, 0)


# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the GPIO Pin mode
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

# Turn all motors off
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0) # right motor # 
GPIO.output(10, 0) # right motor

# Turn the right motor forwards
GPIO.output(9, 0)
GPIO.output(10, 1)

# Wait for 1 seconds
time.sleep(0.5)

# stop right motor
GPIO.output(9, 0)
GPIO.output(10, 0)

time.sleep(1)

# Turn the left motor forwards
GPIO.output(7, 0)
GPIO.output(8, 1)

# Wait for 1 seconds
time.sleep(0.5)

# stop left motor
GPIO.output(7, 0)
GPIO.output(8, 0)

# Wait for 1 seconds
time.sleep(0.5)

# Turn the right motor forwards
GPIO.output(9, 0)
GPIO.output(10, 1)

# Turn the left motor forwards
GPIO.output(7, 0)
GPIO.output(8, 1)

# Wait for 1 seconds
time.sleep(0.5)

# Reset the GPIO pins (turns off motors too)
GPIO.cleanup()
