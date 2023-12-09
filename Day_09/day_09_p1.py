
with open('input.txt') as file:
    content = file.read()
    history_rows = [list(map(int, row.split())) for row in content.split('\n')]
    next_history = 0

    for row in history_rows:
        current_row = row[::-1]  # flip row
        # keeping only the row values that we need for later calculation
        last_row_values = [current_row[0]]
        not_all_zeros = True

        while not_all_zeros:
            current_row = [current_row[i] - current_row[i + 1]
                           for i in range(0, len(current_row) - 1)]

            last_row_values.insert(0, current_row[0])

            if current_row.count(0) == len(current_row):
                not_all_zeros = False

        new_history = [0]  # initial new history values for row

        for i in range(1, len(last_row_values)):
            value = new_history[i - 1] + last_row_values[i]
            new_history.append(value)

        next_history += new_history[-1]  # next value in row history

    print(next_history)
