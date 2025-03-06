# Smart Rover Project 07: Controlled Driving
The following module will guide learners through the individual Smart Rover project. The module contains key terminology used in the project, technology troubleshooting tips, Smart Rover tips and tricks, and extension resources for individual exploration.

## Table of Contents
1. [Project 07: Controlled Driving](#1-Project-07-Controlled-Driving)
2. [Key Terminology](#2-Key-Terminology)
3. [Project 07 Troubleshooting](#3-Project-07-Troubleshooting)
4. [Additional Resources](#4-Additional-Resources)

## 1. Project 07: Controlled Driving
### About Project 07
:sparkles: **Objective:** To program the Rover to drive according to selected inputs.

In this project, you will learn about adding complex logic.

### Required Components
Smart Module, Smart Rover, Selector (S8), Motor Control (U8), 1KΩ Resistor (R2) x4, connector wires (all colors), 2 snap connectors (2) x 4, 3 snap connectors (3) x 2, 4 snap connector (4)

### Instructions
1. First, connect your Smart Module to a monitor. 
2. Add batteries to the Smart Rover.
> :pencil2: for all projects involving the Smart Rover loading batteries are required
3. Build your circuit using the diagram below or the project manual
> :pencil2: You may want to build the circuitry without the snap tray in order to ensure secure connections with the snap connectors. 
4. Once the circuit is created, open up Thonny and load Project07_ControlledDriving.py into the code editor.
5. Once you have completed the circuit, run the program. Firmly press the selector switch buttons in full to ensure responsiveness.

> :information_source: Connecting a monitor via the HDMI cable provided in the Smart Rover kit is the quickest and easiest way to view the output of the Raspberry Pi in the Smart Module. It is possible to connect the Raspberry Pi to a laptop by creating a Virtual Network Connection (VNC) but this is a more advanced approach and should be utilized only if an HDMI-compatiable monitor is not available.

### Project 07 Diagram
![Project 07 Build Diagram](https://articulateusercontent.com/rise/courses/OPWIuvResEl9INY4HipVSEYrbPxCWNTG/VQDlrTntuSUHYpck.jpg)

### Project 07 Build Video
### Project 07 Code-along Video

### Project 07 Code Challenges
Once you have the program running correctly, try the following challenges:

:one: Incorporate the button press timer from Project 5 to add Simon Says to driving functions.

:two: The B pin uses a double If statement. Can you apply the same for the A and C pins?

:three: Replace the 3-length snap connector with a phototransistor; now all 3 buttons are light-dependent. Can you add an outer loop for new driving instructions when there is no light or button presses for more than 5 seconds?

## 2. Key Terminology
The following are key vocabulary terms associated with the Smart Rover Project 07.  The key terms will help support you as you navigate the rover activity. 
- **Boolean Condition (True/False statement):** when a computer program evaluates whether a statement is `true` or `false`
- **`AND` statement:** A complex logic evaluation in which all conditions must be `true` to be executed.
- **`NOT` statement:** A complex logic evaluation in which the computer looks for a condition to be `false`

## 3. Project 07 Troubleshooting

### Solution Code
If you need to debug your code, please refer to the [Project 07 Solution Code](../Resources/Solutions/Project07_ControlledDriving_Solution.py)

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
