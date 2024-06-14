############################################################################################################
# Project 5                                                                                                #
# Learning Objective: Learn to program functions, use timing commands, and program a callback              #
# Introduction: The goal of this project is to program the rover to move along a fixed path for the        #
#     duration of the press. This relies on timing functions and recording the duration of inputs. For     #
#     this project, the main concepts covered are timing, "while" loops, returns, nested "if" statements,  #
#     modules, and modulo operators.                                                                       #
# For this project, you will not need to modify the code to get it to run initially                        #
# You WILL need to heavily modify the code to complete all the listed challenges at the end                #
############################################################################################################

# Step 1: Importing Libraries

from time import sleep
import RPi.GPIO as GPIO

#   - A new import: we will use the time library for the timer function(s). This is the same library that we imported sleep from.
#   - Sleep is one of the modules inside time, but there are other modules that we can use - like timer

import time
#   - By importing sleep directly, we don't need to write it as time.sleep, because we specified it in the code.
#   - One of the modules we will use from the library time is time(), which reports back the current time.
#   - This can be confusing, but there is both a module named "time()" and a library named "time"
#   - Since we didn't import time() directly, we need to write it as time.time() [the library followed by the module within it]

# Step 2: Variables

Left_Forward_Pin = 35 
#   - The internal Pi pin number that goes to snap 1
Left_Backward_Pin = 31 
#   - The internal Pi pin number that goes to snap 2
Right_Forward_Pin = 26 
#   - The internal Pi pin number that goes to snap 3
Right_Backward_Pin = 21 
#   - The internal Pi pin number that goes to snap 4
Button_Pin = 18 
#   - The internal Pi pin number that goes to snap 6

# Step 3: Raspberry Pi Setup

#   - GPIO.setmode can configure the pi board in several ways, and GPIO.BOARD is one of those formats

GPIO.setmode(GPIO.BOARD)

#   - Our motor output pins, start off.
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW)

#   - Our input pin from the button, starts unpressed.
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Step 4: Functions

#   - These functions are the same ones that we use in Project 4. Look at Project 4 for review

#------------------------ CHALLENGE 1: CHANGE THE VALUES BELOW TO DRIVE IN NEW PATTERNS ----------------------
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
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

#   - Here we create a timer function to record the duration of the button press

def button_press_timer():
  Start_Time = time.time() 
  #   - Starts the timer. This function records the current time in relation to an absolute reference time in the computer.
  
  while GPIO.input(Button_Pin): 
    #   - While the button is pressed, the code within the "while" loop runs
    #   - This means it will repeatedly run the "print" command until the button is released
    
    print("Button Pressed")
    
  return round(time.time() - Start_Time,2) 
  #   - When time.time() is run the second time, it records a new time based on the same absolute reference time
  #   - The second use of time.time() records the current time, which will be after the time recorded by time.time() stored in Start_Time 
  #   - The difference in time will be the duration of the "while" loop, which means it will be the duration of the button press.
  #   - round() rounds the number to however many decimal points are listed after the comma (2 in this case)
  #   - So, this function records two times and takes the difference between them, then rounds it to two decimals and returns the value

count = 0
#   - We will use a dummy variable "count" to help with the modulo operator
#   - Modulo (%) is a division operand. It divides the given value by another value and outputs the remainder
#   - For the challenge, replace the True with the modulo operator statement (%)
#   - So modulo 2 ("% 2") keeps track of odd and even presses since an even number divided by 2 has remainder of 0
#   - To use this in the code, try writing it as count % 2 == 0. 
#   - This will divide the value of count by 2 and output the remainder, which will then be compared to 0

# Step 5: Run the Code

while True: 
  #   - Loop over and over again
  sleep(0.25)
  #   - When the button is pressed, let's use the timer function to see how long
  #   - Unless the requirements of the "if" statement below are met, it will continue to sleep over and over again
  
  if GPIO.input(Button_Pin):
    Button_Time = button_press_timer()
    #   - We are adding a variable at this point that contains the result of the button_press_timer() function
    #   - This simultaneously runs the button_press_timer() function, and the "return" component assigns the final value to the variable
    
    print('Button pressed ' + str(Button_Time) + ' seconds') 
    #   - "str" will turn the value of Button_Time into a value that can be printed, and the rest of the line will be printed out in the command line
    
  #------------------------ CHALLENGE 2: CHANGE THE "True" TO THE MODULO OPERATOR count % 2 == 0 ----------------------
    if True: 
  #-------------------------------------- END OF CHALLENGE 2 ------------------------------------------

    #------------------------ CHALLENGE 3: ADD NEW DRIVING FUNCTIONS TO THE LOOP BELOW FOR EVEN BUTTON PRESSES ----------------------
      drive_forward(Button_Time)
      #   - Rover drives forward for the duration of the Button_Time variable
      
      count = count + 1 
      #   - We increment the counter for the next button press
    else: 
    #------------------------ CHALLENGE 4: ADD NEW DRIVING FUNCTIONS TO THE LOOP BELOW FOR ODD BUTTON PRESSES ----------------------
      count = count + 1 
      #   - We increment the counter for the next button press
      #   - Do not be confused by the "else" statement. In the current code state, the "else" never runs because the previous "if" condition is True
      #   - Once the modulo operator is added, the "else" portion will run on every other press
      #   - Overall, once the code is run, it will be triggered by the button press. It records the time of the press, then assigns it to the variable
      #   - Then, the second "if" statement is triggered and the rover moves in the programmed path. Then the count variable increases by 1

#   - Now that you  have read through the project, hit Run and press the button on the rover!
#   - Once you add the modulo operator to the specified section, try it again. It should run the "else" section on every other press!

##############
# Challenges #
##############

#Challenge 1
# Try changing the drive functions to switch the driving directions
#    - See the section marked Challenge 1 in the code.
#    - Also try changing the drive functions that are called later in the code after the button press

#Challenge 2
# Change the "True" to  the modulo operator "count % 2 == 0"
#    - See the section marked Challenge 2 in the code.
#    - Q: What would happen if you made it 3? Think about how division and remainders work...

#Challege 3
# With the modulo, add new dirivng functions for even numbered presses
#    - See the section marked Challenge 3 in the code.
#    - Q: What are some practical applications for this? Brainstorm some ideas for this kind of program.

#Challege 4
# With the modulo, add new dirivng functions for odd numbered presses
#    - See the section marked Challenge 4 in the code.
#    - Q: Can you get the rover to return to its starting point?
