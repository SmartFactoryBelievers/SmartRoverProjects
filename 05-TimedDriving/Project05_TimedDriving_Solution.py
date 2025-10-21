# Project 5: Timed Driving
# Version v2.2, August 2025
#
# Goal:
# Learn how to program your Raspberry Pi using callback functions to drive in a coded path for the duration of the button push.
#
# Step 1: Read the Code Carefully
# - At the top of the code, you’ll see lines starting with '#'.
# - These are comments that explain what the code is doing. Read each comment to understand the steps.
# - Read every line of this code carefully to understand the variables & functions
#
# Step 2: Build Your Circuit
# - Gather the components: Smart Rover, Smart Module, Press Switch (S2), Motor Control (U8), 
# - 1KΩ R2 Resistor (x4), connector wires (all colors), 2-snap connectors (x4), 3-snap connectors (x3).
# - Follow the diagram or instructions provided by your teacher to connect the components to the correct pins on your Raspberry Pi.
#
# Step 3: Open the Python File in Thonny
# - Open Thonny on your Raspberry Pi.
# - Load the file Project05_TimedDriving.py.
#
# Step 4: Run the Code
# - Click the green 'Run' Button to run the code.
#
# Step 5: Try the Challenges
# - Challenge 1:
#   - Try replacing the driving function in line 138 to make the rover drive in a different direction.
# - Challenge 2:
#   - Try adding other driving functions after line 138 to create a new driving path.
# - Challenge 3:
#   - The modulo operator (%) gives you the remainder left over after dividing one number by another.
#     For example: 4 % 2 = 0, 5 % 2 = 1.
#   - Even numbers divided by 2 have a remainder of 0, while odd numbers have a remainder of 1.
#   - You can use the modulo operator to check if the number of button presses is even or odd, and use that to change the driving direction.
#   - On line 136, replace ‘if True:’ with ‘if count % 2 == 0:’. This will make the rover drive forward only on even button presses.
# - Challenge 4:
#   - In line 143, replace 'Break' with additional driving functions in the ‘else:’ section to control the rover’s movement on odd-numbered button presses.
#
# Step 6: Ask for Help if Needed
# - If you get stuck, ask your teacher or a classmate for help!

# Importing libraries
# Libraries are defined sets of code for specific uses
# Here we want the sleep function for timing and GPIO for the Pi's pin
from time import sleep
import RPi.GPIO as GPIO
# We also now are using the general time library for the timer function
import time

# Clears harmless error warnings 
GPIO.setwarnings(False)

# Let's define variables so we can use them later
# Variables are words that take on values within the code
# This way, we can edit the value at the beginning and the changes flow through
Left_Forward_Pin =  35 # the internal Pi pin number that goes to snap 1
Left_Backward_Pin =  31 # the internal Pi pin number that goes to snap 2
Right_Forward_Pin =  26 # the internal Pi pin number that goes to snap 3
Right_Backward_Pin =  21 # the internal Pi pin number that goes to snap 4
Button_Pin =  18 # the internal Pi pin number that goes to snap 6

# Let's set up our Raspberry Pi
GPIO.setmode(GPIO.BOARD) # Sets pin numbering to match the physical Raspberry Pi board layout.

# Create output pins for the motor pins
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Left_Forward_Pin as an Output pin, start off
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Left_Backward_Pin as an Output pin, start off
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Right_Forward_Pin as an Output pin, start off
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Right_Backward_Pin as an Output pin, start off

# Create input pin for the button
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Let's write some driving functions we can use later to program a driving path
# For a code snippet we will reuse, we can turn it into a function to call later 
# The function name is in blue, and then the variables it uses are in parentheses

# Here's a function to make the rover drive forward for a specific amount of time
def drive_forward(time):    
    GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Left motor forward
    GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Right motor forward
    sleep(time)
    GPIO.output(Left_Forward_Pin, GPIO.LOW) #Left motor off
    GPIO.output(Right_Forward_Pin, GPIO.LOW) #Right motor off
    print('forward')
    sleep(1)

# Here's a function to make the rover turn left for a specific amount of time
def drive_left_turn(time):
    GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Left motor backward
    GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Right motor forward
    sleep(time)
    GPIO.output(Left_Backward_Pin, GPIO.LOW) #Left motor off
    GPIO.output(Right_Forward_Pin, GPIO.LOW) #Right motor off
    print('left turn')
    sleep(1)
    
# Here's a function to make the rover turn right for a specific amount of time
def drive_right_turn(time):
    GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Left motor forward
    GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Right motor backward
    sleep(time)
    GPIO.output(Left_Forward_Pin, GPIO.LOW) #Left motor off
    GPIO.output(Right_Backward_Pin, GPIO.LOW) #Right motor off
    print('right turn')
    sleep(1)

# Here's a function to make the rover drive backward for a specific amount of time
def drive_backward(time):
    GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Left motor backward
    GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Right motor backward
    sleep(time)
    GPIO.output(Left_Backward_Pin, GPIO.LOW) #Left motor off
    GPIO.output(Right_Backward_Pin, GPIO.LOW) #Right motor off
    print('backward')
    sleep(1)

# Here we are creating a timer function to record the duration of the button press
def button_press_timer():
    Start_Time = time.time() # start the timer
    while GPIO.input(Button_Pin): # while the button is pressed...
        print("Button Pressed")
    return round(time.time() - Start_Time,2) # stop the timer, return elapsed time

# Let's define a variable to count how many times the button is pressed.
count = 0

while True: # Looping over and over again
    sleep(0.25)
    
    # If the button is pressed, let's use the timer function to see how long
    if GPIO.input(Button_Pin):
        Button_Time = button_press_timer()
        print('Button pressed ' + str(Button_Time) + ' seconds')

        # In challenge 3, replace "if True:" with "if count % 2 == 0:" to check if the number of button presses is even or odd
        if count % 2 == 0:
            # For challenges 1 and 2, try adding new driving functions here
            drive_forward(Button_Time)
            drive_left_turn(Button_Time)
            drive_right_turn(Button_Time)
            
        else: # To be used in challenges 3 and 4
            # Add other drive functions here for odd button presses
            drive_backward(Button_Time)
            
        count = count + 1 # We increment the counter each time the button is pressed
    
GPIO.cleanup() # Turn off all output pins
