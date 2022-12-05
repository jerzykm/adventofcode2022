from helpers import get_stacks

if __name__ == '__main__':
    stacks = get_stacks(9)
    for stack in stacks.items():
        print(stack)

    with open('data.txt', 'r') as f:
        ops = [line.rstrip() for line in f.readlines()[10:]]

    for op in ops:
        op = op.split(' ')
        n_elements = int(op[1])
        from_stack = int(op[3])
        to_stack = int(op[5])

        for el in range(n_elements):
            print(stacks[from_stack])
            stacks[to_stack].append(stacks[from_stack].pop())

    output = ''
    for stack in stacks.items():
        output += stack[1].pop()

    print(output)






