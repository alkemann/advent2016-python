import re


def has_ssl(ip):
    length = len(ip)
    in_brackets = False
    i = 0
    while i < length - 2:
        c = ip[i]
        if c == '[':
            in_brackets = True
        elif c == ']':
            in_brackets = False
        else:
            o = ip[i + 1]
            if not in_brackets and c is ip[i+2] and c is not o and o != '[' and o != ']':
                pattern = '\[[a-z]*' + o + c + o
                result = re.search(pattern, ip)
                if result is not None:
                    return True

        i += 1
    return False


def has_tls(ip):
    length = len(ip)
    abba = False
    cancel = False
    in_brackets = False
    i = 0
    while i < length - 3:
        c = ip[i]
        if c == '[':
            in_brackets = True
        elif c == ']':
            in_brackets = False
        else:
            if c == ip[i+3] and ip[i+1] == ip[i+2] and c != ip[i+1]:
                if in_brackets:
                    cancel = True
                else:
                    abba = True
                i += 3

        i += 1

    return abba and not cancel


if __name__ == "__main__":
    strings = [s.rstrip() for s in open("input.txt", "r").readlines()]
    count = 0
    for s in strings:
        if has_ssl(s):
            count += 1
    print("Count:", count)



