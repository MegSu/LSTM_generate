#-*-coding:utf-8 -*-

import poet
import poet_head

from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__) # __name__代表目前執行的模組
CORS(app)

@app.route("/") # 函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
def home():
    return 'hello!'


@app.route('/predict', methods=["POST"])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    heading = insertValues['keyin']
    total_length = insertValues['row']
    result = poet.get_hidden_poetry(heading,total_length)
    return jsonify(result)

@app.route('/hidden', methods=["POST"])
def hiddenInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    heading = insertValues['keyin']
    result = poet_head.get_hidden_poetry(heading)
    return jsonify(result)


@app.route("/test") # 函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
def getValue():
    result = poet.get_hidden_poetry('美好',6)
    print(result)
    return jsonify(result)


if __name__=="__main__": # 如果以主程式執行
    app.run(host='0.0.0.0', port=80, debug=True) # 立刻啟動伺服器