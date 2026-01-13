from genericpath import isfile
import os.path
from PIL import Image
import TOOLS_COMMON as common

def main():

    print('请给我一个路径:直接回车，就是dir的当前路径了')
    print('    ※dir路径的话，那么下面的所有文件都必须要是图片文件，否则报错，然后将这些图片全部变成同名pdf')
    print('    ※file路径的话，这个文件必须是图片')
    
    path = common.input_path_dir_file()

    if os.path.isfile(path):
        process_pic_file(path)
    else:
        process_pic_files(path)


def process_pic_files(dir_path):
    
    for file in os.listdir(dir_path):
        process_pic_file(file)


def process_pic_file(img_path):

    folder_path = os.path.dirname(img_path)

    print('-------------------')
    print(f'当前文件{img_path}')
    print("请输入转换后的pdf的名字，直接回车的话，默认和图片名一样")
    file_name = input()
    if file_name == "":
        file_name = os.path.splitext(os.path.basename(img_path))[0]+".pdf"
    pdf_path = os.path.join(folder_path,file_name)

    print(pdf_path)
    img_to_pdf(img_path,pdf_path)




def img_to_pdf(img,pdf_path):
    img = Image.open(img)  # 替换成你的图片路径
    img.convert("RGB").save(pdf_path)
    print(f"已保存为：{pdf_path}")


if __name__ == '__main__':
    main()