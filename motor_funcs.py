# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

# TODO
# [ ] sort out fwd and backward and make it make sense!
# [ ] decide where change will happen - what level

import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

left_motor_fwd_pin =    7
left_motor_back_pin =   8
right_motor_fwd_pin =   9
right_motor_back_pin =  10

def setup_GPIO():
    # Set the GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Set the GPIO Pin mode
    GPIO.setup(left_motor_fwd_pin, GPIO.OUT) # left fwd
    GPIO.setup(left_motor_back_pin, GPIO.OUT) # left backward

    GPIO.setup(right_motor_fwd_pin, GPIO.OUT) # right forward
    GPIO.setup(right_motor_back_pin, GPIO.OUT) # right backward

def right_motor_fwd():
    GPIO.output(right_motor_fwd_pin, 1)
    GPIO.output(right_motor_back_pin, 0)

def right_motor_back():
    GPIO.output(right_motor_fwd_pin, 0)
    GPIO.output(right_motor_back_pin, 1)
    
def right_motor_off():
    GPIO.output(right_motor_fwd_pin, 0)
    GPIO.output(right_motor_back_pin, 0)
    
def left_motor_fwd():
    GPIO.output(left_motor_fwd_pin, 1)
    GPIO.output(left_motor_back_pin, 0)

def left_motor_back():
    GPIO.output(left_motor_fwd_pin, 0)
    GPIO.output(left_motor_back_pin, 1)
    
def left_motor_off():
    GPIO.output(left_motor_fwd_pin, 0)
    GPIO.output(left_motor_back_pin, 0)

def stop_motors():
    right_motor_off()
    left_motor_off()
    
def rotate_left(mv_time):
    right_motor_fwd()
    left_motor_back()
    time.sleep(mv_time)
    stop_motors()

def rotate_right(mv_time):
    right_motor_back()
    left_motor_fwd()
    time.sleep(mv_time)
    stop_motors()

def turn_left(mv_time):
    right_motor_fwd()
    time.sleep(mv_time)
    stop_motors()

def turn_right(mv_time):
    left_motor_fwd()
    time.sleep(mv_time)
    stop_motors()

def move_fwd(mv_time):
    right_motor_fwd()
    left_motor_fwd()
    time.sleep(mv_time)
    stop_motors()

def move_back(mv_time):
    right_motor_back()
    left_motor_back()
    time.sleep(mv_time)
    stop_motors()

def setup_GPIO():
    # Set the GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Set the GPIO Pin mode
    GPIO.setup(left_motor_fwd_pin, GPIO.OUT)
    GPIO.setup(left_motor_back_pin, GPIO.OUT)
    GPIO.setup(right_motor_fwd_pin, GPIO.OUT)
    GPIO.setup(right_motor_back_pin, GPIO.OUT)

setup_GPIO()

#rotate_left(0.71)
#rotate_right(0.71)

move_fwd(0.5)
# move_back(1)
# for i in range(4):
#     move_fwd(1.5)
#     rotate_left(0.6)
#     time.sleep(0.1)
#rotate_right(1)

# Reset the GPIO pins (turns off motors too)
GPIO.cleanup()
