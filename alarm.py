"""
一个简单的闹钟脚本（Windows 优先）。

功能：
- 显示/监看系统时间（确保与你电脑系统时间一致）
- 到点触发闹钟：蜂鸣 / 播放本地音频 / 打开 URL（例如 YouTube）
- 可选：NTP 偏差检测（需要安装 ntplib）

使用示例：
  python alarm.py --watch 10
  python alarm.py --at 07:30 --beep
  python alarm.py --in 10m --url "https://www.youtube.com/watch?v=xxxx"
  python alarm.py --at 23:10 --sound "D:\\music\\alarm.wav"
"""

from __future__ import annotations

import argparse
import datetime as _dt
import logging
import os
import sys
import time
import urllib.parse
import webbrowser
from typing import Optional, Tuple


LOG_FILE = os.path.join(os.path.dirname(__file__), "alarm.log")


def setup_logger() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def now_local() -> _dt.datetime:
    # 使用系统时间（用户要求：必须与系统时间一致）
    return _dt.datetime.now().astimezone()


def watch_system_time(seconds: int) -> None:
    end = time.time() + max(0, seconds)
    while time.time() < end:
        print(now_local().strftime("%Y-%m-%d %H:%M:%S %Z%z"))
        time.sleep(1)


def ntp_check(server: str = "pool.ntp.org", timeout: float = 3.0) -> None:
    """
    可选功能：检测系统时间相对 NTP 的偏差。
    需要：pip install ntplib
    """
    try:
        import ntplib  # type: ignore
    except Exception:
        logging.error("未安装 ntplib，无法做 NTP 检查。可执行：pip install ntplib")
        sys.exit(2)

    c = ntplib.NTPClient()
    try:
        resp = c.request(server, version=3, timeout=timeout)
    except Exception as e:
        logging.error("NTP 请求失败：%s", e)
        sys.exit(2)

    # resp.offset：本机时间与 NTP 的偏移（秒）。正数表示本机慢了，负数表示本机快了。
    offset_ms = resp.offset * 1000.0
    logging.info("NTP 服务器：%s", server)
    logging.info("系统时间：%s", now_local().strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    logging.info("NTP 偏差：%.2f ms（正=本机慢，负=本机快）", offset_ms)


def parse_duration(s: str) -> int:
    """
    支持：
      30s / 10m / 2h
    返回秒数
    """
    s = s.strip().lower()
    if not s:
        raise ValueError("duration 不能为空")
    unit = s[-1]
    num_str = s[:-1] if unit in ("s", "m", "h") else s
    unit = unit if unit in ("s", "m", "h") else "s"
    if not num_str.isdigit():
        raise ValueError(f"无法解析 duration：{s}")
    n = int(num_str)
    if unit == "s":
        return n
    if unit == "m":
        return n * 60
    return n * 3600


def parse_at_time(at: str, date_str: Optional[str]) -> _dt.datetime:
    """
    at: "HH:MM" or "HH:MM:SS"
    date_str: "YYYY-MM-DD" (可选)
    """
    at = at.strip()
    parts = at.split(":")
    if len(parts) not in (2, 3):
        raise ValueError("时间格式应为 HH:MM 或 HH:MM:SS")
    hh = int(parts[0])
    mm = int(parts[1])
    ss = int(parts[2]) if len(parts) == 3 else 0

    now = now_local()
    if date_str:
        y, m, d = (int(x) for x in date_str.split("-"))
        target_date = _dt.date(y, m, d)
    else:
        target_date = now.date()

    target = _dt.datetime(
        year=target_date.year,
        month=target_date.month,
        day=target_date.day,
        hour=hh,
        minute=mm,
        second=ss,
        tzinfo=now.tzinfo,
    )

    # 如果没给 date，并且目标时间已过，则默认设为“明天同一时间”
    if not date_str and target <= now:
        target = target + _dt.timedelta(days=1)
    return target


def ensure_youtube_autoplay(url: str) -> str:
    """
    尝试为 YouTube URL 添加 autoplay=1（注意：浏览器/YouTube 可能仍会阻止自动播放）。
    """
    try:
        parsed = urllib.parse.urlparse(url)
    except Exception:
        return url

    host = (parsed.netloc or "").lower()
    if "youtube.com" not in host and "youtu.be" not in host:
        return url

    q = dict(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
    q.setdefault("autoplay", "1")
    new_query = urllib.parse.urlencode(q)
    return urllib.parse.urlunparse(parsed._replace(query=new_query))


def play_beep_loop(stop_after_seconds: Optional[int] = None) -> None:
    """
    最稳妥的“响铃方式”：蜂鸣（Windows 用 winsound，其它平台退化为打印）。
    """
    start = time.time()
    try:
        import winsound  # Windows only

        while True:
            winsound.Beep(1000, 500)  # 频率 1000Hz，持续 500ms
            time.sleep(0.2)
            if stop_after_seconds is not None and (time.time() - start) >= stop_after_seconds:
                return
    except Exception:
        while True:
            print("BEEP")
            time.sleep(1)
            if stop_after_seconds is not None and (time.time() - start) >= stop_after_seconds:
                return


def try_play_sound_once(sound_path: str) -> bool:
    """
    尝试播放本地音频文件。
    - .wav: Windows 优先用 winsound
    - 其它: 尝试 playsound（可选依赖）
    """
    sound_path = os.path.abspath(sound_path)
    if not os.path.exists(sound_path):
        logging.error("铃声文件不存在：%s", sound_path)
        return False

    ext = os.path.splitext(sound_path)[1].lower()
    if ext == ".wav":
        try:
            import winsound

            winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            return True
        except Exception as e:
            logging.error("winsound 播放 wav 失败：%s", e)
            return False

    try:
        from playsound import playsound  # type: ignore

        playsound(sound_path, block=False)
        return True
    except Exception as e:
        logging.error("播放失败（可能未安装 playsound 或该格式不支持）：%s", e)
        logging.error("可选安装：pip install playsound==1.3.0（或把铃声换成 .wav）")
        return False


def wait_until(target: _dt.datetime) -> None:
    logging.info("目标闹钟时间：%s", target.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    while True:
        now = now_local()
        if now >= target:
            return
        # 轻量睡眠：避免过度 CPU，同时保持秒级精度
        time.sleep(0.5)


def interactive_flow() -> argparse.Namespace:
    print("=== Python 闹钟 ===")
    print("1) 先确认系统时间（直接回车跳过；输入数字=监看秒数，比如 10）：")
    w = input().strip()
    args = argparse.Namespace()
    args.watch = int(w) if w.isdigit() else 0
    args.ntp_check = False
    args.ntp_server = "pool.ntp.org"

    print("2) 设置闹钟时间：输入 HH:MM（例如 07:30） 或输入 in（例如 10m / 30s）")
    t = input("请输入：").strip()
    args.at = None
    args.date = None
    args.in_ = None
    if ":" in t:
        args.at = t
    else:
        args.in_ = t

    print("3) 选择闹钟动作：1=蜂鸣  2=本地音频文件  3=打开 URL(YouTube)")
    mode = input("请输入 1/2/3：").strip()
    args.beep = mode == "1" or mode == ""
    args.sound = None
    args.url = None
    if mode == "2":
        args.sound = input("请输入音频文件路径（推荐 .wav）：").strip().strip('"')
        args.beep = False
    elif mode == "3":
        args.url = input("请输入 URL：").strip()
        args.beep = False

    return args


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="简单闹钟（系统时间/到点响铃/打开 URL）")
    p.add_argument("--watch", type=int, default=0, help="监看系统时间 N 秒（用于确认与系统时间一致）")
    p.add_argument("--ntp-check", action="store_true", help="NTP 偏差检测（需要 ntplib）")
    p.add_argument("--ntp-server", default="pool.ntp.org", help="NTP 服务器（默认 pool.ntp.org）")

    g = p.add_mutually_exclusive_group()
    g.add_argument("--at", help="闹钟时间：HH:MM 或 HH:MM:SS（默认如果已过则算明天）")
    g.add_argument("--in", dest="in_", help="多少时间后触发：例如 10m / 30s / 2h")
    p.add_argument("--date", help="配合 --at 使用：YYYY-MM-DD（不填则默认今天/已过则明天）")

    a = p.add_mutually_exclusive_group()
    a.add_argument("--beep", action="store_true", help="到点蜂鸣（默认动作）")
    a.add_argument("--sound", help="到点播放本地音频（推荐 wav；mp3 需要 playsound）")
    a.add_argument("--url", help="到点打开 URL（例如 YouTube）")
    return p


def main(argv: Optional[list[str]] = None) -> int:
    setup_logger()

    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        args = interactive_flow()
    else:
        args = build_parser().parse_args(argv)

    if getattr(args, "watch", 0):
        watch_system_time(args.watch)

    if getattr(args, "ntp_check", False):
        ntp_check(getattr(args, "ntp_server", "pool.ntp.org"))

    # 计算目标时间
    target: Optional[_dt.datetime] = None
    if getattr(args, "in_", None):
        sec = parse_duration(args.in_)
        target = now_local() + _dt.timedelta(seconds=sec)
    elif getattr(args, "at", None):
        target = parse_at_time(args.at, getattr(args, "date", None))

    if target is None:
        logging.info("未指定闹钟时间（--at 或 --in）。进入交互模式更方便：直接运行 python alarm.py")
        return 1

    wait_until(target)

    # 触发动作
    logging.info("闹钟触发！当前系统时间：%s", now_local().strftime("%Y-%m-%d %H:%M:%S %Z%z"))

    url = getattr(args, "url", None)
    sound = getattr(args, "sound", None)
    beep = bool(getattr(args, "beep", False)) or (not url and not sound)

    if url:
        final_url = ensure_youtube_autoplay(url)
        logging.info("打开 URL：%s", final_url)
        webbrowser.open(final_url, new=2)
        # URL 打开后仍给一个蜂鸣兜底（避免浏览器阻止自动播放导致“没响”）
        play_beep_loop(stop_after_seconds=10)
        return 0

    if sound:
        ok = try_play_sound_once(sound)
        if not ok:
            logging.info("改用蜂鸣作为兜底")
            play_beep_loop(stop_after_seconds=10)
            return 0
        # 播放一次后，再用蜂鸣兜底提示（避免音频太短/播放失败用户没察觉）
        play_beep_loop(stop_after_seconds=5)
        return 0

    if beep:
        play_beep_loop()
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
