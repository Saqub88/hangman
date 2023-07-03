# Task 1
word_list = ['mangoes', 'apples', 'raspberries', 'pomegranate', 'passion fruit']
print(word_list)

# Task 2
import random
word = random.choice(word_list)
print(word)

# Task 3
guess = input("Please enter a single letter as your guess: ")

# Task 4
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
