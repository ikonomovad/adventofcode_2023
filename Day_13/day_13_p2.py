# If flipped is set to True that means that we are checking pattern with flipped rows
# Note: For perfect reflection, edge row must be touched
def find_pattern_reflection(pattern, flipped=False):
    rows_above = 0

    for i in range(1, len(pattern) // 2 + 1):
        count_diff = 0
        part1 = pattern[:i]
        part2 = pattern[i:i*2][::-1]

        for row1, row2 in zip(part1, part2):
            count_diff += count_difference(row1, row2)

        if count_diff == 1:
            rows_above = i
            if flipped:
                rows_above = len(pattern) - rows_above

    return rows_above


def count_difference(string1, string2):
    diff = sum(char1 != char2 for char1, char2 in zip(string1, string2))
    return diff


with open('input.txt') as file:
    patterns = file.read().split('\n\n')
    patterns = [pattern.split('\n') for pattern in patterns]
    total = 0

    for pattern in patterns:
        transposed_pattern = [''.join(row) for row in zip(*pattern)]

        # in order to find perfect reflection we will check four lists
        combinations = {
            'regular': [pattern, transposed_pattern],
            'flipped': [pattern[::-1], transposed_pattern[::-1]]
        }

        result = 0
        for type, pattern_combinations in combinations.items():
            for i, pattern_combination in enumerate(pattern_combinations):
                if type == 'flipped':
                    result = find_pattern_reflection(
                        pattern_combination, flipped=True)
                else:
                    result = find_pattern_reflection(pattern_combination)

                if result:
                    if i == 0:  # first lists are regular ones
                        result = result * 100
                    total += result
                    break
            else:
                continue
            break
    print(total)
