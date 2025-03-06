# Smart Rover Project 12: Light Seeking Driving
The following module will guide learners through the individual Smart Rover project. The module contains key terminology used in the project, technology troubleshooting tips, Smart Rover tips and tricks, and extension resources for individual exploration.

## Table of Contents
1. [Project 12: Light Seeking Driving](#1-Project-12-Light-Seeking-Driving)
2. [Key Terminology](#2-Key-Terminology)
3. [Project 12 Troubleshooting](#3-Project-12-Troubleshooting)
4. [Additional Resources](#4-Additional-Resources)

## 1. Project 12: Light Seeking Driving
### About Project 12
:sparkles: **Objective:** To program the rover to drive toward the light it detects.

In this project, you will learn about intermediate autonomous driving.

### Required Components
Smart Module, Smart Rover, Press Switch (S2), Motor Control (U8), 1KΩ Resistor (R2) x 4, connector wires (all colors), 2 snap connector (2) x 4, 3 snap connector (3)
> :flashlight: **Additional Required Materials:** Flashlight

### Instructions
1. First, connect your Smart Module to a monitor. Then build the circuit as shown below.
2. Add batteries to the Smart Rover.
> :pencil2: for all projects involving the Smart Rover loading batteries are required
3. Build the circuit using the diagram below or the project manual
4. Once the circuit is created, open up Thonny and load Project12-LightSeekingDriving.py into the code editor. 
5. Once you have completed the program, use a flashlight to guide the rover as it drives and detects light.

> :information_source: Connecting a monitor via the HDMI cable provided in the Smart Rover kit is the quickest and easiest way to view the output of the Raspberry Pi in the Smart Module. It is possible to connect the Raspberry Pi to a laptop by creating a Virtual Network Connection (VNC) but this is a more advanced approach and should be utilized only if an HDMI-compatiable monitor is not available.

### Project 12 Diagram
![Project 12 Build Diagram](https://articulateusercontent.com/rise/courses/K4O9aPmKUezeewmXR5nJV18joQmIGeYs/Uzcq6SQSW1d_Xxcp.jpg)

### Project 12 Build Video
### Project 12 Code-along Video

### Project 12 Code Challenges
Once you have the program running correctly, try the following challenges:

:one: Try changing the ‘left’ and ‘right’ thresholds to force different turning patterns. 

:two: Try using the modulo `%` function and loop counter to go from ‘forward’ to ‘reverse’ every cycle. 

:three: Can you add a timer to the loop to have the rover do a spin after thirty seconds of searching?

:four: Can you set the drive_time duration based on the ratio of left-to-right light?

## 2. Key Terminology
The following are key vocabulary terms associated with the Smart Rover Project 12.  The key terms will help support you as you navigate the rover activity. 
- **Light-Seeking Autonomous Driving:** A method in which an autonomous vehicle determines which direction is brightest and rotates until it is properly aligned in order to drive toward the target.

## 3. Project 12 Troubleshooting

### Solution Code
If you need to debug your code, please refer to the [Project 12 Solution Code](../Resources/Solutions/Project12_LightSeekingDriving_Solution.py)

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
