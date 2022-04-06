game = [
    ".", ".", ".",
    ".", ".", ".",
    ".", ".", "."
]
def showGame():
    print(game[0] + game[1] + game[2])
    print(game[3] + game[4] + game[5])
    print(game[6] + game[7] + game[8])
i = 0
while i < 9:
    if i % 2 == 0:
        next_position = int(input("Position for player 1: "))
        
        if game[next_position - 1] != "x":
            if game[next_position - 1] != "o":
                game[next_position - 1] = "x"   
                showGame()
            else:
                print("Error")     
                break
        else:
            print("Error")     
            break
    else:
        next_position = int(input("Position for player 2: "))
        if game[next_position - 1] != "x":
            if game[next_position - 1] != "o":
                game[next_position - 1] = "o"   4t4
                showGame()
            else:
                print("Error")     
                break
        else:
            print("Error")     
            break

    if game[0] == "x" and game[1] == "x" and game[2] == "x" or game[3] == "x" and game[4] == "x" and game[5] == "x" or game[6] == "x" and game[7] == "x" and game[8] == "x" or game[0] == "x" and game[3] == "x" and game[6] == "x" or game[1] == "x" and game[4] == "x" and game[7] == "x" or game[2] == "x" and game[5] == "x" and game[8] == "x" or game[0] == "x" and game[4] == "x" and game[8] == "x" or game[2] == "x" and game[4] == "x" and game[6] == "x":
        print("you win")
        break

    if game[0] == "o" and game[1] == "o" and game[2] == "o" or game[3] == "o" and game[4] == "o" and game[5] == "o" or game[6] == "o" and game[7] == "o" and game[8] == "o" or game[0] == "o" and game[3] == "o" and game[6] == "o" or game[1] == "o" and game[4] == "o" and game[7] == "o" or game[2] == "o" and game[5] == "o" and game[8] == "o" or game[0] == "o" and game[4] == "o" and game[8] == "o" or game[2] == "o" and game[4] == "o" and game[6] == "o":
        print("you win")
        break

    i += 1
