game = [
    ".", ".", ".",
    ".", ".", ".",
    ".", ".", "."
]
def showGame():
    print(game[0] + game[1] + game[2])
    print(game[3] + game[4] + game[5])
    print(game[6] + game[7] + game[8])
i = 1
while i < 10:
    if i % 2 != 0:
        next_position = int(input("Type what position: "))
        game[next_position - 1] = "x"
        showGame()
    else:
        next_position = int(input("Type what position: "))
        game[next_position - 1] = "o"
        showGame()
    i += 1
        

