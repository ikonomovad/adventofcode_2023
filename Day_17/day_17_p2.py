import heapq

# Dijkstra's algorithm implementation


def find_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    end = (rows - 1, cols - 1)
    allowed_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    # heat loss, row, col, direction row, direction col, steps count
    priority_queue = [(0, 0, 0, 0, 0, 0)]

    while priority_queue:
        heat_loss, row, col, dir_row, dir_col, steps_count = heapq.heappop(
            priority_queue)

        if (row, col) == end:
            return heat_loss

        if (row, col, dir_row, dir_col, steps_count) not in visited:
            # excluding the heat loss value allows the algorithm to consider multiple paths to a state
            visited.add((row, col, dir_row, dir_col, steps_count))

            # if we are at the start or if we have 4 steps min in same line we can go in other direction
            if (row, col) == (0, 0) or steps_count >= 4:
                for next_dir_row, next_dir_col in allowed_directions:
                    if (dir_row, dir_col) != (next_dir_row, next_dir_col) and (-dir_row, -dir_col) != (next_dir_row, next_dir_col):
                        next_row = row + next_dir_row
                        next_col = col + next_dir_col

                        if 0 <= next_row < rows and 0 <= next_col < cols:  # check if valid row, col
                            next_heat_loss = heat_loss + \
                                grid[next_row][next_col]
                            next_steps_count = 1  # reset

                            heapq.heappush(priority_queue, (next_heat_loss, next_row, next_col,
                                                            next_dir_row, next_dir_col, next_steps_count))

            # other option is to keep going in the same direction until we have 10 steps max in line
            if (row, col) != (0, 0):
                if steps_count < 10:
                    next_row = row + dir_row
                    next_col = col + dir_col

                    if 0 <= next_row < rows and 0 <= next_col < cols:  # check if valid row, col
                        next_heat_loss = heat_loss + grid[next_row][next_col]
                        next_steps_count = steps_count + 1  # continue

                        heapq.heappush(priority_queue, (next_heat_loss, next_row, next_col,
                                                        dir_row, dir_col, next_steps_count))


with open('input.txt') as file:
    grid = [list(map(int, row)) for row in file.read().split('\n')]

    print(find_path(grid))
