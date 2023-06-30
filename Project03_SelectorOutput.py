# Project 3
# Learning to program, writing functions, and using inputs and outputs
# Build the the Project 3 circuit and control a LED and buzzer with a selector
# Press and hold buttons A, B, and C on the selector

#Challenge 1
# Try changing the Pin_On and Pin_Off variables to change the blinking pattern

#Challenge 2
# Replace the color LED with buzzer or white LED to try other outputs

#Challenge 3
# Try changing input pins A and C in the While loop to switch what A and C do when pressed

#Challenge 4
# Try changing output pins LED and Buzzer in the While loop to switch what A and C do when pressed

#Challenge 5
# Try switching the order of the LED and Buzzer functions for a cool lightshow when pressing B

#Importing libraries
# Here we want the sleep function for timing and GPIO for the Pi's pins
from time import sleep
import RPi.GPIO as GPIO

#Let's define variables so we can use them later
A_Pin = 7 #the internal Pi pin number that goes to snap 7
C_Pin = 18 #the internal Pi pin number that goes to snap 6
LED_Pin = 26 #the internal Pi pin number that goes to snap 3
Buzzer_Pin = 21 #the internal Pi pin number that goes to snap 4

#------------------------ CHALLENGE 1: CHANGE THE VALUES OF LED_ON AND LED_OFF ----------------------
Pin_On = 3 #duration of LED flash, seconds
Pin_Off = 0.5 #duration in between flashes, seconds
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

#Setting up our pins
GPIO.setmode(GPIO.BOARD)
#We need to setup our LED and Button
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Buzzer_Pin, GPIO.OUT, initial=GPIO.LOW)
#We need to setup our ABC Selector Buttons
GPIO.setup(A_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Let's write some functions we can use to make the coding easier!
# For a code snippet we will reuse, we can turn it into a function to call later
# The function name is in blue, and then the arguments it takes are in parentheses
#Here's a function for seeing if a selector button is pressed
def read_selector_button(In_Pin): # So, read_selector_button reads and returns the value of In_Pin
  return GPIO.input(In_Pin) # This will be helpful for reading the A and C button pins

#Here's a function for turning an output pin on
def output_pin_on(Out_Pin, Delay): #So, output_pin_on reads the pin number and turns it on after a defined delay
  sleep(Delay)
  GPIO.output(Out_Pin, GPIO.HIGH)

#Here's a function for turning an output pin off, can you fill in the missing pieces?
def output_pin_off(Out_Pin, Delay):
  
  #------------------------ NOW YOU TRY: REPLACE THE ?? WITH THE CORRECT VARIABLES IN LINES 62 & 63 AND UNCOMMENT ----------------------
  #sleep(??) #wait the Delay
  #GPIO.output(??, GPIO.LOW) #turn the Out_Pin off
  #-------------------------------------- END OF EXERCISE ------------------------------------------

while True: #Looping over and over again
  # Here we can use the functions we defined to read buttons and control outputs
  # For the challenges, try changing the button and output pins in the below code
  # If A is pressed and C is not, the LED blinks
  if read_selector_button(A_Pin) and not(read_selector_button(C_Pin)):
    output_pin_on(LED_Pin, Pin_Off)
    output_pin_off(LED_Pin, Pin_On)
    # If C is pressed and A is not, the buzzer will buzz
  if read_selector_button(C_Pin) and not(read_selector_button(A_Pin)):
    output_pin_on(Buzzer_Pin, Pin_Off)
    output_pin_off(Buzzer_Pin, Pin_On)
    #By pressing B, both A and C will be pressed. This will turn on both the LED and buzzer.
  
  #------------------------ NOW YOU TRY: REPLACE THE ?? WITH THE LED_Pin or Buzzer_Pin IN LINES 81-85 VARIABLES AND UNCOMMENT ----------------------
  if read_selector_button(A_Pin) and read_selector_button(C_Pin):
    #output_pin_on(??, Pin_Off)
    #output_pin_off(??, Pin_On)
    #output_pin_on(??, Pin_Off)
    #output_pin_off(??, Pin_On)
  #-------------------------------------- END OF EXERCISE ------------------------------------------
    
  # Wait 1 second to reset
  sleep(1)

#------------------------ CHALLENGE 2: REPLACE THE LED SNAP COMPONENT WITH THE BUZZER SNAP COMPONENT AND RUN THE PROGRAM AGAIN ----------------------
#WHAT HAPPENS WHEN YOU COVER THE PHOTOTRANSISTOR WITH YOUR HAND?

#------------------------ CHALLENGE 3: TRY CHANGING THE INPUT PINS FOR A & C BUTTONS (LINES 70 & 74) ----------------------

#------------------------ CHALLENGE 4: TRY CHANGING THE OUTPUT PINS FOR A & C BUTTONS (LINES 71, 72, 75 & 76)----------------------

#------------------------ CHALLENGE 5: TRY CHANGING THE ORDER OF LED AND BUZZER FUNCTIONS IN LINES 81-84 ----------------------
