word = "gerfuffle"
resampled_word = word.lower()
guess = input("Please enter a single letter as your guess: ")
letters_in_play = set(resampled_word)

#def ask_for_input(current_guess):
while True:
    if len(guess) == 1 and guess.isalpha():
#        return str(current_guess)
        break
    else:
        guess = (input("Invalid letter. Please, enter a single alphabetical character."))

#def check_guess(current_guess):
if guess.lower() in letters_in_play:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")


# guess = ask_for_input(guess)
# check_guess(guess)
