# Smart Rover Project 11: Color Detection Driving
The following module will guide learners through the individual Smart Rover project. The module contains key terminology used in the project, technology troubleshooting tips, Smart Rover tips and tricks, and extension resources for individual exploration.

## Table of Contents
1. [Project 11: Color Detection Driving](#1-Project-11-Color-Detection-Driving)
2. [Key Terminology](#2-Key-Terminology)
3. [Project 11 Troubleshooting](#3-Project-11-Troubleshooting)
4. [Additional Resources](#4-Additional-Resources)

## 1. Project 11: Color Detection Driving
### About Project 11
:sparkles: **Objective:** To program the camera to detect sign colors and drive accordingly.

In this project, you will learn about introductory autonomous driving.

### Required Components
Smart Module, Smart Rover, Motor Control (U8), Press Switch (S2), 1KΩ Resistor (R2) x 4, connector wires (all colors), 2 snap connectors (2) x 4, 3 snap connector (3) x 1, cutout color signs (found in [The Smart Rover Project Manual](../Resources/Smart-Rover-Manual.pdf))

### Instructions
1. First, connect your Smart Module to a monitor. Then build the circuit as shown below.
2. Add batteries to the Smart Rover.
> :pencil2: for all projects involving the Smart Rover loading batteries are required
3.Build the circuit using the diagram below or the project manual
4. Once the circuit is created, open up Thonny and load Project11-ColorDetectionDriving.py into the code editor. 
5. Once you have completed the program, use the rover and the cut-out signs in the back of the manual (also provided below) to have it drive according to the signs.

> :information_source: Connecting a monitor via the HDMI cable provided in the Smart Rover kit is the quickest and easiest way to view the output of the Raspberry Pi in the Smart Module. It is possible to connect the Raspberry Pi to a laptop by creating a Virtual Network Connection (VNC) but this is a more advanced approach and should be utilized only if an HDMI-compatiable monitor is not available.

### Project 11 Diagram
![Project 11 Build Diagram](https://articulateusercontent.com/rise/courses/WVKxIldX45myjE-ViohObRgIWdFPgG51/DCc3EAHepQy0GKak.jpg)

### Cutout Color Signs
Click on the image below and then print and cut out to use them for the Color-Detection-Driving projects (Project #11 and Project #11) or with your own projects with the camera. The signs can be folded to stand up on their own.

![Cutout Color Signs](https://articulateusercontent.com/rise/courses/j5EbK7AaGYjxxWnCNjqkzlA749c83LVA/qfINESsSv92lN8qP.jpg)

### Project 11 Build Video
### Project 11 Code-along Video

### Project 11 Code Challenges
Once you have the program running correctly, try the following challenges:

:one: Try changing the colors associated with the driving commands.

:two: Try adding a modulo `%` operator to alternate between left and right turns on blue signs.

:three: Try setting the drive_time variable based on the prominence of color from the argmax. 

:four: Try adding a memory variable for the last color identified and dictate driving based on the pattern.

## 2. Key Terminology
The following are key vocabulary terms associated with the Smart Rover Project 11.  The key terms will help support you as you navigate the rover activity. 
- **Autonomous driving:** the capability of a vehicle to drive partly or fully by itself, with limited or no human intervention

## 3. Project 11 Troubleshooting

### Solution Code
If you need to debug your code, please refer to the [Project 11 Solution Code](../Resources/Solutions/Project11_ColorDetectionDriving_Solution.py)

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
