# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

def setup_GPIO():
    # Set the GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Set the GPIO Pin mode
    GPIO.setup(7, GPIO.OUT) # left fed
    GPIO.setup(8, GPIO.OUT) # left backward

    GPIO.setup(9, GPIO.OUT) # right forward
    GPIO.setup(10, GPIO.OUT) # right backward

def right_motor_fwd():
    GPIO.output(9, 0)
    GPIO.output(10, 1)

def right_motor_back():
    GPIO.output(9, 1)
    GPIO.output(10, 0)
    
def right_motor_off():
    GPIO.output(9, 1)
    GPIO.output(10, 0)
    
def left_motor_fwd():
    GPIO.output(7, 0)
    GPIO.output(8, 1)

def left_motor_back():
    GPIO.output(7, 1)
    GPIO.output(8, 0)
    
def left_motor_off():
    GPIO.output(7, 1)
    GPIO.output(8, 0)

def stop_motors():
    right_motor_off()
    left_motor_off()
    
def rotate_right(mv_time):
    right_motor_fwd()
    left_motor_back()
    time.sleep(mv_time)
    stop_motors()

def rotate_left(mv_time):
    left_motor_fwd()
    right_motor_back()
    time.sleep(mv_time)
    stop_motors()

def turn_right(mv_time):
    right_motor_fwd()
    time.sleep(mv_time)
    stop_motors()

def turn_left(mv_time):
    left_motor_fwd()
    time.sleep(mv_time)
    stop_motors()

def move_fwd(mv_time):
    right_motor_fwd()
    left_motor_back()
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
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)

setup_GPIO()

move_fwd(1)
move_back(1)
rotate_left(1)
rotate_right(1)

# Reset the GPIO pins (turns off motors too)
GPIO.cleanup()
