# Project 3: Selector Output
# Version v2.2, August 2025
#
# Goal:
# Learn how to program your Raspberry Pi using functions to control an LED & horn using the selector.
#
# Step 1: Read the Code Carefully
# - At the top of the code, you’ll see lines starting with '#'.
# - These are comments that explain what the code is doing. Read each comment to understand the steps.
# - Read every line of this code carefully to understand the variables & functions
#
# Step 2: Build Your Circuit
# - Gather the components: Smart Module, Selector (S8), LED (D4), Horn (W1), 100 ohm resistor (R1), 
# - 4 snap connector (4), 3 snap connector (3), 2 snap connector x 2 (2).
# - Follow the diagram or instructions provided by your teacher to connect the components to the correct pins on your Raspberry Pi.
#
# Step 3: Open the Python File in Thonny
# - Open Thonny on your Raspberry Pi.
# - Load the file Project03_SelectorOutput.py.
#
# Step 4: Run the Code
# - Click the green 'Run' Button to run the code.
#
# Step 5: Try the Challenges
# - Challenge 1:
#   - The code uses two INPUT variables for duration: Pin_On and Pin_Off.
#   - Try changing their values to see how it changes the blinking pattern of the LED & horn.
#   - For example, set Pin_On = 1 and Pin_Off = 0.5 and watch what happens!
# - Challenge 2:
#   - Swap the positions of the LED & Horn components in your circuit.
#   - Run the code again. Why are these components interchangeable?
# - Challenge 3:
#   - Initially, pressing the A button will blink the LED and pressing C will sound the horn.
#   - Can you swap the INPUT variables A_Pin and C_Pin in the While loop for the opposite result?
#   - Run the code again. Does pressing A sound the horn? Does pressing C blink the LED?
# - Challenge 4:
#   - After Challenge 3, pressing the A button will sound the horn and pressing C will blink the LED.
#   - Can you swap the OUTPUT variables LED_Pin and Buzzer_Pin in the While loop for the opposite result?
#   - Run the code again. Does pressing A blink the LED? Does pressing C sound the horn?
# - Challenge 5:
#   - Rearrange the order of your code in lines 128-131 to change the pattern.
#   - Can you make the LED turn on and off BEFORE the horn makes a sound?
#   - Can you make the LED blink at the same time as the horn makes a sound?
#   - Can you make the LED turn on and off AFTER the horn makes a sound?
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
A_Pin =  7 # the internal Pi pin number that goes to snap 7
C_Pin =  18 # the internal Pi pin number that goes to snap 6
LED_Pin = 26 # the internal Pi pin number that goes to snap 3
Buzzer_Pin = 21 # the internal Pi pin number that goes to snap 4

# For challenge 1, we can try different values here to blink in new patterns
Pin_On = 3 # duration of LED flash, seconds
Pin_Off = 1 # duration in between flashes, seconds

# Let's set up our Raspberry Pi
GPIO.setmode(GPIO.BOARD) # Sets pin numbering to match the physical Raspberry Pi board layout.

# Create output pins for the LED and Buzzer
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW)  # Set LED_Pin as an Output pin, start off
GPIO.setup(Buzzer_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Buzzer_Pin as an Output pin, start off

# Create input pins for the selector buttons
GPIO.setup(A_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set A_Pin as an Input pin, start off
GPIO.setup(C_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set C_Pin as an Input pin, start off

# Let's write some functions we can use to make the coding easier
# For a code snippet we will reuse, we can turn it into a function to call later 
# The function name is in blue, and then the variables it uses are in parentheses

# Here's a function for seeing if a selector button is pressed
# So, read_selector_button reads and returns the value of an input variable called In_Pin
# This will be helpful for reading the A and C button pins as "In_Pin"
def read_selector_button(In_Pin):
    return GPIO.input(In_Pin)

# Here's a function for turning an output pin on
# So, output_pin_on waits for the duration of a variable called "Delay"
# Then, the function turns on the output variable called Out_Pin 
def output_pin_on(Out_Pin, Delay):
    sleep(Delay) # wait the delay
    GPIO.output(Out_Pin, GPIO.HIGH) # Turn the Out_Pin on
    
# Here's a function for turning an output pin off, can you fill in the missing pieces?
# Replace the ?? with the variables and then uncomment
def output_pin_off(Out_Pin, Delay):
    #sleep(??) # wait the Delay
    #GPIO.output(??, GPIO.LOW) # turn the Out_Pin off

while True: #Looping over and over again
    
    # Here we can use the functions we defined to read buttons and control outputs
    # For the challenges 3, 4, and 5, try changing the INPUT and OUTPUT variables in the code below
    
    # If the A button is pressed and C is not, let's blink the LED
    # For Challenge 3, try swapping A_Pin and C_Pin to reverse the inputs
    if read_selector_button(A_Pin) and not(read_selector_button(C_Pin)): 
        # For Challenge 4, try using the Buzzer_Pin instead of the LED_Pin to reverse the outputs
        output_pin_on(LED_Pin, Pin_On) # turn on the LED_Pin
        output_pin_off(LED_Pin, Pin_Off) # turn off the LED_Pin
        
    # If the C button is pressed and A is not, let's buzz the buzzer
    # For Challenge 3, try swapping A_Pin and C_Pin to reverse the inputs
    if read_selector_button(C_Pin) and not(read_selector_button(A_Pin)): 
        # For Challenge 4, try using the LED_Pin instead of the Buzzer_Pin to reverse the outputs
        output_pin_on(Buzzer_Pin, Pin_On) # turn on the Buzzer_Pin
        output_pin_off(Buzzer_Pin, Pin_Off) # turn off the Buzzer_Pin

    # Pressing the B button on the selector is the same as pressing the A & C buttons at the exact same time
    # By pressing B, can you blink the LED and make a sound with the horn?
    # Replace the ?? with the LED_Pin and Buzzer_Pin variables and then uncomment
    # For Challenge 5, can you make new blinking patterns by rearranging the code below?
    if read_selector_button(A_Pin) and read_selector_button(C_Pin):
        #output_pin_on(??, Pin_On)
        #output_pin_off(??, Pin_Off)
        #output_pin_on(??, Pin_On)
        #output_pin_off(??, Pin_Off)
        
    # Wait 1 second to reset    
    sleep(1)
    
GPIO.cleanup() # Turn off all output pins
