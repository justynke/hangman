from random import choice


# GAME INTRO

print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
chosen_word = choice(words)
temp_word = list(len(chosen_word)*"-")


lives = 8

while lives > 0:
    print()
    print("".join(temp_word))
    char = input("Input a letter:")
    if char in chosen_word:
        if char in temp_word:
            print("No improvements")
            lives -= 1
        else:
            for i in range (len(chosen_word)):
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