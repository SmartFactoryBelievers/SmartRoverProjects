#################################################################################################
# Project 1                                                                                     #
# Objective: Learn to program and use outputs                                                   #
# Activity: Build the Project 1 circuit and blink an LED                                        #
# Goal: The code should cause the rover to blink the LED based on timed programming from user   #
#################################################################################################

# NOTE: Every line starting with a hashtag (#) is a "comment". These lines are not counted as code, and can be used to take notes or add messages to our coding file!

# Step 1: Importing Libraries (Read-Only)
#   - Libraries are defined sets of code for specific uses. 
#   - They let us use pre-created code, instead of having to build it ourselves!
from time import sleep # Here we import the sleep function to act as a timer.
import RPi.GPIO as GPIO # Here we import the GPIO library to activate the Raspberry Pi computer.

# Step 2: Variables (Read-Only)
#   - Variables are words that take on values for our code.
#   - You can think of them as boxes that we store numbers in, and we'll later take the number out of the box when we want to use it!

#   - Here, we'll define some variables for our LED that we'll use later.
#   - Each Raspberry Pi has 40 physical pins within it. The number 7 corresponds to one of those pins within it. Snap 7 is connected to Pin 7 by shear coincidence.
LED_Pin = 7 # The internal Pi pin number that goes to snap 7

#------------------------ CHALLENGE 1: CHANGE THE VALUES OF LED_ON AND LED_OFF ----------------------
LED_On = .2 # Duration of LED flash, seconds
LED_Off = .1 # Duration in between flashes, seconds
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

# Step 3: Raspberry Pi Setup (Read-Only)
#   - We'll setup our Pi to use the right pins and other details.
#   - GPIO.setmode deals with assigning a certain pin configuration to the Pi. We are using GPIO.BOARD as our configuration.
GPIO.setmode(GPIO.BOARD)
#   - Each pin can either be an input (ex. receive a signal from a button) or an output (ex. send a signal to a motor)
#   - A default state also needs to be declared (does it have to be turned on initially or turned off initially?)
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) # This line says we want to use the LED_Pin (in this case, 7) as an output and start with the LED off.

# Step 4: Main program (Read-Only)
#   - This is where we'll do the main steps of our program.
#   - Disregard the try: loop. It ensure the rover shuts down properly. Do not remove this piece of code or the associated KeyboardExcept and finally section.
try:
    while True: # This line says we'll loop over and over again, until we end the program.
        sleep(LED_Off) # Pause the program for the defined duration, keeping the LED off 

        GPIO.output(LED_Pin, GPIO.HIGH) #Turn LED on
        sleep(LED_On) #Pause the program for the defined duration, keeping the LED on 

        GPIO.output(LED_Pin, GPIO.LOW) #Turn LED off

        # NOTE: We'll repeat the four lines above, in the while True, over and over again. This is an easy way to code our program to keep running!
except KeyboardInterrupt:
    print("Program Successfully Interrupted") #sends a signal to the Pi to print the enclosed line of text on the screen
finally:
# Step 5: Clean-up (Read-Only)
  #   - When using motors, we want to set the motors to LOW and use GPIO to clean-up the pins.
  #   - Clean-up steps make sure we close out resources properly, so we don't have problems the next time we use them.

    GPIO.output(LED_Pin, GPIO.LOW) #sets the pin low (turns it off)
    print("Cleaning Up")
    GPIO.cleanup() #properly deactivates the pins to ensure that the program has been stopped successfully


##############
# Challenges #
##############

# Challenge 1: Try changing the LED_On and LED_Off variables to change the blinking pattern.
#   - See the CHALLENGE 1 section above for the variables to change.
#   - Change the values on the LED_On and LED_Off variables
#   - Q: What does increasing or decreasing LED_On and LED_Off do?

# Challenge 2: Replace the color LED with the buzzer or white LED to try other outputs.
