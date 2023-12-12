def count_different_arrangements(size_of_group, current_row, numbers):
    number_of_arrangements = 0

    # no combination
    if current_row == '' and len(numbers):
        return 0
    # combination found
    elif current_row == '' and len(numbers) == 0:
        return 1

    char_to_check = current_row[0]

    # if the first element in the row string is '?' that means that it can be replaced with '.' or '#'
    if current_row[0] == '?':
        char_to_check = '.#'

    for char in char_to_check:
        if char == '.':
            # if we did not entered a group of elements, we will just remove '.' and iterate again
            if size_of_group == 0:
                number_of_arrangements += count_different_arrangements(
                    current_row=current_row[1:], numbers=numbers, size_of_group=0)
            else:
                # if we are counting elements in group (we are in group) that means we are closing the group now
                if len(numbers) and numbers[0] == size_of_group:
                    # remove first char, remove closed group and reset the size of the group
                    number_of_arrangements += count_different_arrangements(
                        current_row=current_row[1:], numbers=numbers[1:], size_of_group=0)
        elif char == '#':
            # if we are not in group we will start new one, if we are we will add one element plus in that group
            size_of_group += 1
            number_of_arrangements += count_different_arrangements(
                current_row=current_row[1:], numbers=numbers, size_of_group=size_of_group)

    return number_of_arrangements


with open('input.txt') as file:
    rows = [row.split() for row in file.read().split('\n')]
    rows = [[tuple(map(int, num.split(','))), row] for row, num in rows]

    total_arrangements_by_row = []

    for num, row in rows:
        # append '.' at the end of the row so in the recursion we can close the group at the end
        total_arrangements_by_row.append(count_different_arrangements(
            size_of_group=0, current_row=row + '.', numbers=num))

    print(sum(total_arrangements_by_row))
