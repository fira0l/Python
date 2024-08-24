import requests
from twilio.rest import Client
from Access import *

ACCOUNT_SID = ACCOUNT_SID
AUTH_TOKEN = AUTH_TOKEN

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

Alpha_API = "V5LLPZGZBLDLUCEA"
NEWS_API_KEY = "fa42fba871b2432587b027fc44a5f8b4"

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
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)


difference = abs(float(yesterday_closing_data) - float(day_before_yesterday_closing_price))
print(difference)

diff_percent = (difference / float(yesterday_closing_data)) * 100
print(diff_percent)

if diff_percent > 3:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    three_articles = articles[:3]
    print(three_articles)
    formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_= '+12088048774',
            to='+251976104860'
        )






