import os
import datetime
import time

def extract_error_logs(log_path="/var/log/syslog", output_path=None):
    try:
        # check if the log exist
        if not os.path.exists(log_path):
            print("==============================")
            print(f"This file {log_path} does not exist. Please check the path!")
            print("==============================")
            return

        # key word
        error_keywords = ["error", "fail", "critical", "warning"]

        # read log
        with open(log_path, "r") as log_file:
            logs = log_file.readlines()

        # key word filter
        error_logs = [
            log for log in logs
            if any(keyword in log.lower() for keyword in error_keywords)
        ]

        if not error_logs:
            print("No error logs found!")
            return

        # 输出到指定文件或屏幕
        if output_path:
            with open(output_path, "w") as output_file:
                output_file.writelines(error_logs)
            print(f"Error logs saved to {output_path}")
        else:
            print("Error logs found: Displaying first 50 entries:")
            for log in error_logs[:50]:  # 前50行避免屏幕刷屏
                print(log.strip())

    except PermissionError:
        print("Access Denied. Please run with sudo privileges!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("log monitoring service is starting...")
    # 文件name
    while True:
        output_file = f"error_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        print("Checking... logs...")
        log_path = "/var/log/syslog"  # path
        extract_error_logs(log_path=log_path, output_path=output_file)
        time.sleep(30)  # 每30秒检查一次

