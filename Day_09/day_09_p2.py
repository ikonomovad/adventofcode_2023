
with open('input.txt') as file:
    content = file.read()
    history_rows = [list(map(int, row.split())) for row in content.split('\n')]
    previous_history = 0

    for row in history_rows:
        current_row = row[::-1]  # flip row
        # keeping only the row values that we need for later calculation
        first_row_values = [current_row[-1]]
        not_all_zeros = True

        while not_all_zeros:
            current_row = [current_row[i] - current_row[i + 1]
                           for i in range(0, len(current_row) - 1)]

            first_row_values.append(current_row[-1])

            if current_row.count(0) == len(current_row):
                not_all_zeros = False

        new_values_for_row = [0]  # initial new values for row at left

        first_row_values = first_row_values[::-1]

        for i in range(1, len(first_row_values)):
            value = first_row_values[i] - new_values_for_row[i - 1]
            new_values_for_row.append(value)

        previous_history += new_values_for_row[-1]  # new value in row history

    print(previous_history)
