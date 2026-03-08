import heapq

# Manhattan distance heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(node, board):
    x, y = node
    neighbors = []

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 10 and 0 <= ny < 10:
            # 0 = empty
            # 1 = player
            # 2 = obstacle
            # 3 = enemy
            if board[ny][nx] != 2 and board[ny][nx] != 3:
                neighbors.append((nx, ny))

    return neighbors


def find_player(board):
    for y in range(10):
        for x in range(10):
            if board[y][x] == 1:
                return (x, y)
    return None


def ai(board, startx, starty):

    start = (startx, starty)
    goal = find_player(board)

    if goal is None:
        return (0, 0)

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

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

        for neighbor in get_neighbors(current, board):

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return (0,0)