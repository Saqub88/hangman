
import random

word_list = ['mangoes', 'apples', 'raspberries', 'pomegranate', 'passion fruit']
print(word_list)

word = random.choice(word_list)

guess = input("Please enter a single letter as your guess: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")