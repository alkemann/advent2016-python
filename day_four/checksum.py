import re
from collections import OrderedDict

pattern = re.compile("(?P<name>[\w-]+)-(?P<id>\d+)\[(?P<checksum>\w+)\]")


def mysorter(tuple):
    return tuple[1] * 1000 + (1000 - ord(tuple[0]))


def calc_checksum(name):
    counter = {}
    for c in name:
        if c == '-': continue;
        counter[c] = counter[c] + 1 if c in counter else 1
    result = OrderedDict(sorted(counter.items(), key=mysorter, reverse=True))
    top = list(result)[:5]
    return ''.join(top)


def room_is_real(name, checksum):
    real = calc_checksum(name)
    return real == checksum


if __name__ == '__main__':
    strings = [s.rstrip() for s in open("rooms.txt", "r").readlines()]
    result = 0
    for s in strings:
        m = re.search(pattern, s)
        if m is None:
            raise Exception("Failed to understand [ %s ]!" % s)
        name = m.group("name")
        id = m.group("id")
        cs = m.group("checksum")
        result += int(id) if room_is_real(name, cs) else 0
    print("Result: %d" % result)
