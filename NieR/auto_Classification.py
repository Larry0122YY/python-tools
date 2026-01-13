import os
import shutil
import time

import TOOLS_COMMON as common

def main():
    print("打印name磁盘所有的folder名")
    name_path = "H:\\"

    for folder in os.listdir(name_path):
        cur_file_path = os.path.join(name_path,folder)
        if os.path.isdir(cur_file_path):
            print(folder)

    # input_file = r"D:\download\FX\juq-963.mp4"
    # target_folder = r"I:\aaa"

    print("拖入前，请确定folder下有且只有要分类的视频文件")
    print("或者拖入个单个文件")
    path = common.input_path()

    if path == "":
        path = r"D:\download\FX\name"

    print("请参考上面的name，输入目标的folder")
    name = input()

    target_folder = os.path.join(name_path,name)

    move_method(path,target_folder)




def move_method(input_file,target_folder):

    print()
    if os.path.isdir(input_file):

        for file in os.listdir(input_file):

            cur_input_file = os.path.join(input_file,file)

            move_execute(cur_input_file,target_folder)

    elif os.path.isfile(input_file):

            move_execute(input_file, target_folder)

    else:
        print("输入的内容不是folder或者file")

def move_execute(cur_input_file,target_folder):
    # 移动开始
    print(cur_input_file + "开始移动.....")
    start_time = time.time()

    # 主要的移动方法
    shutil.move(cur_input_file, target_folder)

    # 移动结束
    end_time = time.time()

    # 移动时间花费
    cost_time = end_time - start_time
    print("移动完成！用时：" + str(round(cost_time, 3)))


if __name__ == '__main__':
    main()

