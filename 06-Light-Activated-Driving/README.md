# Smart Rover Project 06: Light-Activated Driving
The following module will guide learners through the individual Smart Rover project. The module contains key terminology used in the project, technology troubleshooting tips, Smart Rover tips and tricks, and extension resources for individual exploration.

## Table of Contents
1. [Project 06: Light-Activated Driving](#1-Project-06-Light-Activated-Driving)
2. [Key Terminology](#2-Key-Terminology)
3. [Project 06 Troubleshooting](#3-Project-06-Troubleshooting)
4. [Additional Resources](#4-Additional-Resources)

## 1. Project 06: Light-Activated Driving
### About Project 06
:sparkles: **Objective:** To program the Rover to detect light before driving forward.

In this project, you will learn about adding loop complexity.

### Required Components
Smart Module, Smart Rover, Phototransistor (Q4), Motor Control (U8), 1KΩ Resistor (R2) x 4, connector wires (all colors), 2 snap connectors (2) x 4, 3 snap connector (3).
> :flashlight: **Additional Required Materials:** Flashlight

### Instructions
1. First, connect your Smart Module to a monitor. 
2. Add batteries to the Smart Rover.
> :pencil2: for all projects involving the Smart Rover loading batteries is required
3. Build your circuit using the diagram below or the project manual
> :pencil2: You may want to build the circuitry without the snap tray in order to ensure secure connections with the snap connectors. 
4. Once the circuit is created, open up Thonny and load Project06_LightActivatedDriving.py into the code editor.
5. Once you have completed the circuit, run the program. Use a flashlight in a dark room to have the rover drive to follow the light source.

> :information_source: Connecting a monitor via the HDMI cable provided in the Smart Rover kit is the quickest and easiest way to view the output of the Raspberry Pi in the Smart Module. It is possible to connect the Raspberry Pi to a laptop by creating a Virtual Network Connection (VNC) but this is a more advanced approach and should be utilized only if an HDMI-compatiable monitor is not available.

### Project 06 Diagram
![Project 06 Build Diagram](https://articulateusercontent.com/rise/courses/Kh8wfJBq7l33N8vBTBYIDV1XxZaoMlDw/CQ9SF3JPGk8rtImO.jpg)

### Project 06 Build Video
### Project 06 Code-along Video

### Project 06 Code Challenges
Once you have the program running correctly, try the following challenges:

:one: Try adding new drive functions to change the light-seeking spin pattern.

:two: Add the 100 Ohm resistor in series with the phototransistor to increase light sensitivity.

:three: After a certain amount of time, have the rover spin to look for light.

:four: With the modulo `%`, have the rover alternate left or right when spinning to search for light.

## 2. Key Terminology
The following are key vocabulary terms associated with the Smart Rover Project 06.  The key terms will help support you as you navigate the rover activity. 
- **Time:** A measurement in seconds determined by he internal clock in the Pi which can be used to time certain events, such as how long the push button is held for.
- **Modulo Operator:** This operator returns the remainder of a division equation.
- **Callback Function:** a function passed into another function as an argument, which is then called inside the outer function to complete some kind of routine or action.

## 3. Project 06 Troubleshooting

### Solution Code
If you need to debug your code, please refer to the [Project 06 Solution Code](../Resources/Solutions/Project06_LightActivatedDriving_Solution.py)

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
