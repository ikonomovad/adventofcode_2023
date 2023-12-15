# If flipped is set to True that means that we are checking pattern with flipped rows
# Note: For perfect reflection, edge row must be touched
def find_pattern_reflection(pattern, flipped=False):
    rows_above = 0

    for j in range(len(pattern) - 1, 0, -1):
        if pattern[0] == pattern[j]:
            mirroring = True

            # if we find two same rows we should check rows in between to see if they are the same
            for k in range(1, j // 2 + 1):
                if pattern[k] != pattern[j - k]:
                    mirroring = False
                    break

            if mirroring:
                rows_above = int((j+1)/2)
                if flipped:
                    rows_above = len(pattern) - rows_above
                break

    return rows_above


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
