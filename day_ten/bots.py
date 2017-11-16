import re


class Node:
    def __init__(self, id):
        self.id = id
        self.values = []
        self.low = None
        self.high = None
        self.sources = []

    def __int__(self):
        return int(self.id[4:])

    # To string override for debugging
    def __repr__(self):
        if self.is_output():
            return str(self.values)
        else:
            low = self.low.id if self.low else "N/A"
            high = self.high.id if self.high else "N/A"
            out = str(self.values) + "\tL:" + low + "  H:" + high + "\t\t"
            for s in self.sources:
                out += "'" + s.id + "' "
            return  out

    def is_output(self):
        return self.id[:3] == "out"

    def send_values_down(self):
        if len(self.values) != 2:
            self.populate_values()
        low = self.values[0] if self.values[0] < self.values[1] else self.values[1]
        high = self.values[0] if self.values[0] > self.values[1] else self.values[1]
        # BUGGY sends value down too many times
        self.low.values.append(low)
        self.high.values.append(high)

    def populate_values(self):
        for s in self.sources:
            s.send_values_down()
        if len(self.values) != 2:
            print(self)
            raise Exception("Bot does not have 2 values after 'populate_values'")

    def provide_high_value(self):
        if len(self.values) != 2:
            self.populate_values()
        return max(self.values)

    def provide_low_value(self):
        if len(self.values) != 2:
            self.populate_values()
        return min(self.values)

    def dig(self, target, other):
        if self.is_output():
            print("Output", self.id, "reached")
            return None
        print("Digging on ", self.id)
        if len(self.values) != 2:
            self.populate_values()
        if target in self.values and other in self.values:
            print("Found match for ", target, other, "in", self.values, "on", self.id)
            return int(self)

        # while n is not output, loop down from low and ask them to populate values
        result = self.low.dig(target, other)
        if result is not None:
            return result

        # then repeat for high
        result = self.high.dig(target, other)
        if result is not None:
            return result

        return None


# value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
def find_answer(commands, t1, t2):
    nodes = {}
    value_pattern = re.compile("value (?P<value>\d+) goes to (?P<bot>bot \d+)")
    bot_pattern = re.compile(
        "(?P<from_target>bot \d+) gives low to (?P<low_target>(bot|output) \d+) and high to (?P<high_target>(bot|output) \d+)")

    start1 = start2 = "N/A"
    for c in commands:
        if c[:5] == "value":  # assign value to bot
            matches = re.search(value_pattern, c)
            if matches is None:
                print(c)
                raise Exception("Value Pattern fails")
            key = matches.group("bot")
            value = int(matches.group("value"))
            nodes.setdefault(key, Node(key)).values.append(value)
            if value == t1:
                start1 = key
            if value == t2:
                start2 = key
        else:  # create links from this node to it's two children
            matches = re.search(bot_pattern, c)
            if matches is None:
                print(c)
                raise Exception("Bot Pattern fails")
            from_key = matches.group("from_target")
            low_target = matches.group("low_target")
            high_target = matches.group("high_target")

            target = nodes.setdefault(from_key, Node(from_key))

            low = nodes.setdefault(low_target, Node(low_target))
            low.sources.append(target)
            target.low = low

            high = nodes.setdefault(high_target, Node(high_target))
            high.sources.append(target)
            target.high = high

    # start with t1, follow it all way way to meeting unknown or output, if unknown go up to find value
    bot = nodes[start1]
    result = bot.dig(t1, t2)

    # print(str(t1) + " starts at " + start1)
    # print(str(t2) + " starts at " + start2)
    print("Nodes:")
    for n in sorted(nodes.items()):
        print(n)

    print("Result: ", result)
    return result


if __name__ == '__main__':
    strings = [s.rstrip() for s in open("instructions.txt", "r").readlines()]
    n = 1
    print("Number of bots: ", find_answer(commands=strings))
