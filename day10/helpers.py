def get_stacks(n_stacks=9):
    stacks = {i + 1: [] for i in range(n_stacks)}

    with open('data.txt', 'r') as f:
        stacks_txt = [line.rstrip() for line in f.readlines()[0:8]]

    for stack in reversed(stacks_txt):
        stack = stack.replace('[', '').replace(']', '')
        stack = stack.replace('    ', ',').replace(' ', ',')
        stack = stack.split(',')

        for i, letter in enumerate(stack, start=1):
            if letter != '':
                stacks[i].append(letter)

    return stacks