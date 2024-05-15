###########################################################################################
# Project 8                                                                               #
# GOAL: Trying out the Pi Camera and learning about the different image settings          #
# TASK: Build the Project 8 circuit and experiment with the camera in cool ways           #
###########################################################################################

# Step 1: Importing libraries
from picamera import PiCamera, Color
from time import sleep
# Here we want sleep for timing and picamera for the Pi's camera

# Step 2: Setting up the camera
camera = PiCamera() 

# Change the number of pixels and clarity of the camera
#------------------------ CHALLENGE 1: CHANGE THE RESOLUTION TO THE MINIMUM (64, 64) -------------------------------------------
camera.resolution = (640, 480)
#-------------------------------------- END OF CHALLENGE 1 ---------------------------------------------------------------------

# Change the rate at which the camera records images
#------------------------ CHALLENGE 2: CHANGE THE RESOLUTION TO THE MAXIMUM (2592, 1944) AND FRAME RATE to 15  -----------------
camera.framerate = 30
#-------------------------------------- END OF CHALLENGE 2 ---------------------------------------------------------------------

# Rotate the image by x degrees - Note that the camera assembly is upside down so 180 is right side up
#------------------------ CHALLENGE 3: CHANGE THE CAMERA ROTATION TO FLIP IT UPSIDE DOWN (0) OR LEFT/RIGHT (90, 270) ----------
camera.rotation = 180
#-------------------------------------- END OF CHALLENGE 3 ------------------------------------------

#------------------------ CHALLENGE 4: ADD TEXT ON TOP OF THE IMAGE AND TRY TO CHANGE THE COLOR AND SIZE ----------------------
camera.annotate_text = 'Hello World!'
# Change the text size on top of the image between 6 and 160
camera.annotate_text_size = 50
# Change the text color in front and back
camera.annotate_foreground = Color('red')
camera.annotate_background = Color('blue')
#-------------------------------------- END OF CHALLENGE 4 ---------------------------------------------------------------------

# Change the contrast between 0 and 100 (color/luminence difference between objects)
camera.contrast = 75
# Change the brightness of the image between 0 and 100
camera.brightness = 75

# Step 3: Start the preview to view the camera image stream and automatically run through three demos back-to-back

# Demo 1
camera.start_preview() #turn camera on 
sleep(5)
camera.stop_preview() #turn camera off

# Demo 2
camera.start_preview() #turn camera on
for i in range(100):
  #------------------------ CHALLENGE 5: CHANGE THE VARIABLE TO ITERATE THROUGH BRIGHTNESS INSTEAD OF CONTRAST ------------------
  camera.contrast = i
  #-------------------------------------- END OF CHALLENGE 5 -------------------------------------------------------------------
  
  camera.annotate_text = '%s' %i
  sleep(0.1)
camera.stop_preview() #turn camera off

#Demo 3
#------------------ CHALLENGE 6: CHANGE THE "for" STATEMENT TO ITERATE THROUGH IMAGE_EFFECTS, EXPOSURE_MODES, and AWB_MODES -----
camera.start_preview() #turn camera on
for effect in camera.IMAGE_EFFECTS:
#-------------------------------------- END OF CHALLENGE 6 ----------------------------------------------------------------------
  
  camera.annotate_text = '%s' %effect
  camera.image_effect = effect
  sleep(1)
camera.stop_preview() #turn camera off
camera.close() #close the camera
