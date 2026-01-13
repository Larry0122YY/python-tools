import cv2
import ffmpeg
import os
import TOOLS_COMMON as common

def main():
    print("请给我一个video file的的全路径，我转换成16：9")
    file_path = common.input_file()
    change_resolution(file_path)

def change_resolution(input_file):
    width,height = _get_width_height()

    folder_path = os.path.dirname(input_file)
    ext = os.path.basename(input_file).split(".")[1]
    output_video = os.path.join(folder_path,"transfered"+ext)
    print("output_video:"+output_video)

    input_video = r"H:\y叶紀美子\GAS-332.m4v"
    (
    ffmpeg
    .input(input_video)
    .filter("scale", width, height)
    .output(output_video, acodec="aac", vcodec="libx264", audio_bitrate="192k")  # 保留音频
    .run()
    )

def _get_width_height(video_path):

    cap = cv2.VideoCapture(video_path)

    # 获取分辨率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cap.release()

    return width,height

if __name__ == '__main__':
    main()




