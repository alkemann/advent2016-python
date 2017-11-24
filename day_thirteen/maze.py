import math
import sys
from collections import deque as Queue


def calc(x, y):
    return x * x + 3 * x + 2 * x * y + y + y * y


def binary(n):
    return bin(n)[2:]


def is_binary_wall(b):
    return b.count('1') % 2 == 1


def is_wall(x, y, f):
    return is_binary_wall(binary(calc(x, y) + f))


def draw_maze(size, fav, target_x, target_y, path):
    if size >= 10:
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
            # if x == target_x and y == target_y: row += "O"; continue
            if (x, y) in path: row += "o"; continue
            row += "#" if is_wall(x, y, fav) else "."
        print(row)


# Graphing taken from https://www.redblobgames.com/pathfinding/a-star/implementation.html
class Maze:
    def __init__(self, favorite):
        self.fav = favorite

    def in_bounds(self, id):
        (x, y) = id
        return x >= 0 and y >= 0

    def passable(self, id):
        (x, y) = id
        return is_wall(x, y, self.fav) is False

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def map_to(self, start):
        frontier = Queue()
        frontier.append(start)
        came_from = {}
        came_from[start] = None
        while len(frontier) > 0:
            current = frontier.popleft()
            for to in self.neighbors(current):
                if to not in came_from:
                    frontier.append(to)
                    came_from[to] = current
        return came_from


if __name__ == '__main__':
    size = fav = target_x = target_y = 10
    if len(sys.argv) >= 2: fav = int(sys.argv[1])
    if len(sys.argv) >= 3: target_x  = int(sys.argv[2])
    if len(sys.argv) >= 4: target_y = int(sys.argv[3])
    if len(sys.argv) >= 5: size= int(sys.argv[4])

    maze = Maze(fav)
    came_from = maze.map_to((1, 1))

    target = (target_x, target_y)
    path = [target]
    f = came_from[target]
    while f is not None:
        path.append(f)
        f = came_from[f]


    steps = (len(path) - 1)
    print("Steps to target: %d" % steps)

    draw_maze(size, fav, target_x, target_y, path)
