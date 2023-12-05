# Part 1

with open('input.txt') as file:
    content = file.read()
    content = content.split('\n\n')
    seeds = [int(row) for row in content[0].split(':')[1].strip().split(' ')]
    maps = [row.split('\n')[1:] for row in content[1:]]

    map_ranges = []
    for part in maps:
        row_ranges = []
        for row in part:
            destination, source, range_len = map(int, row.split())
            # store destination and source as ranges
            row_ranges.append(
                [range(destination, (destination + range_len)), range(source, (source + range_len))])
        map_ranges.append(row_ranges)

    # keeping only last category that we are checking so at the end we just have list from locations
    current_category = seeds
    for i in range(0, len(map_ranges)):
        category_values = []
        # if value is in source range, based on the index we can find corresponding destination value
        for value in current_category:
            for map_part in map_ranges[i]:
                value_is_in_range = value in map_part[1]
                if value_is_in_range:
                    break
            if value_is_in_range:
                ind = map_part[1].index(value)
                category_values.append(int(map_part[0][ind]))
            else:
                category_values.append(value)
        current_category = category_values
    print(min(current_category))
