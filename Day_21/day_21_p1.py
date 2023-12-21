from collections import deque
from copy import deepcopy


def find_start_pos(grid):
    start = ()
    for i, row in enumerate(grid):
        if 'S' in row:
            col_ind = row.index('S')
            start = (i, col_ind)
            break

    return start


def bfs(start, grid, steps):
    rows = len(grid)
    cols = len(grid[0])
    new_queue = deque([(start[0], start[1])])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while steps > 0:
        queue = deepcopy(new_queue)
        visited = set(deepcopy(new_queue))
        new_queue = deque()

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_col = col + dc
                new_row = row + dr

                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#' and (new_row, new_col) not in visited:
                    new_queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

        steps -= 1

    return len(new_queue)


with open('input.txt') as file:
    grid = [list(row) for row in file.read().split('\n')]
    start = find_start_pos(grid)
    result = bfs(start, grid, 64)
    print(result)
