# Music to MIDI
將 MP3 或 M4A 音訊檔案轉換為 MIDI 格式，適用於單聲道音訊（例如鋼琴獨奏、人聲旋律）。專案使用 Python 開發，基於 librosa、pydub 和 mido 等庫，實現音訊載入、音高檢測、音符起始檢測和 MIDI 檔案生成。

## 功能
* 音訊載入：支援 MP3 和 M4A 檔案，轉換為波形資料。
* 音高檢測：使用 librosa.pyin 演算法提取音高並轉換為 MIDI 音符。
* 音符起始檢測：檢測音符的開始時間和持續時間。
* MIDI 生成：根據音高和音符起始生成標準 MIDI 檔案。
* 輔助工具：提供檔案驗證和臨時檔案清理功能。
目前專案最適合處理單聲道音訊（例如簡單旋律）。

## 安裝
環境需求
* Python 3.8 或以上
* FFmpeg（用於處理 MP3/M4A 檔案）
  
## 步驟
1. 克隆專案
```bash
git clone https://github.com/ChenkailiuG/music_verilog_transformer.git
cd ./music_verilog_transformer/m2M/
```
3. 安裝依賴
```bash
pip install -r requirements.txt
```
5. 安裝 FFmpeg：
  * Windows：從 FFmpeg 官網 下載並加入系統環境變數。
  * macOS：
```bash
brew install ffmpeg
```
  * Linux：
```bash
sudo apt-get install ffmpeg
```

## 使用方法
### 使用 CLI 將 MP3 或 M4A 檔案轉換為 MIDI 檔案：
```bash
python scripts/cli.py --input examples/input/test.mp3 --output examples/output/output.mid
```
### 參數說明
* --input：輸入音訊檔案的路徑（支援 .mp3 和 .m4a）。
* --output：輸出 MIDI 檔案的路徑（必須以 .mid 結尾）。
生成的 output.mid 可在 MIDI 編輯器（如 GarageBand、Reaper）中開啟。

## 專案結構
```
m2M/
├── src/                     # 核心程式碼
│   ├── __init__.py          # 模組初始化
│   ├── audio_loader.py      # 音訊載入與預處理
│   ├── pitch_detector.py    # 音高檢測
│   ├── onset_detector.py    # 音符起始與持續時間檢測
│   ├── midi_generator.py    # MIDI 檔案生成
│   └── utils.py             # 輔助功能（檔案驗證、臨時檔案清理）
├── examples/                # 輸入輸出資料夾
│   ├── input/               # 輸入音訊檔案
│   └── output/              # 生成的 MIDI 檔案
├── scripts/                 # 執行腳本
│   └── cli.py               
└── requirements.txt         # 依賴清單
``` 

## 限制
* 目前僅支援單聲道音訊（例如鋼琴獨奏、人聲旋律）。複雜音訊（如多樂器混音）需額外處理。
* 音高和音符起始檢測可能因音訊品質或複雜度而有誤差，建議後期在 DAW 中手動調整 MIDI 檔案。
* 音符力度（velocity）目前為固定值（64）。
