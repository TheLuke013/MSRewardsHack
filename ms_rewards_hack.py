import subprocess
import time
import pyautogui

#Open Microsoft Browser window
def open_msedge():
    print("Opening MS Edge")
    msedge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    process = subprocess.Popen([msedge_path], shell=True)
    
    time.sleep(5)
    
    focus_search_bar()

#focus search bar
def focus_search_bar():
    pyautogui.hotkey('ctrl', 'l')

#-------MAIN------
def main():
    open_msedge()

if __name__ == "__main__":
    main()
