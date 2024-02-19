#!/usr/bin/env python3

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class State:
    def __init__(self, positions, prev_moves):
        self.positions = positions
        self.prev_moves = prev_moves

class Priority_Queue_Node:
    def __init__(self, state, priority):
        self.state = state
        self.priority = priority

class Priority_Queue:
    def __init__(self):
        self.queue = []

    def insert(self, node):
        index = 0

        while index < len(self.queue) and self.queue[index].priority <= node.priority:
            index += 1

        self.queue.insert(index, node)

    def pop(self):
        return self.queue.pop(0).state

    def empty(self):
        return self.queue == []



def convert_index_to_coord(index):
    return Coord(index % 3, index // 3)

def convert_coord_to_index(coord):
    return coord.x + (3 * coord.y)

def swap_tiles(cur_state, cur_coord, new_coord):
    new_state = State(cur_state.positions[:], cur_state.prev_moves[:])

    temp = new_state.positions[convert_coord_to_index(cur_coord)]
    new_state.positions[convert_coord_to_index(cur_coord)] = new_state.positions[convert_coord_to_index(new_coord)]
    new_state.positions[convert_coord_to_index(new_coord)] = temp

    return new_state

def swap_left(cur_state, index):
    cur_coord = convert_index_to_coord(index)
    if cur_coord.x == 0:
        return None

    new_coord = Coord(cur_coord.x - 1, cur_coord.y)

    new_state = swap_tiles(cur_state, cur_coord, new_coord)

    swap_value = cur_state.positions[convert_coord_to_index(new_coord)]
    new_state.prev_moves.append(f"{swap_value}R")

    return new_state


def swap_right(cur_state, index):
    cur_coord = convert_index_to_coord(index)
    if cur_coord.x == 2:
        return None

    new_coord = Coord(cur_coord.x + 1, cur_coord.y)

    new_state = swap_tiles(cur_state, cur_coord, new_coord)

    swap_value = cur_state.positions[convert_coord_to_index(new_coord)]
    new_state.prev_moves.append(f"{swap_value}L")

    return new_state


def swap_up(cur_state, index):
    cur_coord = convert_index_to_coord(index)
    if cur_coord.y == 0:
        return None

    new_coord = Coord(cur_coord.x, cur_coord.y - 1)

    new_state = swap_tiles(cur_state, cur_coord, new_coord)

    swap_value = cur_state.positions[convert_coord_to_index(new_coord)]
    new_state.prev_moves.append(f"{swap_value}D")


    return new_state


def swap_down(cur_state, index):
    cur_coord = convert_index_to_coord(index)
    if cur_coord.y == 2:
        return None

    new_coord = Coord(cur_coord.x, cur_coord.y + 1)

    new_state = swap_tiles(cur_state, cur_coord, new_coord)

    swap_value = cur_state.positions[convert_coord_to_index(new_coord)]
    new_state.prev_moves.append(f"{swap_value}U")

    return new_state


def expand_node(cur_state):
    # global num_expansions
    # num_expansions += 1
    for i in range(len(cur_state.positions)):
        if cur_state.positions[i] == "_":
            blank_index = i
            break

    results = [swap_down(cur_state, blank_index), swap_right(cur_state, blank_index), swap_left(cur_state, blank_index), swap_up(cur_state, blank_index)]

    return results


# Test if the current state is a goal state -> Blank in top left, then numerical order left to right, top to bottom
def test_goal(cur_state):
    goal_state = ["_", "1", "2", "3", "4", "5", "6", "7", "8"]
    if cur_state.positions == goal_state:
        return True

    return False

def dfs(start_state):
    stack = [start_state]
    visited = []

    while stack != []:
        cur_state = stack.pop(0)
        # Don't expand the state if it is None or it has already been visited
        if cur_state != None and cur_state.positions not in visited:
            visited.append(cur_state.positions)

            if test_goal(cur_state):
                return cur_state.prev_moves

            next_states = expand_node(cur_state)
            stack[:0] = next_states

    return None

def bfs(start_state):
    stack = [start_state]
    visited = []

    while stack != []:
        cur_state = stack.pop(0)
        # Don't expand the state if it is None or it has already been visited
        if cur_state != None and cur_state.positions not in visited:
            visited.append(cur_state.positions)

            if test_goal(cur_state):
                return cur_state.prev_moves

            next_states = expand_node(cur_state)
            stack.extend(next_states)

    return None

def ucs(start_state):
    pqueue = Priority_Queue();
    pqueue.insert(Priority_Queue_Node(start_state, 0))
    visited = []

    while not pqueue.empty():
        cur_state = pqueue.pop()

        # Don't expand the state if it is None or it has already been visited
        if cur_state != None and cur_state.positions not in visited:
            visited.append(cur_state.positions)

            if test_goal(cur_state):
                return cur_state.prev_moves

            next_states = expand_node(cur_state)
            for state in next_states:
                if state != None:
                    pqueue.insert(Priority_Queue_Node(state, 1))

    return None

def manhattan_distance(state):
    correct_indexes = {"_": convert_index_to_coord(0), "1": convert_index_to_coord(1), "2": convert_index_to_coord(2), "3": convert_index_to_coord(3), "4": convert_index_to_coord(4), "5": convert_index_to_coord(5), "6": convert_index_to_coord(6), "7": convert_index_to_coord(7), "8": convert_index_to_coord(8)}
    sum = 0

    for i in range(len(state.positions)):
        cur_coord = convert_index_to_coord(i)
        correct_coord = correct_indexes[state.positions[i]]

        sum += (abs(correct_coord.x - cur_coord.x) + abs(correct_coord.y - cur_coord.y))

    return sum


def euclidian_distance(state):
    correct_indexes = {"_": convert_index_to_coord(0), "1": convert_index_to_coord(1), "2": convert_index_to_coord(2), "3": convert_index_to_coord(3), "4": convert_index_to_coord(4), "5": convert_index_to_coord(5), "6": convert_index_to_coord(6), "7": convert_index_to_coord(7), "8": convert_index_to_coord(8)}
    sum = 0

    for i in range(len(state.positions)):
        cur_coord = convert_index_to_coord(i)
        correct_coord = correct_indexes[state.positions[i]]

        sum += (pow(pow((correct_coord.x - cur_coord.x), 2) + pow((correct_coord.y - cur_coord.y), 2), 0.5))

    return sum

def a_star(start_state, heuristic):
    pqueue = Priority_Queue();
    pqueue.insert(Priority_Queue_Node(start_state, 0))
    visited = []

    while not pqueue.empty():
        cur_state = pqueue.pop()

        # Don't expand the state if it is None or it has already been visited
        if cur_state != None and cur_state.positions not in visited:
            visited.append(cur_state.positions)

            if test_goal(cur_state):
                return cur_state.prev_moves

            next_states = expand_node(cur_state)
            for state in next_states:
                if state != None:
                    pqueue.insert(Priority_Queue_Node(state, len(state.prev_moves) + heuristic(state)))

    return None


def print_grid(cur_state):
    for y in range(3):
        for x in range(3):
            print(f"{cur_state.positions[convert_coord_to_index(Coord(x, y))]}", end=" ")
        print("")
    print(f"{cur_state.prev_moves}\n")



if __name__ == '__main__':
    # global num_expansions

    input = open("input.txt", "r")
    start_state = input.read().strip().split(",")
    start_state = State(start_state, [])

    # num_expansions = 0
    print("The solution of Q1.1a is:")
    print(",".join(dfs(start_state)))
    # print(f"{num_expansions}")
    print("")

    # num_expansions = 0
    print("The solution of Q1.1b is:")
    print(",".join(bfs(start_state)))
    # print(f"{num_expansions}")
    print("")

    # num_expansions = 0
    print("The solution of Q1.1c is:")
    print(",".join(ucs(start_state)))
    # print(f"{num_expansions}")
    print("")

    # num_expansions = 0
    print("The solution of Q1.1d is:")
    print(",".join(a_star(start_state, manhattan_distance)))
    # print(f"{num_expansions}")
    print("")

    # num_expansions = 0
    print("The solution of Q1.1e is:")
    print(",".join(a_star(start_state, euclidian_distance)))
    # print(f"{num_expansions}")
    print("")
