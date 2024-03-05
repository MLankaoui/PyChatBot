import requests
from dotenv import load_dotenv
import os
from currency_api.exchange import exchange

load_dotenv()
api_key = os.getenv('API_KEY_EXCHANGE')


def commands_handling(user_input):
    global users_currency, target_currency, amount

    if 'currency exchange' in user_input or 'global currency' in user_input or 'exchange' in user_input or 'USD' in user_input or 'money' in user_input or 'trade' in user_input:
        print('hello i know a little bit about global currencies , how can i assist you')
        users_currency = input('-> please enter your current currency: ').upper()
        target_currency = input('-> please enter your target currency: ').upper()
        amount = input('please enter the ammount : ')

                            
    print(f'ammount: {amount}')
    print(f'users_currency: {users_currency}')
    print(f'target currency: {target_currency}')
    exchange(users_currency, target_currency, amount)





