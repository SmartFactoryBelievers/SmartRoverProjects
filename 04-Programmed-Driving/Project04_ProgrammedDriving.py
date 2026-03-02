# Project 4: Programmed Driving
# Version v2.2, August 2025
#
# Goal:
# Learn how to program your Raspberry Pi using functions and motor control to drive in a coded path.
#
# Step 1: Read the Code Carefully
# - At the top of the code, you’ll see lines starting with '#'.
# - These are comments that explain what the code is doing. Read each comment to understand the steps.
# - Read every line of this code carefully to understand the variables & functions
#
# Step 2: Build Your Circuit
# - Gather the components: Smart Module, Selector (S8), LED (D4), Horn (W1), 100 ohm resistor (R1), 
# - 4 snap connector (4), 3 snap connector (3), 2 snap connector x 2 (2).
# - Follow the diagram or instructions provided by your teacher to connect the components to the correct pins on your Raspberry Pi.
#
# Step 3: Open the Python File in Thonny
# - Open Thonny on your Raspberry Pi.
# - Load the file Project04_ProgrammedDriving.py.
#
# Step 4: Run the Code
# - Click the green 'Run' Button to run the code.
#
# Step 5: Try the Challenges
# - Challenge 1:
#   - The code uses five INPUT variables for drive time in each direction (forward, backward, left turn, & right turn).
#   - Try changing the drive time variables in lines 59-63 to create a new driving path
# - Challenge 2:
#   - Python reads and executes code line by line from top to bottom, following the order it’s written.
#   - Rearrange the order of your drive functions in lines 128-131 to create a new driving path.
# - Challenge 3:
#   - Python functions can accept arguments as variable names or numbers because variables hold values 
#   - and numbers are values themselves; both supply input for the function to use.
#   - In lines 128-131, try replacing the drive time variable name with a number. 
#   - What is the benefit of using variable names instead of numbers?
#
# Step 6: Ask for Help if Needed
# - If you get stuck, ask your teacher or a classmate for help!

# Importing libraries
# Libraries are defined sets of code for specific uses
# Here we want the sleep function for timing and GPIO for the Pi's pin
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

# Here we can define the timing variables for the driving functions, in seconds
# For challenge 1, try changing each of the values to drive in new patterns
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

# Let's write some driving functions we can use later to program a driving path
# For a code snippet we will reuse, we can turn it into a function to call later 
# The function name is in blue, and then the variables it uses are in parentheses

# Here's a function to make the rover drive forward for a specific amount of time
def drive_forward(time):    
    GPIO.output(Left_Forward_Pin, GPIO.HIGH) # Left motor forward
    GPIO.output(Right_Forward_Pin, GPIO.HIGH) # Right motor forward
    sleep(time) # Wait for specified amount of time
    GPIO.output(Left_Forward_Pin, GPIO.LOW) # Left motor off
    GPIO.output(Right_Forward_Pin, GPIO.LOW) # Right motor off
    print('forward') # print the direction
    sleep(1) # Wait 1 second for the wheels to stop

# Here's a function to make the rover turn left for a specific amount of time
def drive_left_turn(time):
    GPIO.output(Left_Backward_Pin, GPIO.HIGH) # Left motor backward
    GPIO.output(Right_Forward_Pin, GPIO.HIGH) # Right motor forward
    sleep(time) # Wait for specified amount of time
    GPIO.output(Left_Backward_Pin, GPIO.LOW) # Left motor off
    GPIO.output(Right_Forward_Pin, GPIO.LOW) # Right motor off
    print('left turn') # print the direction
    sleep(1) # Wait 1 second for the wheels to stop

# Here's a function to make the rover turn right for a specific amount of time
def drive_right_turn(time):
    GPIO.output(Left_Forward_Pin, GPIO.HIGH) # Left motor forward
    GPIO.output(Right_Backward_Pin, GPIO.HIGH) # Right motor backward
    sleep(time) # Wait for specified amount of time
    GPIO.output(Left_Forward_Pin, GPIO.LOW) # Left motor off
    GPIO.output(Right_Backward_Pin, GPIO.LOW) # Right motor off
    print('right turn') # print the direction
    sleep(1) # Wait 1 second for the wheels to stop

# Here's a function for driving backward, can you fill in the missing pieces?
# Replace the ?? with the variables and then uncomment
# Just like the other drive functions, both backward pins should be set to HIGH, then LOW
def drive_backward(time):
    #GPIO.output(??, GPIO.???) # Left motor backward
    #GPIO.output(??, GPIO.???) # Right motor backward
    #sleep(time) # Wait for specified amount of time
    #GPIO.output(??, GPIO.???) # Left motor off
    #GPIO.output(??, GPIO.???) # Right motor off
    #print('backward') # print the direction
    #sleep(1) # Wait 1 second for the wheels to stop

# Here we can use a "for" loop to repeat the code a set number of times
# Changing the value of range() increases the number of repetitions
for n in range(1):
    
    # Let's use the driving functions defined above to create a driving path
    # For challenge 2, try changing the order of the drive functions below 
    # For challenge 3, try replacing the drive time variables with numbers
    sleep(Wait_Time)
    drive_forward(Forward_Time)
    drive_left_turn(Left_Turn_Time)
    drive_backward(Backward_Time)
    drive_right_turn(Right_Turn_Time)

GPIO.cleanup() # Turn off all output pins
