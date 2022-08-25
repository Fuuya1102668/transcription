import speech_recognition as sr
import mp3_wav as mw
import sys

mw.yt_dl(sys.argv[1])
mw.mp3_wav("temp.mp3")
r = sr.Recognizer()
with sr.AudioFile("temp.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio, language="ja-JP")
print(text)
