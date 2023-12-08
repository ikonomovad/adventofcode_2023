from collections import Counter

with open('input.txt') as file:
    # for easier sorting
    trans = str.maketrans('AKQT98765432J', 'ABCDEFGHIJKLM')
    hands = [[hand[0].translate(trans), hand[1]]
             for hand in (line.split() for line in file)]
    hands = sorted(hands)

    # empty lists for grouping hands by strength
    # 0 - five, 1 - four, 2 - full house, 3 - three, 4 - two pair, 5 - one pair, 6 - high
    group_by_strength = [[] for _ in range(7)]

    for hand in hands:
        card, bid = hand
        has_joker = card.count('M')

        counter_values = sorted(Counter(card).values())

        if counter_values == [5]:  # five of a kind
            group_by_strength[0].append(hand)
        elif counter_values == [1, 4]:  # four of a kind
            if has_joker:
                group_by_strength[0].append(hand)  # becomes five of a kind
            else:
                group_by_strength[1].append(hand)
        elif counter_values == [2, 3]:  # full house
            if has_joker:
                group_by_strength[0].append(hand)  # becomes five of a kind
            else:
                group_by_strength[2].append(hand)
        elif counter_values == [1, 1, 3]:  # three of a kind
            if has_joker:
                group_by_strength[1].append(hand)  # becomes four of a kind
            else:
                group_by_strength[3].append(hand)
        elif counter_values == [1, 2, 2]:  # two pair
            if has_joker and has_joker == 2:
                group_by_strength[1].append(hand)  # becomes four of a kind
            elif has_joker and has_joker == 1:
                group_by_strength[2].append(hand)  # becomes full house
            else:
                group_by_strength[4].append(hand)
        elif counter_values == [1, 1, 1, 2]:  # one pair
            if has_joker:
                group_by_strength[3].append(hand)  # becomes three of a kind
            else:
                group_by_strength[5].append(hand)
        else:
            if has_joker:
                group_by_strength[5].append(hand)  # becomes one pair
            else:
                group_by_strength[6].append(hand)

    merged_groups = []
    for group in group_by_strength:
        if group != []:
            merged_groups.extend(group)

    print(sum([int(hand[1]) * i for i, hand in enumerate(merged_groups[::-1], 1)]))
