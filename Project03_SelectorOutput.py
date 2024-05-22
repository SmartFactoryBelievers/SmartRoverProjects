#########################################################################################################
# Project 3                                                                                             #
# Goal: Learn to program by writing functions and using inputs and outputs                              #
# Task: Build the the Project 3 circuit and control a LED and buzzer with a selector                    #
# NOTE: THis project will not run until the user completes and uncomments a portion of the main program #
#########################################################################################################

# Step 1: Importing Libraries
from time import sleep
import RPi.GPIO as GPIO

# Step 2: Variables
A_Pin = 7 # The internal Pi pin number that goes to snap 7
C_Pin = 18 # The internal Pi pin number that goes to snap 6
LED_Pin = 26 # The internal Pi pin number that goes to snap 3
Buzzer_Pin = 21 # The internal Pi pin number that goes to snap 4

#------------------------ CHALLENGE 1: CHANGE THE VALUES OF LED_ON AND LED_OFF ----------------------
Pin_On = 3 #duration of LED flash, seconds
Pin_Off = 0.5 #duration in between flashes, seconds
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

# Step 3: Raspberry Pi Setup 
GPIO.setmode(GPIO.BOARD)
# We need to setup our LED and Button
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Buzzer_Pin, GPIO.OUT, initial=GPIO.LOW)
# We need to setup our ABC Selector Buttons
GPIO.setup(A_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Step 4: Functions
#   - If we have a code snippet we use a lot, we can turn it into a function to make re-using it easier!
#   - The function name is at the beginning / in blue, and then the arguments it takes are in parentheses.
#   - Let's write some functions we can use to make the coding easier!

# Here's a function for seeing if a selector button is pressed.
#   - The function name is "read_selector_button" and takes an input of "In_Pin". 
#   - "In_Pin" can be replaced when the function is used, and it will be replaced automatically through the rest of the function.
def read_selector_button(In_Pin): # Function name and inputs
  # Return/output the GPIO result of the pin. This will be helpful for reading the A and C button pins
  return GPIO.input(In_Pin) 

# Here's a function for turning an output pin on.
#   - The function name is "output_pin_on" and takes an input of "Out_Pin" and "Delay"
def output_pin_on(Out_Pin, Delay):
  sleep(Delay) # Pause the program for "Delay" seconds
  GPIO.output(Out_Pin, GPIO.HIGH) # Turn on "Out_Pin"

# Here's a function for turning an output pin off. 
#   - Can you fill in the missing pieces?
def output_pin_off(Out_Pin, Delay):
  #--------------- NOW YOU TRY: REPLACE "??" WITH THE CORRECT VARIABLES AND UNCOMMENT --------------
  # sleep(??) #wait the Delay
  # GPIO.output(??, GPIO.LOW) #turn the Out_Pin off
  #-------------------------------------- END OF EXERCISE ------------------------------------------

# Step 5: Main program
try:
  while True: #Loop over and over again
    # Here, we can use the functions we defined to read buttons and control outputs
    # For the challenges, try changing the button and output pins in the below code

    #------------- CHALLENGE 3: CHANGE THE BUTTON THAT IS USED (A_Pin vs. C_Pin) ---------------------
    #----------- CHALLENGE 4: CHANGE THE OUTPUT THAT IS USED (LED_Pin vs. Buzzer_Pin) ----------------
    #---------- CHALLENGE 5: CHANGE THE ORDER OF OUTPUT FUNCTIONS (LIKE output_pin_on) ---------------

    # If A is pressed and C is not, the LED blinks.
    if read_selector_button(A_Pin) and not(read_selector_button(C_Pin)):
      output_pin_on(LED_Pin, Pin_Off)
      output_pin_off(LED_Pin, Pin_On)

    # If C is pressed and A is not, the buzzer will buzz.
    if read_selector_button(C_Pin) and not(read_selector_button(A_Pin)):
      output_pin_on(Buzzer_Pin, Pin_Off)
      output_pin_off(Buzzer_Pin, Pin_On)
      
    # By pressing B, both A and C will be pressed. This will turn on both the LED and buzzer.
    if read_selector_button(A_Pin) and read_selector_button(C_Pin):
      #-------------- NOW YOU TRY: REPLACE "??" WITH LED_Pin or Buzzer_Pin AND UNCOMMENT -------------
      # output_pin_on(??, Pin_Off)
      # output_pin_off(??, Pin_On)
      # output_pin_on(??, Pin_Off)
      # output_pin_off(??, Pin_On)
      #-------------------------------------- END OF EXERCISE ----------------------------------------
      
    # Wait 1 second to reset.
    sleep(1)
except KeyboardInterrupt:
  print("Program Successfully Interrupted")

finally:
  # Step 6: Clean-up
  #   - When using motors, we want to set the motors to LOW and use GPIO to clean-up the pins.
  #   - Clean-up steps make sure we close out resources properly, so we don't have problems the next time we use them.

  GPIO.output(LED_Pin, GPIO.LOW)
  GPIO.output(Buzzer_Pin, GPIO.LOW)
  print("Cleaning Up")
  GPIO.cleanup()


##############
# Challenges #
##############

# Challenge 1: Try changing the LED_On and LED_Off variables to change the blinking pattern.
#   - See the CHALLENGE 1 section above for the variables to change.
#   - Q: What does increasing or decreasing LED_On and LED_Off do?

# Challege 2: Replace the push button with the phototransistor and cover it with your hand.
#   - Q: What happens when you do this?

# Challenge 3: Try changing A_Pin and C_Pin in the While loop to switch what A and C do when pressed.

# Challenge 4: Try changing LED_Pin and Buzzer_Pin in the While loop to switch what A and C do when pressed.

# Challenge 5: Try switching the order of the LED and Buzzer functions for a cool lightshow when pressing B.
#   - Q: What happens if you add more function calls?
