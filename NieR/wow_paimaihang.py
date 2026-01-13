import time

from pynput import mouse
import win32api
import TOOLS_COMMON as common


def main():
    print("请输入1至8其中之一，买几个物品,直接回车就是8个")
    times_count = common.input_digital_or_none()
    if times_count == "":
        times_count = "8"
    
    print("5秒钟后开始自动买东西。一共买"+times_count+"个东西")
    time.sleep(5)
    拍卖行买东西(int(times_count))

    print("执行完成！！")

def 拍卖行买东西(times):
    product = (508,375)
    buy = (1200,895)
    confirm = (1166,334)
    for i in range(times):
        mouse1 = mouse.Controller()

        click_once(mouse1,product,.5)
        click_once(mouse1,buy,1)
        click_once(mouse1,confirm,2)

def click_once(mouse1,position,delay):
    win32api.SetCursorPos(position)
    time.sleep(.5)
    mouse1.click(mouse.Button.left, 1)
    time.sleep(delay)


if __name__ == '__main__':
    main()