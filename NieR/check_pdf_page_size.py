import fitz  # PyMuPDF
import TOOLS_COMMON as common

def main():
    print("请输入一个以.pdf结尾的文件")
    file = common.input_file()

    if file.endswith(".pdf"):
       process(file)
    else:
        print("这不是pdf文件，程序结束~")



def process(pdf_path):

    # 获取PDF页面大小
    page_sizes = get_pdf_page_sizes(pdf_path)

    # 打印每页的宽度和高度，并计算和显示比例
    for page_num, width, height in page_sizes:
        if width > height:
            ratio_w = width / height
            ratio_h = 1
            ratio_str = f"{ratio_h:.2f}(height) : {ratio_w:.2f}(width)"
        elif width < height:
            ratio_w = 1
            ratio_h = height / width
            ratio_str = f"{ratio_w:.2f}(width) : {ratio_h:.2f}(height)"
        else:
            ratio_w = 1
            ratio_h = 1
            ratio_str = f"{ratio_w:.2f}(width) : {ratio_h:.2f}(height)"

        print(f"Page {page_num}: Width = {width} pt, Height = {height} pt, Ratio = {ratio_str}")


def get_pdf_page_sizes(pdf_path):
    document = fitz.open(pdf_path)
    page_sizes = []

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        rect = page.rect
        width = rect.width
        height = rect.height
        page_sizes.append((page_num + 1, width, height))

    document.close()
    return page_sizes

if __name__ == '__main__':
    main()
