###########################################################################################################
# Project 6                                                                                               #
# Learning Objective: Learn to program functions, use modulo operators, and "While not" loops             #
# Introduction: The goal of this project is to program the rover to move along a fixed path when light is #
#     detected, and to have it automatically search for light when it does not detect any. The main       #
#     concepts covered in this project are phototransistors, "If" loops, modulos, and "while not" loops.  #
# For this project, you will NOT not need to modify the code to get it to run initially                   #
#     You WILL need to heavily modify the code to complete all the listed challenges at the end           #
###########################################################################################################

# Step 1: Importing Libraries

import time
from time import sleep
import RPi.GPIO as GPIO

#   - Standard imports (review in previous projects)

# Step 2: Variables

Left_Forward_Pin = 35 
#   - The internal Pi pin number that goes to snap 1
Left_Backward_Pin = 31 
#   - The internal Pi pin number that goes to snap 2
Right_Forward_Pin = 26 
#   - The internal Pi pin number that goes to snap 3
Right_Backward_Pin = 21 
#   - The internal Pi pin number that goes to snap 4

#   - The next variable is the Photo_Pin, which connects to the Phototransistor. A Phototransistor sends a signal when it detects light.

Photo_Pin = 18 
#   - The internal Pi pin number that goes to snap 6

#   - Below we can define the timing variables for the driving functions, in seconds

Forward_Time = 2
Backward_Time = 1
Left_Turn_Time = 0.5
Right_Turn_Time = 0.5
Wait_Time = 1

# Step 3: Raspberry Pi Setup

#   - GPIO.setmode can configure the pi board in several ways, and GPIO.BOARD is one of those formats

GPIO.setmode(GPIO.BOARD)

#   - Our motor output pins, start off.
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)

#   - Our input pin from the phototransistor, starts with no signal.
GPIO.setup(Photo_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Step 4: Functions

#   - These functions are the same ones that we use in previous projects. Look at ealier projects for review

def drive_forward(time):
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

def drive_backward(time):
  GPIO.output(Left_Backward_Pin, GPIO.HIGH) 
  #   - Move left motor backward
  GPIO.output(Right_Backward_Pin, GPIO.HIGH) 
  #   - Move right motor backward
  sleep(time) 
  #   - Wait for "time" seconds. This controls how long we move the motors for!

  GPIO.output(Left_Backward_Pin, GPIO.LOW) 
  #   - Turn left motor off
  GPIO.output(Right_Backward_Pin, GPIO.LOW) 
  #   - Turn right motor off
  print('backward')
  sleep(1) 
  #   - Pause before our next function

#   - For challenge 4, we will use a dummy variable to help with modulo operator

count = 0
#   - The modulo operator statement is %, which means remainder in division
#   - So modulo of 2 keeps track of odd and even presses since an even number divided by 2 has remainder of 0
#   - To use this as a logical, let's try count % 2 == 0

#   - For challenge 5, we will set a maximum light search time for the loop

Max_Search_Time = 4 
#   - seconds
#   - If the rover has not found light by then, we can get out of the loop with a break statement
#   - break exits the innermost loop and allows the rover to return to the first sleep command

# Step 5: Run the Code

while True: 
  #   - Continuous outer while loop
  sleep(0.25)
  count = count + 1 
  #   - Increment the counter for the modulo
  
  #   - If the phototransistor detects enough light, drive towards it
  
  if GPIO.input(Photo_Pin):
    #------------------------ CHALLENGE 1: CHANGE THE VALUES BELOW TO DRIVE IN NEW PATTERNS ----------------------
    #------------------------ CHALLENGE 2: GET CREATIVE AND ADD NEW DRIVING FUNCTIONS TO CHANGE THE LIGHT-SEEKING SPIN PATTERNS ----------------------
    drive_forward(Forward_Time)
    #   - If the phototransistor detects light, the Photo_Pin variable goes high, which triggers the "If" loops
    #   - If there's not enough light, let's look for it by spinning the rover
  
  else:
    # For challenge 5, we can use the timer function to control the light seach
    
    Start_Time = time.time()
    #   - This is the same timer that we used in previous projects. Review them for more information
    
    while not(GPIO.input(Photo_Pin)):
       #   - A while not loop is the opposite of while loop. 
       #   - A "while not" loop loops until a specific signal is received (goes high), but a while loop loops until a certain signal ends (goes low)
       #   - As long as the Photo_Pin does not send a signal, the while not loop will continue to loop
      
      Elapsed_Time = round(time.time() - Start_Time,2)
      #   - Same timer that was used in previous projects
      
      print('Not enough light, searching for more')
    
        #------------------------ CHALLENGE 4: REPLACE THE "True" WITH THE MODULO OPERATOR ----------------------
        #------------------------ CHALLENGE 5: REPLACE THE "True" WITH A COMPARATIVE (<) BETWEEN Elapsed_Time and Max_Search_Time ----------------------
      #   - if True means this piece of the code will run
      #    - Therefore, the piece of code within if True will run, then cycle back to the start of the while not loop, and repeat, making the rover spin to look for light
      if True:
        drive_left_turn(Left_Turn_Time)
        sleep(Wait_Time)
        #   - This section of code will cause the rover to rotate to "search" for more light
        
      else: 
        #   - For challenge 4, modulo uses these drive commands on odd loops
        drive_right_turn(Right_Turn_Time)
        sleep(Wait_Time)
      # else:
        #   - This else section should be uncommented for challenge 4. Leave it commented out unless working on Challenge 4

      break 
        #   - Exits the loop after Max Search Time exceeded

#   - Now that you  have read through the project, hit Run and place the rover in the light!
#   - Try moving the rover into the dark and see how it reacts.
#   - Once you add the modulo operator to the specified section, try it again. It should run the "else" section on every other press!
#   - Also try adding in the Max_Search_Time and having it stop once it is reached!

##############
# Challenges #
##############

#Challenge 1
# Try changing the drive functions to switch the driving directions
#    - See the section Challenge 1 in the main code
#    - Q: Do you think there is an ideal light seeking pattern? Why or why not?

#Challenge 2
# Add new drive functions to change its light seeking spin pattern
#    - See the section Challenge 2 in the main code
#    - Q: Do you think there is an ideal light seeking pattern? Why or why not?

#Challege 3
# Add the 100 Ohm resistor in series with the photoresistor to increase light sensitivity
#    - Q: Why does this increase light sensitivity? Think about voltage and resistance...

#Challege 4
# With the modulo operator, have the rover alternate left or right spins in light searching
#    - Q: What motion do you think would be best to find more light? Try to program it!

#Challenge 5
# After a certain amount of time, have the rover spin to look for light
