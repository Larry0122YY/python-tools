# Python 小工具合集

## `alarm.py`（闹钟）

### 你要的两步

- **步骤 1：测试/确认系统时间**
  - `alarm.py` 使用的就是系统时间（`datetime.now()`），所以它天然与 Windows 系统时间一致。
  - 你可以用 `--watch` 让它连续打印当前系统时间，肉眼确认即可。

- **步骤 2：到点响铃**
  - 支持三种方式：
    - **蜂鸣**（最稳妥，不依赖外部软件）
    - **播放本地音频**（推荐 `.wav`；`mp3` 可能需要额外依赖）
    - **打开 URL**（例如 YouTube；是否能“自动播放”取决于浏览器/YouTube 的限制，所以脚本会额外蜂鸣几秒做兜底）

### 常用命令

- **监看系统时间 10 秒**：

```bash
python alarm.py --watch 10
```

- **在 07:30 响铃（蜂鸣）**：

```bash
python alarm.py --at 07:30 --beep
```

- **10 分钟后打开 YouTube（并蜂鸣兜底）**：

```bash
python alarm.py --in 10m --url "https://www.youtube.com/watch?v=xxxx"
```

- **到点播放本地 wav**：

```bash
python alarm.py --at 23:10 --sound "D:\music\alarm.wav"
```

### 可选：NTP 偏差检测（高级）

如果你想知道“系统时间相对网络时间偏差多少”，可以用：

```bash
python alarm.py --ntp-check
```

需要先安装依赖（见 `requirements.txt`）。

