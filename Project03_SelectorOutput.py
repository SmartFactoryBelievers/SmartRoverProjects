#########################################################################################################
# Project 3                                                                                             #
# Learning Objective: Learn to program functions and use them with multiple inputs and outputs          #
# Introduction: The goal of this project is to program the rover to blink an LED or to buzz a buzzer    #
#      depending on what button is selected. This introduces the idea of multiple inputs (some of which #
#      are simultaneous) and how to control for more complicated scenarios. The main concepts covered   #
#      in this project are Functions, Definitions, Returns, and Nested If statements.                   #
# For this project, you WILL need to modify code to get it to run properly. The sections that need to   #
#      be changed will be called out in the code                                                        #
#      You WILL need to modify code to complete the challenges listed at the end of the project         #
#########################################################################################################

# Step 1: Importing Libraries

#   - Here we want the sleep function for timing and GPIO for the Pi's pins.
#   - These are the same functions and libraries that we used in the previous project

from time import sleep
import RPi.GPIO as GPIO

# Step 2: Variables

#   - We used variables in the previous project
#   - Remember that variables store values for us to reference later, and we are using six in this project

A_Pin = 7 
#   - The internal Pi pin number that goes to snap 7
#   - This variable will be used to receive the signal from the A button

C_Pin = 18
#   - The internal Pi pin number that goes to snap 6
#   - This variable will be used to receive the signal from the C button

LED_Pin = 26 
#   - The internal Pi pin number that goes to snap 3
#   - This variable will be used to send a signal to the LED

Buzzer_Pin = 21
#   - The internal Pi pin number that goes to snap 4
#   - This variable will be used to send a signal to the buzzer

#------------------------ CHALLENGE 1: CHANGE THE VALUES OF LED_ON AND LED_OFF ----------------------
Pin_On = 3 
#   - Duration of LED flash, seconds
#   - This variable is not related to a specific pin and stores a value for later reference

Pin_Off = 0.5 
#   - Duration in between flashes, seconds
#   - This variable is not related to a specific pin and stores a value for later reference

#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

# Step 3: Raspberry Pi Setup 

#   - Here is where we set up and configure our Raspberry Pi
#   - First, we are going to assign the BOARD pin configuration

GPIO.setmode(GPIO.BOARD)

#   - Next, we need to setup our LED and Buzzer

GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Buzzer_Pin, GPIO.OUT, initial=GPIO.LOW)
#   - These lines define LED_Pin and Buzzer_Pin as outputs that are initially off

#   - Next, we need to setup our ABC Selector Buttons

GPIO.setup(A_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#   - These lines define A_Pin and C_Pin as inputs that are initially off

# Step 4: Functions

#   - If we have a code snippet that we use a lot, we can turn it into a function to make re-using it easier!
#   - The function follows the "def", and then the arguments it takes are in parentheses.
#   - Arguments refers to the variables that the function intakes when it runs. Think of it as stating what values you want it to access
#   - Let's write some functions to simplify our code

#   - Here's a function for seeing if a selector button is pressed.
#   - The function name is "read_selector_button" and takes an input of "In_Pin". Think of this as a placeholder.
#   - "In_Pin" can be replaced when the function is used, and it will be replaced automatically through the rest of the function.
#   - It's like a mini-variable! It only exists as a way to easily modify what variables the function is referencing

def read_selector_button(In_Pin): 
  #   - Function name and inputs
  #   - Return generates the GPIO value of the pin (on or off). This will be helpful for reading the A and C button pins
  
  return GPIO.input(In_Pin) 

#   - Here's a function for turning an output pin on.
#   - The function name is "output_pin_on" and takes an input of "Out_Pin" and "Delay"
#   - Don't let the term "input" confuse you. The input for this function is an output pin, as in it references an output

def output_pin_on(Out_Pin, Delay):
  sleep(Delay) 
  GPIO.output(Out_Pin, GPIO.HIGH) 
  #   - Turns on the "Out_Pin". "Out_Pin" will be replaced by another variable when called

#   - Here's a function for turning an output pin off. 
#   - Can you fill in the missing pieces? Replace the question marks with variables and uncomment lines 105 and 106

def output_pin_off(Out_Pin, Delay):
  
  #--------------- NOW YOU TRY: REPLACE "??" WITH THE CORRECT VARIABLES AND UNCOMMENT --------------
  # sleep(??) #wait the Delay
  # GPIO.output(??, GPIO.LOW) #turn the Out_Pin off
  #-------------------------------------- END OF EXERCISE ------------------------------------------

# Step 5: Run the Code

while True: 
  #   - Loops over and over again
  #   - Here, we can use the functions we defined to read buttons and control outputs
  #   - For the challenges, try changing the button and output pins in the below code

  #------------- CHALLENGE 3: CHANGE THE BUTTON THAT IS USED (A_Pin vs. C_Pin) ---------------------
  #----------- CHALLENGE 4: CHANGE THE OUTPUT THAT IS USED (LED_Pin vs. Buzzer_Pin) ----------------
  #---------- CHALLENGE 5: CHANGE THE ORDER OF OUTPUT FUNCTIONS (LIKE output_pin_on) ---------------

  #   - If A is pressed and C is not, the LED blinks.
  if read_selector_button(A_Pin) and not(read_selector_button(C_Pin)):
    output_pin_on(LED_Pin, Pin_Off)
    output_pin_off(LED_Pin, Pin_On)
    #   - This "if" statement checks which input pin was pressed and makes sure only one was pressed
    #   - This "and not" portion is new! Did you catch that?
    #   - "and" is used to check if two things occur at once, as you can see in a later "if" statement
    #   - "not" can be applied to many conditions to make them the opposite of what they normally are
    #   - Also, you will notice that "In_Pin" and "Out_Pin" have been replaced by the variables we defined earlier!

  #   - If C is pressed and A is not, the buzzer will buzz.
  if read_selector_button(C_Pin) and not(read_selector_button(A_Pin)):
    output_pin_on(Buzzer_Pin, Pin_Off)
    output_pin_off(Buzzer_Pin, Pin_On)
    #   - This "if" statement checks which input pin was pressed and makes sure only one was pressed
    
  #   - By pressing B, both A and C will be pressed. This will turn on both the LED and buzzer.
  if read_selector_button(A_Pin) and read_selector_button(C_Pin):
    #   - Here is where you add your own code!
    #   - Look at the earlier sections we just went through, and try to fill in the question marks with variables
    #   - Once you are finished, uncomment lines 142 - 145
    
    #-------------- NOW YOU TRY: REPLACE "??" WITH LED_Pin or Buzzer_Pin AND UNCOMMENT -------------
    # output_pin_on(??, Pin_Off)
    # output_pin_off(??, Pin_On)
    # output_pin_on(??, Pin_Off)
    # output_pin_off(??, Pin_On)
    #-------------------------------------- END OF EXERCISE ----------------------------------------
    
  sleep(1)
  #   - Wait 1 second to reset.

#   - Congratulations! You just wrote your first piece of code
#   - Now that you  have read through the project, hit Run and try pressing the buttons on the selector to see what happens
#   - Quick note: If the buzzer or LED are not working, check to make sure that they are connected in the right direction. They are directional!

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
