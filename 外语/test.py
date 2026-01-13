import os


def main():
    path = r"D:\OneDrive\OneSyncFiles\EP04_resource"
    改所有的wav格式的文件名(path)


def init():
    path = r"C:\Users\Administrator\Desktop\sss.txt"
    file = open(path,"r")
    dict_data = {}
    for line in file.readlines():
        key = line.split(".")[0]
        value = line.split(".")[1].split("\n")[0]
        dict_data[key] = value

    return dict_data


def 改所有的wav格式的文件名(path):
    dict_data = init()

    files = os.listdir(path)
    for file in files:
        full_path = os.path.join(path,file)
        c1 = os.path.isfile(full_path)
        c2 = file.endswith(".wav")
        file_num = file[0:2]
        c3 = file_num in dict_data.keys()
        if c1 and c2 and c3:
            print("============")
            print(full_path)
            new_file_name = os.path.join(path,file_num+"."+dict_data[file_num]+".wav")
            print(new_file_name)
            os.rename(full_path,new_file_name)

def sss():
    aaa = "abcdefg"
    print(aaa[0:2])

if __name__ == '__main__':
    main()
    # sss()