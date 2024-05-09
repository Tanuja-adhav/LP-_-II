from heapq import heappush, heappop

def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                for x in range(3):
                    for y in range(3):
                        if goal_state[x][y] == state[i][j]:
                            distance += abs(x - i) + abs(y - j)
                            break
    return distance

def get_neighbors(state):
    neighbors = []
    blank_row, blank_col = next((i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == 0)

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [list(row) for row in state]
            new_state[blank_row][blank_col] = new_state[new_row][new_col]
            new_state[new_row][new_col] = 0
            neighbors.append(new_state)

    return neighbors

def astar(start_state, goal_state):
    open_set = [(manhattan_distance(start_state, goal_state), start_state)]
    closed_set = set()

    while open_set:
        _, current = heappop(open_set)

        if current == goal_state:
            return current

        closed_set.add(tuple(map(tuple, current)))

        for neighbor in get_neighbors(current):
            if tuple(map(tuple, neighbor)) not in closed_set:
                heappush(open_set, (manhattan_distance(neighbor, goal_state), neighbor))

    return None  # No path found

# Example puzzle
start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

path = astar(start_state, goal_state)
if path:
    print("Shortest path found:")
    for row in path:
        print(row)
else:
    print("No path found")
