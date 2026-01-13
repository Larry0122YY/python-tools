import pandas as pd
import os
import xml.etree.ElementTree as ET
import shutil
from xml.dom.minidom import parseString
import openpyxl
import time

# 临时xml输出folder名字
temp_xml_folder_path = r"C:\Users\Administrator\Desktop\A2_xml_path"

f_excel_path = r"D:\OneDrive\OneSyncFiles\data\france.xlsx"
f_android_xml_path = r"D:\Android\WorkSpace\France\app\src\main\res\xml"

e_excel_path = r"D:\OneDrive\OneSyncFiles\data\english.xlsx"
e_android_xml_path = r"D:\Android\WorkSpace\English\app\src\main\res\xml"

j_excel_path = r"D:\OneDrive\OneSyncFiles\data\japanese.xlsx"
j_android_xml_path = r"D:\Android\WorkSpace\Japanese\app\src\main\res\xml"


def main():
    print("请输入你想改变哪个语言的数据？")
    print("直接回车：日语")
    print("e.英语")
    print("f.法语")
    lang = input_params(["","e","f"])
    if lang == "":
        lang = "j"
    main_exe(lang)

    input("执行完成！")

def input_params(check_collection=[]):
    while True:
        select = input()
        if select in check_collection:
            return select
        print("输入的参数不匹配！")
        time.sleep(1)
        print("请重新输入")


def main_exe(lang):
    excel_path, sheet_names, android_xml_path = _language_select(lang)

    if os.path.exists(temp_xml_folder_path):
        shutil.rmtree(temp_xml_folder_path)

    os.mkdir(temp_xml_folder_path)

    for sheet_name in sheet_names:
        output_xml_name = "{temp_xml_folder_path}\{file_name}_{sheet_name}.xml".format(
            temp_xml_folder_path=temp_xml_folder_path,
            sheet_name=sheet_name, file_name="file")
        generate_xml_from_excel(excel_path, sheet_name, output_xml_name)

    # 格式化整个xml
    _format_xml_main(temp_xml_folder_path)

    # 删掉安卓项目上现存的xml文件
    _delete_old_xml(android_xml_path)

    # 将新做好的xml文件放到安卓项目里去
    _move_xml_to_android_xml_path(temp_xml_folder_path,android_xml_path)

# 删掉安卓项目上现存的xml文件
def _delete_old_xml(android_xml_path):
    for file in os.listdir(android_xml_path):
        if file.endswith("xml") and file.startswith("file_"):
            file_full_path = os.path.join(android_xml_path,file)
            os.remove(file_full_path)

# 将新做好的xml文件放到安卓项目里去
def _move_xml_to_android_xml_path(new_android_xml_folder,android_xml_path):
    for file in os.listdir(new_android_xml_folder):
        if file.endswith("xml"):
            cur_full_xml_path = os.path.join(new_android_xml_folder,file)
            shutil.move(cur_full_xml_path,android_xml_path)

def _language_select(lang):
    android_xml_path = ""

    if lang == "j":
        excel_path = j_excel_path
        android_xml_path = j_android_xml_path
    elif lang == "e":
        excel_path = e_excel_path
        android_xml_path = e_android_xml_path
    elif lang =="f":
        excel_path = f_excel_path
        android_xml_path = f_android_xml_path

    return excel_path,get_sheet_names(excel_path),android_xml_path

def get_sheet_names(file_path):
    """
    获取 Excel 文件中所有工作表名称的列表。

    :param file_path: Excel 文件的完整路径
    :return: 包含所有工作表名称的列表
    """
    try:
        # 加载 Excel 文件
        workbook = openpyxl.load_workbook(filename=file_path)
        # 获取所有工作表名称
        sheet_names = workbook.sheetnames
        return sheet_names
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return []
    except Exception as e:
        print(f"发生错误: {e}")
        return []

def _format_xml_main(temp_xml_folder_path):
    for file in os.listdir(temp_xml_folder_path):
        if file.endswith(".xml"):
            cur_xml = os.path.join(temp_xml_folder_path,file)

            # 格式化XML并保存
            formatted_xml = _format_xml(cur_xml)
            _save_formatted_xml(cur_xml, formatted_xml)


# 读取XML文件并解析
def _format_xml(file_path):
    # 打开并解析XML文件
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_data = file.read()

    # 使用minidom解析并格式化
    dom = parseString(xml_data)
    pretty_xml_as_string = dom.toprettyxml(indent="    ")

    # 输出格式化后的XML
    return pretty_xml_as_string


# 保存格式化后的XML
def _save_formatted_xml(file_path, formatted_xml):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_xml)

def generate_xml_from_excel(excel_path, sheet_name, output_xml_name):
    # 读取Excel文件
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # 创建XML的根节点
    root = ET.Element("data")

    # 遍历Excel中的每一行，将Q列和A列的数据加入XML
    for _, row in df.iterrows():
        if row["T"] != "N":
            item = ET.SubElement(root, "item")
            question = ET.SubElement(item, "question")
            question.text = str(row["Q"])
            answer = ET.SubElement(item, "answer")
            answer.text = str(row["A"])

    # 生成XML树
    tree = ET.ElementTree(root)

    tree.write(output_xml_name, encoding="utf-8", xml_declaration=True)

    print(f"XML file has been generated at: {output_xml_name}")


if __name__ == '__main__':
    main()
