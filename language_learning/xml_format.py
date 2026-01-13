import os.path


def main():
    print("'这个py的作用就是为了找到换行的地方，格式化")
    print("给我一下xml的path")
    path = input()
    _print_xml_huanhang(path)
    input()



def _print_xml_huanhang(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if file.startswith("file_"):
                xml_file = os.path.join(path,file)
                clean_specific_lines(xml_file)
    else:
        print("入力path错误！")


def clean_specific_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 创建一个新的列表，用于存储修改后的行
    new_lines = []
    for line_num, line in enumerate(lines, start=1):
        # 去除前导空格
        stripped_line = line.lstrip()
        # 检查是否不以 "<" 开头
        if not stripped_line.startswith("<"):
            # 如果不以 "<" 开头，则去掉前导空格的版本加入新列表
            new_lines.append(stripped_line)
        else:
            # 否则保留原始行
            new_lines.append(line)

    # 将修改后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)



if __name__ == '__main__':
    main()