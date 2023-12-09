# Part 2

with open('input.txt') as file:
    content = file.read()
    content = content.split('\n\n')
    seeds = [int(row) for row in content[0].split(':')[1].strip().split(' ')]
    seeds = [(seeds[i], seeds[i] + seeds[i+1])
             for i in range(0, len(seeds), 2)]
    maps = [row.split('\n')[1:] for row in content[1:]]

    map_ranges = []
    for part in maps:
        row_ranges = []
        for row in part:
            destination, source, range_len = map(int, row.split())
            row_ranges.append(
                (source, source + range_len, destination - source))  # we need delta for converting
        map_ranges.append(row_ranges)

    """
    Instead of checking each seed we will work with ranges
    and converting whole ranges from one to other map group.
    """

    segments = seeds  # initially we start with seed ranges

    for mapping in map_ranges:
        checked_ranges = []

        while segments:
            start, end = segments.pop()  # start with any segment

            # for each row from map group we check
            for map_row in mapping:
                start_source, end_source, delta = map_row
                partial_left_overlap = start_source <= start < end_source
                partial_right_overlap = start_source < end <= end_source

                # Case 1: Complete overlap
                if partial_left_overlap and partial_right_overlap:
                    #         start --- end
                    #  s_s ------------------- e_s

                    # In this case whole segment is converted [start, end]
                    checked_ranges.append((start + delta, end + delta))
                    break

                # Case 2: Partial left overlap
                if partial_left_overlap:
                    #                 start ------ end
                    #  s_s ------------------- e_s

                    # In this case only part [start, end_source] is converted
                    checked_ranges.append((start + delta, end_source + delta))
                    # we keep new segment that is not converted [end_source, end]
                    segments.append((end_source, end))
                    break

                # Case 3: Partial right overlap
                if partial_right_overlap:
                    #   start ------ end
                    #         s_s ------------------- e_s

                    # In this case only part [start_source, end] is converted
                    checked_ranges.append((start_source + delta, end + delta))
                    # we keep new segment that is not converted [start, start_source]
                    segments.append((start, start_source))
                    break

                # Case 4: Inner overlap
                if start < start_source and end > end_source:
                    #   start -------------------- end
                    #           s_s ------- e_s

                    # In this case only part [start_source, end_source] is converted
                    checked_ranges.append(
                        (start_source + delta, end_source + delta))
                    # two new segments left that are not converted
                    segments.append((start, start_source))
                    segments.append((end_source, end))
                    break

            else:
                # If there is no overlap
                checked_ranges.append((start, end))

        segments = checked_ranges  # segments to check with next map group

    # at the end we have list of ranges of locations and should find lowest number
    print(min(sorted(segments)[0]))
