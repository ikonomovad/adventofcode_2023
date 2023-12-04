# Part 1

values = []

with open('input.txt') as file:
    for line in file:
        integer = ''
        for char in line:
            if char.isdigit():
                integer += char
        values.append(int(integer[0] + integer[-1]))

print(sum(values))
