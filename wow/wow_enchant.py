import os
import time

from pynput import mouse
import win32api


def main():
    time.sleep(5)

    # 获取鼠标position()

    # 附魔包裹第一格子(7)



    # 附魔做药(14)

    # 次级魔法杖，可以到95
    # 强效魔法杖，可以到130
    # 附魔做魔杖(10)

    # 获取鼠标position()
    获取声望(115)
    # 拍卖行买东西(8)

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


def 获取声望(yumao_count):
    # 身影重叠NPC

    times = yumao_count // 5

    # print("现在是和人对话的状态：")
    quest_people= (1282, 795)
    kingblood = (247, 700)
    kingblood = (173, 487)

    continue_button = (145, 895)
    complete_button = continue_button

    for i in range(times):
        mouse1 = mouse.Controller()

        click_once_right(mouse1, quest_people, 1.5)
        click_once(mouse1, kingblood, .5)
        click_once(mouse1, continue_button, .5)
        click_once(mouse1, complete_button, 3)


    print("aaaaaaaa")

#附魔前，要打开人物栏和附魔栏
def 附魔包裹第一格子(times):
    fumo_button = (381, 893)
    confirm_position = (1197, 315)

    first_package_cell_position = (2155, 853)


    for i in range(times):
        mouse1 = mouse.Controller()

        click_once(mouse1,fumo_button,.5)
        click_once(mouse1,first_package_cell_position,1)
        click_once(mouse1,confirm_position,6)


def 附魔做魔杖(count_times):
    mouse1 =mouse.Controller()

    # 鼠标左键点一下
    for i in range(count_times):
        mouse1.click(mouse.Button.left, 1)
        time.sleep(11)

def 附魔做药(count_times):
    mouse1 =mouse.Controller()

    # 鼠标左键点一下
    for i in range(count_times):
        mouse1.click(mouse.Button.left, 1)
        time.sleep(6)

def 获取鼠标position():
    def when_press(x, y):
        print(str(x) + ":" + str(y))

    with mouse.Listener(on_move=when_press) as ml:
        ml.join()

def click_once(mouse1,position,delay):
    win32api.SetCursorPos(position)
    time.sleep(.5)
    mouse1.click(mouse.Button.left, 1)
    time.sleep(delay)

def click_once_right(mouse1,position,delay):
    win32api.SetCursorPos(position)
    time.sleep(.5)
    mouse1.click(mouse.Button.right, 1)
    time.sleep(delay)

if __name__ == '__main__':
    main()