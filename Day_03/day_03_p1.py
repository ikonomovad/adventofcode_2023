# Part 1
import re


def is_sign(char):
    # if char is digit or dot it will return false
    return bool(re.match(r'[^0-9.]', char))


with open('input.txt') as file:
    part_numbers = []
    lines = [line.strip() for line in file]
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
            # creating a range for all positions that need to be check in rows up, down and current one
            all_pos = range(start_pos, end_pos)
            is_part_number = False
            for pos in all_pos:
                if is_sign(line[pos]) or (row_up and is_sign(lines[row_num - 1][pos])) or (row_down and is_sign(lines[row_num + 1][pos])):
                    is_part_number = True
                    break
            if (is_part_number):
                part_numbers.append(int(number.group()))

print(sum(part_numbers))
