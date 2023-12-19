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


def parse_ratings(ratings_content):
    ratings = []

    for row in ratings_content:
        row = row.rstrip('}').lstrip('{').split(',')

        dict = {}
        for element in row:
            category, value = element.split('=')
            dict[category] = int(value)

        ratings.append(dict)

    return ratings


with open('input.txt') as file:
    workflows_content, ratings_content = file.read().split('\n\n')
    workflows_content = workflows_content.split('\n')
    ratings_content = ratings_content.split('\n')
    ratings = parse_ratings(ratings_content)
    workflows = parse_workflow(workflows_content)

    accepted = []

    for part in ratings:
        not_processed = True
        current_workflow = 'in'

        while not_processed:
            for condition in workflows[current_workflow]:
                if condition.get('sign'):
                    category, sign, value, workflow = condition.values()

                    if sign == '>':
                        if part[category] > value:
                            current_workflow = workflow
                            break
                    elif sign == '<':
                        if part[category] < value:
                            current_workflow = workflow
                            break
                else:
                    current_workflow = condition['workflow']

            if current_workflow == 'R':
                not_processed = False
                break
            elif current_workflow == 'A':
                accepted.append(part)
                not_processed = False
                break
    total = 0

    for part in accepted:
        total += sum(part.values())

    print(total)
