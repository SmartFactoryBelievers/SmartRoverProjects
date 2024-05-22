##########################################################################
# Project 2                                                              #
# Goal: Learn to program using inputs and outputs                        #
# Task: Build the the Project 2 circuit and control an LED with a button #
##########################################################################

# Step 1: Importing Libraries
#   - Here we want the sleep function for timing and GPIO for the Pi's pins.
from time import sleep
import RPi.GPIO as GPIO

# Step 2: Variables
Button_Pin = 18 # The internal Pi pin number that goes to snap 6
LED_Pin = 26 # The internal Pi pin number that goes to snap 3

#------------------------ CHALLENGE 1: CHANGE THE VALUES OF LED_ON AND LED_OFF ----------------------
LED_On = 1 # Duration of LED flash, seconds
LED_Off = 1 # Duration in between flashes, seconds
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

# Step 3: Raspberry Pi Setup 
GPIO.setmode(GPIO.BOARD)
#   - Pins can be set to either inputs or outputs, and we have one of each in this project.
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) # This line says we want to use the LED_Pin (in this case, 26) and start with the LED off.
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # This line says we want to use the Button_Pin (in this case, 18) and start with the button not pressed.

# Step 4: Main program
try:
  while True: # Loop over and over again

    # Below is an "If statement", which lets our code do different things depending on a "condition".
    # It is checking if the button is pressed by reading the value of the pin.
    # If the button is pressed, the button pin reads True (on) and we execute the indented code under "if".
    # Otherwise, we instead execute the indented code under "else".

    #------------------------ CHALLENGE 4: CHANGE THE "IF" STATEMENT FROM TRUE TO FALSE ----------------------
    if GPIO.input(Button_Pin) == True: # When the button is pressed, blink LED (the code below)
    #-------------------------------------- END OF CHALLENGE 4 ------------------------------------------
      
      sleep(LED_Off) # Pause the program for the defined duration, keeping the LED off 

      GPIO.output(LED_Pin, GPIO.HIGH) #Turn LED on
      sleep(LED_On) #Pause the program for the defined duration, keeping the LED on 

      GPIO.output(LED_Pin, GPIO.LOW) #Turn LED off

    # If the button is not pressed, the code will go to the else statement.
    else:
      print('Button not pressed')
      sleep(1) # Pause the program for 1 second.

#   - If ctrl+C is pressed, it triggers a keyboard interrupt that exits out of the program. The except portion of the code triggers when a Keyboard Interrupt is detected
except KeyboardInterrupt:
  print("Program Successfully Interrupted")

# Step 6: Clean-up
  #   - When using motors, we want to set the motors to LOW and use GPIO to clean-up the pins.
  #   - Clean-up steps make sure we close out resources properly, so we don't have problems the next time we use them.
#   - After the except section runs, the finally section is triggered. Think of it as the code will be tried over and over until it runs, unless a certain exception occurs, then finally occurs.
finally:
  GPIO.output(LED_Pin, GPIO.LOW) #sets the output pin LED_Pin to low (turns it off)
  print("Cleaning Up")
  GPIO.cleanup() #ensures that the pins on the Pi are properly deactivated before ending the program

##############
# Challenges #
##############

# Challenge 1: Try changing the LED_On and LED_Off variables to change the blinking pattern.
#   - See the CHALLENGE 1 section above for the variables to change.
#   - Q: What does increasing or decreasing LED_On and LED_Off do?

# Challenge 2: Replace the color LED with the buzzer or white LED to try other outputs.

# Challege 3: Replace the push button with the phototransistor and cover it with your hand.
#   - Q: What happens when you do this?

# Challege 4: Try changing the "If" statement from True to False.
#   - Q: Now what does the button/phototransitor do?
