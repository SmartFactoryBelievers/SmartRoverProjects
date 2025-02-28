# Happy STEM Day! Copy this code into a new file in Thonny editor on the Smart Rover and
# run the file to blink a message in Morse Code. Try swapping the LED component with the horn!

#How-to: after running the file, type your message in the Thonny shell below and click "enter"

from time import sleep
import RPi.GPIO as GPIO

# Dictionary to convert characters to morse code leaving a 'space' for word separation
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '  
}

# Setting GPIO pin number - successfully tested the HORN and LED device
dvcPin = 7  # we're using BOARD pin num, not BCM pin num (BCM = 4)

# Duration in seconds for dots, dashes, space between dots and dash, and word serparation
dot = 0.1  
dash = 0.4  
space = 0.15
wrdSpc = 0.6

# Setup GPIO on the Raspberry Pi
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering (7), not Broadcam SOC (4)
GPIO.setup(dvcPin, GPIO.OUT, initial=GPIO.LOW)  # Configure the pin as an output

# Function to display Morse code for whatever device is connected, 
# Setting output to high or low based on dot, dashes or spaces
def blink_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            GPIO.output(dvcPin, GPIO.HIGH)
            sleep(dot)
        elif symbol == '-':
            GPIO.output(dvcPin, GPIO.HIGH)
            sleep(dash)
        elif symbol == ' ':
            GPIO.output(dvcPin, GPIO.LOW)
            sleep(space)
        else:  # Ignore any unknown characters
            continue
        GPIO.output(dvcPin, GPIO.LOW)
        sleep(space)

try:
    while True:
        # ask user to input phrase and convert to UPPER
        user_input = input("Enter a phrase: ").upper()
        
        # set morse code string
        morse_code = ''
        
        # translate to morse code
        for char in user_input:
            if char in morse_code_dict:
                morse_code += morse_code_dict[char]
                morse_code += ' '  # Add space between characters
        morse_code = morse_code.strip()  # Remove trailing space
        
        # display the morse code
        print("Morse Code:", morse_code)
        blink_morse_code(morse_code)
        sleep(wrdSpc)

except KeyboardInterrupt:
    print("Program terminated.")
finally:
    # Ensure the GPIO is low before cleanup
    GPIO.output(dvcPin, GPIO.LOW)
    # Clean up GPIO settings to release the pins
    GPIO.cleanup()

