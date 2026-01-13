import os

import TOOLS_COMMON as common

def main():
    print("请将目标搜索folder拖进来：")
    select_path = common.input_folder()
    print("select_path:", select_path)
    print("请输入搜索的关键字：")
    key_words = input()

    print("+++++++++++++++++++")
    print()
    search_key_words_in_folder(select_path,key_words)
    print()
    print("+++++++++++++++++++")


def search_key_words_in_folder(select_path,key_words):
    for root,dirs,files in os.walk(select_path):
        for dir in dirs:
            if key_words in dir:
                cur_path = os.path.join(root,dir)
                print(cur_path)
        for file in files:
            if key_words in file:
                cur_path = os.path.join(root,file)
                print(cur_path)

if __name__ == '__main__':
    main()