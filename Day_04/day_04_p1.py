# Part 1

with open('input.txt') as file:
    card_worth = 0
    for line in file:
        line = line.split(':')
        card = line[1]
        winning_numbers, numbers = card.split('|')
        winning_numbers = winning_numbers.strip().split(' ')
        winning_numbers = [num for num in winning_numbers if num]
        numbers = numbers.strip().split(' ')
        numbers = [num for num in numbers if num]
        match_numbers = set(winning_numbers) & set(numbers)

        if match_numbers != set():
            result = 1
            for i,  match in enumerate(match_numbers):
                if i != 0:
                    result *= 2

            card_worth += result
    print(card_worth)
