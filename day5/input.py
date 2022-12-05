if __name__ == '__main__':

    # initialize stacks
    n_stacks = 9
    stacks = {i + 1: [] for i in range(n_stacks)}

    with open('data.txt', 'r') as f:
        stacks_txt = [line.rstrip() for line in f.readlines()[0:8]]

    for stack in reversed(stacks_txt):
        stack = stack.replace('[', '').replace(']', '')
        stack = stack.replace(5 * '    ', 5 * ',')
        stack = stack.replace(4 * '    ', 4 * ',')
        stack = stack.replace(3 * '    ', 3 * ',')
        stack = stack.replace(2 * '    ', 2 * ',')
        stack = stack.replace(1 * '    ', 1 * ',')
        stack = stack.replace(' ', ',')
        stack = stack.split(',')

        for i, letter in enumerate(stack, start=1):
            if letter != '':
                stacks[i].append(letter)

    for stack in stacks.items():
        print(stack)
