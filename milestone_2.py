
import random

word_list = ['mangoes', 'apples', 'raspberries', 'pomegranate', 'passion fruit']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter as your guess: ")
print(guess)