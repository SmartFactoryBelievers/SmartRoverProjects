# Project 9: Light Detection
# Version v2.2, August 2025
#
# Goal:
# To learn about HSV (Hue, Saturation, Value) image processing and program the camera to detect light. 
# HSV image processing is a way for computers to look at pictures and find colors by thinking about what the color is, how bright it is, and how strong it is- kind of like how we see and describe colors in real life. 
# This helps computers easily find things like red apples or green leaves in photos.
#
# Step 1: Read the Code Carefully
# - At the top of the code, you’ll see lines starting with '#'.
# - These are comments that explain what the code is doing. Read each comment to understand the steps.
# - Read every line of this code carefully to understand the variables & functions
#
# Step 2: Build Your Circuit
# - Gather the components: Smart Module, LED (D4), 1KΩ R2 Resistor (x1), 2-snap connector (x2)
# - Follow the diagram or instructions provided by your teacher to connect the components to the correct pins on your Raspberry Pi.
#
# Step 3: Open the Python File in Thonny
# - Open Thonny on your Raspberry Pi.
# - Load the file Project09_LightDetection.py.
#
# Step 4: Run the Code
# - Click the green 'Run' Button to run the code.
#
# Step 5: Try the Challenges
# - Challenge 1:
#   - Try changing the Light Threshold value to keep the LED always on
# - Challenge 2:
#   - Try changing the Light Threshold value to keep the LED always off
# - Challenge 3:
#   - Can you add another pin for the buzzer to sound when the ambient light is too low?
# - Challenge 4:
#   - Can you swap out the Max and Min Light thresholds to activate the LED in darkness?
#
# Step 6: Ask for Help if Needed
# - If you get stuck, ask your teacher or a classmate for help!

# Importing libraries
# Libraries are defined sets of code for specific uses
# Here we want the sleep function for timing and GPIO for the Pi's pin
from time import sleep
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
LED_Pin =  21 # the internal Pi pin number that goes to snap 4
Buzzer_Pin =  26 # the internal Pi pin number that goes to snap 3

# Let's set up our Raspberry Pi
GPIO.setmode(GPIO.BOARD)

# Create output pins for the LED & Buzzer
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) # Set LED_Pin as an Output pin, start off
GPIO.setup(Buzzer_Pin, GPIO.OUT, initial=GPIO.LOW) # Set Buzzer_Pin as an Output pin, start off

# Setting up the camera for light detection
camera = PiCamera() # Create camera object
camera.resolution = (640, 480) # Set the resultion (width, height)
camera.framerate = 30 # Set the framerate in fps

# Let's create an array to store the images
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

# Light_Threshold is the percentage of bright pixels needed to turn the LED on.
# For challenges 1 and 2, Try changing this value to see how sensitive the LED is to light.
Light_Threshold = 40

# Let's create a Loop Counter to help the camera adjust to the room's light when starting
i = 0

# This loop keeps capturing images from the camera, one after another and converts to HSV
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    sleep(3) # wait 3 seconds
    image = frame.array # Get the image data from the camera
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # Convert the image from normal color (BGR) to HSV color space

    # On the first loop, measure the average brightness in the room
    if i < 1:
        Ambient_Light = np.mean(np.mean(hsv[:,:,2])) # Find the average brightness (Value) in the image
        
        # For challenge 4, try replacing Light_Min with Light_Max to see what happens
        Light_Max = np.array([0,50,Ambient_Light], np.uint8) # Set the minimum brightness to the average found

    # Filter out (ignore) pixels that are less bright than our minimum value.
    # This creates a "mask" that highlights only the bright parts of the image.
    Light_Filter = cv2.inRange(hsv,Light_Min,Light_Max)
    
    # Calculate the percentage of pixels that are bright enough.
    # This is the number of bright pixels divided by the total number of pixels in the image
    Light_Percent = round(sum(sum(Light_Filter ==255))/(640*480),2)
    print(str(Light_Percent) + ' of image above ambient light levels') # print the result message
        
    
    # If enough of the image is bright, turn the LED on for 2 seconds, then off
    if Light_Percent > Light_Threshold/100:
        GPIO.output(LED_Pin, GPIO.HIGH) #LED on
        sleep(2) # wait 2 seconds
        GPIO.output(LED_Pin, GPIO.LOW) #LED off
        
    # If not enough of the image is bright, do not turn on the LED
    else:
        print('Not enough light detected') 
        
        # For challenge 3, if there's not enough light, turn on the Buzzer
    
        GPIO.output(Buzzer_Pin, GPIO.HIGH) #Buzzer on
        sleep(2)
        GPIO.output(Buzzer_Pin, GPIO.LOW) #Buzzer off
        
    # Clearing image cache to avoid overwhelming the Pi memory
    rawCapture.truncate(0)

    # Increase the counter by 1 for the next loop
    i = i +1

GPIO.cleanup()  # Turn off all output pins
