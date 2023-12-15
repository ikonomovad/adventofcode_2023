def hash_algorithm(string):
    value = 0
    for char in string:
        value = ((value + ord(char)) * 17) % 256
    return value


def remove_lens(step):
    label = step[:-1]
    i = hash_algorithm(label)
    label_index = next((index for index, lens in enumerate(
        boxes[i]) if lens.startswith(label)), None)

    if label_index is not None:
        boxes[i].pop(label_index)


def add_lens(step):
    label = step[:-2]
    focal_length = step[-1]
    i = hash_algorithm(label)
    label_index = next((index for index, lens in enumerate(
        boxes[i]) if lens.startswith(label)), None)

    if label_index is not None:
        boxes[i][label_index] = f'{label} {focal_length}'
    else:
        boxes[i].append(f'{label} {focal_length}')


with open('input.txt') as file:
    steps = file.read().split(',')
    total = 0
    boxes = []

    for _ in range(256):
        boxes.append([])

    for step in steps:
        if '-' in step:
            remove_lens(step)
        elif '=' in step:
            add_lens(step)

    result = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            result = (i + 1) * (j + 1) * int(lens[-1])
            total += result

    print(total)
