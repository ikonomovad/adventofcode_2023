import re
from itertools import combinations


def line_intersection(line1, line2):
    # Code from: https://stackoverflow.com/a/20677983

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)

    if div == 0:
        raise Exception('Lines do not intersect.')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return x, y


def is_inside_test_area(point):
    x, y = point
    min = 200000000000000
    max = 400000000000000

    return min <= x <= max and min <= y <= max


def check_intersection_future(line1, line2, point):
    # Solved thanks to comments on Reddit:
    # https://www.reddit.com/r/adventofcode/comments/18pnycy/2023_day_24_solutions/?utm_source=share&utm_medium=web2x&context=3
    # *** signs of velocity and delta must be same if in future ***

    x1, y1, _, vx1, vy1, _ = line1
    x2, y2, _, vx2, vy2, _ = line2
    x, y = point

    dx1 = x - x1
    dy1 = y - y1

    future_condition1 = (dx1 > 0) == (vx1 > 0) and (dy1 > 0) == (vy1 > 0)

    dx2 = x - x2
    dy2 = y - y2

    future_condition2 = (dx2 > 0) == (vx2 > 0) and (dy2 > 0) == (vy2 > 0)

    return future_condition1 and future_condition2


with open('input.txt') as file:
    lines = [list(map(int, re.findall(r'-?\d+', line.replace(' @ ', ', '))))
             for line in file.read().split('\n')]

    splitted = []

    for line in lines:
        x, y, z, vx, vy, vz = line
        splitted.append([(x, y, z), (x + vx, y + vy, z + vz), (vx, vy, vz)])

    inside = 0
    line_combinations = list(combinations(splitted, 2))

    for line in line_combinations:
        try:
            point = line_intersection(line[0][:2], line[1][:2])
            if is_inside_test_area(point) and check_intersection_future(list(line[0][0] + line[0][2]), list(line[1][0] + line[1][2]), point):
                inside += 1
        except Exception as e:
            continue

    print(inside)
