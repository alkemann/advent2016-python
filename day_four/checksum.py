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


def decrypt(name, id):
    out = ''
    for c in name:
        out += ' ' if c == '-' else chr(((ord(c) - 97 + id) % 26) + 97)
    return out


if __name__ == '__main__':
    strings = [s.rstrip() for s in open("rooms.txt", "r").readlines()]
    result = 0
    for s in strings:
        m = re.search(pattern, s)
        if m is None:
            raise Exception("Failed to understand [ %s ]!" % s)
        name = m.group("name")
        id = int(m.group("id"))
        cs = m.group("checksum")
        if room_is_real(name, cs):
            result += id
            print(id, decrypt(name, id))

    print("Result: %d" % result)
    print(" (try `python3 checksum.py | grep north`)")
