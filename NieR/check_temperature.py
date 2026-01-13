import time
import TOOLS_COMMON as common


def main():
    find_cmd = common.get_find_cmd()
    print("请输入每过几秒后，显示一次温度：(直接回车，默认1秒)")
    select = common.input_digital_or_none()
    if select == "":
        delay_time = 1
    else:
        delay_time = int(select)
    check_temperature_main(find_cmd, delay_time)


def check_temperature_main(find_cmd, delay_time):
    while True:
        battery_cmd = "adb shell dumpsys battery | %s temperature" % find_cmd
        rw = common.run_shell(battery_cmd)
        # 解析温度值：处理换行符和字节字符串格式
        if rw is None:
            rw = ""
        rw = rw.strip()  # 去除首尾空白和换行符
        # 处理可能的字节字符串前缀（如 b'...' 或 b"..."）
        if rw.startswith("b'") and rw.endswith("'"):
            rw = rw[2:-1]
        elif rw.startswith('b"') and rw.endswith('"'):
            rw = rw[2:-1]
        # 分割并提取温度值（通常在最后一个部分）
        parts = rw.split()
        if len(parts) >= 2:
            result = parts[-1].strip()
        elif len(parts) == 1 and ":" in parts[0]:
            # 处理类似 "temperature:320" 的格式
            result = parts[0].split(":")[-1].strip()
        elif len(parts) > 3:
            # 保持原有逻辑作为备选
            result = parts[3].strip()
        else:
            result = parts[0] if parts else ""
        temperature = formate_temperature(result)
        battery_disp = "当前手机温度为" + temperature + "度"
        print(battery_disp)
        time.sleep(delay_time)


def formate_temperature(num):
    temperature = ""
    for i in range(len(num)):
        if i == len(num) - 1:
            temperature += "."
        temperature += num[i]
    return temperature


if __name__ == '__main__':
    main()
