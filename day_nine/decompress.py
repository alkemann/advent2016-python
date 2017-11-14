import re


pattern = re.compile("(?P<extract>\d+)x(?P<repeat>\d+)")


def decompress(s):
    out = ""
    i = 0
    length = len(s)
    is_operation = False
    operation = ""
    pattern = re.compile("(?P<extract>\d+)x(?P<repeat>\d+)")
    while i < length:
        c = s[i]
        if c is '(':
            is_operation = True
            i += 1
            continue

        if is_operation:
            if c is ')':  # at this point we know the entire operation
                # operation at this point contains "\d+x\d+"
                result = re.search(pattern, operation);
                extract = int(result.group("extract"))
                repeat = int(result.group("repeat"))
                value = s[i+1:extract+i+1]
                out += value * repeat
                i += extract + 1
                operation = ""
                is_operation = False
                continue
            else:
                operation += c
        else:
            out += c
        i += 1
    return out


def value_of(s):

    result = re.search(pattern, operation);
    extract = int(result.group("extract"))
    repeat = int(result.group("repeat"))
    value = s[i + 1:extract + i + 1]
    return value * repeat



def decompress_two(s):
    n = 0
    i = 0
    length = len(s)
    is_operation = False
    operation = ""
    while i < length:
        c = s[i]
        if c is '(':
            is_operation = True
            i += 1
            continue

        if is_operation:
            if c is ')':  # at this point we know the entire operation
                # operation at this point contains "\d+x\d+"
                result = re.search(pattern, operation);
                extract = int(result.group("extract"))
                repeat = int(result.group("repeat"))
                value = s[i+1:extract+i+1]

                n += repeat * value_of(value)
                i += extract + 1
                operation = ""
                is_operation = False
                continue
            else:
                operation += c
        else:
            n += 1
        i += 1
    return n


if __name__ == "__main__":
    strings = [s.rstrip() for s in open("input.txt", "r").readlines()]
    count = 0
    for s in strings:
        print("Length:", len(decompress(s)))
