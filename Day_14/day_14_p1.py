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


with open('input.txt') as grid:
    grid = transpose()
    tilt()
    grid = transpose()
    total_load = load()

    print(total_load)
