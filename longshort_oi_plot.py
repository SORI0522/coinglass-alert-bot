import requests
import pandas as pd
import matplotlib.pyplot as plt

# 🔑 Coinglass API 키 입력
API_KEY = '3d409a829b1d4a4b861028df5e524e15'

# 헤더 구성
headers = {
    'accept': 'application/json',
    'CG-API-KEY': API_KEY
}

# API 엔드포인트
url_ratio = "https://open-api-v4.coinglass.com/api/futures/global-long-short-account-ratio/history?exchange=Binance&symbol=BTCUSDT&interval=h1"
url_oi = "https://open-api-v4.coinglass.com/api/futures/open-interest/aggregated-history?symbol=BTC&interval=1h"

# 요청 및 파싱
resp_ratio = requests.get(url_ratio, headers=headers).json()
resp_oi = requests.get(url_oi, headers=headers).json()

# 데이터프레임 정리
df_ratio = pd.DataFrame(resp_ratio['data'])
df_ratio['time'] = pd.to_datetime(df_ratio['time'], unit='ms')
df_ratio.set_index('time', inplace=True)

df_oi = pd.DataFrame(resp_oi['data'])
df_oi['time'] = pd.to_datetime(df_oi['time'], unit='ms')
df_oi.set_index('time', inplace=True)

# 📊 시각화 - 롱숏 비율
plt.figure(figsize=(12, 5))
plt.bar(
    df_ratio.index,
    df_ratio['global_account_long_short_ratio'],
    color=['green' if r > 1 else 'red' for r in df_ratio['global_account_long_short_ratio']]
)
plt.title('🟢🔴 Global Long/Short Ratio (Binance BTCUSDT, 1H)')
plt.xlabel('Time')
plt.ylabel('Long/Short Ratio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
