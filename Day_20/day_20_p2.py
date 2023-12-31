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

    """
    I solved the exercise by manually inspecting my input.
    I found the 'rx' module and the module that feeds 'rx'.
    In my case, this module was a conjunction module 'rs'.
    I also found the modules that are feeding the module 'rs'.
    There were four modules and all were conjunction modules.
    So, in this case for 'rs' to send low pulse to 'rx', all connected modules to 'rs'
    need to send high pulse to 'rs'.
    I will count how many button pushes it requires for each of the connected modules
    to send first high pulse to the 'rs'.
    At the end, the final result will be product of total button pushes for each of these modules.
    """

    feeding_rx = ''

    for n, c in modules.items():
        if 'rx' in c['destination_modules']:
            feeding_rx = n

    connections = []

    for n, c in modules.items():
        if feeding_rx in c['destination_modules']:
            connections.append(n)

    # when connected modules sent first HP we will store the module name and number of button pushes (i) here
    modules_send_hp = {}
    i = 0  # number of button pushes

    # looping until all of the connected modules send first HP
    while len(modules_send_hp) != len(connections):
        # pulses are always processed in the order they are sent
        queue = deque()
        element = {}

        for destination in broadcaster['destination_modules']:
            element = {'module': 'broadcaster',
                       'destination': destination, 'pulse': 'LP'}
            queue.append(element)

        i += 1

        while queue:
            current = queue.popleft()
            from_module = current['module']
            to_module = current['destination']
            sent_pulse = current['pulse']

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

                    # HP sent from connected module to module that feeds 'rx'
                    if to_module == feeding_rx and from_module in connections and sent_pulse == 'HP' and from_module not in modules_send_hp:
                        modules_send_hp[from_module] = i

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

total = 1

for value in modules_send_hp.values():
    total *= value

print(total)
