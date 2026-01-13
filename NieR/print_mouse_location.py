from pynput.mouse import Controller
import time

def main():
    mouse = Controller()  # 创建一个 Controller 对象，用于查询鼠标位置
    try:
        while True:
            print(f"{mouse.position}")
            time.sleep(1)  # 每秒打印一次
    except KeyboardInterrupt:
        print("程序已退出。")

if __name__ == '__main__':
    main()
