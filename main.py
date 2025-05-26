# ✅ 1. Flask 기반 webhook 수신 서버 (main.py)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"✅ 웹훅 수신됨: {data}")
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
