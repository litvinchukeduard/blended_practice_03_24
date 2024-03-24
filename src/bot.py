from src.AddressBook import AddressBook
from abc import ABC, abstractmethod
import logging

# Створити абстрактний клас бота (ABC, @abstractmethod) AbstractBot -> add, hello, exit
class AbstractBot(ABC):
    @abstractmethod
    def exit(self):
        pass

    def all(self, *args, addressbook):
        return addressbook
    @abstractmethod
    def add(self, *args, addressbook):
        pass

# Створити бот українською мовою та англійською мовою UkranianBot, EnglishBot

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
            try:
                name, phone = args 
                addressBook.update({name: phone})
                logging.info(f' User added: {name} - {phone}')
                print('User added!')
            except Exception:
                logging.warning(f'User not added')
            
        elif command == 'all':
            print(addressBook)
        elif command in ['exit', 'bye']:
            print('Good bye!')
            break