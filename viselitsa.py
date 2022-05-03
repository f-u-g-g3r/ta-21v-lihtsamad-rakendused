import random

words = ["cat", "mathematic", "games", "computer", "elephant", "estonia"]

wordToGuess = random.choice(words)

letters = ["_"] * len(wordToGuess)
print(letters)

