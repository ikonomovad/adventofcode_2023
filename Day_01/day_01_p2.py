# Part 2

string_numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

formatted_lines = []

with open('input.txt') as file:
    for line in file:
        integer = ''
        for i, char in enumerate(line):
            sub_string = ''
            if char.isdigit():
                integer += char
            else:
                sub_string = line[i:]
                for num_as_string, num in string_numbers.items():
                    if sub_string.startswith(num_as_string):
                        integer += num
        formatted_lines.append(integer)

values = []

for number in formatted_lines:
    newLine = int(number[0] + number[-1])
    values.append(newLine)

print(sum(values))
