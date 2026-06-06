import subprocess
from pathlib import Path

# ========== 配置区域 ==========
AUDIO_DIR = r"E:\Games\Jiaozuo3Test\game\audio"   # wav 文件所在目录
VOICE_DIR = r"E:\Games\Jiaozuo3Test\game\voice"   # ogg 输出目录
FFMPEG_AUDIO_QUALITY = 5                           # ogg 音质 0-10
# =================================

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def convert_wav_to_ogg():
    ensure_dir(VOICE_DIR)
    wav_files = list(Path(AUDIO_DIR).glob("*.wav"))
    if not wav_files:
        print("没有找到任何 .wav 文件，跳过转换。")
        return

    for wav_path in wav_files:
        ogg_path = Path(VOICE_DIR) / (wav_path.stem + ".ogg")
        # 若 ogg 已存在且比 wav 新，则跳过
        if ogg_path.exists() and ogg_path.stat().st_mtime >= wav_path.stat().st_mtime:
            print(f"跳过转换（已存在且较新）：{ogg_path.name}")
            continue
        print(f"转换：{wav_path.name} -> {ogg_path.name}")
        cmd = [
            "ffmpeg", "-y", "-i", str(wav_path),
            "-c:a", "libvorbis", "-q:a", str(FFMPEG_AUDIO_QUALITY),
            str(ogg_path)
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"转换失败：{wav_path.name}\n错误信息：{e.stderr}")

def main():
    print("开始将 .wav 转换为 .ogg ...")
    convert_wav_to_ogg()
    print("全部完成！")

if __name__ == "__main__":
    main()