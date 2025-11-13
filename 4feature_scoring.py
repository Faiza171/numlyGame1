# Acknowledgement:
# I co-created this code with the help of ChatGPT (OpenAI GPT-5).
# Numly - 3-Digit Number Guessing Game
# Features included:
# 1. Limited guesses (5 attempts)
# 2. Feedback system (P/M/X)
# 3. Scoring system (logic: total = 100 points - (10 * total no. of wrong guess))

import random

class NumlyGame:
    """3-digit number guessing game with limited guesses, feedback, and scoring."""

    def __init__(self):
        # Computer chooses a random 3-digit number between 100 and 999
        self.secret_number = random.randint(100, 999)

    def play(self):
        MAX_ATTEMPTS = 5  # maximum guesses per player
        attempts = 0
        score = 100  # starting score

        print("Welcome to Numly – 3-digit Number Guessing Game!")
        print("Try to guess the number between 100 and 999.")
        print("Type 'exit' anytime to quit the game.\n")
        print("P = perfect in position and number, M = correct number but wrong position, X = number not present\n")

        while True:
            # Prompt player for input
            guess = input(f"Enter your guess (Attempt {attempts + 1}/{MAX_ATTEMPTS}): ")

            # Exit option
            if guess.lower() == "exit":
                print("You quit the game. The number was:", self.secret_number)
                print(f"Your final score: {score}")
                break

            # Validate input
            if not guess.isdigit() or len(guess) != 3:
                print("Please enter a valid 3-digit number.\n")
                attempts += 1  # invalid input counts as an attempt
                if attempts >= MAX_ATTEMPTS:
                    print(f"Maximum attempts reached! The number was: {self.secret_number}")
                    print(f"Your final score: {score}")
                    break
                continue

            guess = int(guess)
            attempts += 1  # count valid attempt
#-------------------------------------
#scoring: start at 100 point, deduct 10 pt if wrong guess
#--------------------------------------------------
           
            if guess != self.secret_number:
                score -= 10
                if score < 0:  # for score to never negative no.
                    score = 0

            # Correct guess
            if guess == self.secret_number:
                print("You guessed it right! You win!")
                print(f"Your final score: {score}")
                break

# -------------------------------
# RUN THE GAME
# -------------------------------
# Create a game instance and start playing
game = NumlyGame()
game.play()