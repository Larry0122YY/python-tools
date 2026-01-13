from ast import main
import subprocess
import os

import TOOLS_COMMON as common
from pathlib import Path

def main():
    print('请将一个iso文件拖进来，我把他变成mp4格式')
    file_path = common.input_file()
    if file_path.endswith('.iso'):
        print('这个文件不是iso结尾的，程序结束')

    file_path = Path(file_path)
    
    print('出力的文件的话，会默认变成iso_mp4.mp4')
    output_path = os.path.join(file_path.parent,'iso_mp4.mp4')
    iso_to_mp4(file_path,output_path)


def iso_to_mp4(input_iso,output_mp4):

    cmd = [
        "ffmpeg",
        "-i", input_iso,
        "-c:v", "libx264",   # 视频编码器
        "-c:a", "aac",       # 音频编码器
        output_mp4
    ]

    subprocess.run(cmd, check=True)
    print("转换完成！")


if __name__ == '__main__':
    main()