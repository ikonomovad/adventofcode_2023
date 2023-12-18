def calc_coordinates(grid):
    x, y = 0, 0
    x_coordinates = [x]
    y_coordinates = [y]
    edges = 0

    for direction, distance in grid:
        distance = int(distance)
        edges += distance

        if direction == 'R':
            x += distance
        elif direction == 'L':
            x -= distance
        elif direction == 'U':
            y -= distance
        elif direction == 'D':
            y += distance

        x_coordinates.append(x)
        y_coordinates.append(y)

    return x_coordinates, y_coordinates, edges


def calculate_area(x_coordinates, y_coordinates, edges):
    # Calculates the area of the lagoon using the Shoelace Formula and adjusts for interior points using Pick's Theorem.
    area = 0

    for i in range(len(x_coordinates) - 1):
        area += x_coordinates[i] * y_coordinates[i + 1] - \
            y_coordinates[i] * x_coordinates[i + 1]
    area += x_coordinates[-1] * y_coordinates[0] - \
        y_coordinates[-1] * x_coordinates[0]

    area = abs(area) / 2
    area += edges / 2 + 1

    return int(area)


def convert_instructions(instructions):
    new_instructions = []
    num_to_dir = {
        '0': 'R',
        '1': 'D',
        '2': 'L',
        '3': 'U'
    }

    for _, _, hexcolor in instructions:
        hexcolor = hexcolor.lstrip('(#').rstrip(')')
        new_direction = num_to_dir[hexcolor[-1]]
        new_distance = int(hexcolor[:-1], 16)
        new_instructions.append([new_direction, new_distance])

    return new_instructions


with open('input.txt') as file:
    dig_plan = [row.split() for row in file.read().split('\n')]
    new_plan = convert_instructions(dig_plan)
    x, y, edges = calc_coordinates(new_plan)
    print(calculate_area(x, y, edges))
