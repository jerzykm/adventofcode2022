if __name__ == '__main__':

    with open('data.txt', 'r') as f:
        signals = [line.rstrip() for line in f.readlines()]

    forest = []

    X = 1
    cycle = 0

    cycles = [20, 60, 100, 140, 180, 220]
    results = []

    for i, signal in enumerate(signals):
        print(f"register is {X} and cycle is {cycle}")
        if signal == 'noop':
            cycle = cycle + 1
            if cycle in cycles:
                print(f'ADDING NOOP register is {X} and cycle is {cycle}')
                results.append(cycle * X)

        else:
            _, val = signal.split(' ')
            cycle = cycle + 1
            if cycle in cycles:
                results.append(cycle * X)
                print(f'ADDING ADDX register is {X} and cycle: {cycle}')
            cycle = cycle + 1
            if cycle in cycles:
                results.append(cycle * X)
                print(f'ADDING ADDX register is {X} and cycle: {cycle}')

            X = X + int(val)

    print(results)
    print(sum(results))