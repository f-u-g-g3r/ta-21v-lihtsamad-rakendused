import random

words = ["cat", "mathematic", "games", "computer", "elephant", "estonia"]

wordToGuess = random.choice(words)

letters = ["_"] * len(wordToGuess)
print(letters)

lives = 5

def drawGameField():
    if(lives == 4):
        print("Г------------")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|            ")
    elif(lives == 3):
        print("Г------------")
        print("|       |    ")
        print("|       O    ")
        print("|            ")
        print("|            ")
        print("|            ")

