# 这两句加在这里之后，双击此文件就能够找到上层的TOOLS的包了
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TOOLS import study_lang as common

def main():
    # 入力
    sheet_name = get_sheet_name()
    column_Q_name = "words"
    column_A_name = "pronounce"

    common.test_study(common.japanese_book_name, sheet_name,column_Q_name,column_A_name)

def get_sheet_name():
    print("请选择您要测试的scene单词：")
    print("1.01~03")
    print("2.04~07")
    print("3.08~09")
    print("4.10~12")
    print("5.13~15")
    print("6.16~18")
    print("7.19~21")
    print("8.22~23")
    print("9.24~25")
    print("10.26~27")
    print("11.28~30")
    print("12.31~32")
    print("13.33~34")
    print("14.35~36")
    select = input()

    return select


if __name__ == '__main__':
    main()


