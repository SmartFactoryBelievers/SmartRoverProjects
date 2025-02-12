# Project 1
# Learning to program and use outputs
# Build the the Project 1 circuit and blink a LED

# Challenge 1
# Try changing the LED_On and LED_Off variables to change the blinking pattern

#Challenge 2
# Replace the color LED with buzzer or white LED to try other outputs

#Importing libraries
# Libraries are defined sets of code for specific uses
from time import sleep #here we import the sleep function to act as a timer
import RPi.GPIO as GPIO #here we import the GPIO library to activate the Raspberry Pi computer

# Let's define variables so we can use them later
# Variables are words that take on values within the code
# This way, we can edit the value at the beginning and the changes flow through
LED_Pin = 7 #the internal Pi pin number that goes to snap 7

#------------------------ CHALLENGE 1: CHANGE THE VALUES OF LED_ON AND LED_OFF ----------------------
LED_On = .2 #duration of LED flash, seconds
LED_Off = .1 #duration in between flashes, seconds
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

#Setting up our pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) #This line says we want to use the LED_Pin and start with the LED off
while True: #Looping over and over again
    sleep(LED_Off) #Keep LED off for defined duration
    GPIO.output(LED_Pin, GPIO.HIGH) #Turn lED on
    sleep(LED_On) #Keep LED on for defined duration
    GPIO.output(LED_Pin, GPIO.LOW) #Turn lED off
