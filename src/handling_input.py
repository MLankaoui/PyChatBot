import requests
from dotenv import load_dotenv
import os
from currency_api.exchange import exchange

load_dotenv()
api_key = os.getenv('API_KEY_EXCHANGE')

users_currency = ''
target_currency = ''
amount = ''

def commands_handling(user_input):
    global users_currency, target_currency, amount
    if 'currency exchange' in user_input or 'global currency' in user_input or 'exchange' in user_input or 'USD' in user_input:
        print('hello i know a little bit about global currencies , how can i assist you')
    
    currency = requests.get(f"https://api.currencyapi.com/v3/latest",params={"apikey": api_key, "base_currency": users_currency})

    exchanges = currency.json()

    for currency_one in user_input.split():
        if currency_one in exchanges['data']:
            users_currency = currency_one
            for currency_two in user_input.split():
                if currency_two in exchanges['data']:
                    target_currency = currency_two
                    for currency_amount in user_input.split():
                        if currency_amount.isdigit():
                            amount = currency_amount

    exchange(users_currency, target_currency, amount)
