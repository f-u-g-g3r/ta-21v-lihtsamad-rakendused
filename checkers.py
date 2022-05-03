


from distutils.command.build_scripts import first_line_re
from tabnanny import check


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

#def chooseIndex(checker_num_position, checker_char_position):


#def nextPositionWhite():
    
def checkFirstIndex(checker_num_position):
    while True:
        if checker_num_position == "1":
            firstIndex = 7
            return firstIndex
        elif checker_num_position == "2":
            firstIndex = 6
            return firstIndex
        elif checker_num_position == "3":
            firstIndex = 5
            return firstIndex
        elif checker_num_position == "4":
            firstIndex = 4
            return firstIndex
        elif checker_num_position == "5":
            firstIndex = 3
            return firstIndex
        elif checker_num_position == "6":
            firstIndex = 2
            return firstIndex
        elif checker_num_position == "7":
            firstIndex = 1
            return firstIndex
        elif checker_num_position == "8":
            firstIndex = 0
            return firstIndex
        else:
            print("Wrong checker_num_position")
            break

def checkSecondIndex(checker_char_position):
    while True:
        if checker_char_position == "a":
            secondIndex = 0
            return secondIndex
        elif checker_char_position == "b":
            secondIndex = 1
            return secondIndex
        elif checker_char_position == "c":
            secondIndex = 2
            return secondIndex
        elif checker_char_position == "d":
            secondIndex = 3
            return secondIndex
        elif checker_char_position == "e":
            secondIndex = 4
            return secondIndex
        elif checker_char_position == "f":
            secondIndex = 5
            return secondIndex
        elif checker_char_position == "g":
            secondIndex = 6
            return secondIndex
        elif checker_char_position == "h":
            secondIndex = 7
            return secondIndex
        else:
            print("Wrong checker_char_position")
            break

def checkNewFirstIndex(next_checker_num):
    while True:
        if next_checker_num == "1":
            firstIndex = 7
            return firstIndex
        elif next_checker_num == "2":
            firstIndex = 6
            return firstIndex
        elif next_checker_num == "3":
            firstIndex = 5
            return firstIndex
        elif next_checker_num == "4":
            firstIndex = 4
            return firstIndex
        elif next_checker_num == "5":
            firstIndex = 3
            return firstIndex
        elif next_checker_num == "6":
            firstIndex = 2
            return firstIndex
        elif next_checker_num == "7":
            firstIndex = 1
            return firstIndex
        elif next_checker_num == "8":
            firstIndex = 0
            return firstIndex
        else:
            print("Wrong checker_num_position")
            break

def checkNewSecondIndex(next_checker_char):
    while True:
        if next_checker_char == "a":
            new_secondIndex = 0
            return new_secondIndex
        elif next_checker_char == "b":
            new_secondIndex = 1
            return new_secondIndex
        elif next_checker_char == "c":
            new_secondIndex = 2
            return new_secondIndex
        elif next_checker_char == "d":
            new_secondIndex = 3
            return new_secondIndex
        elif next_checker_char == "e":
            new_secondIndex = 4
            return new_secondIndex
        elif next_checker_char == "f":
            new_secondIndex = 5
            return new_secondIndex
        elif next_checker_char == "g":
            new_secondIndex = 6
            return new_secondIndex
        elif next_checker_char == "h":
            new_secondIndex = 7
            return new_secondIndex
        else:
            print("Wrong checker_char_position")
            break

def checkCanGoNext():
    if field1[checkFirstIndex(checker_num_position)][checkSecondIndex(checker_char_position)] == " W ":
        old_check_index_1 = [checkFirstIndex(checker_num_position)]
        old_check_index_2 = [checkSecondIndex(checker_char_position)]
        print(old_check_index_1, old_check_index_2)

        next_checker_num = input("(White player) Choose next checker num position: ")
        next_checker_char = input("(White player) Choose next checker char position: ")

        if field1[checkFirstIndex(next_checker_num)][checkSecondIndex(next_checker_char)] == " + ":
            new_check_index_1 = [checkFirstIndex(checker_num_position)]
            new_check_index_2 = [checkSecondIndex(checker_char_position)]
            print(new_check_index_1, new_check_index_2)
while True:
    for i in range(0, 999999999):
        if i % 2 == 0:
            checker_num_position = input("(White player) Choose checker num position: ")
            checker_char_position = input("(White player) Choose checker char position: ")
            checkCanGoNext()
            
        else:
            next_position = int(input("Position for black player: "))



# if field1[checkFirstIndex(checker_num_position)][checkSecondIndex(checker_char_position)] == " W ":
            #     checkerIndex = [checkFirstIndex(checker_num_position)] + [checkSecondIndex(checker_char_position)]
            #     print(checkerIndex)
            #     checker_num_position = input("(White player) Choose next checker num position: ")
            #     checker_char_position = input("(White player) Choose next checker char position: ")
            #     if field1[checkFirstIndex(checker_num_position)][checkSecondIndex(checker_char_position)] == " + ":
            #         newCheckerIndex = [checkFirstIndex(checker_num_position)] + [checkSecondIndex(checker_char_position)]
            #         newCheckerIndex[0] += 1 
            #         newCheckerIndex[1] -= 1
            #         if newCheckerIndex == checkerIndex:
            #             field1[checkerIndex] = " + "
            #             field1[newCheckerIndex] = " W "
                        
            #             showField()
                    
                #if next_num_position[checkFirstIndex(nex)]