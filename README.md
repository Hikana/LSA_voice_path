# LSA_Ai_Ids
一個 Ctrl + c 與 Ctrl + v 的解決方案....

## 目的 X 小目標:
現在最終目標是能夠實現簡易 Plug In 任何有報錯區塊的 Server。

小目標已達成，能自動定時讀取 Linux 系統中的 System Log 並丟給 GPT ，且有回傳解決辦法。

## 情境:
架設已FLASK架構為主得網站時，常常報錯，卻不知道從何開 Debug ，於是採用了最簡單而暴力的方式，把 Error Log 貼給 GPT 。

## 工具能做到的事:
不須頻繁切換瀏覽器的 GPT 頁面，而是直接將 Error Log 轉成 txt 檔案，寫個小外掛再將 txt 丟給 GPT ， 最終結果以網頁方式呈現。

## 環境 Setting 說明:

撰寫定時讀檔案的服務

[Linux Service]

/etc/systemd/system

sudo vim log_monitor.service

在裡面寫入
```
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
```

[Install]
WantedBy=multi-user.target

[app.py]
use 
pip install -r requirements.txt
pip install flask[asnyc]
before using the code

## 讀取檔案程式友善提醒:

GPT API 部分請自行替換成可使用 API 金鑰。

## 分工:

薛閔容  報告、買空氣消夜

馬康傑  提供技術上幫忙和debugg

黃子懿  製作ppt

周聖倫  自動啟動服務/抓取系統資訊/整合

蘇柏安   HTML和FLASK 

劉姵岑   製作ppt
