# The Smart Rover Projects
To foster the next generation of believers, The Smart Factory @ Wichita has partnered with Elenco® Electronics to produce a new STEM
education product: the Smart Rover. The Smart Rover kit includes Elenco® Electronics’ award-winning Snap Circuits® products and adds
a new component, the Smart Module. Assembled in a custom-designed housing produced and assembled live at The Smart Factory @
Wichita, the module holds a Raspberry Pi microcomputer and camera.

The projects within the Smart Rover kit begin with teaching the basics of computer programming on the Raspberry Pi and explore all
the way up to enabling the rover to self-drive and “see” using the embedded camera. But innovation does not end with the last page of
this booklet. The Smart Rover kit seeks to empower all students, across all ages, with the enduring skills needed to design, code, and
build for the future.

> ℹ️ [Click here](./Resources/about-the-smart-rover.pdf) to learn more about the Smart Rover, Elenco Electronics, or The Smart Factory @ Wichita.

![image](https://github.com/user-attachments/assets/505212ed-4ce0-44e5-8f4b-8d03a27f8a7b)

## Project Progression
The introductory projects will teach the basics of programming, as well as circuitry, using both the Raspberry Pi within the Smart
Module and various components, including the LED light, the horn, the phototransistor, and the selector. Next, you will learn about
motor controls and how to program the rover to drive. Finally, we will use the camera within the Smart Module to detect color and light,
then incorporate those inputs into driving. All the projects have a starting program file pre-loaded to the Raspberry Pi. A code
reference guide for all projects is available on The Smart Factory @ Wichita website.

Please note that not all possible kit components are included in the projects. These include: the Programmable Fan, the Speaker,
and the NPN Transistor. However, using the concepts introduced in the projects will allow you to incorporate all possible components.

## Each lesson includes:

📖 README file containing Introduction, circuit diagram, code challenges, and more

🐍 Python code script (which is also pre-loaded onto the Smart Module)

🎥 Code-along videos with line-by-line instructions

🔗 Links to additional resources and troubleshooting tips

## The Projects

|       |              Project Name                      |  Learning Objectives |
| :---: | :--------------------------------------------: | :---------------------:  |
|  00   | [Introduction to Circuits](./00-Introduction/01-Introduction-to-Circuits/README.md)      | Introduction to Circuits  |
|  00   | [Introduction to Python](./00-Introduction/02-Introduction-to-Python/README.md)    | Introduction to Python |
|  00   | [Smart Rover Kit](./00-Introduction/03-Smart-Rover-Kit/README.md)    | Introduction to the Smart Rover Kit |
|  00   | [Introduction to Motor Control](./00-Introduction/04-Introduction-to-Motor-Control/README.md)    | Introduction to Motor Control |
|  01   | [Blinking LED](./01-Blinking-LED/README.md)  | To learn programming basics and make the LED light blink |
|  02   | [Light-Activated LED](./02-Light-Activated-LED/README.md)    | To control the LED light with a push button |
|  03   | [Selector Output](./03-Selector-Output/README.md)    | To program the selector to turn on the LED light in programmed patterns. |
|  04   | [Programmed Driving](./04-Programmed-Driving/README.md)    | To program the rover to drive in a coded path. |
|  05   | [Timed Driving](./05-Timed-Driving/README.md)    | To program the Rover to drive in a coded path for the duration of the button push. |
|  06   | [Light-Activated Driving](./06-Light-Activated-Driving/README.md)  | To program the Rover to detect light before driving forward. |
|  07   | [Controlled Driving](./07-Controlled-Driving/README.md)  | To program the Rover to drive according to selected inputs. |
|  08   | [Introduction to Camera](./08-Introduction-To-Camera/README.md)  | To learn about the camera and different image settings. |
|  09   | [Light Detection](./09-Light-Detection/README.md)  | To program the camera to detect light. |
|  10   | [Color Detection](./10-Color-Detection/README.md)  | To program the rover to distinguish between various colors. |
|  11   | [Color Detection Driving](./11-Color-Detection-Driving/README.md)  | To program the camera to detect sign colors and drive accordingly. |
|  12   | [Light Seeking Driving](./12-Light-Seeking-Driving/README.md)  | To program the rover to drive toward the light it detects. |

## Hardware
The Smart Rover uses building blocks with snaps to build the different circuits for each project. Each component has a different
function and is colored so you can identify it. Each component easily snaps together so you can build the circuit. 

> 💁 You can read more [about the components](Resources/about-the-components.pdf) and find a [list of what's included](Resources/snap-circuit-components.png) in your Smart Rover Kit in the [Resources folder](Resources/README.md)!

## Installation
To use this curriculum on your own, fork the entire repo and complete the exercises on your own, starting with reading the lesson content in the README files and completing the rest of the activities. Try to complete the projects by comprehending the lessons rather than copying the solution code; however that code is available in the /solutions folders in each project-oriented lesson. To get started, follow these steps:

1. Click here to create your own copy of this repository: [![Fork](https://img.shields.io/badge/Fork%20this%20repo-green?style=flat-square)](https://github.com/SmartFactoryBelievers/SmartRoverProjects/fork)
2. Open a terminal on your Smart Module by clicking this icon in the top left menu bar: ![image](https://github.com/user-attachments/assets/a323731a-4304-48fa-ac3e-df3e7e939355)
3. In the terminal navigate to the Projects Folder on your Smart Module: `cd Desktop/Projects`
4. Copy the HTTPS link to your forked repository: ![image](https://github.com/user-attachments/assets/66524c1b-4dce-4096-8058-36757f0cbda6)
5. Clone the repository: `git clone <paste your link here>`
6. Navigate to the project directory: `cd SmartRoverProjects`
7. Install the required dependencies: `python pip install -r requirements.txt`
8. Now, you are ready to begin! Keep this GitHub page open on your Smart Module browser to review the lesson content alongside your code in the Thonny IDE.
> :white_check_mark: Don't forget to save your changes often! We recommend creating a new branch each time you work on the code using the following command:
> 
> `git checkout -b <your-name-today's-date>`
> 
> Then, make your edits directly in the python project code files in Thonny IDE and save the files. Once you reach a stopping point, run the following commands to update your repository in GitHub:
> 
> `git add . `
> 
> `git commit -m "a short description of the change"`
> 
> `git push`

## Additional Resources
In the [Resources](Resources/README.md) folder, you will find additional resources to help you complete the Smart Rover Projects. You can click the links below to jump to the file.

- [The Smart Rover Project Manual](Resources/Smart-Rover-Manual.pdf)
- [The Smart Rover Project Code Solutions](Resources/Solutions/README.md)
- [Snap Circuit Components list](Resources/snap-circuit-components.pdf)

### Contributing
We welcome contributions from the community! If you would like to contribute to the SmartRoverProjects, please follow [these steps.](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project). Lastly, we'd love to hear what you thoughts of this course [in our discussion board](https://github.com/SmartFactoryBelievers/SmartRoverProjects/discussions).
> Please ensure that your contributions adhere to our [Code of Conduct](link).

## License
Copyright © 2024 Deloitte Development LLC. All rights reserved. See the [LICENSE](LICENSE) file for more information.

## Contact
If you have any questions or need further assistance, feel free to reach out to us at contact@smartfactorybelievers.com. We look forward to your contributions and feedback.

<footer>

<!--
  <<< Author notes: Footer >>>
  Add a link to get support, code of conduct.
-->

---

Get help: [Post in our discussion board](https://github.com/SmartFactoryBelievers/SmartRoverProjects/discussions) &bull; [Review the GitHub status page](https://www.githubstatus.com/)

&copy; 2024 Deloitte Development LLC. All rights reserved &bull; [Code of Conduct]()

</footer>
