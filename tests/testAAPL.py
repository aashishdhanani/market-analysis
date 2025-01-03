import requests
import os
from dotenv import load_dotenv
import finnhub
load_dotenv()

alphavantage = os.getenv('VANTAGE_KEY')
finnhubkey = os.getenv('FINNHUB')

#get current price of AAPL
finnhub_client = finnhub.Client(api_key=finnhubkey)
prices = finnhub_client.quote('AAPL')
print(prices['c'])

url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey={alphavantage}'
r = requests.get(url)
data = r.json()

print(data)