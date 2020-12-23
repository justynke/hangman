from random import choice


# GAME INTRO

print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript']
chosen_word = choice(words)
temp_word = list(len(chosen_word)*"-")


tries = 0

while tries < 8:

    print("".join(temp_word))
    char = input("Input a letter:")
    if char in chosen_word:
        print()
        for i in range (len(chosen_word)):
            if chosen_word[i] == char:
                temp_word[i] = char
    else:
        print("That letter doesn't appear in the word\n")
    tries += 1

print("Thanks for playing!\nWe'll see how well you did in the next stage")
