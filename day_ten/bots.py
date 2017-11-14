import re


class Node:
    def __init__(self, id):
        self.id = id
        self.values = []
        self.low = None
        self.high = None
        self.source = None

    # To string override for debugging
    def __repr__(self):
        if self.id[:3] == "out":
            return self.id + ":" + str(self.values)
        else:
            low = self.low.id if self.low else "N/A"
            high = self.high.id if self.high else "N/A"

            return str(self.values) + ":" + low + "<" + high


# value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
def find_answer(commands, t1, t2):
    nodes = {}
    value_pattern = re.compile("value (?P<value>\d+) goes to (?P<bot>bot \d+)")
    bot_pattern = re.compile(
        "(?P<from_target>bot \d+) gives low to (?P<low_target>(bot|output) \d+) and high to (?P<high_target>(bot|output) \d+)")

    for c in commands:
        if c[:5] == "value":  # assign value to bot
            result = re.search(value_pattern, c)
            if result is None:
                print(c)
                raise "Value Pattern fails for : "
            key = result.group("bot")
            value = int(result.group("value"))
            nodes.setdefault(key, Node(key)).values.append(value)
            if value == t1:
                start1 = key
            if value == t2:
                start2 = key
        else:  # create links from this node to it's two children
            result = re.search(bot_pattern, c)
            if result is None:
                print(c)
                raise "Bot Pattern fails"
            from_key = result.group("from_target")
            low_target = result.group("low_target")
            high_target = result.group("high_target")

            target = nodes.setdefault(from_key, Node(from_key))
            low = nodes.setdefault(low_target, Node(low_target))
            low.source = target
            high = nodes.setdefault(high_target, Node(high_target))
            high.source = target
            target.low = low
            target.high = high

    print(str(t1) + " starts at " + start1)
    print(str(t2) + " starts at " + start2)
    print(nodes)
    return len(commands)


if __name__ == '__main__':
    strings = [s.rstrip() for s in open("instructions.txt", "r").readlines()]
    n = 1
    print("Number of bots: ", find_answer(commands=strings))
