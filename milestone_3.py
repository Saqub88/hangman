guess = input("Please enter a single letter as your guess: ")

while True:
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        guess = (input("Invalid letter. Please, enter a single alphabetical character."))