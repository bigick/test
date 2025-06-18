python - <<'EOF' 25
import sys, time, datetime, os, platform, subprocess

# 读取分钟数，并打印开始与结束时间
mins = int(sys.argv[1]) if len(sys.argv) > 1 else 25
end  = datetime.datetime.now() + datetime.timedelta(minutes=mins)
print(f"⏰ 专注时钟已启动：{mins} 分钟（将于 {end:%H:%M:%S} 结束）")

# 倒计时（每分钟刷新一次）
for m in range(mins, 0, -1):
    time.sleep(60)
    print(f"   · 剩余 {m-1} 分钟")

# 完成后发提示音（Windows / macOS / Linux 通用）
print("✨ 时间到！休息一下吧")
if platform.system() == "Windows":
    import winsound; winsound.MessageBeep()
elif platform.system() == "Darwin":
    subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])
else:
    os.system('play -nq -t alsa synth 0.3 sine 440')  # 需安装 sox
EOF
