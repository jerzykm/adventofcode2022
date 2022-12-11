N_ROUNDS = 10000
WORRY_DIV = 1

if __name__ == '__main__':

    with open('data.txt', 'r') as f:
        monkeys_lines = [line.rstrip() for line in f.readlines()]

    monkeys_data = [monkeys_lines[i:i + 6] for i in range(0, len(monkeys_lines), 7)]
    monkeys = {}

    for m in monkeys_data:
        items = m[1].replace('Starting items: ', '').split(',')
        op = m[2].replace('Operation: new = ', '').strip()
        test_div = m[3].replace('Test: divisible by ', '').strip()
        test_true = f"monkey {m[4].replace('If true: throw to monkey ', '').strip()}"
        test_false = f"monkey {m[5].replace('If false: throw to monkey ', '').strip()}"
        monkey = {'items': [int(item.strip()) for item in items],
                  'op': op, 'test_div': test_div,
                  'if_true': test_true, 'if_false': test_false,
                  'inspections': 0}
        # op =
        monkeys[m[0].replace(':', '').lower()] = monkey

    common_div = 1
    for monkey in monkeys.values():
        common_div = int(monkey['test_div']) * common_div

    print(common_div)
    for r in range(N_ROUNDS):
        print(f"starting round {r}")
        for monkey in monkeys:
            for i, item in enumerate(monkeys[monkey]['items']):
                # inspecting item
                op = monkeys[monkey]['op']
                val = op.split(' ')[-1]
                if '+' in op:
                    item = item + int(val)
                elif '*' in op:
                    if val == 'old':
                        item = item * item
                    else:
                        item = item * int(val)
                else:
                    print('wtf')

                # divide by WORRY_DIV
                item = int(item // WORRY_DIV)
                monkeys[monkey]['inspections'] = monkeys[monkey]['inspections'] + 1

                # check test
                if item > common_div:
                    item = item % common_div

                if item % int(monkeys[monkey]['test_div']) == 0:
                    monkeys[monkeys[monkey]['if_true']]['items'].append(item)
                else:
                    monkeys[monkeys[monkey]['if_false']]['items'].append(item)
                monkeys[monkey]['items'] = monkeys[monkey]['items'][1:]

    print('after inspections')

    inspections = [int(monkey['inspections']) for monkey in monkeys.values()]
    inspections.sort(reverse=True)

    print(inspections[0] * inspections[1])
