import re

types = []


class Floor:
    def __init__(self, id, has_elevator=False):
        self.id = id
        self.generators = []
        self.chips = []
        self.elevator = has_elevator

    def __str__(self):
        out = "F" + str(self.id) + "\t" + ("E\t" if self.elevator else ".\t")
        for t in types:
            if t in self.generators:
                out += t[:2].title() + "G\t"
            else:
                out += " . \t"

        for t in types:
            if t in self.chips:
                out += t[:2].title() + "C\t"
            else:
                out += " . \t"

        return out


# Rules:
#
# 1. 1 or 2 items must be in elevator
# 2. the two items may be in any combination
# 3. Elevator must stop on each floor
# 4. When an elevator stops, items on it and the floor are considerd in one space
# 5. A chip and gen is considered together even if 1 is in elevator and other on floor
# 6. Elevator starts on first floor
# 7. Actor starts on first floor
#
def find_answer(instructions):
    gen_pattern = re.compile("a (?P<type>\w+) generator")
    chip_pattern = re.compile("a (?P<type>\w+)-compatible microchip")
    building = {}
    for n in [0, 1, 2, 3]:
        f = Floor(n + 1)
        f.generators = re.findall(gen_pattern, instructions[n])
        for g in f.generators:
            if g not in types:
                types.append(g)

        f.chips = re.findall(chip_pattern, instructions[n])
        for c in f.generators:
            if c not in types:
                types.append(c)

        building[n + 1] = f

    print(map(lambda s: s.title(), types))
    for k in building:
        print(building[k])
    return 11


if __name__ == '__main__':
    instructions = [
        "The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.",
        "The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.",
        "The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.",
        "The fourth floor contains nothing relevant."
    ]
    print("Answer:" + str(find_answer(instructions=instructions)))
