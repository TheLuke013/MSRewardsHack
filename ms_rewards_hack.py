import subprocess
import time
import random
import string
import pyautogui
from pynput.keyboard import Controller

#open Microsoft Browser window
def open_msedge():
    print("Opening MS Edge")
    msedge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    process = subprocess.Popen([msedge_path], shell=True)
    
    time.sleep(10)
    
    #do random searches 30 times to get 90 points in total
    for i in range(30):
        print("Searching..")
        focus_search_bar()
        search()
        time.sleep(5)

def search():
    random_search = generate_random_word()
    print(f"Random Search: {random_search}")
    
    keyboard = Controller()

    keyboard.type(random_search)
    time.sleep(1)
    pyautogui.press('enter')

def generate_random_word(size=8):
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for _ in range(size))
    return random_word

#focus search bar
def focus_search_bar():
    pyautogui.hotkey('ctrl', 'l')

#-------MAIN------
def main():
    open_msedge()

if __name__ == "__main__":
    main()
