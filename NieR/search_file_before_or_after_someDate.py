import os
import time
from datetime import datetime
import TOOLS_COMMON as common


def main():
    print("请输入目标路径：")
    path = common.input_folder()
    print("请输入以什么为后缀：")
    key = common.input_not_none()

    print("从这里开始输入一个日期，与想找出的文件的最后修改日期相比较")
    print("请输入年数，直接回车默认为今年")
    year = common.input_digital_or_none()
    if year == "":
        year = datetime.now().year
    else:
        year = int(year)

    print("请输入月份，直接回车默认为当前月")
    month = common.input_digital_or_none()
    if month == "":
        month = datetime.now().month
    else:
        month = int(month)

    print("请输入日数，直接回车默认为今天")
    date = common.input_digital_or_none()
    if date == "":
        date = datetime.today().day
    else:
        date = int(date)

    select_datetime = datetime(year, month, date)
    search_date_str = select_datetime.strftime('%Y-%m-%d')

    print("请输入想找的文件在这个日期之前,之后还是等于？")
    print("直接回车：之后")
    print("输入 '=' ：刚好这个日期")
    print("直接回车和'='以外：之前")
    status = input()
    if status == "":
        before_or_after = 1
    elif status == "=":
        before_or_after = 0
    else:
        before_or_after = -1

    print("开始搜索")
    print("+++++++++++++++++++++++++")

    result = search_docx_files(path, key, search_date_str, before_or_after)
    if result:
        print("符合条件的文件:")
        for file_path, mod_time in result:
            mod_time_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
            print(f"最后修改时间: {mod_time_str}\t{file_path}")
    else:
        print("没有找到符合条件的文件。")


def search_docx_files(folder, key, search_date_str, before_or_after):
    matching_files = []

    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(key):
                file_path = os.path.join(dirpath, filename)
                file_mod_time = os.path.getmtime(file_path)
                file_mod_date_str = datetime.fromtimestamp(file_mod_time).strftime('%Y-%m-%d')

                if before_or_after == 1 and file_mod_date_str > search_date_str:
                    matching_files.append((file_path, file_mod_time))
                elif before_or_after == 0 and file_mod_date_str == search_date_str:
                    matching_files.append((file_path, file_mod_time))
                elif before_or_after == -1 and file_mod_date_str < search_date_str:
                    matching_files.append((file_path, file_mod_time))

    return matching_files


if __name__ == '__main__':
    main()
