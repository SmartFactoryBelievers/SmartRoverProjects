#########################################################
# Project 1                                             #
# Goal: Learn to program and use outputs                #
# Task: Build the the Project 1 circuit and blink a LED #
#########################################################

# NOTE: Every line starting with a hashtag (#) is a "comment". These lines are not counted as code, and can be used to take notes or add messages to our coding file!

# Step 1: Importing Libraries
#   - Libraries are defined sets of code for specific uses. 
#   - They let us use pre-created code, instead of having to build it ourselves!
from time import sleep # Here we import the sleep function to act as a timer.
import RPi.GPIO as GPIO # Here we import the GPIO library to activate the Raspberry Pi computer.

# Step 2: Variables
#   - Variables are words that take on values for our code.
#   - You can think of them as boxes that we store numbers in, and we'll later take the number out of the box when we want to use it!

# Here, we'll define some variables for our LED that we'll use later.
LED_Pin = 7 # The internal Pi pin number that goes to snap 7

#------------------------ CHALLENGE 1: CHANGE THE VALUES OF LED_ON AND LED_OFF ----------------------
LED_On = .2 # Duration of LED flash, seconds
LED_Off = .1 # Duration in between flashes, seconds
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

# Step 3: Raspberry Pi Setup 
#   - We'll setup our Pi to use the right pins and other details.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) # This line says we want to use the LED_Pin (in this case, 7) and start with the LED off.

# Step 4: Main program
#   - This is where we'll do the main steps of our program.
while True: # This line says we'll loop over and over again, until we end the program.
    sleep(LED_Off) # Pause the program for the defined duration, keeping the LED off 

    GPIO.output(LED_Pin, GPIO.HIGH) #Turn LED on
    sleep(LED_On) #Pause the program for the defined duration, keeping the LED on 

    GPIO.output(LED_Pin, GPIO.LOW) #Turn LED off

    # NOTE: We'll repeat the four lines above, in the while True, over and over again. This is an easy way to code our program to keep running!


##############
# Challenges #
##############

# Challenge 1: Try changing the LED_On and LED_Off variables to change the blinking pattern.
#   - See the CHALLENGE 1 section above for the variables to change.
#   - Q: What does increasing or decreasing LED_On and LED_Off do?

# Challenge 2: Replace the color LED with the buzzer or white LED to try other outputs.
