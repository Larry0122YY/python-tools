# 这两句加在这里之后，双击此文件就能够找到上层的TOOLS的包了
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TOOLS import study_lang as common
def main():
    # 入力
    sheet_name = get_sheet_name()
    column_Q_name = "Q"
    column_A_name = "A"

    common.test_study(common.france_book_name,sheet_name,column_Q_name,column_A_name)


def get_sheet_name():
    print("请输入下面的番号，然后拿到sheet名：")
    print("1.8个主语代词")
    print("2.动词变位")
    print("3.habiter动词变位——规则1")
    print("4.Finir动词变位——规则2")
    print("5.être动词变位——无规则")
    print("6.number")
    print("7.字母读音")
    print("8.职业")
    print("9.地方")
    print("10.运动爱好")
    print("11.定冠词")
    print("12.介绍别人")
    print("13.连词_介词_代词")
    print("14.动词")
    print("15.名词")
    print("16.形容词")
    print("17.副词")
    print("18.短语")
    print("19.主有形容词")
    print("20.疑问形容词")

    select = input()

    if select == "1":
        return "zhuyu_daici"
    elif select == "2":
        return "动词变位"
    elif select == "3":
        return "habiter"
    elif select == "4":
        return "Finir"
    elif select == "5":
        return "Être"
    elif select == "6":
        return "number"
    elif select == "7":
        return "zimu_yuyin"
    elif select == "8":
        return "job"
    elif select == "9":
        return "place"
    elif select == "10":
        return "sports"
    elif select == "11":
        return "定冠词"
    elif select == "12":
        return "介绍别人"
    elif select == "13":
        return "连词_介词_代词"
    elif select == "14":
        return "动词"
    elif select == "15":
        return "名词"
    elif select == "16":
        return "形容词"
    elif select == "17":
        return "副词"
    elif select == "18":
        return "短语"
    elif select == "19":
        return "主有形容词"
    elif select == "20":
        return "疑问形容词"
    else:
        print("输入错误")

if __name__ == '__main__':
    main()


