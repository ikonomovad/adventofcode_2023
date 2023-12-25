def parse_workflow(workflows_content):
    workflows = {}

    for row in workflows_content:
        name, instructions = row.split('{')
        instructions = instructions.rstrip('}').split(',')

        workflow = []
        for condition in instructions:
            dict = {}
            if '<' in condition:
                c, w = condition.split(':')
                dict['category'] = c[0]
                dict['sign'] = '<'
                dict['value'] = int(c[2:])
                dict['workflow'] = w
            elif '>' in condition:
                c, w = condition.split(':')
                dict['category'] = c[0]
                dict['sign'] = '>'
                dict['value'] = int(c[2:])
                dict['workflow'] = w
            else:
                dict['workflow'] = condition

            workflow.append(dict)

        workflows[name] = workflow

    return workflows


def count_accepted_combinations(workflows, ratings, current_workflow):
    if current_workflow == 'R':  # this ranges were rejected
        return 0

    if current_workflow == 'A':  # this ranges were accepted
        product = 1

        for low, high in ratings.values():
            product *= high - low + 1

        return product

    accepted_count = 0

    for condition in workflows[current_workflow]:
        if condition.get('sign'):
            category, sign, value, workflow = condition.values()
            low, high = ratings[category]

            if sign == '>':
                true_range = (value + 1, high)
                false_range = (low, value)

            elif sign == '<':
                true_range = (low, value - 1)
                false_range = (value, high)

            copy_ratings = dict(ratings)
            copy_ratings[category] = true_range
            accepted_count += count_accepted_combinations(
                workflows, copy_ratings, workflow)

            ratings[category] = false_range

        else:
            workflow = condition['workflow']
            accepted_count += count_accepted_combinations(
                workflows, ratings, workflow)

    return accepted_count


with open('input.txt') as file:
    workflows_content, ratings_content = file.read().split('\n\n')
    workflows_content = workflows_content.split('\n')
    workflows = parse_workflow(workflows_content)
    ratings = {var: (1, 4000) for var in 'xmas'}

    print(count_accepted_combinations(workflows, ratings, 'in'))
