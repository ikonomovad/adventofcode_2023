# Part 2
import re


def is_star(char):
    return char == '*'


with open('input.txt') as file:
    star_touches_numbers = {}
    lines = [line.strip() for line in file]

    # initialize empty dictionary for each row
    for i, _ in enumerate(lines):
        star_touches_numbers[i] = {}

    for row_num, line in enumerate(lines):
        # find all numbers in current row and check if there are rows up and down
        numbers = re.finditer(r'\d+', line)
        row_up = row_num != 0
        row_down = row_num < len(lines) - 1
        for number in numbers:
            # for each number we should check all positions around the number (row up, down and current row)
            start_pos = number.start()
            if start_pos > 0:
                start_pos -= 1
            end_pos = number.end()
            if end_pos != len(line):
                end_pos += 1
            # creating a range for all positions that need to be check in row up and down
            all_pos = range(start_pos, end_pos)
            """
            For each position around the number check if at any position there is a star
            and if it is, add this number in corresponding row and column in star_touches_numbers dictionary
            """
            # check if number touches stars in current row
            if is_star(line[start_pos]):
                star_touches_numbers[row_num].setdefault(
                    start_pos, []).append(int(number.group()))
            if is_star(line[end_pos - 1]):
                star_touches_numbers[row_num].setdefault(
                    end_pos - 1, []).append(int(number.group()))
            # check if number touches stars in row up
            if row_up:
                for pos in all_pos:
                    if is_star(lines[row_num - 1][pos]):
                        star_touches_numbers[row_num - 1].setdefault(
                            pos, []).append(int(number.group()))
            # check if number touches stars in row down
            if row_down:
                for pos in all_pos:
                    if is_star(lines[row_num + 1][pos]):
                        star_touches_numbers[row_num + 1].setdefault(
                            pos, []).append(int(number.group()))

gear_ratios = []

for row, value in star_touches_numbers.items():
    if value != {}:
        for column, numbers_touched in value.items():
            if len(numbers_touched) == 2:
                result = 1
                for num in numbers_touched:
                    result *= num
                gear_ratios.append(result)

print(sum(gear_ratios))
