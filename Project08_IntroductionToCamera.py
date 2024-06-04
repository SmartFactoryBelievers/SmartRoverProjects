###########################################################################################
# Project 8                                                                               #
# GOAL: Trying out the Pi Camera and learning about the different image settings          #
# TASK: Build the Project 8 circuit and experiment with the camera in cool ways           #
###########################################################################################

# Step 1: Importing libraries
from picamera import PiCamera, Color
from time import sleep
# Here we want sleep for timing and picamera for the Pi's camera

# Step 2: Variables 
camera = PiCamera() 

# Step 3: Setting up the camera 
# Change the number of pixels and clarity of the camera
#------------------------ CHALLENGE 1: CHANGE THE RESOLUTION TO THE MINIMUM (64, 64) -------------------------------------------
camera.resolution = (640, 480)
# number of pixels on the width and height of the image
#-------------------------------------- END OF CHALLENGE 1 ---------------------------------------------------------------------

# Change the rate at which the camera records images
#------------------------ CHALLENGE 2: CHANGE THE RESOLUTION TO THE MAXIMUM (2592, 1944) AND FRAME RATE to 15  -----------------
camera.framerate = 30
# video is just a stream of images that gives the illusion of movement
# framerate is the number of images recorded each second. Most films are 24 frames per second (fps), and most games target 30 or 60 fps
#-------------------------------------- END OF CHALLENGE 2 ---------------------------------------------------------------------

# Rotate the image by x degrees - Note that the camera assembly is on its side, so 90 is right side up
#------------------------ CHALLENGE 3: CHANGE THE CAMERA ROTATION TO FLIP IT UPSIDE DOWN (0) OR LEFT/RIGHT (90, 270) ----------
camera.rotation = 90
# The camera in the pi is on its side, so you need to rotate the image to make it right side up. 
# Experiment with different numbers to get some weird perspectives!
#-------------------------------------- END OF CHALLENGE 3 ------------------------------------------

#------------------------ CHALLENGE 4: ADD TEXT ON TOP OF THE IMAGE AND TRY TO CHANGE THE COLOR AND SIZE ----------------------
# annotating refers to adding text to an image. Notice that you need the quotation marks to denote that it is a string and not a variable
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

# Step 4: Main Code Body
# Start the preview to view the camera image stream and automatically run through three demos back-to-back

# Demo 1
camera.start_preview() #turn camera on 
sleep(5)
camera.stop_preview() #turn camera off
# You should see the camera turn on with the annotations that you added earlier on, and then turn off after 5 seconds.

# Demo 2
camera.start_preview() #turn camera on
# for i in range(100) means that starting at i = 1, the loop will repeat 100 times, with i increasing in value by 1 each repetition
for i in range(100):
  
  #------------------------ CHALLENGE 5: CHANGE THE VARIABLE TO ITERATE THROUGH BRIGHTNESS INSTEAD OF CONTRAST ------------------
  camera.contrast = i
  #-------------------------------------- END OF CHALLENGE 5 -------------------------------------------------------------------

  # the %s in the line below is declaring that a percent symbol followed by a string will be output in this section
  # the %i is the variable that will go in that section
  # if you think about what we've already done, this code will add an increasing percentage on the video that will increase with the contrast
  camera.annotate_text = '%s' %i
  sleep(0.1)
camera.stop_preview() #turn camera off

# Demo 3
#------------------ CHALLENGE 6: CHANGE THE "for" STATEMENT TO ITERATE THROUGH IMAGE_EFFECTS, EXPOSURE_MODES, and AWB_MODES -----
camera.start_preview() #turn camera on
for effect in camera.IMAGE_EFFECTS:
#-------------------------------------- END OF CHALLENGE 6 ----------------------------------------------------------------------
  
  camera.annotate_text = '%s' %effect
  camera.image_effect = effect
  sleep(1)
camera.stop_preview() #turn camera off
camera.close() #close the camera

##############
# Challenges #
##############

#Challenge 1
# Try changing the camera resolution to the minimum with 64, 64 and see how it looks
#    - See the Challenge 1 Section in the main code
#    - Q: Do you think this requires more or less processing power from the pi?

#Challenge 2
# Try changing the camera resolution the maximum with 2592, 1944 and
# the framerate to 15 and see how it looks
#    - See the Challenge 2 Section in the main code
#    - Q: Do you think this requires more or less processing power from the pi?

#Challege 3
# Try changing the camera rotation to flip it upside down (0) or left or right (90, 270)
#    - See the Challenge 3 Section in the main code

#Challenge 4
# Try adding a text on top of the image and changing the colors and size
#    - See the Challenge 4 Section in the main code

#Challenge 5
# Try looping through all the contrast and brightness options
# and annotate the image with their current levels
#    - See the Challenge 5 Section in the main code

#Challenge 6
# Try looping through all the IMAGE_EFFECTS, EXPOSURE_MODES, and AWB_MODES options
# and annotate the image with their current levels
#    - See the Challenge 6 Section in the main code
