# Credit for the solution https://youtu.be/NTLYL7Mg2jU?si=4qapaP5_iY3NN31Z

with open('input.txt') as file:
    grid = file.read().split('\n')
    start = (0, grid[0].index('.'))
    rows = len(grid)
    cols = len(grid[0])
    end = (rows - 1, grid[rows - 1].index('.'))

    points = [start, end]

    for i, row in enumerate(grid):
        for j, col in enumerate(grid[i]):
            if col != '#':
                neighbors_count = 0
                neighbors = [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1),
                ]

                for r, c in neighbors:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#':
                        neighbors_count += 1

                if neighbors_count >= 3:
                    points.append((i, j))

    directions = {
        "^": [(-1, 0)],
        "v": [(1, 0)],
        "<": [(0, -1)],
        ">": [(0, 1)],
        ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    }

    graph = {point: {} for point in points}

    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()

            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in directions[grid[r][c]]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) not in seen:
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))

    seen = set()

    def dfs(point):
        if point == end:
            return 0

        max_length = -float("inf")  # if we don't find path

        seen.add(point)

        for nx in graph[point]:
            if nx not in seen:
                max_length = max(max_length, dfs(nx) + graph[point][nx])

        seen.remove(point)

        return max_length

    print(dfs(start))
