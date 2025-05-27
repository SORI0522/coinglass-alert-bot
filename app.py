from flask import Flask, request
import requests

app = Flask(__name__)

TRADINGVIEW_WEBHOOK_URL = "TRADINGVIEW_WEBHOOK_URL = "https://coinglass-alert-bot.onrender.com/alert"

@app.route('/', methods=['GET'])
def home():
    return "Coinglass TradingView Webhook Bot Running"

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    print("📩 Alert Triggered:", data)

    # 조건 예시: 롱숏 비율이 2.5 이상이면 TradingView에 알림 전송
    if data['long_short_ratio'] >= 2.5:
        payload = {"text": f"🚀 강한 롱 우세: 비율 = {data['long_short_ratio']}"}
        requests.post(TRADINGVIEW_WEBHOOK_URL, json=payload)
    return {"status": "ok"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
