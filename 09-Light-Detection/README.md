# Smart Rover Project 09: Light Detection
The following module will guide learners through the individual Smart Rover project. The module contains key terminology used in the project, technology troubleshooting tips, Smart Rover tips and tricks, and extension resources for individual exploration.

## Table of Contents
1. [Project 09: Light Detection](#1-Project-09-Light-Detection)
2. [Key Terminology](#2-Key-Terminology)
3. [Project 09 Troubleshooting](#3-Project-09-Troubleshooting)
4. [Additional Resources](#4-Additional-Resources)

## 1. Project 09: Light Detection
### About Project 09
:sparkles: **Objective:** To program the camera to detect light.

In this project, you will learn about HSV image processing and light detection.

### Required Components
Smart Module, LED (D4), 1KΩ Resistor (R2), 2 snap connector (2)

### Instructions
1. First, connect your Smart Module to a monitor. Then build the circuit as shown below. 
2. Once the circuit is created, open up Thonny and load Project09-LightDetection.py into the code editor. 
3. Once you have completed the program, notice how the light flashes when different light thresholds are met.

> :information_source: Connecting a monitor via the HDMI cable provided in the Smart Rover kit is the quickest and easiest way to view the output of the Raspberry Pi in the Smart Module. It is possible to connect the Raspberry Pi to a laptop by creating a Virtual Network Connection (VNC) but this is a more advanced approach and should be utilized only if an HDMI-compatiable monitor is not available.

### Project 09 Diagram
![Project 09 Build Diagram](https://articulateusercontent.com/rise/courses/sbTZO9vT9ZXhcgNhd7SybORbpIcGSqXq/xp-jn0P82ZQ2ADks.jpg)

### Project 09 Build Video
### Project 09 Code-along Video

### Project 09 Code Challenges
Once you have the program running correctly, try the following challenges:

:one: Try changing the light threshold value to keep the LED on at all times.

:two: Try changing the light threshold value to keep the LED off at all times.

:three: Can you add another pin for the horn to sound when the light is too low?

:four: how can you activate the LED in darkness?

## 2. Key Terminology
The following are key vocabulary terms associated with the Smart Rover Project 09.  The key terms will help support you as you navigate the rover activity. 
- **LED:** Light Emitting Diode
- **Light Threshold:** The brightness of light needed to activate the sensor
- **Ambient Light:** Indirect lighting coming from the surrounding environment

## 3. Project 09 Troubleshooting

### Solution Code
If you need to debug your code, please refer to the [Project 09 Solution Code](../Resources/Solutions/Project09_LightDetection_Solution.py)

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
