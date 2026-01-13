import os

import TOOLS_COMMON as common

def main():
    # 示例用法

    print("请输入folder 名字，或者直接拖进来：")

    folder = common.input_folder()

    print('AAAAAAAAAA')
    print(folder)

    print("请输入合并后的文件名，默认是和文件名一样")
    merged_file_name = input()

    if merged_file_name == "":
        merged_file_name = os.path.join(os.path.basename(folder + ".pdf"))
    else:
        merged_file_name += '.pdf'

    common.merge_pdfs_design(folder,merged_file_name)




if __name__ == '__main__':
    main()
