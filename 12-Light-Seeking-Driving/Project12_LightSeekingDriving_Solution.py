# Project 12: Light Seeking Driving
# Version v2.2, August 2025
#
# Goal:
# To program the rover to drive toward the light it detects.
#
# Step 1: Read the Code Carefully
# - At the top of the code, you’ll see lines starting with '#'.
# - These are comments that explain what the code is doing. Read each comment to understand the steps.
# - Read every line of this code carefully to understand the variables & functions
#
# Step 2: Build Your Circuit
# - Gather the components: Smart Module, Press Switch (S2), Horn (W1), LED (D4), 1KΩ Resistor (R2), 
# - 2-snap connector x2, 3-snap connector x1, cutout color signs (found in project manual).
# - Follow the diagram or instructions provided by your teacher to connect the components to the correct pins on your Raspberry Pi.
#
# Step 3: Open the Python File in Thonny
# - Open Thonny on your Raspberry Pi.
# - Load the file Project11_ColorDetectionDriving.py.
#
# Step 4: Run the Code
# - Click the green 'Run' Button to run the code.
#
# Step 5: Try the Challenges
# - Challenge 1:
#   - Try changing the Left and Right Thresholds in lines 144 & 145 to force different turning patterns
# - Challenge 2:
#   - The modulo operator (%) helps you alternate actions, like switching between forward and reverse.
#   - Try using the modulo function and loop counter to go from forward to reverse every few cycles
#   - In line 198, replace "if True:" with "if count % 2 == 0:" to check if the number of button presses is even or odd
# - Challenge 3:
#   - Can you add a timer to the loop in line 196 to do a spin after a 30 seconds of searching?
# - Challenge 4: 
#   - Can you set the drive time duration based on the ratio of left-to-right light by completing the code in line 183?
#
# Step 6: Ask for Help if Needed
# - If you get stuck, ask your teacher or a classmate for help!

# Importing libraries
# Libraries are defined sets of code for specific uses
# Here we want sleep for timing, GPIO for the Pi's pins, & picamera for the Pi's camera
from time import sleep
import time
import RPi.GPIO as GPIO
from picamera import PiCamera
# We will also need PiRGBArray and cv2 for computer vision/image processing
from picamera.array import PiRGBArray
import cv2
# Numpy is a great numerical tools package to help computers do math with a lot of numbers very quickly. 
# People use this function to add, multiply, and work with big groups of numbers when making games, apps, or solving puzzles with computers. 
import numpy as np

# Clears harmless error warnings 
GPIO.setwarnings(False)

# Let's define variables so we can use them later
# Variables are words that take on values within the code
# This way, we can edit the value at the beginning and the changes flow through
Left_Forward_Pin =  35 #the internal Pi pin number that goes to snap 1
Left_Backward_Pin =  31 #the internal Pi pin number that goes to snap 2
Right_Forward_Pin =  26 #the internal Pi pin number that goes to snap 3
Right_Backward_Pin =  21 #the internal Pi pin number that goes to snap 4

#Here we can define the timing variables for the driving functions, in seconds
Forward_Time = 2
Backward_Time = 1
Left_Turn_Time = 0.5
Right_Turn_Time = 0.5
Wait_Time = 1

# Let's set up our Raspberry Pi
GPIO.setmode(GPIO.BOARD)

# Create output pins for the motor pins
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Left_Forward_Pin as an Output pin, start off
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Left_Backward_Pin as an Output pin, start off
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Right_Forward_Pin as an Output pin, start off
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Right_Backward_Pin as an Output pin, start off

# Let's write some driving functions we can use later to program a driving path
# For a code snippet we will reuse, we can turn it into a function to call later 
# The function name is in blue, and then the variables it uses are in parentheses

# Here's a function to make the rover drive forward for a specific amount of time
def drive_forward(time):    
    GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Left motor forward
    GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Right motor forward
    sleep(time)
    GPIO.output(Left_Forward_Pin, GPIO.LOW) #Left motor off
    GPIO.output(Right_Forward_Pin, GPIO.LOW) #Right motor off
    print('forward')
    sleep(1)

# Here's a function to make the rover turn left for a specific amount of time
def drive_left_turn(time):
    GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Left motor backward
    GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Right motor forward
    sleep(time)
    GPIO.output(Left_Backward_Pin, GPIO.LOW) #Left motor off
    GPIO.output(Right_Forward_Pin, GPIO.LOW) #Right motor off
    print('left turn')
    sleep(1)
    
# Here's a function to make the rover turn right for a specific amount of time
def drive_right_turn(time):
    GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Left motor forward
    GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Right motor backward
    sleep(time)
    GPIO.output(Left_Forward_Pin, GPIO.LOW) #Left motor off
    GPIO.output(Right_Backward_Pin, GPIO.LOW) #Right motor off
    print('right turn')
    sleep(1)

