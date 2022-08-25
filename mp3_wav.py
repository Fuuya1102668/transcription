def yt_dl(url):
    import subprocess
    cmd = "youtube-dl -o temp.mp3 --extract-audio --audio-format mp3 " + url
    return subprocess.check_call(cmd.split())

def mp3_wav(mp):
    import ffmpeg
    stream = ffmpeg.input(mp)
    stream = ffmpeg.output(stream, "temp.wav")
    return ffmpeg.run(stream)

if __name__ == "__main__":
    import sys
    yt_dl(sys.argv[1])