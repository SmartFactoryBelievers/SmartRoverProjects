# Project 7: Controlled Driving
# Version v2.2, August 2025
#
# Goal:
# Learn how to program your Raspberry Pi to drive the rover with button presses A, B, and C.
#
# Step 1: Read the Code Carefully
# - At the top of the code, you’ll see lines starting with '#'.
# - These are comments that explain what the code is doing. Read each comment to understand the steps.
# - Read every line of this code carefully to understand the variables & functions.
#
# Step 2: Build Your Circuit
# - Gather the components: Smart Module, Smart Rover, Selector (S8), Motor Control (U8), 1KΩ R2 Resistor (x4), 
# - connector wires (all colors), 2-snap connectors (x4), 3-snap connectors (x2), 4-snap connectors (x1).
# - Follow the diagram or instructions provided by your teacher to connect the components to the correct pins on your Raspberry Pi.
#
# Step 3: Open the Python File in Thonny
# - Open Thonny on your Raspberry Pi.
# - Load the file Project07_ControlledDriving.py.
#
# Step 4: Run the Code
# - Click the green 'Run' Button to run the code.
#
# Step 5: Try the Challenges
# - Challenge 1:
#   - Try replacing the driving functions in lines 144 and 160 to make the rover drive in a different direction.
# - Challenge 2:
#   - Add new drive functions after lines 144 and 160 to change the driving patterns for each button press.
# - Challenge 3:
#   - Use the function `button_press_timer()' to set how long the rover drives based on how long you hold a button.
# - Challenge 4:
#   - Nested "if" statements let your code check something, wait, then check it again. 
#   - The B button uses a nested "if" statement to check if the button is pressed or held.
#   - For A and C buttons, can you add nested "if" statements to check if the button is pressed or held?
# - Challenge 5:
#   - Replace the length-3 snap connector with the phototransistor. This will make the all three buttons light-dependent. 
#   - Can you add an outer loop for new driving instructions when there is no light or button presses for more than 5 seconds?
#
# Step 6: Ask for Help if Needed
# - If you get stuck, ask your teacher or a classmate for help!

# Importing libraries
# Libraries are defined sets of code for specific uses
# Here we want the sleep function for timing and GPIO for the Pi's pin
import time
from time import sleep
import RPi.GPIO as GPIO

# Clears harmless error warnings 
GPIO.setwarnings(False)

# Let's define variables so we can use them later
# Variables are words that take on values within the code
# This way, we can edit the value at the beginning and the changes flow through
Left_Forward_Pin =  35 #the internal Pi pin number that goes to snap 1
Left_Backward_Pin =  31 #the internal Pi pin number that goes to snap 2
Right_Forward_Pin =  26 #the internal Pi pin number that goes to snap 3
Right_Backward_Pin =  21 #the internal Pi pin number that goes to snap 4
A_Pin =  7 #the internal Pi pin number that goes to snap 7
C_Pin =  18 #the internal Pi pin number that goes to snap 6

# Here we can define the timing variables for the driving functions, in seconds
Forward_Time = 2
Backward_Time = 1
Left_Turn_Time = 0.5
Right_Turn_Time = 0.5
Wait_Time = 0.5

# Let's set up our Raspberry Pi
GPIO.setmode(GPIO.BOARD)

# Create output pins for the motor pins
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Left_Forward_Pin as an Output pin, start off
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Left_Backward_Pin as an Output pin, start off
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Right_Forward_Pin as an Output pin, start off
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Right_Backward_Pin as an Output pin, start off

# Create input pin for the Selector Buttons
GPIO.setup(A_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

# Here's a function to make the rover drive backwards for a specific amount of time
def drive_backward(time):
    GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Left motor backward
    GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Right motor backward
    sleep(time)
    GPIO.output(Left_Backward_Pin, GPIO.LOW) #Left motor off
    GPIO.output(Right_Backward_Pin, GPIO.LOW) #Right motor off
    print('backward')
    sleep(1)
    
# Here we are creating a timer function to record the duration of the button press
def button_press_timer(Button_Pin):
    Start_Time = time.time() # start the timer
    while GPIO.input(Button_Pin): # while the button is pressed...
        print("Button Pressed")
    return round(time.time() - Start_Time,2) # stop the timer, return elapsed time

while True: #Looping over and over again
    sleep(0.5)
    
    # Only pressing A
    if GPIO.input(A_Pin) and not GPIO.input(C_Pin): # only pressing A
        sleep(0.5) # For challenge 4, use a sleep delay to check whether A was pressed and released or held  
        
        Press_Time = button_press_timer(A_Pin) # For challenge 3, remove the comment before "Press_Time"

        # Press A and hold, check if still pressed after delay
        if GPIO.input(A_Pin) and not GPIO.input(C_Pin): 
            # For challenges 1 & 2, try changing the driving functions to create new driving paths
            drive_forward(Press_Time) # drive for duration of button press
            drive_left_turn(Press_Time) # drive for duration of button press

        # Press A and released, not still pressed after delay
        else:
            drive_right_turn(Press_Time)
        
    # Only pressing C
    if GPIO.input(C_Pin) and not GPIO.input(A_Pin): # only pressing C
        sleep(0.5) # For challenge 4, use a sleep delay to check whether A was pressed and released or held  
        
        Press_Time = button_press_timer(C_Pin) # For challenge 3, remove the comment before "Press_Time"

        # Press C and hold, check if still pressed after delay
        if GPIO.input(C_Pin) and not GPIO.input(A_Pin): 
            # For challenges 1 & 2, try changing the driving functions to create new driving paths
            drive_backward(Press_Time) # drive for duration of button press
            drive_right_turn(Press_Time) # drive for duration of button press

        # Press C and released, not still pressed after delay
        else:
            drive_left_turn(Press_Time)        

    # Pressing the B button is the same as pressing the A & C buttons simultaneously.
    # Pressing B, we can use timing to determine if it's released or held
    if GPIO.input(C_Pin) and GPIO.input(A_Pin):
        sleep(0.5)
        # Press B and hold, check if still pressed after delay
        if GPIO.input(C_Pin) and GPIO.input(A_Pin):
            drive_left_turn(Left_Turn_Time)
        # Press B and released, not still pressed after delay
        else:
            drive_right_turn(Right_Turn_Time)

GPIO.cleanup()  # Turn off all output pins
