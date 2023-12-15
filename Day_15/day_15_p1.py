def hash_algorithm(string):
    value = 0
    for char in string:
        value = ((value + ord(char)) * 17) % 256
    return value


with open('input.txt') as file:
    steps = file.read().split(',')
    total = 0

    for step in steps:
        total += hash_algorithm(step)

    print(total)
