
# Credit for the solution goes to the explanation in this video: https://youtu.be/WCVOBKUNc38?si=MMz5uyqNXd719f3K

def transpose():
    global grid

    return [''.join(row) for row in zip(*grid)]


def tilt():
    global grid

    for i, row in enumerate(grid):
        splitted_row = row.split('#')
        sorted_groups = []

        for group in splitted_row:
            sort_elements = "".join(sorted(list(group), reverse=True))
            sorted_groups.append(sort_elements)

        grid[i] = '#'.join(sorted_groups)


def load():
    global grid

    total_load = 0

    for i, row in enumerate(grid[::-1]):
        total_load += (i + 1) * row.count('O')

    return total_load


def rotate():
    global grid

    grid = tuple(row[::-1] for row in grid)


def cycle():
    # one complete cycle

    global grid

    # one tilt in each of the four directions.
    for _ in range(4):
        # transposes the grid, tilts the platform, and then rotates the grid
        grid = transpose()
        tilt()
        rotate()


with open('input.txt') as file:
    grid = tuple(file.read().split('\n'))
    seen = set(grid)  # to check for repetition
    array = [grid]  # stored configurations

    i = 0

    # iterate through cycles until we detect a repeated configuration
    while True:
        i += 1
        cycle()

        if grid in seen:
            break
        seen.add(grid)
        array.append(grid)

    # once a repeated configuration is detected, we get the starting index
    first = array.index(grid)
    grid = array[(1000000000 - first) % (i - first) + first]

    total_load = load()
    print(total_load)
