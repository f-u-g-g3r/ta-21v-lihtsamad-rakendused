import random

words = ["cat", "mathematic", "games", "computer", "elephant", "estonia", "dogs", "apple", "money", "rat", "dinosaur", "logic", "shark", "banana", "monkey"] 

word_to_guess = random.choice(words)

word_length = 0
for i in word_to_guess:
    word_length += 1

letters = ["_"] * word_length
lives = 8
print(letters)


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
    drawGameField()

    if lives == 0:
        print("You lost all your lives, game over!")
        break

    try:
        try_index = int(input("Enter a letter position you want to guess: "))
    except:
        print("You have to type a number")
        continue

    if try_index > word_length:
        print("Out of range")
        continue

    try_letter = input("Enter a letter: ")

    if try_letter in word_to_guess[try_index - 1]:
        letters[try_index - 1] = try_letter
        print(letters)
    else:
        lives -= 1
        print("Wrong letter")
        print(letters)

if "_" not in letters:
    print("You won!")


