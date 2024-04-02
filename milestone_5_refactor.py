import random

class Hangman:
    def __init__(self):
        self.word_list = ["apple", "grapefruit", "orange", "mango", "passionfruit"]
        self.selected_word = random.choice(self.word_list)
        print("Secret word:", self.selected_word)
        self.word_guessed = ['_' for _ in self.selected_word]
        self.remaining_letters = len(set(self.selected_word))
        self.remaining_lives = 5
        self.guesses = []

    def check_guess(self, guess):
        lowercase_guess = guess.lower()
        if guess in self.selected_word:
            print(f"Good guess! '{lowercase_guess}' is in the word.")
            self.update_word_guessed(guess)
        else: 
            print(f"Sorry, '{lowercase_guess}' is not in the word.")
            self.remaining_lives -= 1
            print(f"You have {self.remaining_lives} lives left.")

    def update_word_guessed(self, guess):
        for i, letter in enumerate(self.selected_word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.remaining_letters -= 1

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            lowercase_guess = guess.lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif lowercase_guess in self.guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.guesses.append(lowercase_guess)
                break

def play_game():
    game = Hangman()
    
    while True:
        if game.remaining_lives == 0:
            print('You lost!')
            break
        elif game.remaining_letters == 0:
            print('Congratulations. You won the game!')
            break
        else:
            game.ask_for_input()

play_game()