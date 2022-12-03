import string
points = {}

for num, letter in enumerate([*string.ascii_lowercase], start=1):
    points[letter] = num

for num, letter in enumerate([*string.ascii_uppercase], start=27):
    points[letter] = num

if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        rucksacks = [line.rstrip() for line in f]

    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append(rucksacks[i:i + 3])

    items = []
    for group in groups:
        e1, e2, e3 = [[*item] for item in group]
        items = items + (list(set(e1) & set(e2) & set(e3)))

    sum_points = 0

    for item in items:
        sum_points = sum_points + points[item]

    print(sum_points)
