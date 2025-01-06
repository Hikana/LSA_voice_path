# LSA_Ai_Ids

## 目的 X 小目標:
試著解決以當前大學生角色遇到的種種小麻煩。

## 情境:
架設已FLASK架構為主得網站時，常常報錯，卻不知道從何開 Debug ，於是採用了最簡單而暴力的方式，把 Error Log 貼給 GPT 。

## 工具能做到的事:
不須頻繁切換瀏覽器的 GPT 頁面，而是直接將 Error Log 轉成 txt 檔案，寫個小外掛再將 txt 丟給 GPT。

## 環境架設:

Linux Service

/etc/systemd/system

sudo vim log_monitor.service

[Unit]
Description=Log Monitoring Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/hikana/Desktop/LSA_Ai_Ids/LSA_Ai_Ids/ggez.py
Restart=always
RestartSec=5s
User=root
WorkingDirectory=/home/hikana/Desktop/LSA_Ai_Ids/LSA_Ai_Ids/
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target

[app.py]
use 
pip install -r requirements.txt
pip install flask[asnyc]
before using the code
