#!/usr/bin/env python3
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def convert_index_to_coord(index):
    return Coord(index % 3, index // 3)
    # if index == 0:
    #     return (0,0)
    # elif index == 1:
    #     return (1, 0)
    # elif index == 2:
    #     return (2, 0)
    # elif index == 3:
    #     return (0, 1)
    # elif index == 4:
    #     return (1, 1)
    # elif index == 5:
    #     return (2, 1)
    # elif index == 6:
    #     return (0, 2)
    # elif index == 7:
    #     return (1, 2)
    # elif index == 8:
    #     return (2, 2)

def convert_coord_to_index(coord):
    return coord.x + (3 * coord.y)

def swap_left(cur_state, index):
    cur_coord = convert_index_to_coord(index)
    if cur_coord.x == 0:
        return None

    new_coord = Coord(cur_coord.x - 1, cur_coord.y)

    new_state = cur_state[:]
    temp = new_state[convert_coord_to_index(cur_coord)]
    new_state[convert_coord_to_index(cur_coord)] = new_state[convert_coord_to_index(new_coord)]
    new_state[convert_coord_to_index(new_coord)] = temp

    return new_state

def swap_right(cur_state, index):
    cur_coord = convert_index_to_coord(index)
    if cur_coord.x == 2:
        return None

    new_coord = Coord(cur_coord.x + 1, cur_coord.y)

    new_state = cur_state[:]
    temp = new_state[convert_coord_to_index(cur_coord)]
    new_state[convert_coord_to_index(cur_coord)] = new_state[convert_coord_to_index(new_coord)]
    new_state[convert_coord_to_index(new_coord)] = temp

    return new_state

def swap_up(cur_state, index):
    cur_coord = convert_index_to_coord(index)
    if cur_coord.y == 0:
        return None

    new_coord = Coord(cur_coord.x, cur_coord.y - 1)

    new_state = cur_state[:]
    temp = new_state[convert_coord_to_index(cur_coord)]
    new_state[convert_coord_to_index(cur_coord)] = new_state[convert_coord_to_index(new_coord)]
    new_state[convert_coord_to_index(new_coord)] = temp

    return new_state

def swap_down(cur_state, index):
    cur_coord = convert_index_to_coord(index)
    if cur_coord.y == 2:
        return None

    new_coord = Coord(cur_coord.x, cur_coord.y + 1)

    new_state = cur_state[:]
    temp = new_state[convert_coord_to_index(cur_coord)]
    new_state[convert_coord_to_index(cur_coord)] = new_state[convert_coord_to_index(new_coord)]
    new_state[convert_coord_to_index(new_coord)] = temp

    return new_state

def get_next_states(cur_state):
    for i in range(len(cur_state)):
        if cur_state[i] == "_":
            blank_index = i
            break

    results = [swap_left(cur_state, blank_index), swap_right(cur_state, blank_index), swap_up(cur_state, blank_index), swap_down(cur_state, blank_index)]

    return results

def print_grid(cur_state):
    for y in range(3):
        for x in range(3):
            print(f"{cur_state[convert_coord_to_index(Coord(x, y))]}", end=" ")
        print("")
    print("")

next_state = get_next_states([1,2,3,4, "_", 5,6,7,8])
for state in next_state:
    if state != None:
        print_grid(state)
