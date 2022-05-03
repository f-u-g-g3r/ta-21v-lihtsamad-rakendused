import random

words = ["cat", "mathematic", "games", "computer", "elephant", "estonia"]

wordToGuess = random.choice(words)

numLetters = len(words)
print(numLetters)
letters = []
letters.append("_" * numLetters)

lives = 8

def drawGameField():
    if(lives == 7):
        print("Г------------")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|            ")
    elif(lives == 6):
        print("Г------------")
        print("|       |    ")
        print("|       O    ")
        print("|            ")
        print("|            ")
        print("|            ")
    elif(lives == 5):
        print("Г------------")
        print("|       |    ")
        print("|       O    ")
        print("|       |    ")
        print("|            ")
        print("|            ")
    elif(lives == 4):
        print("Г------------")
        print("|       |    ")
        print("|       O    ")
        print("|       |\   ")
        print("|            ")
        print("|            ")
    elif(lives == 3):
        print("Г------------")
        print("|       |    ")
        print("|       O    ")
        print("|      /|\   ")
        print("|            ")
        print("|            ")
    elif(lives == 2):
        print("Г------------")
        print("|       |    ")
        print("|       O    ")
        print("|      /|\   ")
        print("|      /     ")
        print("|            ")
    elif(lives == 1):
        print("Г------------")
        print("|       |    ")
        print("|       O    ")
        print("|      /|\   ")
        print("|      / \   ")
        print("|            ")
    elif(lives == 0):
        print("Г------------")
        print("|            ")
        print("|  YOU DIED  ")
        print("|            ")
        print("|      0     ") #grave
        print("|     /X\    ")
