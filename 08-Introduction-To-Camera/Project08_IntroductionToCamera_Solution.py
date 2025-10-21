# Project 8: Introduction to Camera
# Version v2.2, August 2025
#
# Goal:
# In this project, you will learn about the camera and different image settings.
#
# Step 1: Read the Code Carefully
# - At the top of the code, you’ll see lines starting with '#'.
# - These are comments that explain what the code is doing. Read each comment to understand the steps.
# - Read every line of this code carefully to understand the variables & functions
#
# Step 2: Build Your Circuit
# - Gather the components: Smart Module
# - Follow the diagram or instructions provided by your teacher to connect the components to the correct pins on your Raspberry Pi.
#
# Step 3: Open the Python File in Thonny
# - Open Thonny on your Raspberry Pi.
# - Load the file Project08_IntroductionToCamera.py.
#
# Step 4: Run the Code
# - Click the green 'Run' Button to run the code.
#
# Step 5: Try the Challenges
# - Challenge 1:
#   - Try changing the camera resolution in line 55 to the minimum with 64, 64 and framerate to 15 in line 60 and see how it looks.
# - Challenge 2:
#   - Try changing the camera resolution in line 55 the maximum with 2592, 1944 and the framerate to 15 in line 60 and see how it looks.
# - Challenge 3:
#   - Try changing the camera rotation in line 66 to flip it upside down (0) or left or right (90, 270).
# - Challenge 4:
#   - Try adding a text on top of the image in line 70 and changing the colors and size.
# - Challenge 5:
#   - In line 100, try looping through all the brightness options and annotate the image with their current levels.
# - Challenge 6:
#   - In line 107, try looping through all the EXPOSURE_MODES and AWB_MODES options and annotate the image with their current levels.
#
# Step 6: Ask for Help if Needed
# - If you get stuck, ask your teacher or a classmate for help!

# Importing libraries
# Libraries are defined sets of code for specific uses
# Here we want the sleep function for timing and GPIO for the Pi's pin
from picamera import PiCamera, Color
from time import sleep

# Let's set up our camera as an object.
# Objects are created from a "class," which acts like a blueprint. 
# Think of a class as a recipe and an object as the cake you bake from that recipe.
# An object like our camera can have properties (camera data, like resolution or brightness) and methods (camera actions, like start_preview() or close()).
camera = PiCamera()

# camera.resolution sets the camera's resolution (width, height) in pixels.
# Higher numbers mean more detail, but bigger files. Lower numbers are faster and use less memory.
# For challenges 1 and 2, see what low (64, 64) and high (2592, 1944) resolution look like.
camera.resolution = (2592, 1944)

# camera.framerate sets how many frames per second (fps) the camera captures.
# Higher framerate means smoother video, but uses more power and memory.
# For challenges 1 and 2, change the framerate to 15 fps
camera.framerate = 15

# camera.rotation rotates the camera's image by a certain number of degrees.
# This is useful if your camera is installed upside down or sideways.
# Example: 180 flips the image right side up, 90 or 270 turns the image sideways.
# For challenge 3, try rotating the camera
camera.rotation = 90

# camera.annotate_text adds text to the camera preview/image.
# For challenge 4, try annotating the image with your own message
camera.annotate_text = 'I completed Challenge 4!'

# camera.annotate_text_size sets the size of the annotation text.
# Can be between 6 (very small) and 160 (very large).
camera.annotate_text_size = 50

# camera.annotate_foreground sets the color of the annotation text.
# Use Color('colorname') or RGB values.
camera.annotate_foreground = Color('red')

# camera.annotate_background sets the background color behind the annotation text.
camera.annotate_background = Color('blue')

# camera.contrast adjusts the image contrast (difference between light and dark areas).
# Range is from 0 (no contrast) to 100 (high contrast). 
camera.contrast = 75

# camera.brightness adjusts the image brightness.
# Range is from 0 (dark) to 100 (bright).
camera.brightness = 75

# Show a live preview of the camera image for 5 seconds.
camera.start_preview()
sleep(5)
camera.stop_preview()

# Loop through all contrast levels from 0 to 99, updating the annotation.
# For challenge 5, try iterating through the brightness levels instead of contrast.
camera.start_preview() # start the camera
for i in range(100): # loop through each number from 0 to 99
    camera.brightness = i # set camera brightness as the number of current loop
    camera.annotate_text = '%s' %i # display the number of brightness level
    sleep(0.1) # wait 0.1 second before moving to the next brightness level
camera.stop_preview() # stop the camera preview

# For challenge 6, try iterating through IMAGE_EFFECTS, EXPOSURE_MODES, and AWB_MODES 
camera.start_preview() # start the camera
for mode in camera.EXPOSURE_MODES: # For challenge 6, replace IMAGE_EFFECTS with EXPOSURE_MODES or AWB_MODES
    camera.annotate_text = '%s' %mode # display the name of the current effect
    camera.exposure_mode= mode # change the camera's image effect to the current value from the loop
    sleep(1) # wait 1 second before moving to the next effect
camera.stop_preview() # stop the camera preview

camera.close() # close the camera object to free up memory and resources
