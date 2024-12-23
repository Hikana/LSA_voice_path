from flask import Flask, render_template, jsonify
import os
from openai import AsyncOpenAI
from datetime import datetime
import asyncio

OPENAI_API_KEY = "put here"

aclient = AsyncOpenAI(api_key=OPENAI_API_KEY)

# 初始化 Flask 應用
app = Flask(__name__)

WATCH_DIR = os.getcwd()  
print(f"監控目錄: {WATCH_DIR}")

class FileReader:
    @staticmethod
    def read_file(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"

    @staticmethod
    def get_file_info(filepath):
        try:
            stats = os.stat(filepath)
            return {
                "size": stats.st_size,
                "modified": datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            return {"error": str(e)}

# ChatGPT 處理文件內容
async def process_with_gpt(content):
    try:
        response = await aclient.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一個文件分析助手。"},
                {"role": "user", "content": f"請分析以下內容：\n{content}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

# 文件內容與分析API
@app.route('/api/file/chatgpt', methods=['GET'])
async def get_file_content_with_chatgpt():
    filepath = os.path.join(WATCH_DIR, "error_log_123.txt")
    print(f"嘗試讀取的檔案路徑: {filepath}")

    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    # 讀取文件內容
    content = FileReader.read_file(filepath)
    if content.startswith("Error"):
        return jsonify({"error": content}), 500

    # 調用 ChatGPT 分析
    analysis = await process_with_gpt(content)

    return jsonify({
        "content": content,
        "analysis": analysis
    })

if __name__ == '__main__':
    # 在 Windows 上支持 asyncio 的事件循环
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app.run(debug=True)