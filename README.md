# Numly – 3-Digit Number Guessing Game

## Credits
Co-created with the help of ChatGPT (OpenAI GPT-5).  
All Git branching (feature branches), merging, commits, and upload to GitHub were done manually as part of my learning process.
Initial prototyping and testing was done in Jupyter Notebook before moving to local Git branches.


## Description
Numly is a simple text-based number guessing game inspired by Wordle. 
Players try to guess a random 3-digit number. The game provides feedback for each guess and tracks the score. It includes both single-player and two-player modes (two-player is in a separate branch).

---

## Features

### Single-Player Mode (Master branch)
- Random 3-digit number (100–999)  
- Limited guesses: 5 attempts  
- Feedback system:  
  - **P** = correct number in correct position  
  - **M** = correct number but wrong position  
  - **X** = number not present  
- Scoring system: starts at 100, minus 10 points per wrong guess  
- Exit anytime by typing `exit`  

### Two-Player Mode (two-player branch)
- Alternating turns between Player 1 and Player 2  
- Each player has 5 attempts  
- Feedback and scoring per player  
- Winner determined by higher score or correct guess  

---

## How I Built This Project
1. **Logic and testing** were first done in **Jupyter Notebook** to verify input handling, feedback system, limited guesses, and scoring.  
2. Then I moved the code to a **local Git repository** (`numly3`) and created feature branches for each addition:  
   - Base game  
   - Limited guesses  
   - Feedback system  
   - Scoring system  
   - Two-player mode  
3. Finally, I **pushed the repository to GitHub**, keeping the master branch for single-player features(basic+other features except 2player) and the two-player mode in a separate branch.  

---