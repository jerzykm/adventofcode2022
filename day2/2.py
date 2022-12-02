ROCK_O = 'A'
PAPER_O = 'B'
SCISSORS_O = 'C'

ROCK_P = 'X'
PAPER_P = 'Y'
SCISSORS_P = 'Z'

WIN = 6
DRAW = 3
LOSS = 0

ROCK_POINTS = 1
PAPER_POINTS = 2
SCISSORS_POINTS = 3

if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        moves = [line.rstrip() for line in f]

    points = 0
    for m in moves:
        move_o, move_p = m.split(' ')
        if move_o == ROCK_O:
            if move_p == ROCK_P:
                points = points + DRAW + ROCK_POINTS
            if move_p == PAPER_P:
                points = points + WIN + PAPER_POINTS
            if move_p == SCISSORS_P:
                points = points + LOSS + SCISSORS_POINTS
        elif move_o == PAPER_O:
            if move_p == ROCK_P:
                points = points + LOSS + ROCK_POINTS
            if move_p == PAPER_P:
                points = points + DRAW + PAPER_POINTS
            if move_p == SCISSORS_P:
                points = points + WIN + SCISSORS_POINTS
        elif move_o == SCISSORS_O:
            if move_p == ROCK_P:
                points = points + WIN + ROCK_POINTS
            if move_p == PAPER_P:
                points = points + LOSS + PAPER_POINTS
            if move_p == SCISSORS_P:
                points = points + DRAW + SCISSORS_POINTS
        else:
            print('WTF!?')

    print(points)
