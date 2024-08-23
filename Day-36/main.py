import requests

STOCK_NAME = "TSLA"

Alpha_API = "V5LLPZGZBLDLUCEA"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": Alpha_API
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_data = yesterday_data["4. close"]
print(yesterday_closing_data)


day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. closing"]
print(day_before_yesterday_closing_price)



