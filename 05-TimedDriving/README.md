# Smart Rover Project 05: Timed Driving
The following module will guide learners through the individual Smart Rover project. The module contains key terminology used in the project, technology troubleshooting tips, Smart Rover tips and tricks, and extension resources for individual exploration.

## Table of Contents
1. [Project 05: Timed Driving](#1-Project-05-Timed-Driving)
2. [Key Terminology](#2-Key-Terminology)
3. [Project 05 Troubleshooting](#3-Project-05-Troubleshooting)
4. [Additional Resources](#4-Additional-Resources)

## 1. Project 05: Timed Driving
### About Project 05
:sparkles: **Objective:** To program the Rover to drive in a coded path for the duration of the button push. 

In this project, you will learn about callback functions.

### Required Components
Smart Rover, Smart Module, Press Switch (S2), Motor Control (U8), 1KΩ R2 Resistor (x4), connector wires (all colors), 2 snap connector (2) x 4, 3 snap connector (3).

### Instructions
1. First, connect your Smart Module to a monitor. 
2. Add batteries to the Smart Rover.
> :pencil2: for all projects involving the Smart Rover loading batteries is required
3. Build your circuits using the diagram below or the project manual
> :pencil2: You may want to build the circuitry without the snap tray in order to ensure secure connections with the snap connectors. 
4. Once the circuit is created, open up Thonny and load Project05_TimedDriving.py into the code editor.
5. Once you have completed the circuit, run the program. Press and hold the switch to drive the rover for the duration of the button push.

> :information_source: Connecting a monitor via the HDMI cable provided in the Smart Rover kit is the quickest and easiest way to view the output of the Raspberry Pi in the Smart Module. It is possible to connect the Raspberry Pi to a laptop by creating a Virtual Network Connection (VNC) but this is a more advanced approach and should be utilized only if an HDMI-compatiable monitor is not available.

### Project 05 Diagram
![Project 05 Build Diagram](https://articulateusercontent.com/rise/courses/mJcJD0oEhWcevdz-EaRCO9Qas-RvMHY9/N0X39cbDbHdjMIx5.jpg)

### Project 05 Build Video
### Project 05 Code-along Video

### Project 05 Code Challenges
Once you have the program running correctly, try the following challenges:

:one: Try changing the drive functions to switch the driving directions.

:two: Add new drive functions activated in the loop to create a new driving path.

:three: Use the modulo `%` operator to change the driving direction based on even- or odd-numbered presses.

:four: With the modulo `%`, add new driving functions for different driving paths for even- or odd-numbered presses.

## 2. Key Terminology
The following are key vocabulary terms associated with the Smart Rover Project 03.  The key terms will help support you as you navigate the rover activity. 
- **Time:** A measurement in seconds determined by he internal clock in the Pi which can be used to time certain events, such as how long the push button is held for.
- **Modulo Operator:** This operator returns the remainder of a division equation.
- **Callback Function:** a function passed into another function as an argument, which is then called inside the outer function to complete some kind of routine or action.

## 3. Project 05 Troubleshooting

### Solution Code
If you need to debug your code, please refer to the [Project 05 Solution Code](../Resources/Solutions/Project05_TimedDriving_Solution.py)

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
