map = [
    [12, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 24]
]

start_pos_x = 0
start_pos_y = 0
def get_next_free_position():
    if map[start_pos_x][start_pos_y + 1] == 1:
        print("can go right")
        return [start_pos_y, start_pos_x + 1]

    if map[start_pos_x + 1][start_pos_y] == 1:
        print("can go bottom")
        return [start_pos_y + 1, start_pos_x]

next_free_position = get_next_free_position()
print("Next free position is: ", next_free_position)