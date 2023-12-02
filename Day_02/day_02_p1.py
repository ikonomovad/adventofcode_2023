# Part 1

max_cubes_by_color = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

possible_games = []

with open('input.txt') as file:
    for game_line in file:
        # for each game row split game number and rounds as string
        game, rounds = game_line.split(':')
        game_number = int(game.strip().split()[1])
        rounds = rounds.strip().split(';')  # rounds as list

        game_is_possible = True
        for round in rounds:
            # for each round split shown cubes
            round = round.split(',')
            for cubes in round:
                # for each shown cubes check if number of cubes is bigger then max number of cubes that bag can contain
                num_of_cubes, color = cubes.strip().split()
                if (int(num_of_cubes) > max_cubes_by_color[color]):
                    # if one round in the game contains bigger number of cubes, the game is not possible
                    game_is_possible = False
                    break
            else:
                continue
            break
        if (game_is_possible):
            possible_games.append(game_number)

print(sum(possible_games))
