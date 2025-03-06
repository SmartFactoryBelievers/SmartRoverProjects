# Smart Rover Project 10: Color Detection
The following module will guide learners through the individual Smart Rover project. The module contains key terminology used in the project, technology troubleshooting tips, Smart Rover tips and tricks, and extension resources for individual exploration.

## Table of Contents
1. [Project 10: Color Detection](#1-Project-10-Color-Detection)
2. [Key Terminology](#2-Key-Terminology)
3. [Project 10 Troubleshooting](#3-Project-10-Troubleshooting)
4. [Additional Resources](#4-Additional-Resources)

## 1. Project 10: Color Detection
### About Project 10
:sparkles: **Objective:** To program the rover to distinguish between various colors.

In this project, you will learn about primary color identification and object detection.

### Required Components
Smart Module, Press Switch (S2), Horn (W1), LED (D4), 1KΩ Resistor (R2). 2 snap connector (2) x 2, 3 snap connector (3) x 1, cutout color signs (found in [The Smart Rover Project Manual](../Resources/Smart-Rover-Manual.pdf))

### Instructions
1. First, connect your Smart Module to a monitor. Then build the circuit as shown below. 
2. Once the circuit is created, open up Thonny and load Project10-ColorDetection.py into the code editor. 
3. Once you have completed the program, use the camera to capture and analyze the color profile of the cutout signs in the back of the manual (also provided below).

> :information_source: Connecting a monitor via the HDMI cable provided in the Smart Rover kit is the quickest and easiest way to view the output of the Raspberry Pi in the Smart Module. It is possible to connect the Raspberry Pi to a laptop by creating a Virtual Network Connection (VNC) but this is a more advanced approach and should be utilized only if an HDMI-compatiable monitor is not available.

### Project 10 Diagram
![Project 10 Build Diagram](https://articulateusercontent.com/rise/courses/j5EbK7AaGYjxxWnCNjqkzlA749c83LVA/T9MRfvFmh-0lEw1G.jpg)

### Cutout Color Signs
Click on the image below and then print and cut out to use them for the color-detection projects (Project #10 and Project #11) or with your own projects with the camera. The signs can be folded to stand up on their own.

![Cutout Color Signs](https://articulateusercontent.com/rise/courses/j5EbK7AaGYjxxWnCNjqkzlA749c83LVA/qfINESsSv92lN8qP.jpg)

### Project 10 Build Video
### Project 10 Code-along Video

### Project 10 Code Challenges
Once you have the program running correctly, try the following challenges:

:one: Try changing the LED and horn outputs both in the code and on the rover.

:two: Try writing a function to handle the LED and horn so it can be called after each color. 

:three: Try adding a margin that the argmax for color must be exceeded to be considered a certain color. 

:four: Try adding a memory array for the last two colors identified and output flashes or buzzes based on the pattern.

## 2. Key Terminology
The following are key vocabulary terms associated with the Smart Rover Project 10.  The key terms will help support you as you navigate the rover activity. 
- **RGB Color Scale:** Color definitions based on the combination of the levels of red, green and blue included in a color.

## 3. Project 10 Troubleshooting

### Solution Code
If you need to debug your code, please refer to the [Project 10 Solution Code](../Resources/Solutions/Project10_ColorDetection_Solution.py)

## Tips & Tricks
### :warning: **WARNING** :warning: 
Always check your wiring before turning on a circuit. Never leave a circuit unattended while the batteries are installed. Never connect additional batteries or any other power sources to your circuits. Discard any cracked or broken parts.
- Most circuit problems are due to incorrect assembly, always double-check that your circuit exactly matches the drawing for it especially the direction of arrows on the circuits. 
- Be sure that parts with positive/negative markings are positioned as per the build diagram.
- Be sure that all connections are securely snapped.
- Try replacing the batteries in the Rover body

### [Smart Module Pin Layout Guide](../Resources/smart-module-pinout.jpg)
### [Thonny Controls Overview](../Resources/introduction-to-raspberry-pi.pdf)
### [Debugging Python in Thonny](../Resources/introduction-to-raspberry-pi.pdf)

## 4. Additional Resources
- [The Smart Rover Project Manual](../Resources/Smart-Rover-Manual.pdf)
- [Snap Circuit Components list](../Resources/snap-circuit-components.pdf)
- [Circuit Troubleshooting](../Resources/introduction-to-electricity.pdf)
- [FAQ]()

✅ For a full list of additional resources, visit the [Resources Folder](../Resources/README.md)
