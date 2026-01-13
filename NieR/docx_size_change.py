import os
import time

from docx import Document
from docx.shared import Cm

import TOOLS_COMMON as common

def main():
    print("请将一个docx的folder拖进来，我将修改把folder里所有的docx文件页面的size")
    input_folder = common.input_folder()
    print("请输入修改size后的docx的folder名，如果直接回车，我默认为size_change:")
    update_size_folder_name = input()

    if update_size_folder_name == "":
        update_size_folder_name = "size_change"

    output_folder = os.path.join(input_folder,update_size_folder_name)
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    print("+++++++++++++++++++++++++++")
    print("接下来输入size大小，我的折叠屏学日语的话，也就是一半的折叠屏大小的话，是宽20比高52")
    time.sleep(1)
    print("+++++++++++++++++++++++++++")

    print("请输入修改后的页面的宽")
    width_size = int(common.input_digital())

    print("请输入修改后的页面的高")
    height_size = int(common.input_digital())

    print(input_folder)
    print(output_folder)
    print(width_size)
    print(height_size)
    process(input_folder,output_folder,width_size,height_size)


def process(input_folder,output_folder,width,height):
    for file in os.listdir(input_folder):
        print(file)
        if file.endswith(".docx"):
            input_file = os.path.join(input_folder,file)
            output_file = os.path.join(output_folder,file)
            _change_page_size(input_file, output_file, width, height)

def _change_page_size(doc_path, output_path, width_cm, height_cm):
    doc = Document(doc_path)

    section = doc.sections[0]
    section.page_width = Cm(width_cm)
    section.page_height = Cm(height_cm)

    doc.save(output_path)


if __name__ == '__main__':
    main()