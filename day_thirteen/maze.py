import math


def calc(x, y):
    return x * x + 3 * x + 2 * x * y + y + y * y


def binary(n):
    return bin(n)[2:]


def is_binary_wall(b):
    return b.count('1') % 2 == 1


def is_wall(x, y, f):
    return is_binary_wall(binary(calc(x, y) + f))


def draw_maze(size, fav):
    if size > 10:
        top = "    "
        for i in range(1, size + 1):
            top += str(math.floor(i/10)) if i >= 10 else " "
        print(top)
    top = "   "
    for i in range(0, size + 1):
        top += str(i % 10)
    print(top)
    for y in range(0, size+1):
        row = (" " if y < 10 else "") + "%d " % y
        for x in range(0, size+1):
            row += "#" if is_wall(x, y, fav) else "."
        print(row)


if __name__ == '__main__':
    draw_maze(70, 10)
