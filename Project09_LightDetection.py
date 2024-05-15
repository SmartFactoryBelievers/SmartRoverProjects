##########################################################################################################
# Project 9                                                                                              #
# Goal: Learn more about programming the Pi camera to capture and analyze the surrounding light levels   #
# Task: Build the the Project 9 circuit and flash the LED when certain light thresholds are exceeded     #
#       Point a flashlight at the camera to activate the LED                                             #
##########################################################################################################

# Step 1: Importing libraries
# Here we want sleep for timing, GPIO for the Pi's pins, & picamera for the Pi's camera
from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera
# We will also need PiRGBArray and cv2 for computer vision/image processing
from picamera.array import PiRGBArray
import cv2
# Numpy is a great numerical tools package to help with the math required
import numpy as np

# Step 2: Variables
LED_Pin = 21 #the internal Pi pin number that goes to snap 4
Buzzer_Pin = 26 #the internal Pi pin number that goes to snap 3

# Step 3: Raspberry Pi Set Up
GPIO.setmode(GPIO.BOARD)
# Our output pins, start off
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW)

# Step 4: Set Up the Camera for Light Detection
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))

#Setting Min and Max values for HSV image analysis
# Like RGB, HSV is an image color scheme but it's not defined by a color ratio
# Instead, it uses three values: Hue (Color), Saturation (Grayness), and Value (Lightness)
# Hue goes from 0 to 180, while Saturation and Value go from 0 to 255

Light_Min = np.array([0,50,155], np.uint8)
# array refers to a data structure that contains multiple elements, three in this case 
Light_Max = np.array([180,255,255], np.uint8) 
# uint8 is a data value and assigns a maximum value of 255 to the values within the brackets

# Setting up the ambient light percentage threshold for turning the LED - minimum light to trigger LED

#------------------------ CHALLENGE 1: CHANGE THE LIGHT THRESHOLD VALUE TO KEEP THE LED ALWAYS ON ---------------------------------------
#------------------------ CHALLENGE 2: CHANGE THE LIGHT THRESHOLD VALUE TO KEEP THE LED ALWAYS OFF --------------------------------------
Light_Threshold = 40
#-------------------------------------- END OF CHALLENGE 1 & 2 --------------------------------------------------------------------------

# Step 5: Main Code Body
i=0 #Loop Counter variable, used to settle the camera with ambient light

# Using the video camera feature of the camera through an image capture for loop
# Within camera.capture_continuous, the output is defined first, followed by the format and the video port
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
# Capturing an image from the camera and converting it to HSV format
  sleep(3)
  image = frame.array
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  
  #Setting the lower bound as the average of the ambient light
  if i < 1:
    Ambient_Light = np.mean(np.mean(hsv[:,:,2]))
    
    #------------------------ CHALLENGE 4: REPLACE Light_Min WITH Light_Max ----------------------
    Light_Min = np.array([0,50,Ambient_Light], np.uint8)
    #-------------------------------------- END OF CHALLENGE 4 ------------------------------------------
    
    # Filtering out pixels with less lightness than the minimum/ambient average
    # This creates what's called a mask used in demarcating/highlighting key regions of an image
    Light_Filter = cv2.inRange(hsv,Light_Min, Light_Max)
    
    # Percentage of pixels above the light threshold
    # This is calculated as the True regions of the mask / number of pixels in image
    Light_Percent = round(sum(sum(Light_Filter ==255))/(640*480),2)
    
  # If the light percentage threshold is exceeded, blink the LED
  if Light_Percent > Light_Threshold/100:
    print(str(Light_Percent) + ' of image above ambient light levels')
    GPIO.output(LED_Pin, GPIO.HIGH) #LED on
    sleep(2)
    GPIO.output(LED_Pin, GPIO.LOW) #LED off
    
  #----------------- CHALLENGE 3: UNCOMMENT AND REPLACE THE ?? BELOW TO BUZZ THE BUZZER WHEN THERE IS NOT ENOUGH LIGHT ----------------------
  else:
    print('Not enough light detected')
    #GPIO.output(??, GPIO.HIGH) #Buzzer on (CHALLENGE 3)
    #sleep(2)
    #GPIO.output(??, GPIO.LOW) #Buzzer off (CHALLENGE 3)
  #-------------------------------------- END OF CHALLENGE 3 ------------------------------------------
    
  #Clearing image cache to avoid overwhelming the Pi memory
  rawCapture.truncate(0)
  
  # Iterate counter
  i = i +1


#Challenge 1
# Try changing the Light Threshold value to keep the LED always on

#Challenge 2
# Try changing the Light Threshold value to keep the LED always off

#Challege 3
# Can you add another pin for the buzzer to sound when the ambient light is too low?

#Challege 4
# Can you swap out the Max and Min Light thresholds to activate the LED in darkness?