# Here's a function to make the rover drive backward for a specific amount of time
def drive_backward(time):
    GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Left motor backward
    GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Right motor backward
    sleep(time)
    GPIO.output(Left_Backward_Pin, GPIO.LOW) #Left motor off
    GPIO.output(Right_Backward_Pin, GPIO.LOW) #Right motor off
    print('backward')
    sleep(1)
    
# Set up the camera so it can take pictures and help the rover "see" light.
camera = PiCamera() # Create camera object
camera.resolution = (640, 480) # Set the resultion (width, height)
camera.framerate = 30 # Set the framerate in fps

# We'll use 'rawCapture' to hold each image the camera takes, so we can analyze it.
rawCapture = PiRGBArray(camera, size=(640, 480))

# We will set the minimum and maximum values for colors using HSV.
# HSV stands for Hue, Saturation, and Value. It's another way to describe colors, like RGB.
# - Hue means color (like red, green, blue). It goes from 0 to 180.
# - Saturation means how bold or gray the color is. It goes from 0 to 255.
# - Value means how light or dark the color is. It goes from 0 to 255.
#
# By setting minimum and maximum HSV values, we can filter out parts of the image that aren't bright enough.
Light_Min = np.array([0,50,155], np.uint8) # Minimum HSV values for brightness detection
Light_Max = np.array([180,255,255], np.uint8) # Maximum HSV values for brightness detection

# Light threshold is the percentage of bright pixels needed to turn the LED on.
# Let's create left vs right threshold to help the rover decide if there's enough light on the left or right side to turn.
# For challenge 1, try adjusting these values to force more or fewer turns
Left_Threshold = 45
Right_Threshold = 45

# For challenge 2, 'count' will help us alternate between actions, like switching from forward to reverse each cycle using the modulo operator (%).
count = 0

# For challenge 2, We'll use a timer to keep track of how long the rover has been searching for light.
Start_Time = time.time()
Max_Search_Time = 30 #seconds

# Light_Intensity lets us adjust how long the rover moves based on how much light it sees.
# For challenge 4, We'll use this variable to make the rover drive longer or shorter depending on how strong the detected light is.
Light_Intensity = 1

# This loop keeps taking pictures and analyzing them to find where the light is brightest.
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    #Capturing image from camera and converting to HSV format
    sleep(3) # Wait 3 seconds
    Image = frame.array # Get the image data from the camera
    hsv = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV) # Convert the image from normal color (BGR) to HSV color space
    
    # Analyzing the value (lightness) layer of the image (3rd layer)
    Light = hsv[:,:,2]
    
    # Calculating the total light in the left and right halves of the image
    Left_Light = sum(sum(Light[:,0:320]))
    Right_Light = sum(sum(Light[:,320:]))
    
    # Determining the percentage of light of the left and right halves of the image
    Left_Light_Perc = Left_Light  / sum(sum(Light)) 
    Right_Light_Perc = Right_Light / sum(sum(Light))
    print('L = ' + str(Left_Light_Perc) + ' and R = ' + str(Right_Light_Perc))

    # For challenge 3, determining time passed since forward drive
    Elapsed_Time = round(time.time() - Start_Time,2)
    
    # For challenge 4, uncomment line 184 and replace the ? with the correect variables to find the ratio of the max light to the min light
    # We can set this as the intensity with np.max([Left_Light_Perc, Right_Light_Perc])
    # and np.min([Left_Light_Perc, Right_Light_Perc]), respectively
    Light_Intensity = np.max([Left_Light_Perc, Right_Light_Perc]) / np.min([Left_Light_Perc, Right_Light_Perc])
    
    # If there's enough light on the left side, the rover turns left.
    if Left_Light_Perc > Left_Threshold/100:
        drive_left_turn(Left_Turn_Time * Light_Intensity)
        
    # If there's enough light on the right side, the rover turns right.
    else:
        if Right_Light_Perc > Right_Threshold/100:
            drive_right_turn(Right_Turn_Time * Light_Intensity)
            
        # If neither side is bright enough, the rover moves forward or backward (depending on the cycle or timer).
        else: # If the search time gets too long, the rover spins to look for light elsewhere.
            if Elapsed_Time > Max_Search_Time: # Try changing the True to a comparitive (>) between Elapsed_Time and Max_Search_Time for challenge 3
                
                if count % 2 == 0: # Try changing the True to the modulo for challenge 2
                    drive_forward(Forward_Time)
                else: # For challenge 2, these drive commands will be executed on odd loops
                    drive_backward(Backward_Time)
            
                count = count + 1  # Increment the counter for the modulo
                
            else: # If max search time is exceeded, spin and look elsewhere for challenge 3
                drive_left_turn(Left_Turn_Time * 2)
                # Reset the timer for a new searching period
                Start_Time = time.time()
                print('here')
                
    sleep(Wait_Time)           
    
    # Clearing image cache
    rawCapture.truncate(0)

GPIO.cleanup()  # Turn off all output pins
