import heapq

# Manhattan distance (abs between two points)
def decision(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def neighbors_get(node, board):
    x, y = node
    neighbors = []
    size = len(board)

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        # 2 is wall, 3 is enemy, 4 is finish - don't want to hit those
        if 0 <= nx < size and 0 <= ny < size:
            if board[ny][nx] != 2 and board[ny][nx] != 3 and board[ny][nx] != 4:
                neighbors.append((nx, ny))
    return neighbors

def find_player(board):
    size = len(board)
    for y in range(size):
        for x in range(size):
            if board[y][x] == 1:
                return (x, y)
    return False

# Runs the math to check which one gets the closest to the player
def ai(board, x_start, y_start):
    start = (x_start, y_start)
    goal = find_player(board)

    if goal == False:
        return (0, 0)

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {start: 0}
    f_score = {start: decision(start, goal)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()

            if len(path) == 0:
                return (0,0)
            next_step = path[0]

            dx = next_step[0] - start[0]
            dy = next_step[1] - start[1]

            return (dx, dy)

        for neighbor in neighbors_get(current, board):
            possible_g = g_score[current] + 1

            if neighbor not in g_score or possible_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = possible_g
                f_score[neighbor] = possible_g + decision(neighbor, goal)

                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return (0,0)