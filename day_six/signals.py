from collections import Counter


class Char:
    def __init__(self):
        self.occurrences = []
        self.count = 0

    def add(self, c):
        self.occurrences.append(c)
        self.count += 1

    def popular(self):
        counter = Counter(self.occurrences)
        common = counter.most_common(1)
        return common[0][0]

    def least(self):
        counter = Counter(self.occurrences)
        least = counter.most_common(self.count)
        return least[len(least) - 1][0]


def corrected(strings, popular=True):
    characters = []
    char_count = len(strings[0])
    for i in range(char_count):
        characters.append(Char())

    for s in strings:
        for i in range(char_count):
            characters[i].add(s[i])

    out = ""
    for c in characters:
        if (popular):
            out += c.popular()
        else:
            out += c.least()

    return out


if __name__ == '__main__':
    strings = [s.rstrip() for s in open("input.txt", "r").readlines()]
    out = corrected(strings)
    print("Answer:", out)
    out = corrected(strings, False)
    print("Answer:", out)
