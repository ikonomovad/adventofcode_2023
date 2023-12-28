#      0  1  2  3  4  5
# b1: x1 y1 z1 x2 y2 z2
# b2: x1 y1 z1 x2 y2 z2

#   x1   x2
#   -----
#  | b1 |
#  --------
#    | b2 |
#    -----
#    x1   x2


def bricks_overlap(b1, b2):
    x_overlap = (b1[0] <= b2[3]) and (b1[3] >= b2[0])
    y_overlap = (b1[1] <= b2[4]) and (b1[4] >= b2[1])

    return x_overlap and y_overlap


def simulate_brick_fall(snapshot):
    for i, brick in enumerate(snapshot):
        z = 1

        bricks_under = snapshot[:i]

        for brick_under in bricks_under:
            if bricks_overlap(brick_under, brick):
                z = max(z, brick_under[5] + 1)

        brick[5] = z + brick[5] - brick[2]
        brick[2] = z


def find_supporting_bricks(snapshot):
    supported_by = {i: [] for i in range(len(snapshot))}
    supports = {i: [] for i in range(len(snapshot))}

    for i, brick in enumerate(snapshot):
        bricks_under = snapshot[:i]

        for j, brick_under in enumerate(bricks_under):
            if bricks_overlap(brick_under, brick) and brick[2] - 1 == brick_under[5]:
                supported_by[i].append(j)
                supports[j].append(i)

    return supported_by, supports


def find_bricks_safe_to_remove(supported_by, supports):
    safe_to_remove = 0

    for _, supported in supports.items():
        total_brick_supported = len(supported)
        count = 0

        for supported_brick in supported:
            if len(supported_by[supported_brick]) > 1:
                count += 1

        if count == total_brick_supported:
            safe_to_remove += 1

    return safe_to_remove


with open('input.txt') as file:
    snapshot = [list(map(int, el.split(','))) for el in (
        line.replace('~', ',') for line in file.read().split('\n'))]
    snapshot_sorted = sorted(snapshot, key=lambda x: x[2])  # z1 - bottom value

    simulate_brick_fall(snapshot_sorted)

    supported_by, supports = find_supporting_bricks(snapshot_sorted)

    safe_to_remove = find_bricks_safe_to_remove(supported_by, supports)

    print(safe_to_remove)
