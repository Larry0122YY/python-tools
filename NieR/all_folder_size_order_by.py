import os
import TOOLS_COMMON as common

def main():
    print("给我一个folder，我将把里面所有的文件夹的大小从大到小排列，并且输入文件")
    target_path = common.input_folder()
    print(common.get_desktop_path())

    print("查找出文件夹的大小，以什么来表示？")
    print("直接回车：GB")
    print("k：KB")
    print("直接回车和k以外：MB")
    style = common.none_or_what("GB")
    style_tuple = _style_count(style)

    print("给我一个输出文件的路径，直接回车，默认在桌面")
    output_path = common.none_or_what(common.get_desktop_path())
    print(output_path)

    print("请输入输出txt文件的名字，直接回车的话，默认为temp.txt")
    file_name = common.none_or_what("temp.txt")

    output_file_path = os.path.join(output_path, file_name)
    print(output_file_path)

    process(target_path, output_file_path, style_tuple)

def _style_count(style):
    if style == "GB":
        style_count = 1024 * 1024 * 1024
        style_show = "GB"
    elif style == "k":
        style_count = 1024
        style_show = "KB"
    else:
        style_count = 1024 * 1024
        style_show = "MB"

    return style_count, style_show

def process(folder_path, output_file_path, style_tuple):
    folder_sizes = _get_all_folder_sizes(folder_path)
    result_str = ""

    # Sort folders by size in descending order
    sorted_folder_sizes = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)

    # Print folder sizes
    for folder, size in sorted_folder_sizes:
        result_str += f'{folder}: {size / style_tuple[0]:.2f} {style_tuple[1]}\n'

    _print_out(result_str, output_file_path)

def _get_folder_size(folder):
    """Get the total size of a folder, including all subfolders and files."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Check if file exists to avoid broken symlinks
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

def _get_all_folder_sizes(folder):
    """Get the size of each folder and subfolder in the given directory."""
    folder_sizes = {}
    for dirpath, dirnames, filenames in os.walk(folder):
        for dirname in dirnames:
            folder_path = os.path.join(dirpath, dirname)
            folder_sizes[folder_path] = _get_folder_size(folder_path)
    return folder_sizes

def _print_out(text, output_path):
    # 将字符串写入文件
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f'文件已保存到: {output_path}')

if __name__ == '__main__':
    main()
