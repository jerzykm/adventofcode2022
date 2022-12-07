def get_marker_pos(code, n_characters):
    q = []
    for i, letter in enumerate(list(code), start=1):
        q.append(letter)

        if len(q) > n_characters - 1 and len(q[-n_characters:]) == len(set(q[-n_characters:])):
            return i

    return None


if __name__ == '__main__':

    with open('data.txt', 'r') as f:
        code = f.read()

    marker_pos = get_marker_pos(code, 4)
    print(marker_pos)

    start_message_marker = get_marker_pos(code, 14)
    print(start_message_marker)
