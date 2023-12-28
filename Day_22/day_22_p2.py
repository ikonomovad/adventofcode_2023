from collections import deque

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


def find_bricks_not_safe_to_remove(supported_by, supports):
    not_safe_to_remove = []

    for brick, supported in supports.items():
        total_brick_supported = len(supported)
        count = 0

        for supported_brick in supported:
            if len(supported_by[supported_brick]) > 1:
                count += 1

        if count != total_brick_supported:
            not_safe_to_remove.append(brick)

    return not_safe_to_remove


def count_all_falling(bricks):
    count_total_falling_bricks = 0

    # For each brick (a) that is not safe to remove (other bricks fall)
    # we should check bricks that this brick is supporting (b, c);
    # If all bricks that are supporting the brick (b) are falling that
    # means brick (b) is also falling;
    # Continue and check bricks that this brick is supporting and so on...

    for i in bricks:
        queue = deque([i])
        falling_bricks = set()

        while queue:
            brick = queue.popleft()
            falling_bricks.add(brick)

            for j in supports[brick]:
                if all(b in falling_bricks for b in supported_by[j]):
                    queue.append(j)

        count_total_falling_bricks += len(falling_bricks) - 1

    return count_total_falling_bricks


with open('input.txt') as file:
    snapshot = [list(map(int, el.split(','))) for el in (
        line.replace('~', ',') for line in file.read().split('\n'))]
    snapshot_sorted = sorted(snapshot, key=lambda x: x[2])  # z1 - bottom value

    simulate_brick_fall(snapshot_sorted)

    supported_by, supports = find_supporting_bricks(snapshot_sorted)

    not_safe_to_remove = find_bricks_not_safe_to_remove(supported_by, supports)

    total_falling = count_all_falling(not_safe_to_remove)

    print(total_falling)
