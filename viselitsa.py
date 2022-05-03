import random

words = ["cat"] #"mathematic", "games", "computer", "elephant", "estonia"

word_to_guess = random.choice(words)

word_length = 0
for i in word_to_guess:
    word_length += 1

letters = ["_"] * word_length
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


while("_" in letters):
    print(letters)
    drawGameField()
    try_index = int(input("Enter an index for a letter: "))
    if try_index > word_length:
        print("Out of range")
    try_letter = input("Enter a letter: ")
    if try_letter in word_to_guess[try_index]:
        print("1")



