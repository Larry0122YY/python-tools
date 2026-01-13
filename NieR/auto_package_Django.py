import os
import shutil
import subprocess


def main():
    # 你的 Django App 目录路径
    app_path = r"C:\Users\Administrator\Desktop\Django_ws\myproject"  # 替换成你的路径

    # 目标 exe 文件路径（打包后）
    dist_path = os.path.join(app_path, "dist", "run.exe")

    # 桌面路径
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "run.exe")

    # 1️⃣ 切换到 `django/app` 目录
    os.chdir(app_path)

    # 2️⃣ 执行 PyInstaller 打包
    print("🚀 正在打包 EXE 文件...")
    subprocess.run("pyinstaller -F run.py", shell=True, check=True)

    # 3️⃣ 等待打包完成，检查 `dist/run.exe` 是否生成
    if os.path.exists(dist_path):
        # 4️⃣ 复制 EXE 到桌面
        shutil.copy(dist_path, desktop_path)
        print(f"✅ EXE 文件已复制到桌面: {desktop_path}")
    else:
        print("❌ 打包失败，未找到 run.exe")



if __name__ == '__main__':
    main()