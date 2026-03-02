# Project 6: Light Activated Driving
# Version v2.2, August 2025
#
# Goal:
# Learn how to program your Raspberry Pi to seek light before driving forward.
#
# Step 1: Read the Code Carefully
# - At the top of the code, you’ll see lines starting with '#'.
# - These are comments that explain what the code is doing. Read each comment to understand the steps.
# - Read every line of this code carefully to understand the variables & functions
#
# Step 2: Build Your Circuit
# - Gather the components: Smart Module, Smart Rover, Phototransistor (Q4), Motor Control (U8),
# - 1KΩ R2 Resistor (x4), connector wires (all colors), 2-snap connectors (x4), 3-snap connectors (x3).
# - Follow the diagram or instructions provided by your teacher to connect the components to the correct pins on your Raspberry Pi.
#
# Step 3: Open the Python File in Thonny
# - Open Thonny on your Raspberry Pi.
# - Load the file Project06_LightActivatedDriving.py.
#
# Step 4: Run the Code
# - Click the green 'Run' Button to run the code.
#
# Step 5: Try the Challenges
# - Challenge 1:
#   - Try replacing the driving function in line 139 to make the rover drive in a different direction.
# - Challenge 2:
#   - Try adding other driving functions after line 156 to create a new light-seeking spin pattern.
# - Challenge 3:
#   - Add the 100 Ohm resistor (R1) in series with the phototransistor to increase light sensitivity.
# - Challenge 4:
#   - Just like in Project 5, you can use the modulo operator to alternate between turning left and right.
#   - Instead of counting button presses, the code counts the number of times the rover searches for light.
#   - On line 154, replace ‘if True:’ with ‘if count % 2 == 0:’. This will make the rover alternate directions.
# - Challenge 5:
#   - On line 150, replace ‘if True:’ with ‘if Elapsed_Time < Max_Search_Time:’. 
#   - This will make the rover drive forward only if the search time is less than the maximum search time.
#   - Replace the break statement on line 169 with a driving function to make the rover spin all the way around if the Max_Search_Time is reached.
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
Left_Forward_Pin =  35 # the internal Pi pin number that goes to snap 1
Left_Backward_Pin =  31 # the internal Pi pin number that goes to snap 2
Right_Forward_Pin =  26 # the internal Pi pin number that goes to snap 3
Right_Backward_Pin =  21 # the internal Pi pin number that goes to snap 4
Photo_Pin =  18 # the internal Pi pin number that goes to snap 6

# Here we can define the timing variables for the driving functions, in seconds
Forward_Time = 2
Backward_Time = 1
Left_Turn_Time = 0.5
Right_Turn_Time = 0.5
Wait_Time = 1

# Let's set up our Raspberry Pi
GPIO.setmode(GPIO.BOARD) # Sets pin numbering to match the physical Raspberry Pi board layout.

# Create output pins for the motor pins
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Left_Forward_Pin as an Output pin, start off
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Left_Backward_Pin as an Output pin, start off
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Right_Forward_Pin as an Output pin, start off
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Right_Backward_Pin as an Output pin, start off

# Create input pin for the phototransistor
GPIO.setup(Photo_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

# Let's define a variable to count how many times the rover searches for light.
count = 0

# Let's define a variable to set a maximum light search time for the loop
Max_Search_Time = 4 #seconds
# If the rover has not found light by then, we can get out of the loop with a break statement
# break exits the innermost loop and allows the rover to return to the first sleep command

while True: # Continuous outer while loop
    sleep(0.25)
    
    # If the phototransistor detects enough light, drive towards it
    if GPIO.input(Photo_Pin):
        # For challenge 1, change driving instructions here
        drive_forward(Forward_Time)
        
    # If there's not enough light, let's look for it by spinning the rover    
    else:
        # For challenge 5, we can use the timer function to control the light search
        Start_Time = time.time() # start the timer
        while not(GPIO.input(Photo_Pin)): # while not enough light detected...
            Elapsed_Time = round(time.time() - Start_Time,2) # stop the timer, save elapsed time
            print('Not enough light, searching for more')
            
            # For challenge 5, we need to use Elapsed_Time < Max_Search_Time
            if True: # while not enough light is detected
                count = count + 1 # Increment the counter for the modulo
                
                # In challenge 4, replace "if True:" with "if count % 2 == 0:" to make the rover alternate directions
                if True:
                    # For challenge 2, change driving instructions here
                    drive_left_turn(Left_Turn_Time)
                    sleep(Wait_Time)
                    
                else: # For Challenge 4, this code executes on odd-numbered searches
                    drive_right_turn(Right_Turn_Time)
                    sleep(Wait_Time)
            else:

                # The 'break' statement here exits the 'while not(GPIO.input(Photo_Pin)):' loop (line 145).
                # After breaking, the code resumes execution at the next statement in the outer 'while True:' loop (line 131),
                # where the rover waits before checking for light again.
                
                # For Challenge 5, replace "break" with driving functions to make the rover spin all the way around
                break # Exits the loop after Max Search Time exceeded

GPIO.cleanup() # Turn off all output pins
