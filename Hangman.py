import sys
import os

no_of_tries = 5
word = 'stetoskop'
used_letters = []

user_word = []

difficulty = input("Select difficulty level. Press e, m or h. (easy[e], medium[m], hard[h])")
if difficulty == "e":
    no_of_tries = 8
elif difficulty == "m":
    no_of_tries = 5
else:
    no_of_tries = 3

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_state_of_game():
    print()
    print(user_word)
    print('Tries left:', no_of_tries)
    print('Used letters:', used_letters)
    print()


def restart():
    result = input("\nWant to play again? [y/n] > ")
    if result == 'y':
        os.system('python "D:/pycharm/Projekty/Hangman v2.py"')
    else:
        print("\nUntil next time.")
        sys.exit(0)

for _ in word:
    user_word.append("_")

while True:
    letter = input("Enter the letter: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("There is no such letter.")
        no_of_tries -= 1

        if no_of_tries == 0:
            print('Game over...')
            restart()
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Bravo, you guessed!")
            restart()

    show_state_of_game()
