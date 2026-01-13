import os
import shutil

from pdfrw import PdfReader

import TOOLS_COMMON as common

def main():
    print("请输入a路径：")
    folder_path = common.input_folder()
    print("请输入b后缀：")
    file_extension = input()
    print("请输入打包后的folder名字：直接回车的话，默认为temp_folder")
    package_name = input()

    package_file(folder_path,file_extension,package_name)


def package_file(folder_path,file_extension,package_name):
    if package_name == "":
        package_name = "temp_folder";
    # 新的c folder的路径
    c_folder_path = os.path.join(folder_path,package_name)
    # 如果新的c folder的path不存在，建一个
    if not os.path.exists(c_folder_path):
        os.mkdir(c_folder_path)

    # 如果c是一个folder的话
    if os.path.isdir(c_folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(file_extension):
                cur_file_path = os.path.join(folder_path,file)
                shutil.move(cur_file_path,c_folder_path)
    # 如果c是不一个folder的话
    else:
        print("新的c folder不存在，是个file，程序不执行")


if __name__ == '__main__':
    main()
