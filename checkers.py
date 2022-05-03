


field1 = [
    [" - ", " B ", " - ", " B ", " - ", " B ", " - ", " B ", " 8 "], #0
    [" B ", " - ", " B ", " - ", " B ", " - ", " B ", " - ", " 7 "], #1
    [" - ", " B ", " - ", " B ", " - ", " B ", " - ", " B ", " 6 "], #2
    [" + ", " - ", " + ", " - ", " + ", " - ", " + ", " - ", " 5 "], #3
    [" - ", " + ", " - ", " + ", " - ", " + ", " - ", " + ", " 4 "], #4
    [" W ", " - ", " W ", " - ", " W ", " - ", " W ", " - ", " 3 "], #5
    [" - ", " W ", " - ", " W ", " - ", " W ", " - ", " W ", " 2 "], #6
    [" W ", " - ", " W ", " - ", " W ", " - ", " W ", " - ", " 1 "], #7
    [" a ", " b ", " c ", " d ", " e ", " f ", " g ", " h "] #8
    ]

def showField():
    print(field1[0][0] + field1[0][1] + field1[0][2] + field1[0][3] + field1[0][4] + field1[0][5] + field1[0][6] + field1[0][7] + field1[0][8])
    print(field1[1][0] + field1[1][1] + field1[1][2] + field1[1][3] + field1[1][4] + field1[1][5] + field1[1][6] + field1[1][7] + field1[1][8])
    print(field1[2][0] + field1[2][1] + field1[2][2] + field1[2][3] + field1[2][4] + field1[2][5] + field1[2][6] + field1[2][7] + field1[2][8])
    print(field1[3][0] + field1[3][1] + field1[3][2] + field1[3][3] + field1[3][4] + field1[3][5] + field1[3][6] + field1[3][7] + field1[3][8])
    print(field1[4][0] + field1[4][1] + field1[4][2] + field1[4][3] + field1[4][4] + field1[4][5] + field1[4][6] + field1[4][7] + field1[4][8])
    print(field1[5][0] + field1[5][1] + field1[5][2] + field1[5][3] + field1[5][4] + field1[5][5] + field1[5][6] + field1[5][7] + field1[5][8])
    print(field1[6][0] + field1[6][1] + field1[6][2] + field1[6][3] + field1[6][4] + field1[6][5] + field1[6][6] + field1[6][7] + field1[6][8])
    print(field1[7][0] + field1[7][1] + field1[7][2] + field1[7][3] + field1[7][4] + field1[7][5] + field1[7][6] + field1[7][7] + field1[7][8])
    print(field1[8][0] + field1[8][1] + field1[8][2] + field1[8][3] + field1[8][4] + field1[8][5] + field1[8][6] + field1[8][7])
# 0 - cant go / 1 - can go / 2 - white player / 3 - black player

for i in range(0, 9999999999):
    if i % 2 == 0:
        checker_num_position = input("(White player) Choose checker num position: ")
        checker_char_position = input("(White player) Choose checker char position: ")
        
        if checker_num_position == "3" and checker_char_position == "a":
            if field1[5][0] == "W":
                next_num_position = input("(White player) Choose next checker num position: ")
                next_char_position = input("(White player) Choose next checker char position: ")
            else:
                print("You typed wrong!")

        
    else:
        next_position = int(input("Position for black player: "))

