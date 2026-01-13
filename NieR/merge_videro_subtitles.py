
import os
from collections import defaultdict

import TOOLS_COMMON as common

ffmpeg_cmd = "ffmpeg -i {} -i {} -c copy -c:s srt -disposition:s:0 default {}"

def main():
    print("这个folder底下，视频和字幕文件必须同名，所有文件必须配对")
    print("将folder路径拖进来")
    folder_path = common.input_folder()

    List_data = group_files_by_basename(folder_path)

    run_cmd_list(List_data)


def run_cmd_list(List_data):

    for list_1 in List_data:
        video_path = list_1[0]
        seriel_path = list_1[1]
        cmd = _get_cmd(video_path,seriel_path)
        
        common.run_shell(cmd)

        print(+video_path+"合成完成！！！")
        print()


def _get_cmd(video_path,seriel_path):
    folder_name = os.path.dirname(video_path)
    base_name = os.path.splitext(video_path)[0]+"_conversion"
    ext_name = os.path.splitext(video_path)[1]

    output_file_path = os.path.join(folder_name,base_name+ext_name)

    cmd = ffmpeg_cmd.format(video_path,seriel_path,output_file_path)

    return cmd

def group_files_by_basename(folder_path):
    # 使用 defaultdict 存储分组结果
    file_groups = defaultdict(list)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # 提取文件名和后缀
            basename, ext = os.path.splitext(filename)

            # fullpath
            cur_file_full_path = os.path.join(folder_path,filename)

            # 将文件路径添加到以 basename 为键的列表中
            file_groups[basename].append(cur_file_full_path)

    # 将分组结果转换为列表
    grouped_files_list = list(file_groups.values())
    return grouped_files_list



if __name__ == '__main__':
    main()