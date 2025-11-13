# Acknowledgement:
# I co-created this code with the help of ChatGPT (OpenAI GPT-5).
# Numly - 3-Digit Number Guessing Game
# This game is inspired by Wordle, with some interesting added features.
# added feature 1: 5 attempt allowed only

import random  # to generate a random number

class NumlyGame:
    """A simple 3-digit number guessing game with limited guesses."""

    def __init__(self):
        # computer chooses a random 3-digit number between 100 and 999
        self.secret_number = random.randint(100, 999)

    def play(self):
        MAX_ATTEMPTS = 5  # maximum guesses per player
        attempts = 0

        print("Welcome to Numly – 3-digit Number Guessing Game!")
        print("Try to guess the number between 100 and 999.")
        print("Type 'exit' anytime to quit the game.\n")

        # loop until player guesses correctly or reaches max attempts
        while True:
            guess = input(f"Enter your guess (Attempt {attempts + 1}/{MAX_ATTEMPTS}): ")

            # check if player wants to exit
            if guess.lower() == "exit":
                print("You quit the game. The number was:", self.secret_number)
                break

            # check if input is a number and has 3 digits
            if not guess.isdigit() or len(guess) != 3:
                print("Please enter a valid 3-digit number.\n")
                attempts += 1  # count invalid input as attempt
                if attempts >= MAX_ATTEMPTS:
                    print(f"Maximum attempts reached! The number was: {self.secret_number}")
                    break
                continue

            # convert guess to integer
            guess = int(guess)
            attempts += 1

            # check if guess matches the secret number
            if guess == self.secret_number:
                print(" You guessed it right! You win!")
                break
            else:
                print("❌ Wrong guess! Try again.\n")
                if attempts >= MAX_ATTEMPTS:
                    print(f"Maximum attempts reached! The number was: {self.secret_number}")
                    break

# this part runs the game when the file is executed
if __name__ == "__main__":
    game = NumlyGame()
    game.play()
