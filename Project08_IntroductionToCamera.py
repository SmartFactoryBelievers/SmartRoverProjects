###################################################################################
# Project 8
# GOAL: Trying out the Pi Camera and learning about the different image settings
# TASK: Build the Project 8 circuit and experiment with the camera in cool ways
####################################################################################

#Challenge 1
# Try changing the camera resolution to the minimum with 64, 64 and see how it looks

#Challenge 2
# Try changing the camera resolution the maximum with 2592, 1944 and
# the framerate to 15 and see how it looks

#Challege 3
# Try changing the camera rotation to flip it upside down (0) or left or right (90, 270)

#Challenge 4
# Try adding a text on top of the image and changing the colors and size

#Challenge 5
# Try looping through all the contrast and brightness options
# and annotate the image with their current levels

#Challenge 6
# Try looping through all the IMAGE_EFFECTS, EXPOSURE_MODES, and AWB_MODES options
# and annotate the image with their current levels

#Importing libraries
# Here we want sleep for timing and picamera for the Pi's camera
from picamera import PiCamera, Color
from time import sleep

# Setting up the camera
camera = PiCamera()
# Change the number of pixels and clarity of the camera
# For challenge 1 and 2, see what low and high resolution look like

#------------------------ CHALLENGE 1: CHANGE THE RESOLUTION TO THE MINIMUM (64, 64) ----------------------
camera.resolution = (640, 480)
# Change the rate at which the camera records images
#-------------------------------------- END OF CHALLENGE 1 ------------------------------------------

#------------------------ CHALLENGE 2: CHANGE THE RESOLUTION TO THE MAXIMUM (2592, 1944) AND FRAME RATE 15  ----------------------
camera.framerate = 30
# Rotate the image by x degrees
# Note that the camera assembly is upside down so 180 is right side up
#-------------------------------------- END OF CHALLENGE 2 ------------------------------------------

#------------------------ CHALLENGE 3: CHANGE THE CAMERA ROTATION TO FLIP IT UPSIDE DOWN (0) OR LEFT/RIGHT (90, 270) ----------------------
camera.rotation = 180
#-------------------------------------- END OF CHALLENGE 3 ------------------------------------------

#------------------------ CHALLENGE 4: ADD TEXT ON TOP OF THE IMAGE ----------------------
camera.annotate_text = 'Hello World!'
# Change the text size on top of the image between 6 and 160
camera.annotate_text_size = 50
# Change the text color in front and back
camera.annotate_foreground = Color('red')
camera.annotate_background = Color('blue')
#-------------------------------------- END OF CHALLENGE 4 ------------------------------------------

# Change the contrast between 0 and 100 (color/luminence difference between objects)
camera.contrast = 75
# Change the brightness of the image between 0 and 100
camera.brightness = 75
# Start the preview to view the camera image stream
camera.start_preview() #turn camera on
sleep(5)
camera.stop_preview() #turn camera off

camera.start_preview() #turn camera on
for i in range(100):
  # For challenge 5, try iterating through the brightness levels instead of contrast  
  #------------------------ CHALLENGE 5: CHANGE THE VARIABLE TO ITERATE THROUGH BRIGHTNESS INSTEAD OF CONTRAST ----------------------
  camera.contrast = i
  #-------------------------------------- END OF CHALLENGE 5 ------------------------------------------
  camera.annotate_text = '%s' %i
  sleep(0.1)
camera.stop_preview() #turn camera off

# For challenge 6, try iterating through IMAGE_EFFECTS, EXPOSURE_MODES, and AWB_MODES
#------------------------ CHALLENGE 6: CHANGE THE "for" STATEMENT TO ITERATE THROUGH IMAGE_EFFECTS, EXPOSURE_MODES, and AWB_MODES ----------------------
camera.start_preview() #turn camera on
for effect in camera.IMAGE_EFFECTS:
#-------------------------------------- END OF CHALLENGE 6 ------------------------------------------
  camera.annotate_text = '%s' %effect
  camera.image_effect = effect
  sleep(1)
camera.stop_preview() #turn camera off
camera.close() #close the camera
