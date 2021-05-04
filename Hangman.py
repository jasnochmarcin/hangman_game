import sys
import os

no_of_tries = 5
word = 'stetoskop'
used_letters = []

user_word = []


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_state_of_game():
    print()
    print(user_word)
    print('Pozostało prób:', no_of_tries)
    print('Użyte litery:', used_letters)
    print()


def restart():
    result = input("\nCzy chcesz zagrać ponownie? [t/n] > ")
    if result == 't':
        os.system('python "D:/pycharm/Projekty/Hangman v2.py"')
    else:
        print("\nDo następnego razu.")
        sys.exit(0)


for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        no_of_tries -= 1

        if no_of_tries == 0:
            print('Koniec gry...')
            restart()
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Brawo, zgadłeś!")
            restart()

    show_state_of_game()
