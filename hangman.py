from random import choice



print("H A N G M A N\nThe game will be available soon.")
words = ['python', 'java', 'kotlin', 'javascript']
chosen_word = choice(words)
word = input("Guess the word:" + chosen_word[0:3] + (len(chosen_word)-3)*"-")
if word == chosen_word:
    print("You survived!")
else:
    print("You lost!")
