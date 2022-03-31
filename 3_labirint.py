map = [
    [12, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 24]
]

start_pos_x = 0
start_pos_y = 0

if map[start_pos_x][start_pos_y + 1] == 1:
    print("can go right")

if map[start_pos_x + 1][start_pos_y] == 1:
    print("can go bottom")