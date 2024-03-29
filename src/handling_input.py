from currency_api.exchange import exchange
from weather_api.coordinates import display_city_cooredinates 
from weather_api.weather_infos import display_weather_infos
from weather_api.main_infos import display_main_infos
from weather_api.city_visibility import display_city_visibility
from weather_api.overall_infos import display_over_all_infos
from exit_message import exit_message

def commands_handling(user_input):
    global users_currency, target_currency, amount, city, options

    if 'currency exchange' in user_input or 'global currency' in user_input or 'exchange' in user_input or 'USD' in user_input or 'money' in user_input or 'trade' in user_input:
        print('hello i know a little bit about global currencies , how can i assist you')
        users_currency = input('-> please enter your current currency: ').upper()
        target_currency = input('-> please enter your target currency: ').upper()
        amount = input('please enter the ammount : ')
        exchange(users_currency, target_currency, amount)
        exit_message()
    elif 'weather infos' in user_input or 'weather' in user_input or 'weather of a city' in user_input or 'coordinates' in user_input:
        print('hello i know a little bit about global currencies , how can i assist you')  

        print('here are all the things that i can help you with')

        print("1) to see the coordinates of your chosen city")
        print("2) to see weather informations")
        print("3) to see main informations")
        print("4) to see visibility")
        print("5) to see the city overall informations")

        options = input('choose between these options : ')
        if options == '1':
            print('so you decided to to know about a city\'s coordinates, good good')
            city = input("-> enter the city name : ").lower()
            display_city_cooredinates(city)
            exit_message()

        elif options == '2':
            print('so you desided to know the weather infos of a city')
            city = input("-> enter the city name : ").lower()
            display_weather_infos(city)
            exit_message()

        elif options == '3':
            print('so you desided to know the main infos of a city')
            city = input("-> enter the city name : ").lower()
            display_main_infos(city)
            exit_message()

        elif options == '4':
            print('so you desided to know the visibility of a city')
            city = input("-> enter the city name : ").lower()
            display_city_visibility(city)
            exit_message()

        elif options == '5':
            print('so you desided to know the overall infos of a city')
            city = input("-> enter the city name : ").lower()
            display_over_all_infos(city)
            exit_message()




    

                            
    




