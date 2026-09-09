# Text-Based-Hangman-Game-
A simple, text-based Hangman game built in Python. Test your vocabulary and  guessing skills by uncovering the hidden word — one letter at a time!


---

```markdown
# 🎮 Text-Based Hangman Game (Python)

A simple, lightweight, and interactive terminal-based **Hangman Game** built with pure Python. 

Guess the hidden word one letter at a time before you run out of attempts!

---

## 📌 Features

- **Pure Python:** Uses only built-in modules (`random`), no external libraries/dependencies required.
- **Input Validation:** 
  - Prevents invalid inputs (symbols, numbers, multiple characters).
  - Warns you if you repeat an already guessed letter without penalizing lives.
- **Dynamic Display:** Shows hidden letters as `_` and reveals them as you guess correctly.
- **Replayability:** Option to play multiple rounds back-to-back without restarting the script.

---

## 🕹️ Game Rules

1. A random word is chosen from a predefined list.
2. You start with **6 incorrect guesses** (lives).
3. With each turn, guess **one letter**:
   - **Correct guess:** The letter is revealed in its position(s).
   - **Incorrect guess:** You lose 1 life.
4. **Win Condition:** Reveal all letters in the word before running out of lives.
5. **Lose Condition:** Make 6 incorrect guesses.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed on your computer.

Check your Python version:
```bash
python --version
# or
python3 --version
```

### Installation & Running the Game

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/hangman-python.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd hangman-python
   ```

3. **Run the script:**
   ```bash
   python hangman.py
   # or
   python3 hangman.py
   ```

---

## 🖥️ Gameplay Preview

```text
Welcome to Hangman!
You can make 6 incorrect guesses.

Word: _ _ _ _ _ _
Guessed letters: None
Incorrect guesses left: 6
Guess a letter: p

Good guess!

Word: p _ _ _ _ _
Guessed letters: p
Incorrect guesses left: 6
Guess a letter: e

That letter is not in the word.

Word: p _ _ _ _ _
Guessed letters: p, e
Incorrect guesses left: 5
Guess a letter: 
```

---

## ⚙️ Customization

You can easily customize the game by modifying the constants at the top of the `hangman.py` file:

```python
# Add more words to the list
WORDS = ["python", "planet", "garden", "puzzle", "window", "banana", "rocket", "circus", "silver", "orange"]

# Change the difficulty by altering max attempts
MAX_INCORRECT_GUESSES = 6
```

---

## 🛠️ Built With

- **Python 3**
- Standard Library: `random`

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE). Feel free to use and modify it!
```
