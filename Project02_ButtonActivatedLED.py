##########################################################################################################
# Project 2                                                                                              #
# Learning Objective: Learn to program using multiple inputs and outputs                                 #
# Introduction: The goal of this project is to program the rover to blink an LED when a button is pressed# 
#     or when it detects a certain amount of light. This is done using a phototransistor, which sends a  # 
#     signal when it detects light. The main concepts covered in this project are If/Else statements,    #
#     and multiple Inputs/Outputs, and Print commands.                                                 #
# For this project, you will not need to modify any code or add any code to complete the requirements.   #
#     You WILL need to change code and the circuit to complete the challenges at the end of the program. #
##########################################################################################################

# Step 1: Importing Libraries

#   - Here we want the sleep function for timing and GPIO for the Pi's pins.
#   - These are the same functions and libraries that we used in the previous project

from time import sleep
import RPi.GPIO as GPIO

# Step 2: Variables

#   - We used variables in the previous project
#   - Remember that variables store values for us to reference later, and we are using four in this project

Button_Pin = 18 
#   - The internal Pi pin number that goes to snap 6
#   - This variable will be used to reference the pin that receives the button signal

LED_Pin = 26 
#   - The internal Pi pin number that goes to snap 3
#   - This variable will be used to reference the pin that sends the signal to the LED

#------------------------ CHALLENGE 1: CHANGE THE VALUES OF LED_ON AND LED_OFF ----------------------
LED_On = 1 
#   - Duration of LED flash, seconds
#   - This variable does not relate to a pin, and will be used to reference the time of the LED flash

LED_Off = 1 
#   - Duration in between flashes, seconds
#   - This variable does not relate to a pin, and will be used to reference the time between LED flashes
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

# Step 3: Raspberry Pi Setup 

#   - Here is where we set up and configure our Raspberry Pi
#   - First, we are going to assign the BOARD pin configuration

GPIO.setmode(GPIO.BOARD)

#   - Pins can be set to either inputs or outputs, and we have one of each in this project.
#   - Inputs receive a signal, while outputs send them. Let's configure ours.
#   - Reminder: You can't set an input high or low, but you can set whether a signal turns it on or off

GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) 
#   - This line says we want to use the LED_Pin (in this case, 26) and start with the LED off.

GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
#   - This line says we want to use the Button_Pin (in this case, 18) and start with the button not pressed.
#   - This means that the signal the button sends will "turn the pin on"

# Step 4: Run the Code
#   - Here is where we are going to run the code and send commands to the rover
#   - Think of the code before this as preparation for this portion

while True: 
#   - Loops over and over again
#   - This is the same loop that we saw in the previous project

  #   - Below is an "If statement", which lets our code do different things depending on a "condition".
  #   - It is checking if the button is pressed by reading the value of the pin.
  #   - If the button is pressed, the button pin reads True (on) and we execute the indented code under "if".
  #   - Otherwise, we instead execute the indented code under "else".
  #   - If/Else statements can be thought of as "if this is true do something, otherwise do something else"

  #------------------------ CHALLENGE 4: CHANGE THE "IF" STATEMENT FROM TRUE TO FALSE ----------------------
  if GPIO.input(Button_Pin) == True: 
  #   - This code checks if the button is pressed
  #   - When the button is pressed, the "if" section runs and blinks the LED
    
  #-------------------------------------- END OF CHALLENGE 4 ------------------------------------------
    
    sleep(LED_Off) 
    #   - Pause the program for the defined duration, keeping the LED off 

    GPIO.output(LED_Pin, GPIO.HIGH) 
    #   - Turns the LED on by setting LED_Pin to high using GPIO.HIGH
    
    sleep(LED_On)
    #   - Pause the program for the defined duration, keeping the LED on 

    GPIO.output(LED_Pin, GPIO.LOW) 
    #   - Turns LED off by setting the LED_Pin to low using GPIO.LOW

  #   - If the button is not pressed, the code will go to the else statement.
  
  else:
    print('Button not pressed')
    #   - A print statement tells the program to generate the enclosed text in the command line
    #   - This is called "printing to the command line", and requires the text to be enclosed in ""
    
    sleep(1) 
    #   - Pause the program for 1 second.

#   - Let's say the button isn't pressed and the else statement runs... now what?
#   - The If loop will end and exit, which jumps out to the While loop.
#   - The While loop then repeats and runs the If statement again 
#   - So, let's review the logic of this project
#   - The While loop keeps repeating the IF/Else statement
#   - When the button is pressed, the "If" portion runs and then exits into the While loop
#   - When the button is not pressed, the "Else" portion runs and prints the statement before exiting

# After reading through the code in this project, you should now understand the program logic
# Hit Run and press the button... you should see the LED light up!

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
