# transcription
ちなみに精度ゴミ

## 環境構築
まず，おまじない
```
sudo apt-get update
```

speechrecognition をインストール
```
pip install speechrecognition
```

youtube_dl の最新版をインストール
```
sudo apt install youtube-dl
```

ffmpeg のインストール
```
sudo apt-get -y install ffmpeg
pip install ffmpeg-python
```

## 実行
```
python3 transcription.py URL
```

このプログラムは実行毎に「temp.mp3」「temp.wav」を削除する必要があります．←致命的ミス
