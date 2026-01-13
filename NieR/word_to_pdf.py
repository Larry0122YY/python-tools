import os

from docx2pdf import convert
import TOOLS_COMMON as common

def main():
    print("请拖进来一个folder或者file，如果是folder，那么这个folder下的第一层所有docx文件，都会被导出成pdf：")
    select_path = common.input_path()
    print("select_path:",select_path)
    new_ext = ".pdf"
    word_to_pdf(select_path,new_ext)
    print("导出完成！")

def word_to_pdf(select_path,new_ext):
    if os.path.isdir(select_path):
        common.word_to_pdf(select_path)
    else:
        new_ext_file = common.switch_ext(select_path, new_ext)
        print(select_path)
        print(new_ext_file)
        convert(select_path, new_ext_file)




if __name__ == '__main__':
    main()