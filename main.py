import sys
import json


class Phonebook:
    '''Phonebook (Creator phone number list)'''

    def __init__(self):
        '''Initialize'''
        self.__file_name = 'phonebook.json'

    def add(self, name, number):
        '''Adding phone number'''
        # Get latest list number
        list_number = self.__read()
        if not list_number:
            list_number = dict()

        # Add new number
        list_number[name] = number
        # Write new number
        self.__write(list_number)

    def modify(self, name, number):
        '''Modify phone number'''
        # Get latest list number
        list_number = self.__read()
        if not list_number:
            return False

        list_number[name] = number
        self.__write(list_number)

    def remove(self, removable):
        '''Write number to json file'''
        # Get list numbers
        list_number = self.__read()
        # Check list number empty
        if list_number:
            if removable in list_number.keys():
                # Remove item
                del list_number[removable]
                # Write to file
                self.__write(list_number)
            else:
                print('Name of owner not found!\n')
        else:
            print('Your phonebook is empty!\n')

    def show(self):
        '''Show number list'''
        list_number = self.__read()
        # Check list number empty
        if list_number:
            for key, value in list_number.items():
                print(key, value)
            print('\n')
        else:
            print('Your phonebook is empty!\n')

    def __write(self, content):
        '''Write number list'''
        with open(self.__file_name, 'w') as f:
            json.dump(content, f)

    def __read(self):
        '''Read number list'''
        try:
            with open(self.__file_name, 'r') as f:
                # Read file and convert to dict
                content = json.load(f)
                return content
        # If not found error & create file
        except FileNotFoundError:
            with open(self.__file_name, 'w') as f:
                return False
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # Create object
    phonebook = Phonebook()

    # Welcome & guide message
    print('\n========== || ********** Welcome to Phonebook program. ========== || **********\n')

    # Loop for user input
    while True:
        print('Add number = "a" - Modify number = "m" Remove Number = "r" - Show list of numbers = "s" - Exit = "q"')
        # Get user input
        answer = input('Enter your key: ')
        answer = answer.lower()

        print('\n')

        # Check user input
        if answer == 'a':
            name = input('Enter name of owner: ')
            number = input('Enter number: ')
            if name and number:
                phonebook.add(name, number)
            else:
                print('Invalid value! Try again.')
                continue

        elif answer == 'r':
            item = input('Name of removable: ')
            if item:
                phonebook.remove(item)
            else:
                print('Invalid value! Try again.')
                continue

        elif answer == 's':
            phonebook.show()

        elif answer == 'q':
            sys.exit()

        elif answer == 'm':
            name = input('Name for modify: ')
            number = input('New number: ')
            phonebook.modify(name, number)

        else:
            print('Unknown key! Try Again.')
            continue
