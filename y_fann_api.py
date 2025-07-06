import requests
import pandas as pd
import json
from datetime import datetime

url = "https://query2.finance.yahoo.com/v8/finance/chart/SPY"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
}
param = {'period1': 946702800, 'period2': 1606798800, 'interval': '1d', 'events': 'history'}
response = requests.get(url, params=param, headers=headers)
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Extract the timestamp and close prices
    timestamps = data['chart']['result'][0]['timestamp']
    close_prices = data['chart']['result'][0]['indicators']['quote'][0]['close']

    # Convert to DataFrame
    df = pd.DataFrame({
        'Date': [datetime.fromtimestamp(ts) for ts in timestamps],
        'Close': close_prices
    })

    # Set the date as index
    df.set_index('Date', inplace=True)

    # Display the first few rows
    print(df.head())
else:
    print("Error:", response.status_code)
