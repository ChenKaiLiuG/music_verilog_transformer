# Music to MIDI

## 專案結構
m2M/  
├── src/                       
│   ├── __init__.py  
│   ├── audio_loader.py      # 音訊檔案載入與預處理  
│   ├── pitch_detector.py    # 音高檢測模組  
│   ├── onset_detector.py    # 節奏與音符開始檢測  
│   ├── source_separator.py  # 音源分離（尚未實裝）  
│   ├── midi_generator.py    # MIDI 檔案生成  
│   └── utils.py             # 輔助工具  
├── tests/                   # 單元測試  
│   ├── test_audio_loader.py  
│   ├── test_pitch_detector.py  
│   ├── test_onset_detector.py  
│   ├── test_midi_generator.py  
│   └── test_utils.py  
├── examples/                # 示例音訊檔案與結果  
│   ├── input/               # 測試用 MP3/M4A 檔案  
│   └── output/              # 生成的 MIDI 檔案  
└── requirements.txt         # 依賴庫清單  
