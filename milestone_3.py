word = "gerfuffle"
guess = input("Please enter a single letter as your guess: ")
letters_in_play = set(word)

while True:
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        guess = (input("Invalid letter. Please, enter a single alphabetical character."))

if guess in letters_in_play:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")