from tile_counter import count_energized_tiles

with open('input.txt') as file:
    grid = [list(map(str, row)) for row in file.read().split('\n')]
    start = (0, 0, '>')

    print(count_energized_tiles(grid, start))
