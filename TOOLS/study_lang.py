import sys, openpyxl, os
import random
import time
from colorama import Fore, init
import difflib

france_book_name = r"D:\OneDrive\OneSyncFiles\data\france.xlsx"
japanese_book_name = r"D:\OneDrive\OneSyncFiles\data\japanese.xlsx"
english_book_name = r"D:\OneDrive\OneSyncFiles\data\english.xlsx"

def test_study_write(book_path, sheet_name,column_Q_name,column_A_name):
    data_dict = _get_data_from_excel(book_path, sheet_name,column_Q_name,column_A_name)
    time_start = time.time()
    keys_list = list(data_dict.keys())
    # numbers = list(range(0, len(list)))
    # 将列表随机打乱
    random.shuffle(keys_list)

    process_count = 1
    # 依次显示打乱后的数字
    for index in keys_list:
        process_info = "\t\t\t" + str(process_count) + "/" +str(len(keys_list))
        Q_str = data_dict.get(index)[0]
        A_str =  data_dict.get(index)[1]
        print(str(Q_str)+process_info)
        my_answer = input()
        print(check_answer(A_str,my_answer)[0])
        print(check_answer(A_str, my_answer)[1])
        input()

        process_count += 1

    time_end = time.time()
    time_cost_int = time_end - time_start
    # 四舍五入后，取小数点后三位
    time_cost = str(round(time_cost_int, 3))
    print("费时：" + time_cost + "秒")
    input("结束了~~~")

def check_answer(input_word, correct_word):
    # Get the differences between input and correct words
    diff = difflib.ndiff(input_word, correct_word)

    highlighted_result = ""
    for char in diff:
        if char[0] == ' ':  # Correct character
            highlighted_result += char[-1]
        elif char[0] == '-':  # Wrong character in input
            highlighted_result += f"\033[91m{char[-1]}\033[0m"  # Red color for wrong character
        elif char[0] == '+':  # Missing character in input
            highlighted_result += f"\033[92m{char[-1]}\033[0m"  # Green color for missing character

    if correct_word == highlighted_result:
        result = "正确！"
    else:
        result = "错误"

    return result,highlighted_result



# 初始化 Colorama
init()

# 封装一个方法，将指定子字符串变红
def _highlight_substring_red(text, substring):

    # 找到子字符串的开始位置
    start = text.find(substring)

    # 如果找不到子字符串，返回原字符串
    if start == -1:
        return text

    # 计算结束位置
    end = start + len(substring)

    # 将指定子字符串变红
    return text[:start] + Fore.RED + text[start:end] + Fore.RESET + text[end:]


# 封装方法，通过row column，sheet拿到单元格里的value
def get_cur_value(sheet, row, column):
    cur_value = sheet.cell(row=row, column=column).value
    return cur_value


# 拿到book
def get_book(BOOK_PATH):
    book = openpyxl.load_workbook(BOOK_PATH)
    return book


# 关闭book流
def close_book(book):
    book.close()


# 从excel的某列列名中，拿到这一列的所有数据
def get_the_whole_column_data(book_path, sheet_name="py_files", column_name="py_file"):
    book = get_book(book_path)
    sheet = book[sheet_name]
    py_file_list_excel = []

    # 通过给入的column_name，找到列数
    column_number = get_column_by_name(sheet, column_name)

    # 遍历NieR.xlsx中sheet py_files的所有行
    for row in range(2, sheet.max_row + 1):
        # 将除了第一行以外的py_file那一列的数据放入list self.py_file_list_excel中
        cur_value = get_cur_value(row=row, column=column_number, sheet=sheet)
        py_file_list_excel.append(str(cur_value))

    # 关闭book流
    close_book(book)
    # 返回获取到的当前列的数据
    return py_file_list_excel


# 通过列名，找到列数
def get_column_by_name(sheet, column_name):
    # param1 当前sheet
    # parma2 需要search的列名

    # 列数的变量，默认设置为0
    column_number = 0
    # 遍历所有列
    for column in range(1, sheet.max_column + 1):
        # 拿到当前列第一行的cell的value
        cur_value = sheet.cell(row=1, column=column).value
        # 当前给入的列名和当前的cell 的value相同的时候
        if cur_value == column_name:
            # 获取当前的value列数
            column_number = column

    # 当整个第一行的所有列，都没有和当前给的列名相同时
    if column_number == 0:
        # 打印log
        print("没有" + column_name + "这一列！")
        # 退出程序
        sys.exit(2)

    return column_number

def _get_data_from_excel(book_path, sheet_name,column_Q_name,column_A_name):
    column_Q_data = get_the_whole_column_data(book_path, sheet_name=sheet_name,column_name=column_Q_name)
    column_A_data = get_the_whole_column_data(book_path, sheet_name=sheet_name, column_name=column_A_name)
    dict = {}
    if len(column_A_data) != len(column_Q_data):
        print("excel对不上！")

    for i in range(0,len(column_A_data)):
        dict[i] = [column_Q_data[i],column_A_data[i]]

    return dict


def test_study(book_path, sheet_name,column_Q_name,column_A_name):
    data_dict = _get_data_from_excel(book_path, sheet_name,column_Q_name,column_A_name)
    time_start = time.time()
    keys_list = list(data_dict.keys())
    # numbers = list(range(0, len(list)))
    # 将列表随机打乱
    random.shuffle(keys_list)

    process_count = 1
    # 依次显示打乱后的数字
    for index in keys_list:
        process_info = "\t\t" + str(process_count) + "/" +str(len(keys_list))
        Q_str = data_dict.get(index)[0]
        A_str =  data_dict.get(index)[1]
        print(str(Q_str)+process_info)
        input()
        print()
        print(str(A_str))
        input()
        print()
        print()
        process_count += 1

    time_end = time.time()
    time_cost_int = time_end - time_start
    # 四舍五入后，取小数点后三位
    time_cost = str(round(time_cost_int, 3))
    print("费时：" + time_cost + "秒")
    input("结束了~~~")
