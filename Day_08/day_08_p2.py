import math

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

    end_letter = 'Z'
    total_steps = list()
    elements_to_check = [nodes.index(node)
                         for node in nodes if node.endswith('A')]

    """
    For each element that ends with 'A' count the steps until it ends with 'Z';
    At the end, find least common multiple from all the steps.
    """
    for element in elements_to_check:
        not_final_destination = True
        steps = 0

        while not_final_destination:
            for d in directions:
                # check if element ends with letter 'Z'
                if not nodes[element][-1] == end_letter:
                    next_value = instructions[element][d]
                    # change current element with next decided by instructions
                    element = nodes.index(next_value)
                    steps += 1
                else:
                    not_final_destination = False
                    break

        total_steps.append(steps)

    print(math.lcm(*total_steps))
