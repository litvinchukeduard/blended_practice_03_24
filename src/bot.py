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
class UkrBot(AbstractBot):

    def exit(self):
        return 'До побачення'
    
    def add(self, args, addressbook):
        name, phone = args 
        addressbook.update({name: phone})
        logging.info(f' User added: {name} - {phone}')
        return 'Користувача додано!'
    
class EngBot(AbstractBot):

    def exit(self):
        return 'Good bye'
    
    def add(self, args, addressbook):
        name, phone = args 
        addressbook.update({name: phone})
        logging.info(f' User added: {name} - {phone}')
        return 'User added!'


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
    user_input = int(input('Виберіть мову: 1 - укр 2 - англ'))
    if user_input == 1:
        bot = UkrBot()
    else:
        bot = EngBot()

    while True:
        user_input = input('>>> ')
        command, *args = parse_input(user_input)
        if command == 'add':
            try:
                print(bot.add(args,addressBook))
            

            except Exception:
                logging.warning(f'User not added')
            
        elif command == 'all':
            print(addressBook)
        elif command in ['exit', 'bye']:
            print(bot.exit())
            break
        