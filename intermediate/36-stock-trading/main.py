""" Stok market """

import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "VI2OYWOCX0D75NGW"
NEWS_API_KEY = "f241105825bf4cd7ac228d044fd09d33"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before print("Get News").

# TODO1. - Get yesterday's closing stock price.
# Hint: You can perform list comprehensions on Python dictionaries.
# # e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params, timeout=10)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
data_yesterday = data_list[0]
data_yesterday_closing_price = data_yesterday["4. close"]
print(data_yesterday_closing_price)

# TODO2. Get the day before yesterday's closing stock price

data_day_before_yesterday = data_list[1]
data_day_before_yesterday_closing_price = data_day_before_yesterday["4. close"]
print(data_day_before_yesterday_closing_price)

# TODO3. - Find positive difference between 1 and 2. e.g. 40-20= -20, the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp

diff = abs(float(data_yesterday_closing_price) - float(data_day_before_yesterday_closing_price))
print(diff)

# TODO4. - Work out the percentage difference in price between closing price yesterday
# and closing price the day before yesterday.

diff_percent = (diff / float(data_yesterday_closing_price)) * 100
print(diff_percent)

# TODO5. - If TODO4 percentage is greater than 5 then print("Get News").

if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    new_res = requests.get(NEWS_ENDPOINT, params=news_params, timeout=5)
    articles = new_res.json()["articles"]
    
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_articles = articles[:3]
    formated_articles = [f"Headline: {article['title']}.\nBrief:c{article['description']}" for article in three_articles]
    print(formated_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

