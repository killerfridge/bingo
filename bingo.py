import random
import time


def generate_words():

    words = [
        'Ferguson',
        'Stuart Perry',
        'The moose',
        'RnB room Ikon',
        'The Green',
        '2 dinners',
        'Wine dinners',
        'Rudies',
        'Baby Brother',
        'Mr Walsh',
        'Maths',
        'Biology fieldtrip',
        'En - suite of dreams',
        'London Bridge',
        'Bogun',
        'Glucose',
        'The line is a dot to you',
        'Transponsder',
        'Unagi',
        'Hospital Radio',
        'DJ Cat',
        'Sausage',
        'Clothes husband',
        'Finsbury Park',
        'London',
        'Edinburgh',
        'TV',
        'Moons',
        'Stockie',
        'St Mary',
        'Curly hair',
        'Fashion',
        'Clothes',
        'Amsterdam',
        'Majorca',
        'Tenerife',
        'Bride',
        'Bridesmaid',
        'Portugal',
        'San Sabastian',
        'Best friend',
        'Grogan',
        'Cat',
        'Thomas',
    ]

    random.shuffle(words)

    return words


def main():
    print('''
   █████████    █████████   ███████████    █████   ███   █████    ███████    ███████████   ██████████      ███████████  █████ ██████   █████   █████████     ███████   
  ███░░░░░███  ███░░░░░███ ░█░░░███░░░█   ░░███   ░███  ░░███   ███░░░░░███ ░░███░░░░░███ ░░███░░░░███    ░░███░░░░░███░░███ ░░██████ ░░███   ███░░░░░███  ███░░░░░███ 
 ███     ░░░  ░███    ░███ ░   ░███  ░     ░███   ░███   ░███  ███     ░░███ ░███    ░███  ░███   ░░███    ░███    ░███ ░███  ░███░███ ░███  ███     ░░░  ███     ░░███
░███          ░███████████     ░███        ░███   ░███   ░███ ░███      ░███ ░██████████   ░███    ░███    ░██████████  ░███  ░███░░███░███ ░███         ░███      ░███
░███          ░███░░░░░███     ░███        ░░███  █████  ███  ░███      ░███ ░███░░░░░███  ░███    ░███    ░███░░░░░███ ░███  ░███ ░░██████ ░███    █████░███      ░███
░░███     ███ ░███    ░███     ░███         ░░░█████░█████░   ░░███     ███  ░███    ░███  ░███    ███     ░███    ░███ ░███  ░███  ░░█████ ░░███  ░░███ ░░███     ███ 
 ░░█████████  █████   █████    █████          ░░███ ░░███      ░░░███████░   █████   █████ ██████████      ███████████  █████ █████  ░░█████ ░░█████████  ░░░███████░  
  ░░░░░░░░░  ░░░░░   ░░░░░    ░░░░░            ░░░   ░░░         ░░░░░░░    ░░░░░   ░░░░░ ░░░░░░░░░░      ░░░░░░░░░░░  ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░     ░░░░░░░    
                                                                                                                                                                                                                                                                           
''')
    print('Welcome to Cat Bingo')

    words = generate_words()
    used_words = []

    while words:

        print('''\tPlease select an option from the below:
        \t\t1) Draw a new word
        \t\t2) Show the selected words
        ''')

        try:
            selection = int(input('Selected option: '))
        except:
            print('Not a valid option. Please select 1 or 2.')
            continue

        if selection == 1:
            current_word = words.pop()
            used_words.append(current_word)
            print('\nThe selected word is...\n')
            time.sleep(3)
            print(f'\t\t{current_word}!\n')

        elif selection == 2:
            for i, word in enumerate(used_words):
                print(f'\t{i+1}:\t{word}')
        else:
            print('Not a valid selection. Please choose either 1 or 2.')

    print('The game is complete - all words have now been chosen and someone should have won!')
    print('As a reminder, these were the words')
    for i, word in enumerate(used_words):
        print(f'\t\t{i+1}:\t{word}')
        time.sleep(2)
    input('Press enter to finish')


if __name__ == "__main__":
    main()