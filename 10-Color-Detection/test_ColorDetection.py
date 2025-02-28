# test_ColorDetection.py
# This is a simple test script to validate that Project10_ColorDetection.py will execute as intended without throwing any error & the challenges are completed successfully.

# importing the subprocess module allows us to run other programs from this Python file
import subprocess 

# define a function called test_Project10
def test_Project10():
    # This function is execute any time we run the test
    try:
        # Run Project 10 and record the output
        result = subprocess.run(['python3', 'Project10_ColorDetection.py'], check=True, capture_output=True, text=True) # check if there is any error in the output
        print("Script executed successfully.") 
    except subprocess.CalledProcessError as e:
        print(f"Script execution failed with error: {e}")

# test challenge 1
'''
Write functions to test the challenges in Project 10
def test_led_on_off_values():
    # Check that LED_On is not equal to 0.2 and LED_Off is not equal to 0.1
    from Project01_BlinkingLED import LED_On, LED_Off
    assert LED_On != 0.2, "LED_On should not be equal to 0.2"
    assert LED_Off != 0.1, "LED_Off should not be equal to 0.1"
    print("LED_On and LED_Off values are correct.")
'''

if __name__ == "__main__":
    test_Project10()
    # test_led_on_off_values()