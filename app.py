from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🚀 실제 TradingView Webhook 주소 입력
TRADINGVIEW_WEBHOOK_URL = "https://coinglass-alert-bot.onrender.com/alert"

@app.route('/')
def home():
    return "✅ Coinglass TradingView Webhook Bot Running"

@app.route('/alert', methods=['POST'])
def alert():
    try:
        data = request.get_json()
        print("📩 Alert Triggered:", data)

        if not data or 'long_short_ratio' not in data:
            print("❌ 데이터 없음 또는 형식 오류")
            return jsonify({"error": "Missing or invalid JSON"}), 400

        # 조건: long/short 비율이 2.5 이상이면 TradingView에 전달
        if data['long_short_ratio'] >= 2.5:
            payload = {"text": f"🚀 강한 롱 우세! 비율: {data['long_short_ratio']}"}
            resp = requests.post(TRADINGVIEW_WEBHOOK_URL, json=payload)
            print(f"📤 TradingView에 보냄: {resp.status_code}")
        
        return jsonify({"status": "ok"}), 200

    except Exception as e:
        print("❗서버 처리 오류:", str(e))
        return jsonify({"error": str(e)}), 500
