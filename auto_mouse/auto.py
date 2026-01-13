from pynput import mouse
import time
import win32api

def main():
    position1 = (735, 678)
    position2 = (906, 733)
    position3 = (1207, 864)
    
    mouse1 = mouse.Controller()

    count = 20

    time.sleep(5)
    for times in range(count):
        click_once(mouse1,position1)
        time.sleep(.5)
        click_once(mouse1,position2)
        time.sleep(.5)
        click_once(mouse1,position3)
        time.sleep(1)


def click_once(mouse1,position,delay=.5):
    win32api.SetCursorPos(position)
    time.sleep(.5)
    mouse1.click(mouse.Button.left, 1)
    time.sleep(delay)

def click_once_right(mouse1,position,delay=.5):
    win32api.SetCursorPos(position)
    time.sleep(.5)
    mouse1.click(mouse.Button.right, 1)
    time.sleep(delay)


if __name__ == '__main__':
    main()

