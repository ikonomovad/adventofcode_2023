from bisect import bisect

with open('input.txt') as file:
    grid = file.read().split('\n')

    cols_to_expand = []
    rows_to_expand = []

    for i in range(len(grid[0])):
        column = [grid[j][i] for j in range(len(grid))]

        if column.count('.') == len(column):
            cols_to_expand.append(i)

    for i, row in enumerate(grid):
        if row.count('.') == len(row):
            rows_to_expand.append(i)

    galaxy_map = []
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == '#':
                galaxy_map.append((i + (bisect(rows_to_expand, i)),
                                   j + (bisect(cols_to_expand, j))))

    pairs = []
    # finding existing pairs
    for i in range(len(galaxy_map)):
        for j in range(i + 1, len(galaxy_map)):
            pairs.append([galaxy_map[i], galaxy_map[j]])

    steps_between = []
    for pair in pairs:
        i = pair[0]
        j = pair[1]

        steps_between.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))

    print(sum(steps_between))
