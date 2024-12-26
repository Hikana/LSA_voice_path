# LSA_Ai_Ids
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
