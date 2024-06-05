######################################################################################
# Project 4                                                                          #
# Goal: Learn to program by writing functions and using motor control outputs        #
# Task: Build the the Project 4 circuit and drive the rover along your designed path #
######################################################################################

# Step 1: Importing Libraries
from time import sleep
import RPi.GPIO as GPIO

# Step 2: Variables
Left_Forward_Pin = 35 # The internal Pi pin number that goes to snap 1
Left_Backward_Pin = 31 # The internal Pi pin number that goes to snap 2
Right_Forward_Pin = 26 # The internal Pi pin number that goes to snap 3
Right_Backward_Pin = 21 # The internal Pi pin number that goes to snap 4

# Below we can define the timing variables for the driving functions, in seconds
#------------------------ CHALLENGE 1: CHANGE THE VALUES BELOW TO DRIVE IN NEW PATTERNS ----------------------
Forward_Time = 2
Backward_Time = 1
Left_Turn_Time = 0.5
Right_Turn_Time = 0.5
Wait_Time = 1
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

# Step 3: Raspberry Pi Setup
GPIO.setmode(GPIO.BOARD)

# Our motor output pins, start off
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)

# Step 4: Functions
#   - Let's write some driving functions we can use later to program a driving path.

def drive_forward(time):
  GPIO.output(Left_Forward_Pin, GPIO.HIGH) # Move left motor forward
  GPIO.output(Right_Forward_Pin, GPIO.HIGH) # Move right motor forward
  sleep(time) # Wait for "time" seconds. This controls how long we move the motors for!

  GPIO.output(Left_Forward_Pin, GPIO.LOW) # Turn left motor off
  GPIO.output(Right_Forward_Pin, GPIO.LOW) # Turn right motor off
  print('forward')
  sleep(1) # Pause before our next function
  
def drive_left_turn(time):
  GPIO.output(Left_Backward_Pin, GPIO.HIGH) # Move left motor backward
  GPIO.output(Right_Forward_Pin, GPIO.HIGH) # Move right motor forward
  sleep(time) # Wait for "time" seconds. This controls how long we move the motors for!

  GPIO.output(Left_Backward_Pin, GPIO.LOW) # Turn left motor off
  GPIO.output(Right_Forward_Pin, GPIO.LOW) # Turn right motor off
  print('left turn')
  sleep(1) # Pause before our next function
  
def drive_right_turn(time):
  GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Move left motor forward
  GPIO.output(Right_Backward_Pin, GPIO.HIGH) # Move right motor backward
  sleep(time) # Wait for "time" seconds. This controls how long we move the motors for!

  GPIO.output(Left_Forward_Pin, GPIO.LOW) # Turn left motor off
  GPIO.output(Right_Backward_Pin, GPIO.LOW) # Turn right motor off
  print('right turn')
  sleep(1) # Pause before our next function

# Can you finish the function by filling in the blanks for the pins and states?
# This is a backward driving function, so both backward pins should be High then Low.
def drive_backward(time):
  #------------ NOW YOU TRY: REPLACE THE ?? WITH THE CORRECT VARIABLES AND UNCOMMENT -------------
  # GPIO.output(??, GPIO.???) #Move left motor backward
  # GPIO.output(??, GPIO.???) #Move right motor backward
  # sleep(time) # Wait for "time" seconds. This controls how long we move the motors for!

  # GPIO.output(??, GPIO.???) # Turn left motor off
  # GPIO.output(??, GPIO.???) # Turn right motor off
  # print('backward')
  # sleep(1) # Pause before our next function
  #-------------------------------------- END OF EXERCISE ----------------------------------------

#Step 5: Main Program
#Here we use a "for" loop to control the number of times the code is executed.
#If we increase the range, the code will loop multiple times.
#------- NOW YOU TRY: CHANGE THE VALUE IN range() TO INCREASE THE NUMBER OF LOOPS PERFORMED ------
for n in range(1):
  # Let's use the driving functions defined above to create a driving path
  sleep(Wait_Time)
  drive_forward(Forward_Time)
  drive_left_turn(Left_Turn_Time)
  drive_backward(Backward_Time)
  drive_right_turn(Right_Turn_Time)

  #---------- CHALLENGE 2: REORDER THE DRIVE FUNCTIONS TO MAKE A NEW DRIVING PATH  ---------------
  #-- CHALLENGE 3: USE DIFFERENT DRIVE FUNCTIONS AND TIME ARGUMENTS TO MAKE A NEW DRIVING PATH  --

##############
# Challenges #
##############

# Challenge 1: Try changing the driving time variables to create a new driving path.
#   - Q: Can you control what angle the rover turns at by increasing or decreasing the time?

# Challenge 2: Reorder the drive functions to create a new driving path.

# Challenge 3: Create your own custom driving path using different drive functions and time arguments.
