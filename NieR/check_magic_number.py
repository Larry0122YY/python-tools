import TOOLS_COMMON as common


def main():
    print("请将文件拖进来：")
    file = common.input_file()
    print_magic_number(file)


def print_magic_number(filename, num_bytes=4):
    with open(filename, 'rb') as f:
        magic_number = f.read(num_bytes)

    print(magic_number)


if __name__ == '__main__':
    main()
