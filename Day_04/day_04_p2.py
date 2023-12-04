# Part 2

with open('input.txt') as file:
    lines = list(file)
    copies = [1 for _ in enumerate(lines)]

    for row_number, line in enumerate(lines):
        line = line.split(':')
        card = line[1]
        winning_numbers, numbers = card.split('|')
        winning_numbers = winning_numbers.strip().split(' ')
        winning_numbers = [num for num in winning_numbers if num]
        numbers = numbers.strip().split(' ')
        numbers = [num for num in numbers if num]
        match_numbers = len(set(winning_numbers) & set(numbers))

        for num_of_copies in range(copies[row_number]):
            for i in range(match_numbers):
                copies[row_number + i + 1] += 1
    print(sum(copies))
