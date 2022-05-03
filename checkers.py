


field1 = [
    ["0", "3", "0", "3", "0", "3", "0", "3", "8"], #0
    ["3", "0", "3", "0", "3", "0", "3", "0", "7"], #1
    ["0", "3", "0", "3", "0", "3", "0", "3", "6"], #2
    ["1", "0", "1", "0", "1", "0", "1", "0", "5"], #3
    ["0", "1", "0", "1", "0", "1", "0", "1", "4"], #4
    ["2", "0", "2", "0", "2", "0", "2", "0", "3"], #5
    ["0", "2", "0", "2", "0", "2", "0", "2", "2"], #6
    ["2", "0", "2", "0", "2", "0", "2", "0", "1"], #7
    ["a", "b", "c", "d", "e", "f", "g", "h"] #8
    ]

# 0 - cant go / 1 - can go / 2 - white player / 3 - black player

for i in range(0, 9999999999):
    if i % 2 == 0:
        checker_num_position = input("(White player) Choose checker num position: ")
        checker_char_position = input("(White player) Choose checker char position: ")
        
        if checker_num_position == "3" and checker_char_position == "a":
            if field1[5][0] == "2"
        
    else:
        next_position = int(input("Position for black player: "))

