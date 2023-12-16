from collections import deque


def count_energized_tiles(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([start])
    # storing start point of each new path
    infinite_paths = set(start)

    while queue:
        row, col, direction = queue.popleft()
        element = grid[row][col]
        visited.add((row, col))

        # if . just continue
        if element == '.':
            next_row, next_col = move_in_direction(row, col, direction)
            if is_valid(next_row, next_col, rows, cols):
                queue.append((next_row, next_col, direction))

        elif element == '|':
            # two new paths up and down
            if direction in '<>':
                if is_valid(row - 1, col, rows, cols):
                    handle_infinite_paths(
                        queue, infinite_paths, (row - 1, col, '^'))

                if is_valid(row + 1, col, rows, cols):
                    handle_infinite_paths(
                        queue, infinite_paths, (row + 1, col, 'v'))
            else:
                next_row, next_col = move_in_direction(row, col, direction)
                if is_valid(next_row, next_col, rows, cols):
                    queue.append((next_row, next_col, direction))

        elif element == '-':
            # two new paths left and right
            if direction in '^v':
                if is_valid(row, col - 1, rows, cols):
                    handle_infinite_paths(
                        queue, infinite_paths, (row, col - 1, '<'))

                if is_valid(row, col + 1, rows, cols):
                    handle_infinite_paths(
                        queue, infinite_paths, (row, col + 1, '>'))
            else:
                next_row, next_col = move_in_direction(row, col, direction)
                if is_valid(next_row, next_col, rows, cols):
                    queue.append((next_row, next_col, direction))

        elif element in '/\\':
            next_row, next_col, next_direction = reflect_slash(
                row, col, direction) if element == '/' else reflect_backslash(row, col, direction)
            if is_valid(next_row, next_col, rows, cols):
                queue.append(
                    (next_row, next_col, next_direction))

    return len(visited)


def handle_infinite_paths(queue, infinite_paths, starting_pos):
    if starting_pos not in infinite_paths:
        infinite_paths.add(starting_pos)
        queue.append(starting_pos)


def reflect_backslash(row, col, dir):
    reflect = {
        '^': '<',
        'v': '>',
        '<': '^',
        '>': 'v',
    }

    if dir == '^':
        return row, col - 1, reflect[dir]
    elif dir == 'v':
        return row, col + 1, reflect[dir]
    elif dir == '>':
        return row + 1, col, reflect[dir]
    elif dir == '<':
        return row - 1, col, reflect[dir]


def reflect_slash(row, col, dir):
    reflect = {
        '^': '>',
        'v': '<',
        '<': 'v',
        '>': '^',
    }

    if dir == '^':
        return row, col + 1, reflect[dir]
    elif dir == 'v':
        return row, col - 1, reflect[dir]
    elif dir == '>':
        return row - 1, col, reflect[dir]
    elif dir == '<':
        return row + 1, col, reflect[dir]


def is_valid(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def move_in_direction(row, col, dir):
    if dir == '^':
        return row - 1, col
    elif dir == 'v':
        return row + 1, col
    elif dir == '>':
        return row, col + 1
    elif dir == '<':
        return row, col - 1
