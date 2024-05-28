########################################################################################################
# Project 6                                                                                            #
# Goal: Learn to program by writing functions, using motor control outputs, and adding loop complexity #
# Task: Build the the Project 6 circuit and have the rover be controlled by ambient light              #
# Directions: Turn down the light and point a flashlight at the rover to direct it                     #
########################################################################################################

# Step 1: Importing Libraries
import time
from time import sleep
import RPi.GPIO as GPIO

# Step 2: Variables
Left_Forward_Pin = 35 # The internal Pi pin number that goes to snap 1
Left_Backward_Pin = 31 # The internal Pi pin number that goes to snap 2
Right_Forward_Pin = 26 # The internal Pi pin number that goes to snap 3
Right_Backward_Pin = 21 # The internal Pi pin number that goes to snap 4

# The next variable is the Photo_Pin, which connects to the Phototransistor. A Phototransistor sends a signal when it detects light.
Photo_Pin = 18 # The internal Pi pin number that goes to snap 6

# Below we can define the timing variables for the driving functions, in seconds
Forward_Time = 2
Backward_Time = 1
Left_Turn_Time = 0.5
Right_Turn_Time = 0.5
Wait_Time = 1

# Step 3: Raspberry Pi Setup
GPIO.setmode(GPIO.BOARD)

# Our motor output pins, start off.
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)

#Our input pin from the phototransistor, starts with no signal.
GPIO.setup(Photo_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Step 4: Functions
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

def drive_backward(time):
  GPIO.output(Left_Backward_Pin, GPIO.HIGH) # Move left motor backward
  GPIO.output(Right_Backward_Pin, GPIO.HIGH) # Move right motor backward
  sleep(time) # Wait for "time" seconds. This controls how long we move the motors for!

  GPIO.output(Left_Backward_Pin, GPIO.LOW) # Turn left motor off
  GPIO.output(Right_Backward_Pin, GPIO.LOW) # Turn right motor off
  print('backward')
  sleep(1) # Pause before our next function

# For challenge 4, we will use a dummy variable to help with modulo operator
count = 0
#The modulo operator statement is %, which means remainder in division
# So modulo of 2 keeps track of odd and even presses since an even number divided by 2 has remainder of 0
# To use this as a logical, let's try count % 2 == 0

# For challenge 5, we will set a maximum light search time for the loop
Max_Search_Time = 4 #seconds
# If the rover has not found light by then, we can get out of the loop with a break statement
# break exits the innermost loop and allows the rover to return to the first sleep command

try:
  while True: # Continuous outer while loop
    sleep(0.25)
    count = count + 1 # Increment the counter for the modulo
    
    # If the phototransistor detects enough light, drive towards it
    if GPIO.input(Photo_Pin):
      #------------------------ CHALLENGE 1: CHANGE THE VALUES BELOW TO DRIVE IN NEW PATTERNS ----------------------
      #------------------------ CHALLENGE 2: GET CREATIVE AND ADD NEW DRIVING FUNCTIONS TO CHANGE THE LIGHT-SEEKING SPIN PATTERNS ----------------------
      drive_forward(Forward_Time)
      
      # If there's not enough light, let's look for it by spinning the rover
    else:
      # For challenge 5, we can use the timer function to control the light seach
      Start_Time = time.time()
      # A while not loop is the opposite of while loop. 
      # A "while not" loop loops until a specific signal is received (goes high), but a while loop loops until a certain signal ends (goes low)
      while not(GPIO.input(Photo_Pin)):
        Elapsed_Time = round(time.time() - Start_Time,2)
        print('Not enough light, searching for more')
      
          #------------------------ CHALLENGE 4: REPLACE THE "True" WITH THE MODULO OPERATOR ----------------------
          #------------------------ CHALLENGE 5: REPLACE THE "True" WITH A COMPARATIVE (<) BETWEEN Elapsed_Time and Max_Search_Time ----------------------
        if True:
          drive_left_turn(Left_Turn_Time)
          sleep(Wait_Time)
          
        else: # For challenge 4, modulo uses these drive commands on odd loops
          drive_right_turn(Right_Turn_Time)
          sleep(Wait_Time)
        # else:
        #   break # Exits the loop after Max Search Time exceeded
except Exception as error:
  print(error)
finally:
  # Step 6: Clean-up
  #   - When using motors, we want to set the motors to LOW and use GPIO to clean-up the pins.
  #   - Clean-up steps make sure we close out resources properly, so we don't have problems the next time we use them.

  # Set each pin to LOW.
  GPIO.output(Left_Forward_Pin, GPIO.LOW)
  GPIO.output(Left_Backward_Pin, GPIO.LOW)
  GPIO.output(Right_Forward_Pin, GPIO.LOW)
  GPIO.output(Right_Backward_Pin, GPIO.LOW)

  # Clean up everything.
  GPIO.cleanup()


#Challenge 1
# Try changing the drive functions to switch the driving directions

#Challenge 2
# Add new drive functions to change its light seeking spin pattern

#Challege 3
# Add the 100 Ohm resistor in series with the photoresistor to increase light sensitivity

#Challege 4
# With the modulo operator, have the rover alternate left or right spins in light searching

#Challenge 5
# After a certain amount of time, have the rover spin to look for light
