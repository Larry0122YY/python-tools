import os.path
import TOOLS_COMMON as common

import cv2

cur_process = 0

def main():
    print("请将一个视频file拖进来:")
    video_file = common.input_file()
    print("请输入一个folder名，默认和video file在同一路径下，如果直接回车，则默认folder名为img：")
    print("名字必须是字母和数字")
    select_folder_name = input()
    if select_folder_name == "":
        folder_name = "img"
    else:
        folder_name = select_folder_name
    output_folder_path = os.path.join(os.path.dirname(video_file), folder_name)
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)

    print("video_file:",video_file)
    print("output_folder_path:",output_folder_path)
    get_all_frames_from_1video_exe(video_path=video_file, output_folder=output_folder_path)


def get_all_frames_from_1video_exe(video_path, output_folder):
    video_cap = cv2.VideoCapture(video_path)

    total_frame = video_cap.get(cv2.CAP_PROP_FRAME_COUNT)

    frame_number = 0
    print("当前这个视频一共有" + str(total_frame) + "帧")
    if_show_process = False

    while True:
        ret, frame = video_cap.read()
        if ret:
            frame_number += 1
            img_path = os.path.join(output_folder, str(frame_number) + ".png")
            cv2.imwrite(img_path, frame)
            actual_process = str(frame_number)+"/"+str(total_frame)
            process_100 = frame_number*100/total_frame
            check_result = check_if_show_process(process_100)

            if check_result != -1:
                print("当前进度是:"+str(check_result)+"%\t"+actual_process)

        else:
            break

    print("解析完成！")
    print("我们这次解析了前" + str(frame_number) + "帧的图片")

    video_cap.release()

    cv2.destroyAllWindows()

def check_if_show_process(cur_process_100):

    global cur_process
    if cur_process_100 > cur_process:
        result = cur_process
        cur_process += 1
    else:
        result = -1

    return result



if __name__ == '__main__':
    main()
