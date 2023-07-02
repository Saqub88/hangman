import random
fruit_file = open("fruits.txt", 'r')
fruit_raw_text = fruit_file.read()
fruit_cleaned = fruit_raw_text.replace('\n', ' ')
fruits = fruit_cleaned.lower().split()
word = random.choice(fruits)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = list(str(random.choice(self.word_list)))
        self.num_letters = []
        self.list_of_guesses = []
        self.guess = None
    
    def input_guess(self):
        self.guess = input("Please enter a single letter as your guess: ")
        print(self.guess)

    def ask_for_input(self):
        while True:
            if len(self.guess) == 1 and self.guess.isalpha():
                break
            else:
                self.guess = (input("Invalid letter. Please, enter a single alphabetical character."))

    def check_guess(self):
        if self.guess in self.list_of_guesses:
            return print("You have already tried that letter. Please try another letter")
        elif self.guess.lower() in self.word_guessed:
            for x in range(0, len(self.word_guessed)):
                if self.word_guessed[x] == self.guess: self.num_letters[x] = self.guess
            print(self.num_letters)
            self.list_of_guesses.append(str(self.guess))
            return print(f"Good guess! {self.guess} is in the word.")
        else:
            self.num_lives -= 1
            self.list_of_guesses.append(str(self.guess))
            return print(f"Sorry, {self.guess} is not in the word. Try again.")

    def play(self):
        self.num_letters.extend('_' * len(self.word_guessed))
        while self.num_lives > 0 and self.num_letters != self.word_guessed:
            self.input_guess()
            self.ask_for_input()
            self.check_guess()
        if self.num_letters == self.word_guessed: print("nice one geez. you solved it")
        elif self.num_lives == 0: print("Sorry geez. You done goofed")
        else: print("You shouldn't see this statement. If so then something hasnt worked right")

    def __str__(self):
        return f"word_list = {self.word_list} \nnum_lives = {self.num_lives}\nword_guessed = {self.word_guessed}\nnum_letters = {self.num_letters}\nlist_of_guesses = {self.list_of_guesses}\nguess = {self.guess}"
    
play_game = Hangman(fruits)

play_game.play()