from collections import deque


def find_start_position(grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 'S':
                return (i, j)


def find_path(start, grid, directions, mapping, opposites, rows, cols):
    stack = deque([start])
    visited = [start]

    while stack:
        x, y = stack.popleft()
        all_directions = mapping.get(grid[x][y])

        for next_direction in all_directions:
            next_x, next_y = x + \
                directions[next_direction][0], y + \
                directions[next_direction][1]

            if 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] != '.' and opposites.get(next_direction) in mapping.get(grid[next_x][next_y]):
                if (next_x, next_y) not in visited:
                    visited.append((next_x, next_y))
                    stack.append((next_x, next_y))
                    break

    return visited


with open('input.txt') as file:
    grid = [list(row) for row in file.read().split('\n')]

    #      N^
    #  W<     E>
    #     Sv

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1)
    }

    mapping = {
        '|': 'v^',  # S N
        '-': '<>',  # W E
        'L': '>^',  # E N
        'J': '<^',  # W N
        '7': 'v<',  # S W
        'F': 'v>',  # S E
        'S': 'v^<>'
    }

    opposites = {
        'v': '^',
        '^': 'v',
        '<': '>',
        '>': '<',
    }

    start = find_start_position(grid)
    rows = len(grid)
    cols = len(grid[0])
    steps = int(len(find_path(start, grid, directions,
                mapping, opposites, rows, cols))/2)

    print(steps)
