import string
points = {}

for num, letter in enumerate([*string.ascii_lowercase], start=1):
    points[letter] = num

for num, letter in enumerate([*string.ascii_uppercase], start=27):
    points[letter] = num

if __name__ == '__main__':
    print(points)
    with open('data.txt', 'r') as f:
        rucksacks = [line.rstrip() for line in f]

    items = []
    for rucksack in rucksacks:
        comp1, comp2 = [*rucksack[:len(rucksack)//2]], [*rucksack[len(rucksack)//2:]]
        items = items + (list(set(comp1) & set(comp2)))

    sum_points = 0

    for item in items:
        sum_points = sum_points + points[item]

    print(sum_points)
