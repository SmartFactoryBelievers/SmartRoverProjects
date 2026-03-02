# Project 10: Color Detection
# Version v2.2, August 2025
#
# Goal:
# To program the rover to distinguish between various colors.
#
# Step 1: Read the Code Carefully
# - At the top of the code, you’ll see lines starting with '#'.
# - These are comments that explain what the code is doing. Read each comment to understand the steps.
# - Read every line of this code carefully to understand the variables & functions.
#
# Step 2: Build Your Circuit
# - Gather the components: Smart Module, Press Switch (S2), Horn (W1), LED (D4), 1KΩ Resistor (R2), 
# - 2-snap connector x2, 3-snap connector x1, cutout color signs (found in project manual).
# - Follow the diagram or instructions provided by your teacher to connect the components to the correct pins on your Raspberry Pi.
#
# Step 3: Open the Python File in Thonny
# - Open Thonny on your Raspberry Pi.
# - Load the file Project10_ColorDetection.py.
#
# Step 4: Run the Code
# - Click the green 'Run' Button to run the code.
#
# Step 5: Try the Challenges
# - Challenge 1:
#   - After line 142, try swapping the LED and buzzer outputs in the code for each color detected and see what happens.
#   - Now swap the LED and Buzzer components on the rover and run the code agan. What is the result?
# - Challenge 2:
#   - Functions let you group multiple lines of reusable code which can be called with only a single command
#   - For example, it requires 3 lines of code to each time the LED or Buzzer is activated
#   - In line 98-102, try writing a function to activate the correct output pin after each color is detected
# - Challenge 3:
#   - Try replacing "if True:" in line 130 with a conditional statement "if np.max(RGB_Array) * Col_Margin > np.median(RGB_Array):" 
#   - so that the argmax for Color must exceed to be considered a certain color
# - Challenge 4:
#   - Try creating a memory variable in line 112 and 160 and replace "if True:" in line 139 with a logical condition to check for the last color 
#   - identified and activate flashes and buzzes for a new LED or buzzer output based on the pattern, like Red then Green
#
# Step 6: Ask for Help if Needed
# - If you get stuck, ask your teacher or a classmate for help!

# Importing libraries
# Libraries are defined sets of code for specific uses
# Here we want the sleep function for timing and GPIO for the Pi's pin
from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera
# Numpy is a great numerical tools package to help computers do math with a lot of numbers very quickly. 
# People use this function to add, multiply, and work with big groups of numbers when making games, apps, or solving puzzles with computers. 
import numpy as np

# Clears harmless error warnings 
GPIO.setwarnings(False)

# Let's define variables so we can use them later
# Variables are words that take on values within the code
# This way, we can edit the value at the beginning and the changes flow through
LED_Pin =  21 #the internal Pi pin number that goes to snap 4
Buzzer_Pin = 26 #the internal Pi pin number that goes to snap 3
Button_Pin =  18 #the internal Pi pin number that goes to snap 6

# Let's set up our Raspberry Pi
GPIO.setmode(GPIO.BOARD)

# Create output pins for the LED & Buzzer
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) # Set LED_Pin as an Output pin, start off
GPIO.setup(Buzzer_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Buzzer_Pin as an Output pin, start off

# Create input pin for the button so the Pi can tell when you press it.
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Setting up the camera for light detection
camera = PiCamera() # Create camera object
camera.resolution = (640, 480) # Set the resultion (width, height)
camera.framerate = 30 # Set the framerate in fps

sleep(2) # wait 2 seconds to let the camera settle

camera.iso = 100 # Set camera sensitivity to light (ISO) to 100 for clearer images
camera.shutter_speed = camera.exposure_speed # Match shutter speed to current exposure for consistent brightness
camera.exposure_mode = 'off' # Turn off automatic exposure adjustments so settings stay fixed
gain_set = camera.awb_gains # Save the current automatic white balance settings
camera.awb_mode = 'off' # Turn off automatic white balance (awb) so colors don't change automatically
camera.awb_gains = gain_set # Apply the saved white balance settings to keep color detection stable

# Prepare to analyze images by removing background colors ("noise").
# Each image is made up of tiny dots (pixels), and each pixel has a red, green, and blue value.
# Images are stored in a 3D array with each pixel having Red, Green, and Blue values
Image = np.empty((640,480,3),dtype=np.uint8)
Noise = np.empty((640,480,3),dtype=np.uint8)
RGB_Text = ['Red','Green','Blue'] # Array for naming color

# Let's remove the background 'Noise' colors to emphasis the object's color
camera.capture(Noise,'rgb')
Noise = Noise-np.mean(Noise)

# For Challenge 2, try making a function that turns an output (LED or buzzer) on for a set time, then off.
# The function should use the pin number and how long to stay on.
#def your_function(??, ???):
#   sleep(???) 
#   GPIO.output(??, GPIO.?) 
#   sleep(???) 
#   GPIO.output(??, GPIO.?)

# For challenge 3, set a rule so the detected color must be strong enough to count.
# This helps avoid mistakes if the lighting is bad or there's glare.
Col_Margin = 0.8
# In line 129, let's check if the max * margin > mid
# with max as np.max(RGB_Array) and mid as np.median(RGB_Array)

# For Challenge 4, remove the comment in line 112 and create a memory variable to keep track of the last color found, 
# so you can create patterns (like flashing or buzzing in a special way if the color changes from Red to Green).
# Last_Color = ' '

# Main loop to continually check for button presses. When pressed, take a picture and figure out the object's color.
print('Ready to take photo')
while True:
    
   # Press the push button to capture an image
    if GPIO.input(Button_Pin) == True:
        sleep(2)
        print('Photo taken')
        camera.capture(Image,'rgb')
        RGB_Array = []
        
        # For each of red, green, and blue, calculate the most prominent color through means
        for col in range(0,3):
            RGB_Array.append(np.mean(Image[:,:,col]-np.mean(Image)-np.mean(Noise[:,:,col])))
        
        # For challenge 3, replace the True with the logical statement for the margin 
        if True:
            Color = RGB_Text[np.argmax(RGB_Array)]
            print(Color)
        else:
            print('No prominent color found')
            
        # For challenge 4, let's look for a pattern like Red then Color
        # We can use an if statement to see if the Last_Color was Red
        # Replace this True with a logical to check, remember it's ==, not = here
        if True:
            
            # Turn on the LED or buzzer or both depending on which color is detected.
            if Color == 'Red': #LED for Red object
                GPIO.output(LED_Pin, GPIO.HIGH) #LED on
                sleep(2)
                GPIO.output(LED_Pin, GPIO.LOW) #LED off
            
            if Color == 'Green': #Buzzer for Green object
                GPIO.output(Buzzer_Pin, GPIO.HIGH) #Buzzer on
                sleep(2)
                GPIO.output(Buzzer_Pin, GPIO.LOW) #Buzzer off
            
            if Color == 'Blue': #LED and Buzzer for Blue object
                GPIO.output(LED_Pin, GPIO.HIGH) #LED on
                GPIO.output(Buzzer_Pin, GPIO.HIGH) #Buzzer on
                sleep(2)
                GPIO.output(LED_Pin, GPIO.LOW) #LED off
                GPIO.output(Buzzer_Pin, GPIO.LOW) #Buzzer off
        
        # For challenge 4, update Last_Color after outputs
        #Last_Color = Color
        print('Ready to take photo')

GPIO.cleanup()  # Turn off all output pins
