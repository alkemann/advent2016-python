

def travel(instructions):
    x, y = 0, 0
    heading = 0  # N:0, E:1, S:2, W: 3
    visted = []
    for i in instructions:
        turn = i[0]
        distance = int(i[1:])

        heading += 1 if turn is "R" else -1
        heading %= 4

        # N E S W
        movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        move_x, move_y = movements[heading]

        # noinspection PyAssignmentToLoopOrWithParameter
        for i in range(distance):
            x += move_x
            y += move_y
            if (x, y) in visted:
                return abs(x) + abs(y)
            visted.append((x, y))

    return abs(x) + abs(y)


def parse(instructions):
    return instructions.split(", ")


def readfile(filename):
    return open(filename, "r").readlines()[0]


if __name__ == '__main__':
    print ("Shortest:", travel(parse(readfile("instructions.txt"))))
