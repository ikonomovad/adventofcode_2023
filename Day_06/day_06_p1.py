# Part 1
import re

with open('input.txt', 'r') as file:
    content = file.readlines()
    time = [int(num) for num in re.findall(r'\d+', content[0])]
    distance = [int(num) for num in re.findall(r'\d+', content[1])]

    """
    press button => 1
    time record => 7
    distance => 6
    (7 - 1) * 1 = 6 ===> (time - press_button) * press_button = distance ===> time*press_button - press_button^2 = distance
    """

    total = 1
    for i, t in enumerate(time):
        count_t = 0
        for p in range(2, t):
            if t*p - p**2 > distance[i]:
                count_t += 1
        total *= count_t
    print(total)
