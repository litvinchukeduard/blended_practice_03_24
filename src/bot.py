from src.AddressBook import AddressBook
import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.DEBUG,
        handlers=[
        logging.FileHandler("program.log")
    ])

def parse_input(user_input):
    cmd, *args = user_input.strip().split(' ')
    return cmd, *args

def bot():
    addressBook = AddressBook()
    while True:
        user_input = input('>>> ')
        command, *args = parse_input(user_input)
        if command == 'add':
            name, phone = args
            addressBook.update({name: phone})
            logging.info(f' User added: {name} - {phone}')
            print('User added!')
        elif command == 'all':
            print(addressBook)
        elif command in ['exit', 'bye']:
            print('Good bye!')
            break