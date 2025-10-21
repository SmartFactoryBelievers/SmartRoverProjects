# Project 11: Color Detection Driving
# Version v2.2, August 2025
#
# Goal:
# To program the camera to detect sign colors and drive accordingly.
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
#   - After line 192, try changing the colors associated with the driving commands, like flipping red and green 
# - Challenge 2:
#   - The modulo operator (%) gives you the remainder left over after dividing one number by another.
#     For example: 4 % 2 = 0, 5 % 2 = 1.
#   - Even numbers divided by 2 have a remainder of 0, while odd numbers have a remainder of 1.
#   - You can use the modulo operator to check if the number of button presses is even or odd, and use that to change the driving direction.
#   - On line 202, try adding a modulo operator to alternate between left and right turns on blue signs
# - Challenge 3:
#   - In line 184, try adjusting the drive time variables based on the prominance of the color from the argmax
# - Challenge 4:
#   - Try adding a memory variable in line 189 for the last color identified and dictate driving
#   - based on the pattern, like Red then Green
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
Left_Forward_Pin =  35 #the internal Pi pin number that goes to snap 1
Left_Backward_Pin =  31 #the internal Pi pin number that goes to snap 2
Right_Forward_Pin =  26 #the internal Pi pin number that goes to snap 3
Right_Backward_Pin =  21 #the internal Pi pin number that goes to snap 4
Button_Pin =  18 #the internal Pi pin number that goes to snap 6

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

# Create input pin for the button
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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
    
# For challenge 2, we'll use this variable to count how many times the button is pressed to alternate driving directions. 
count = 0
# In challenge 2, replace "if True:" with "if count % 2 == 0:" to check if the number of button presses is even or odd

# For challenge 3, We'll use this variable to make the rover drive longer or shorter depending on how strong the detected color is.
# First, let's define a variable so we can use the code as is
Color_Intensity = 1

# Setting up camera for analysis and to emphasize colors 
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

sleep(2) # let the camera settle

camera.iso = 100                              # Set camera sensitivity to light (ISO) to 100 for clearer images
camera.shutter_speed = camera.exposure_speed  # Match shutter speed to current exposure for consistent brightness
camera.exposure_mode = 'off'                  # Turn off automatic exposure adjustments so settings stay fixed
gain_set = camera.awb_gains                   # Save the current automatic white balance settings
camera.awb_mode = 'off'                       # Turn off automatic white balance (awb) so colors don't change automatically
camera.awb_gains = gain_set                   # Apply the saved white balance settings to keep color detection stable

# Prepare to analyze images by removing background colors ("noise").
# Each image is made up of tiny dots (pixels), and each pixel has a red, green, and blue value.
# Images are stored in a 3D array with each pixel having Red, Green, and Blue values
Image = np.empty((640,480,3),dtype=np.uint8)
Noise = np.empty((640,480,3),dtype=np.uint8)
RGB_Text = ['Red','Green','Blue'] # Array for naming color

# Let's remove the background 'Noise' colors to emphasize the object's color
camera.capture(Noise,'rgb')
Noise = Noise-np.mean(Noise)

# For Challenge 4, remove the comment in line 162 and create a memory variable to keep track of the last color found, 
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
            Color = RGB_Text[np.argmax(RGB_Array)]
            print(Color)
        
        # For challenge 3, let's compare the most prominent color to the second most
        # We can use this ratio to set the Color_Intensity variable with max as np.max(RGB_Array) 
        # and mid as np.median(RGB_Array). However, the color channels can be negative, so let's use a max to keep positive
        # Remove the comment in line 184 and replace the ? with the correct variables for max as np.max(RGB_Array) and mid as np.median(RGB_Array)
        #Color_Intensity = np.max([? / ?, 2])
        
        # For challenge 4, let's look for a pattern like Red then Color
        # We can use an if statement to see if the Last_Color was 'Red'
        # Replace this True with a logical to check, remember it's ==, not = here
        if True:
        
            # Turn on the motor outputs based on the determined object color
            
            if Color == 'Red': # Backward for Red object
                drive_backward(Backward_Time * Color_Intensity)
                sleep(Wait_Time)
          
            if Color == 'Green': # Forward for Green object
                drive_forward(Forward_Time * Color_Intensity)
                sleep(Wait_Time)

            if Color == 'Blue': # Turn for Blue object
                
                if True: # For challenge 2, Use the modulo operator to switch between left and right turns each time a blue sign is detected.
                    drive_left_turn(Left_Turn_Time * Color_Intensity)
                    
                else: 
                    drive_right_turn(Right_Turn_Time * Color_Intensity)
                                
                sleep(Wait_Time)
                count = count + 1 # Increment the counter for the modulo
        
        # For challenge 4, remove the comment to update Last_Color after outputs
        #Last_Color = Color
        print('Ready to take photo')

GPIO.cleanup()  # Turn off all output pins
