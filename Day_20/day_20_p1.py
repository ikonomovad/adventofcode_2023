from collections import deque

with open('input.txt') as file:
    push_btn = 1000
    conf = file.read().split('\n')
    broadcaster = {}
    modules = {}

    FF = '%'
    CNJ = '&'

    for row in conf:
        row = row.split(' -> ')

        if row[0] == 'broadcaster':
            broadcaster['destination_modules'] = row[1].split(', ')
            broadcaster['state'] = 'LP'
        else:
            module_name = row[0][1:]
            module_type = row[0][0]
            modules[module_name] = {}
            modules[module_name]['destination_modules'] = row[1].split(', ')
            modules[module_name]['module_type'] = module_type

            if module_type == FF:
                modules[module_name]['state'] = 'OFF'

            elif module_type == CNJ:
                modules[module_name]['state'] = {}

    # we need to know which modules send pulse because in the configuration as the text says there are 'untyped modules' (don't send pulse)
    typed_modules = modules.keys()

    for module_name, module_conf in modules.items():
        for destination_module in module_conf['destination_modules']:
            if (
                destination_module in typed_modules
                and modules[destination_module]['module_type'] == CNJ
            ):
                modules[destination_module]['state'][module_name] = 'LP'

    LP = 0
    HP = 0
    total = 0

    # pulses are always processed in the order they are sent
    for i in range(push_btn):
        queue = deque()

        # first time we push the button => sends LP to broadcaster => sends LP to all destination modules
        LP += 1  # first push
        element = {}

        for destination in broadcaster['destination_modules']:
            element = {'module': 'broadcaster',
                       'destination': destination, 'pulse': 'LP'}
            queue.append(element)

        while queue:
            current = queue.popleft()
            from_module = current['module']
            to_module = current['destination']
            sent_pulse = current['pulse']

            if sent_pulse == 'LP':
                LP += 1
            else:
                HP += 1

            if to_module in typed_modules:
                # nothing happens if HP is sent to %
                if modules[to_module]['module_type'] == FF and sent_pulse == 'LP':
                    if modules[to_module]['state'] == 'OFF':
                        modules[to_module]['state'] = 'ON'
                        # turn ON => send HP
                        for next_destination in modules[to_module]['destination_modules']:
                            queue.append(
                                {'module': to_module, 'destination': next_destination, 'pulse': 'HP'})

                    else:
                        modules[to_module]['state'] = 'OFF'
                        # turn OFF => send LP
                        for next_destination in modules[to_module]['destination_modules']:
                            queue.append(
                                {'module': to_module, 'destination': next_destination, 'pulse': 'LP'})

                # remembers recent pulse received for each connected module
                if modules[to_module]['module_type'] == CNJ:
                    modules[to_module]['state'][from_module] = sent_pulse
                    remembers = modules[to_module]['state']

                    remembers_hp_for_all = all(
                        p == 'HP' for p in remembers.values())

                    # if remembers HP for all => LP
                    if remembers_hp_for_all:
                        for next_destination in modules[to_module]['destination_modules']:
                            queue.append(
                                {'module': to_module, 'destination': next_destination, 'pulse': 'LP'})
                    else:
                        # else => HP
                        for next_destination in modules[to_module]['destination_modules']:
                            queue.append(
                                {'module': to_module, 'destination': next_destination, 'pulse': 'HP'})

total = HP * LP
print(total)
