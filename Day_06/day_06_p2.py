# Part 2
import re

with open('input.txt', 'r') as file:
    content = file.readlines()
    time = int(''.join(re.findall(r'\d+', content[0])))
    distance = int(''.join(re.findall(r'\d+', content[1])))

    count_t = 0
    for p in range(2, time):
        if time*p - p**2 > distance:
            count_t += 1
    print(count_t)
