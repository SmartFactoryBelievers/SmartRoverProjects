############################################################################################################
# Project 5                                                                                                #
# Goal: Learn to program by writing functions, using motor control outputs, and adding a callback function #
# Task: Build the the Project 5 circuit and drive the rover using button pushes, Simon Says style          #
############################################################################################################

# Step 1: Importing Libraries
from time import sleep
import RPi.GPIO as GPIO
# A new import: we will use the time library for the timer function(s).
import time

# Step 2: Variables
Left_Forward_Pin = 35 # The internal Pi pin number that goes to snap 1
Left_Backward_Pin = 31 # The internal Pi pin number that goes to snap 2
Right_Forward_Pin = 26 # The internal Pi pin number that goes to snap 3
Right_Backward_Pin = 21 # The internal Pi pin number that goes to snap 4
Button_Pin = 18 # The internal Pi pin number that goes to snap 6

# Step 3: Raspberry Pi Setup
GPIO.setmode(GPIO.BOARD)

# Our motor output pins, start off.
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)

# Our input pin from the button, starts unpressed.
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Step 4: Functions
#------------------------ CHALLENGE 1: CHANGE THE VALUES BELOW TO DRIVE IN NEW PATTERNS ----------------------
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
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

# Here we create a timer function to record the duration of the button press
def button_press_timer():
  Start_Time = time.time() # Start the timer
  while GPIO.input(Button_Pin): # While the button is pressed...
    print("Button Pressed")
  return round(time.time() - Start_Time,2) # Stop the timer and return the elapsed time


# TODO: I don't know that the functionality as describe below makes sense. Come back to it when I'm able to test it?

# We will use a dummy variable "count" to help with modulo operator
count = 0
# Replace the True with the modulo operator statement as %, which means remainder in division
# So modulo 2 keeps track of odd and even presses since even divided by 2 has remainder of 0
# To use this as a logical, let's try count % 2 == 0

try:
  #------------------------ CHALLENGE 2: CHANGE THE "True' TO THE MODULO OPERATOR ----------------------
  while True: #Loop over and over again
  #-------------------------------------- END OF CHALLENGE 2 ------------------------------------------
    sleep(0.25)
    # If the button is pressed, let's use the timer function to see how long
    if GPIO.input(Button_Pin):
      Button_Time = button_press_timer()
      print('Button pressed ' + str(Button_Time) + ' seconds')
      
    #------------------------ CHALLENGE 3: CHANGE THE "True" TO THE MODULO OPERATOR ----------------------
    if True: 
    #-------------------------------------- END OF CHALLENGE 3 ------------------------------------------

      #------------------------ CHALLENGE 4: ADD NEW DRIVING FUNCTIONS TO THE LOOP BELOW FOR EVEN BUTTON PRESSES ----------------------
      drive_forward(Button_Time)
      
    else: 
      #------------------------ CHALLENGE 4: ADD NEW DRIVING FUNCTIONS TO THE LOOP BELOW FOR ODD BUTTON PRESSES ----------------------
      count = count + 1 # We increment the counter for the next button press
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
# Change the "True" to  the modulo operator "count % 2 == 0"

#Challege 3
# With the modulo, add new dirivng functions for even numbered presses

#Challege 4
# With the modulo, add new dirivng functions for odd numbered presses