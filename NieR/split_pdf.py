from PyPDF2 import PdfReader, PdfWriter
import  TOOLS_COMMON as common
import os

def main():
    print("请输入需要拆分的pdf文件")
    source_pdf = common.input_file()

    print("分解的pdf文件会放入一个folder中，这个folder会和需要拆分的pdf一个路径")
    print("请输入，这个folde名，直接回车的话，就默认为tmp")
    folder_name = input()
    if folder_name == "":
        folder_name = "tmp"

    output_folder = os.path.join(os.path.dirname(source_pdf),folder_name)

    print("output_folder:"+ output_folder)

    #拆分，默认拆分每一个页面为一个pdf，但是这里能做到以不同页面为单位拆分的
    split_pdf(source_pdf, output_folder)


def split_pdf(source_path, output_dir):
    reader = PdfReader(source_path)
    total_pages = len(reader.pages)

    os.makedirs(output_dir, exist_ok=True)

    for i in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])

        output_path = os.path.join(output_dir, f"page_{i+1}.pdf")
        with open(output_path, "wb") as f:
            writer.write(f)
        print(f"Saved: {output_path}")



if __name__ == '__main__':
    main()