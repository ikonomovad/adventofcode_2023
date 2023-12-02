# Part 2

min_cubes_for_game = []

with open('input.txt') as file:
    for game_line in file:
        # for each game row split game number and rounds as string
        game, rounds = game_line.split(':')
        game_number = int(game.strip().split()[1])
        # combine all rounds as one
        combined_rounds = rounds.strip().replace(';', ',').split(',')
        combined_rounds = [cubes.strip() for cubes in combined_rounds]

        # define min cubes needed per game
        min_cubes = {'red': 0, 'blue': 0, 'green': 0}
        for cubes in combined_rounds:
            num_of_cubes, color = cubes.split()
            num_of_cubes = int(num_of_cubes)
            # save the biggest number of cubes shown for each color
            if (num_of_cubes > min_cubes[color]):
                min_cubes[color] = num_of_cubes

        total_min_cubes = 1
        for value in min_cubes.values():
            total_min_cubes *= value
        min_cubes_for_game.append(total_min_cubes)

print(sum(min_cubes_for_game))
