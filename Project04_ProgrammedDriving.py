######################################################################################
# Project 4                                                                          #
# Learning Objective: Learn to program functions that control the rover motors as    #
#     well as learn how to use for loops in programming. The main concepts covered   #
#     in this project are "for" loops and motor controls.                            #
# For this project, you WILL need to modify code to get it to run properly. The      #
#      sections that need to be changed will be called out in the code               #
#      You WILL need to modify code to complete the challenges listed at the end of  #
#      the project                                                                   #
######################################################################################

# Step 1: Importing Libraries

#   - Here we want the sleep function for timing and GPIO for the Pi's pins.
#   - These are the same functions and libraries that we used in the previous project

from time import sleep
import RPi.GPIO as GPIO

# Step 2: Variables

Left_Forward_Pin = 35 
#   - The internal Pi pin number that goes to snap 1
#   - This variable will be used to send signals to the rover motors

Left_Backward_Pin = 31 
#   - The internal Pi pin number that goes to snap 2
#   - This variable will be used to send signals to the rover motors

Right_Forward_Pin = 26 
#   - The internal Pi pin number that goes to snap 3
#   - This variable will be used to send signals to the rover motors

Right_Backward_Pin = 21 
#   - The internal Pi pin number that goes to snap 4
#   - This variable will be used to send signals to the rover motors


#   - Below we can define the timing variables for the driving functions, in seconds
#   - These variable all store values for timing and are not related to pins

#------------------------ CHALLENGE 1: CHANGE THE VALUES BELOW TO DRIVE IN NEW PATTERNS ----------------------
Forward_Time = 2
Backward_Time = 1
Left_Turn_Time = 0.5
Right_Turn_Time = 0.5
Wait_Time = 1
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

# Step 3: Raspberry Pi Setup

#   - Here is where we set up and configure our Raspberry Pi
#   - First, we are going to assign the BOARD pin configuration

GPIO.setmode(GPIO.BOARD)

#   - Next, we are going to set up our pins like in previous projects

GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)

# Step 4: Functions

#   - Let's write 4 driving functions we can use later to program a driving path.
#   - To review functions, look at Project 3 for more info

def drive_forward(time):
  #   - Function turns on two of the four motors for the duration of the sleep value.
  #   - Then, turns it off and prints a "forward" message in the command line
  
  GPIO.output(Left_Forward_Pin, GPIO.HIGH) 
  #   - Move left motor forward
  GPIO.output(Right_Forward_Pin, GPIO.HIGH) 
  #   - Move right motor forward
  sleep(time) 
  #   - Wait for "time" seconds. This controls how long we move the motors for!

  GPIO.output(Left_Forward_Pin, GPIO.LOW) 
  #   - Turn left motor off
  GPIO.output(Right_Forward_Pin, GPIO.LOW) 
  #   - Turn right motor off
  print('forward')
  sleep(1) 
  #   - Pause before our next function
  
def drive_left_turn(time):
  #   - Function turns on two of the four motors for the duration of the sleep value.
  #   - Then, turns it off and prints a "left turn" message in the command line
  
  GPIO.output(Left_Backward_Pin, GPIO.HIGH) 
  #   - Move left motor backward
  GPIO.output(Right_Forward_Pin, GPIO.HIGH) 
  #   - Move right motor forward
  sleep(time) 
  #   - Wait for "time" seconds. This controls how long we move the motors for!

  GPIO.output(Left_Backward_Pin, GPIO.LOW) 
  #   - Turn left motor off
  GPIO.output(Right_Forward_Pin, GPIO.LOW) 
  #   - Turn right motor off
  print('left turn')
  sleep(1) 
  #   - Pause before our next function
  
def drive_right_turn(time):
  #   - Function turns on two of the four motors for the duration of the sleep value.
  #   - Then, turns it off and prints a "right turn" message in the command line 
  
  GPIO.output(Left_Forward_Pin, GPIO.HIGH) 
  #   - Move left motor forward
  GPIO.output(Right_Backward_Pin, GPIO.HIGH) 
  #   - Move right motor backward
  sleep(time) 
  #   - Wait for "time" seconds. This controls how long we move the motors for!

  GPIO.output(Left_Forward_Pin, GPIO.LOW) 
  #   - Turn left motor off
  GPIO.output(Right_Backward_Pin, GPIO.LOW) 
  #   - Turn right motor off
  print('right turn')
  sleep(1) 
  #   - Pause before our next function

#   - Can you finish the function by filling in the blanks for the pins and states? 
#   - Replace the question marks with variables and then uncomment lines 132 - 139
#   - This is a backward driving function, so both backward pins should be set High then Low.

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

#Step 5: Run the Program
  
#   - Here we use a "for" loop to control the number of times the code is executed.
#   - If we increase the range, the code will loop multiple times.

#------- NOW YOU TRY: CHANGE THE VALUE IN range() TO INCREASE THE NUMBER OF LOOPS PERFORMED ------
for n in range(1):
  #   - Let's use the driving functions defined above to create a driving path
  #   - Feel free to change the order and timing variables. See what paths you can make!
  sleep(Wait_Time)
  drive_forward(Forward_Time)
  drive_left_turn(Left_Turn_Time)
  drive_backward(Backward_Time)
  drive_right_turn(Right_Turn_Time)

  #---------- CHALLENGE 2: REORDER THE DRIVE FUNCTIONS TO MAKE A NEW DRIVING PATH  ---------------
  #-- CHALLENGE 3: USE DIFFERENT DRIVE FUNCTIONS AND TIME ARGUMENTS TO MAKE A NEW DRIVING PATH  --

#   - Now that you  have read through the project, hit Run and see what path the rover takes!
#   - Remember, code reads downward, so the functions at the top will be performed first!

##############
# Challenges #
##############

# Challenge 1: Try changing the driving time variables to create a new driving path.
#   - Q: Can you control what angle the rover turns at by increasing or decreasing the time?

# Challenge 2: Reorder the drive functions to create a new driving path.

# Challenge 3: Create your own custom driving path using different drive functions and time arguments.
