import requests
import os
from datetime import datetime as dt
from datetime import timedelta as td
from twilio.rest import Client

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
stock_api_key = os.environ["stock_api_key"]
news_api_key = os.environ["news_api_key"]
# finding yesterday's date
yesterday_date = (dt.now() - td(1)).strftime("%Y-%m-%d")
previous_date = (dt.now() - td(2)).strftime("%Y-%m-%d")
# news api parameters
news_parameters = {
    "q": COMPANY_NAME,
    "from": previous_date,
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": news_api_key,
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# stock api parameters
stock_parameter = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_api_key,
}
# stock api request module
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameter)
stock_response.raise_for_status()
print(stock_response.status_code)
stock_data = stock_response.json()
print(stock_data)

yesterday_close_price = float(stock_data["Time Series (Daily)"][yesterday_date]["4. close"])
previous_day_close_price = float(stock_data["Time Series (Daily)"][previous_date]["4. close"])
print(yesterday_close_price)
print(previous_day_close_price)
percentage_change = ((yesterday_close_price - previous_day_close_price) / previous_day_close_price) * 100
print(f"{percentage_change}%")
if -1 <= percentage_change >= 1:
    print("Get News")
    if percentage_change <= -1:
        percent = f"🔻{round(percentage_change, 2)}%"
    if percentage_change >= 1:
        percent = f"🔺{round(percentage_change, 2)}%"
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    print(news_response.status_code)
    news_data = news_response.json()
    print(news_data)
    text_heading = []
    text_description = []
    for i in range(0, 2):
        text_heading.append(news_data["articles"][i]["title"])
        text_description.append(news_data["articles"][i]["description"])
    message = f"TSLA: {percent}\nHeadline: {text_heading[0]}\nBrief: {text_description[0]}"
    print(message)
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=message,
        from_='+15154747874',
        to='+919072622722'
    )
    print(message.status)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""