# Made By Prashanth Umapathy
# Specialises is Laziness

# Libraries imported
import pyautogui 
import schedule 
import time 

# User Inputs

print('\n\n###############################################################################################')

print('Welcome to Zoom Schedulers, lazy people!! ^_^')
print('\n>>Enter the following details regarding the meeting to set it up...')
print(">>If you've reached here I'm assuming you've read the README.md and have the settings configured")
print(">>Please check all the configurations before proceeding as it may cause this program to crash otherwise")
print(">>Please keep this program running in the background at all times (if you want to run it everyday)")
print("Requirements : ( python version > 3.0 ) and ( 'schedule','pyautogui' packages installed )")
print('You can exit this program using ( Ctrl+c ) at any time')

print('\n###############################################################################################')
meet_id = input('Enter Meeting ID: ')
password = input('Enter Meeting password: ')
meet_time = input(('Enter everyday meeting time in 24hour format (eg: "15:30" for 3:30pm): '))
total_meet = input('How long will the meeting last for ?(Answer in minutes eg:120 for 2 hours): ')
print('###############################################################################################')

#just for confirmation
total_meet = int(total_meet)
meet_time = str(meet_time)

# Where the Magic happens function
def zoomClass():
    time.sleep(0.2)

    pyautogui.press('esc',interval=0.1)
    
    time.sleep(0.3)

    # open Zoom app using spotlight
    pyautogui.hotkey('command', 'space')
    pyautogui.write('zoom')
    pyautogui.hotkey('enter',interval=0.5)
    time.sleep(10)

    # locate and click 'Join' button
    #x,y = pyautogui.locateCenterOnScreen('joinIMG.png')
    x,y = pyautogui.locateCenterOnScreen('joinIMG.png', confidence = 0.9)
    """
    # Use ln 48 if ln 47 gives 'TypeError: cannot unpack non-iterable NoneType object' error
    # To use the confidence parameter in ln 48, pip install opencv_python
    """

    """
    # coordinates must be divided by 2 to click correct spot as MacBook Pros
    # and MacBook Airs 2018 & later have retina display
    # https://stackoverflow.com/questions/43606520/pyautogui-locate-command-returning-incorrect-coordinates-for-image-recognition
    """
    pyautogui.moveTo(x/2,y/2, duration = 1)    # move mouse to the window
    pyautogui.dragTo(x/2,y/2, button = 'left')    # focus the window
    pyautogui.click(x/2,y/2, interval = 1, button = 'left') 

    pyautogui.write(meet_id)
    print('Entering meeting ID')
    pyautogui.press('enter',interval=5)

    pyautogui.write(password)
    print('Entering passcode')
    pyautogui.press('enter',interval = 10)

    print("Session has started and will continue for %s minutes"%total_meet)

    print('Hold (Ctrl+c) to exit the program ')

    #Total time of zoom session
    time.sleep(total_meet) 

    # closing Zoom
    print('Meeting over! Exiting Zoom')
    pyautogui.hotkey('command', 'q')
    time.sleep(1)
    pyautogui.hotkey('command', 'q')

# Every day at whatever time the user has entered.
schedule.every().day.at("%s"%meet_time).do(zoomClass)
print("Scheduling everyday at ",meet_time)

# Infinite Loop so that the scheduled task keeps running
while True: 

	# Check whether a scheduled task is pending to run or not
	schedule.run_pending() 
	time.sleep(1) 

# Main Func
# if __name__ == "__main__":
    # zoomClass()
