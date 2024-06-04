############################################################################################
# Project 10                                                                               #
# Goal: Use the Pi camera to capture and analyze the color profile of objects              #
# Task: Build the Project 10 circuit and indicate the color of objects with LED and buzzer #
############################################################################################

# Step 1: Importing Libraries
# Here we want sleep for timing, GPIO for the Pi's pins, & picamera for the Pi's camera
from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera
# Numpy is a great numerical tools package to help with the math required
import numpy as np

# Step 2: Defining Variables
#----------------------------------- CHALLENGE 1: SWAP THE POSITION OF THE LED AND BUZZER IN THE CODE & ON THE ROVER ---------------------------
LED_Pin = 21 #the internal Pi pin number that goes to snap 4
Buzzer_Pin = 26 #the internal Pi pin number that goes to snap 3
Button_Pin = 18 #the internal Pi pin number that goes to snap 6
#--------------------------------------------------------------- END OF CHALLENGE 1 ------------------------------------------------------------

# Step 3: Raspberry Pi Set Up
GPIO.setmode(GPIO.BOARD)
#Our output pins, start off
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Buzzer_Pin, GPIO.OUT, initial=GPIO.LOW)
#Our input pins, start down
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Step 4: Setting Up the Camera for Analysis and to Emphasize Colors
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
sleep(2) #let the cameraera settle
camera.iso = 100
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
gain_set = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = gain_set

# Prepping for image analysis and eliminating background Noise
#Images are stored in a 3D array with each pixel having Red, Green, and Blue values
Image = np.empty((640,480,3),dtype=np.uint8)
# Think of the array as a cube, with a width of 640, a height of 480, and a thickness of 3
# The "image" is on the width and height of the cube, and the "depth" is the color of the pixel in each location
# "Depth" 1, 2, and 3 each relate to Blue, Green, and Red. This is a great example of how array's store information!

Noise = np.empty((640,480,3),dtype=np.uint8)
RGB_Text = ['Red','Green','Blue'] #Array for naming color
# Let's remove the background 'Noise' colors to emphasis the object's color
camera.capture(Noise,'rgb')
Noise = Noise-np.mean(Noise)

#------------------------ CHALLENGE 2: UNCOMMENT THE LINES AND REPLACE THE ?? WITHT THE CORRECT VARIABLES ---------------------------------------
# For challenge 2, let's create a function like we've done before for outputs
# The variables should relate to the LED and Buzzer components
# It should have output_pin and delay time arguments to turn them High and then Low
# Don't forget to add your function in the "While True" code block below!
#def your_function(??, ???):
  # sleep(???)
  # GPIO.output(??, GPIO.?)
  # sleep(???)
  # GPIO.output(??, GPIO.?)
#-------------------------------------- END OF CHALLENGE 2 --------------------------------------------------------------------------------------

# Step 5: Main Code Body
#Looping with different images to determine object colors upon button press
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
    
    #------------- CHALLENGE 3: REPLACE "True" WITH A LOGICAL STATEMENT THAT SETS A THRESHOLD THE MAX COLOR MUST EXCEED ----------------------   
    # For challenge 3, let's set a threshold the max color must exceed
    # This will help the camera avoid mistakes in bad lighting or glare
    Col_Margin = 0.8
    # Let's check if the max * margin > mid with max as np.max(RGB_Array) and mid as np.median(RGB_Array)
    # HINT: YOU SHOULD MAKE 2 NEW VARIABLES, Col_Max and Col_Mid
    if True:
      Color = RGB_Text[np.argmax(RGB_Array)]
      print(Color)
    
    else:
      print('No prominent color found')
    #------------------------------------------ END OF CHALLENGE 3 ----------------------------------------------------------------------------
    
    #------------------------ CHALLENGE 4: REPLACE "True" WITH A LOGICAL STATEMENT TO CHECK THE Last_Color ------------------------------------
    # For challenge 4, let's look for a pattern in the colors that are identified
    # HINT: Uncomment Last_Color before testing
    # HINT: We can use an if statement to see if the Last_Color was Red
    # HINT: Make sure Last_Color updates after each output
    # Replace this True with a logical statement to check, remember it's ==, not = here
    if True:
      
      # Activate outputs based on the determined object color
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
        
    #Last_Color = Color
    print('Ready to take photo')
 #------------------------------------------------- END OF CHALLENGE 4 ---------------------------------------------------------------------------------------------------------
    
#Challenge 1
# Try swapping the LED and buzzer outputs in the code and then also on the rover

#Challenge 2
# Try writing a function to handle the LED and buzzer so it can be called after each color

#Challege 3
# Try adding a margin that the argmax for Color must exceed to be considered a certain color

#Challege 4
# Try adding a memory variable for the last color identified and activate flashes and buzzes
# a new LED or buzzer output based on the pattern, like Red then Green
