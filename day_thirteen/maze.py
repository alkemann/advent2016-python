import math
import sys
from collections import deque as Queue
from queue import PriorityQueue


def calc(x, y):
    return x * x + 3 * x + 2 * x * y + y + y * y


def binary(n):
    return bin(n)[2:]


def is_binary_wall(b):
    return b.count('1') % 2 == 1


def is_wall(x, y, f):
    return is_binary_wall(binary(calc(x, y) + f))


def draw_maze(size, fav, highlight):
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
            if (x, y) in highlight: row += 'o'; continue #str(highlight[(x, y)])
            row += "#" if is_wall(x, y, fav) else "."
        print(row)


# Graphing taken from https://www.redblobgames.com/pathfinding/a-star/implementation.html
class Maze:
    def __init__(self, favorite):
        self.fav = favorite

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x <= 60  and 0 <= y <= 60

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

    def map_to(self, start, goal):
        frontier = Queue()
        frontier.append(start)
        came_from = {}
        came_from[start] = None
        while len(frontier) > 0:
            current = frontier.popleft()
            if current == goal:
                break
            for to in self.neighbors(current):
                if to not in came_from:
                    frontier.append(to)
                    came_from[to] = current
        return came_from

    def reachable_in(self, start, steps):
        frontier = PriorityQueue()
        frontier.put(start)
        cost_so_far = {}
        cost_so_far[start] = 0
        new_cost = 0
        while frontier.empty() is False:
            current = frontier.get()
            for to in self.neighbors(current):
                new_cost = cost_so_far[current] + 1
                if to not in cost_so_far or new_cost < cost_so_far[to]:
                    cost_so_far[to] = new_cost
                    frontier.put(to, new_cost)
        reachable = {}
        for place in cost_so_far:
            if cost_so_far[place] <= steps:
                reachable[place] = cost_so_far[place]
        return reachable


if __name__ == '__main__':
    size = fav = target_x = target_y = steps = 10
    if len(sys.argv) >= 2: fav = int(sys.argv[1])
    if len(sys.argv) >= 3: target_x  = int(sys.argv[2])
    if len(sys.argv) >= 4: target_y = int(sys.argv[3])
    if len(sys.argv) >= 5: size = int(sys.argv[4])
    if len(sys.argv) >= 6: steps = int(sys.argv[5])

    target = (target_x, target_y)
    maze = Maze(fav)
    came_from = maze.map_to((1, 1), target)

    path = {}
    path[target] = 'o'
    f = came_from[target]
    while f is not None:
        path[f] = 'o'
        f = came_from[f]

    steps_needed = (len(path) - 1)
    print("Steps to target: %d" % steps_needed)
    draw_maze(size, fav, path)

    print(" ")
    print(" ")
    reachable = maze.reachable_in((1, 1), steps)
    print(" Reachables in %d steps: %d" % (steps, len(reachable)))
    print(" ")
    draw_maze(size, fav, reachable)