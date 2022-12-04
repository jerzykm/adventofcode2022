if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        tasks = [line.rstrip() for line in f]

    def get_ranges(task):
        t_start, t_end = task.split('-')
        t_range = set(range(int(t_start), int(t_end) + 1))
        return t_range

    overlaps = 0
    overlaps2 = 0
    for task in tasks:
        task1, task2 = task.split(',')
        l1 = get_ranges(task1)
        l2 = get_ranges(task2)
        # part 1
        if l1 - l2 == set() or l2 - l1 == set():
            overlaps = overlaps + 1
        # part 2
        if len(l1) + len(l2) > len(l1.union(l2)):
            overlaps2 = overlaps2 + 1

    print(overlaps)
    print(overlaps2)



