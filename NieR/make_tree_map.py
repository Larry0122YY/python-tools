import os
import TOOLS_COMMON as common

def main():
    print("请输入要生成树状图的文件夹路径：")
    folder_path = common.input_folder()
    print(folder_path)
    print_tree(folder_path)


def print_tree(dir_path, prefix=""):
    files = os.listdir(dir_path)
    files.sort()  # 排序，树更整齐

    for i, name in enumerate(files):
        path = os.path.join(dir_path, name)
        connector = "├── " if i < len(files) - 1 else "└── "

        print(prefix + connector + name)

        if os.path.isdir(path):
            new_prefix = prefix + ("│   " if i < len(files) - 1 else "    ")
            print_tree(path, new_prefix)


if __name__ == "__main__":
    main()