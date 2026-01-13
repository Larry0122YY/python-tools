from ast import main
import subprocess
import os

import TOOLS_COMMON as common
from pathlib import Path


def main():
    
    print('请将一个视频文件拖进来，我把他变成16：9的格式')
    file_path = Path(common.input_file())
    
    print('出力的文件的话，会默认变成temp.mp4')
    output_path = os.path.join(file_path.parent,'temp.mp4')

    to_16_9(file_path,output_path)


def to_16_9(input_path,output_path):

    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-vf", "scale=1280:720",  # 任何16:9分辨率都可以
        "-c:a", "copy",           # 保留音频
        output_path
    ]

    subprocess.run(cmd)
    print("拉伸完成:", output_path)



if __name__ == '__main__':
    main()