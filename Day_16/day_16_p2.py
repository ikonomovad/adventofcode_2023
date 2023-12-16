from tile_counter import count_energized_tiles

with open('input.txt') as file:
    grid = [list(map(str, row)) for row in file.read().split('\n')]
    energized_tiles = set()

    print('Processing ...')
    for i in range(len(grid[0])):
        energized_tiles.add(count_energized_tiles(grid, (0, i, 'v')))
        energized_tiles.add(count_energized_tiles(
            grid, (len(grid) - 1, i, '^')))
    print('Top and bottom row checked!')

    print('Processing ...')
    for i in range(len(grid)):
        energized_tiles.add(count_energized_tiles(grid, (i, 0, '>')))
        energized_tiles.add(count_energized_tiles(
            grid, (i, len(grid[0]) - 1, '<')))
    print('Left and right columns checked!')

    print(max(energized_tiles))
