from flask import Flask, request, jsonify

app = Flask(__name__)

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

        # 조건: long_short_ratio >= 2.5 일 때 로깅만 수행
        if data['long_short_ratio'] >= 2.5:
            print(f"🚀 강한 롱 우세! 비율: {data['long_short_ratio']}")

        return jsonify({"status": "ok"}), 200

    except Exception as e:
        print("❗서버 처리 오류:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
