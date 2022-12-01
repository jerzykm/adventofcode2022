if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        capacities = [line.rstrip() for line in f]

    calories_list = []
    calories_sum = 0

    for calories in capacities:
        if calories != '':
            calories_sum = calories_sum + int(calories)
        else:
            calories_list.append(calories_sum)
            calories_sum = 0

    calories_list.sort(reverse=True)
    max_calories = calories_list[0]
    top_three = sum(calories_list[:3])

    print(max_calories)
    print(top_three)
