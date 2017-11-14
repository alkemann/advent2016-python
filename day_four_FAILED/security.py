from collections import OrderedDict


def is_room_real(id):
    return True


# Checksum must be the five most common letters
# Ordered in their occurrence
# ties broken by alpha order
def check_checksum(name, checksum):
    chars = OrderedDict()
    for c in name:
        if c is '-':
            continue
        if c not in chars:
            chars[c] = 1
            continue
        chars[c] += 1

    copy = chars.copy()
    # s = "".join(list(chars.keys()))

    keys = sorted(copy, key=copy.get, reverse=True)
    sorted_tuples = [(k, copy[k]) for k in keys]

    count = 0
    checking = ""
    matched = None
    prev = None
    prev_value = None
    for t in sorted_tuples:
        if prev_value is None:
            prev = t[0]
            prev_value = t[1]
            continue

        if prev_value != t[1]:
            if matched is None:
                count += 1
                checking += prev
                prev = t[0]
                prev_value = t[1]
            else:
                adding = (5-count)
                checking += "".join(sorted(matched)[:adding])
                count += adding
                matched = None
            continue
        else:
            # Add ourselves and prev to the matched dict
            matched = [prev] if matched is None else matched
            matched.append(t[0])

    if matched is not None:
        adding = (5 - count)
        checking += "".join(sorted(matched)[:adding])


    y = 1

    return checking == checksum


