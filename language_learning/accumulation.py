# 这两句加在这里之后，双击此文件就能够找到上层的TOOLS的包了
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TOOLS import study_lang as common

def main():
    # 入力
    sheet_name = "accumulation"
    column_Q_name = "words"
    column_A_name = "pronounce"

    common.test_study(common.japanese_book_name, sheet_name,column_Q_name,column_A_name)

if __name__ == '__main__':
    main()


