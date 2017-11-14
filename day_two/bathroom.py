

# 1 2 3
# 4 5 6
# 7 8 9
def decode(instructions):
    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    dirs = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
    x, y = 1, 1
    code = []
    for line in instructions:
        for c in line:
            if c is "\n":
                continue

            move_x, move_y = dirs[c]
            x = clamp(x + move_x, 2)
            y = clamp(y + move_y, 2)
        code.append(str(pad[y][x]))
    return "".join(code)


def decode_two(instructions):
    pad = [
        [None,  None,   '1',    None,   None],
        [None,  '2',    '3',    '4',    None],
        ['5',   '6',    '7',    '8',    '9'],
        [None,  'A',    'B',    'C',    None],
        [None,  None,   'D',    None,   None]
    ]
    dirs = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
    x, y = 0, 2
    code = []
    for line in instructions:
        for c in line:
            if c is "\n":
                continue

            move_x, move_y = dirs[c]
            new_x = clamp(x + move_x, 4)
            new_y = clamp(y + move_y, 4)
            if pad[new_y][new_x] is not None:
                x, y = new_x, new_y

        code.append(str(pad[y][x]))
    return "".join(code)


def clamp(n, max):
    return 0 if n < 0 else max if n > max else n


if __name__ == '__main__':
    print("Code:", decode_two(open("codes.txt", "r").readlines()))
