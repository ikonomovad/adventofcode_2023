
with open('input.txt') as file:
    maps = file.read()
    directions, network = maps.split('\n\n')
    # instructions for next element are in list ['BBB', 'CCC'], and when we want to get element on the right we want element on position 1
    translator = str.maketrans('RL', '10')
    directions = [int(value) for value in directions.translate(translator)]

    network = [row for row in (n.split(' = ') for n in network.split('\n'))]
    nodes = list()
    instructions = list()

    for row in network:
        nodes.append(row[0])
        row_instructions = row[1].lstrip('(').rstrip(')').split(', ')
        instructions.append(row_instructions)

    final_destination_pos = nodes.index('ZZZ')
    current_element_pos = nodes.index('AAA')
    not_final_destination = True
    steps = 0

    while not_final_destination:
        for d in directions:
            if current_element_pos != final_destination_pos:
                next_value = instructions[current_element_pos][d]
                current_element_pos = nodes.index(next_value)
                steps += 1
            else:
                not_final_destination = False
                break
    print(steps)
