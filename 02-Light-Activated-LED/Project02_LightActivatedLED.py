# Project 2: Light Activated LED
# Version v2.2, August 2025
#
# Goal:
# Learn how to program your Raspberry Pi using inputs and outputs to control an LED with a button.
#
# Step 1: Read the Code Carefully
# - At the top of the code, you’ll see lines starting with '#'.
# - These are comments that explain what the code is doing. Read each comment to understand the steps.
# - Read every line of this code carefully to understand the variables & functions
#
# Step 2: Build Your Circuit
# - Gather the components: Smart Module, Press Switch (S2), LED (D4), 100 ohm resistor (R1), 3 snap connector (3), 2 snap connectors (2) x 2, horn (W1), photoresistor (Q4)
# - Follow the diagram or instructions provided by your teacher to connect the LED, resistor, and button to the correct pins on your Raspberry Pi.
#
# Step 3: Open the Python File in Thonny
# - Open Thonny on your Raspberry Pi.
# - Load the file Project02_LightActivatedLED.py.
#
# Step 4: Run the Code
# - Click the green 'Run' Button to run the code.
#
# Step 5: Try the Challenges
# - Challenge 1:
#   - The code uses two variables: LED_On and LED_Off.
#   - Try changing their values to see how it changes the blinking pattern of your LED.
#   - For example, set LED_On = 1 and LED_Off = 0.5 and watch what happens!
# - Challenge 2:
#   - Replace the LED in your circuit with a buzzer.
#   - Run the code again to see if you can make a sound.
# - Challenge 3:
#   - Try changing the "If" statement in line 72 from True to False.
#   - Run the code again. What does the button do?
# - Challenge 4:
#   - Replace the push button in your circuit with the phototransistor.
#   - Run the code again and cover the phototransistor with your hand - what happens?
#
# Step 6: Ask for Help if Needed
# - If you get stuck, ask your teacher or a classmate for help!

# Importing libraries
# Libraries are defined sets of code for specific uses
# Here we want the sleep function for timing and GPIO for the Pi's pin
from time import sleep
import RPi.GPIO as GPIO

# Clears harmless error warnings 
GPIO.setwarnings(False)

# Let's define variables so we can use them later
# Variables are words that take on values within the code
# This way, we can edit the value at the beginning and the changes flow through
Button_Pin =  18 # the internal Pi pin number that goes to snap 6
LED_Pin = 26 # the internal Pi pin number that goes to snap 3

# For challenge 1, we can try different values here to blink in new patterns
LED_On = .2 #duration of LED flash, seconds
LED_Off = .1 #duration in between flashes, seconds

# Let's set up our Raspberry Pi
GPIO.setmode(GPIO.BOARD) # Sets pin numbering to match the physical Raspberry Pi board layout.
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW)  # Set LED_Pin as an Output pin, start off
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set Button_Pin as an Input pin, start off

while True: #Looping over and over again
    
    # Here we use the If statement which evaluates a logical expression
    # It is checking if the button is pressed by reading the pin value
    # If the button pin reads True (on), then it executes the indented code 

    # For challenge 3, try changing the "If" statement in line 72 from True to False.
    if GPIO.input(Button_Pin) == True: #When the button is pressed, blink LED
        sleep(LED_Off) #Keep LED off for defined duration
        GPIO.output(LED_Pin, GPIO.HIGH) #Turn LED on
        sleep(LED_On) #Keep LED on for defined duration
        GPIO.output(LED_Pin, GPIO.LOW) #Turn LED off
        
    # If the button is not pressed, the code will go to the else statement
    else:
        print('Button not pressed')
        sleep(1)
            
GPIO.cleanup() # Turn off all output pins
