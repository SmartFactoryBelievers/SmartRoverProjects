# Smart Rover Project 03: Selector Output
The following module will guide learners through the Deloitte Smart Rover Project 3: Selector Output.  The module contains key terminology used in the project, technology troubleshooting tips, Smart Rover tips and tricks, and extension resources for individual exploration.  

## Table of Contents
1. [Project 03: Selector Output](#1-project-03-Selector-Output)
2. [Key Terminology](#2-Key-Terminology)
3. [Project 03 Troubleshooting](#3-Project-03-Troubleshooting)
4. [Additional Resources](#4-Additional-Resources)

## 1. Project 03: Selector Output
### About Project 03
:sparkles: **Objective:** To program the selector to turn on the LED light in programmed patterns. 

In this project, you will learn about writing functions. Functions are a crucial tool in programming. You can write a function to perform a specific task or calculation, then, whenever you “call” upon the function, you can perform that task immediately. We will use functions going forward in different ways.

### Required Components
Smart Module, Selector (S8), LED (D4, D8, or D12), Horn (W1), 100 ohm resistor (R1), 4 snap connector (4), 3 snap connector (3), 2 snap connector x 2 (2).

### Instructions
1. First, connect your Smart Module to your monitor. Components: Smart Module, Selector (S8), LED (D4, D8, or D12), Horn (W1), 100 ohm resistor (R1), 4 snap connector (4), 3 snap connector (3), 2 snap connector x 2 (2).
2. Then, build the circuit as shown below. Ensure the arrows flow in the correct direction and the + on the horn attach to the Raspberry Pi module
3. Once the circuit is created, open up Thonny and load Project03_SelectorOutput.py into the code editor. You will need to edit the question marks and remove the hashtag symbol (#) from the commented-out lines for the code to run.
4. Once you have completed the program, upload it the to the rover and see how the LED light blinks in the programmed patterns. Please be sure to firmly push the selector buttons.

> :information_source: Connecting a monitor via the HDMI cable provided in the Smart Rover kit is the quickest and easiest way to view the output of the Raspberry Pi in the Smart Module. It is possible to connect the Raspberry Pi to a laptop by creating a Virtual Network Connection (VNC) but this is a more advanced approach and should be utilized only if an HDMI-compatiable monitor is not available.

### Project 03 Diagram
![Project 03 Build Diagram](https://articulateusercontent.com/rise/courses/wK4Yb3gnvh7hjU22JZpEOTDwclWKpunE/cMfmIO7uQpKXFUEo.jpg)

### Project 03 Build Video
### Project 03 Code-along Video

### Project 03 Code Challenges
Once you have the program running correctly, try the following challenges:

:one: Try changing the LED variables to change the blinking pattern.

:two: Replace the LED with the horn (W1) or a different LED to try different outputs.

:three: Change input pins A and C in the While loop. What happens?

:four: Change output pins LED and horn (W1) in the While loop. What happens?

:five: Try to switch the order of the LED and horn (W1) function loops. What happens?

## 2. Key Terminology
The following are key vocabulary terms associated with the Smart Rover Project 03.  The key terms will help support you as you navigate the rover activity. 
- **Functions**: a block of organized, reusable code that is used to perform a single, related action.
- **Comment:**: Human Readable Descriptions inside of computer programs detailing what the Code is doing. In Python, comments are indicated by placing a hashtag [#} in front of the comment text of the comment.

## 3. Project 03 Troubleshooting

### Solution Code
If you need to debug your code, please refer to the [Project 03 Solution Code](../Resources/Solutions/Project03_SelectorOutput_Solution.py)

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
