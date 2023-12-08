from collections import Counter

with open('input.txt') as file:
    # for easier sorting
    trans = str.maketrans('AKQJT98765432', 'ABCDEFGHIJKLM')
    hands = [[hand[0].translate(trans), hand[1]]
             for hand in (line.split() for line in file)]
    hands = sorted(hands)

    # empty lists for grouping hands by strength
    group_by_strength = [[] for _ in range(7)]

    for hand in hands:
        card, bid = hand
        counter_values = sorted(Counter(card).values())

        if counter_values == [5]:  # five of a kind
            group_by_strength[0].append(hand)
        elif counter_values == [1, 4]:  # four of a kind
            group_by_strength[1].append(hand)
        elif counter_values == [2, 3]:  # full house
            group_by_strength[2].append(hand)
        elif counter_values == [1, 1, 3]:  # three of a kind
            group_by_strength[3].append(hand)
        elif counter_values == [1, 2, 2]:  # two pair
            group_by_strength[4].append(hand)
        elif counter_values == [1, 1, 1, 2]:  # one pair
            group_by_strength[5].append(hand)
        else:
            group_by_strength[6].append(hand)

    merged_groups = []
    for group in group_by_strength:
        if group != []:
            merged_groups.extend(group)

    print(sum([int(hand[1]) * i for i, hand in enumerate(merged_groups[::-1], 1)]))
