from random import choice


def player_input():
    while True:
        znak = input("Input a letter:")
        if len(znak) == 1 and znak.islower():
            if znak in guessed_letters:
                print("You've already guessed this letter")
                print()
                print("".join(temp_word))
            else:
                return znak
        else:
            if len(znak) != 1:
                print("You should input a single letter")
                print()
                print("".join(temp_word))
            elif not znak.islower():
                print("Please enter a lowercase English letter")
                print()
                print("".join(temp_word))


def menu():
    while True:
        menu_choice = input()
        print('Type "play" to play the game, "exit" to quit:')
        if menu_choice == "exit":
            exit()
        elif menu_choice == "play":
            break


# GAME INTRO

print("H A N G M A N")
menu()
words = ['python', 'java', 'kotlin', 'javascript']
chosen_word = choice(words)
temp_word = list(len(chosen_word)*"-")

# GAME
guessed_letters = set()
lives = 8
while lives > 0:
    print()
    print("".join(temp_word))
    char = player_input()
    guessed_letters.add(char)
    if char in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == char:
                temp_word[i] = char
    else:
        print("That letter doesn't appear in the word")
        lives -= 1
    if "-" not in temp_word:
        print("".join(temp_word))
        print("You guessed the word!\nYou survived!")
        exit()

print("You lost!")
