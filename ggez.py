import os
import datetime
import time

def extract_error_logs(log_path="/var/log/syslog", output_path=None, max_lines=20):
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
        ][:max_lines]  # 限制抓取的日誌數量

        if not error_logs:
            print("No error logs found!")
            return

        # output to setting screen or file
        if output_path:
            with open(output_path, "w") as output_file:
                output_file.writelines(error_logs)
            print(f"Error logs saved to {output_path}")
        else:
            print(f"Error logs found: Displaying first {max_lines} entries:")
            for log in error_logs:
                print(log.strip())

    except PermissionError:
        print("Access Denied. Please run with sudo privileges!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("log monitoring service is starting...")
    while True:
        output_file = f"error_log_123.txt"
        print("Checking... logs...")
        log_path = "/var/log/syslog"  # path
        extract_error_logs(log_path=log_path, output_path=output_file, max_lines=20)  # limit 20
        time.sleep(30)  # 30sec check
