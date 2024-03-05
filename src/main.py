from handling_input import commands_handling

def main():
    greetings()


    while True:
        user_input = input('-> ').lower()

        if 'hello' in user_input:
            print('hello how can i assist you today')

        elif user_input == 'quit':
            print('exiting ...')
            exit(0)
        else:
            commands_handling(user_input)
        '''elif 'hru' in user_input or 'how are you' in user_input:
            print('hello , i don\'t experience emotions, how about you , you feeling good today?')

        elif 'yes' in user_input or 'im good' in user_input or 'i\'m alright' in user_input or 'alright' in user_input or 'good' in user_input:
            print('good to know!')

        elif 'no'in user_input or 'exshausted' in user_input or 'bad' in user_input or 'tired' in user_input or 'not feeling good' in user_input or 'not feeling well' in user_input:
            print('im sorry to hear that , how can i help you?')
        '''

        
        
       

def greetings():
    print('hello welcome to PYCHATBOT')

main()
