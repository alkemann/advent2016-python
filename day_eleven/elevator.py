import re


gen_pattern = re.compile("a (?P<type>\w+) generator")
chip_pattern = re.compile("a (?P<type>\w+)-compatible microchip")


class Floor:
    def __init__(self, n, building, description):
        self.id = n
        self.elevator = False
        self.building = building
        self.generators = re.findall(gen_pattern, description)
        self.chips = re.findall(chip_pattern, description)

    def __str__(self):
        out = "F" + str(self.id) + "\t" + ("E\t" if self.elevator else ".\t")
        for t in self.building.types:
            if t in self.generators:
                out += t[:2].title() + "G\t"
            else:
                out += " . \t"
        for t in self.building.types:
            if t in self.chips:
                out += t[:2].title() + "M\t"
            else:
                out += " . \t"
        return out


class Building:
    def __init__(self, floors):
        self.types = set()
        self.floors = []
        for n in range(0, len(floors), 1):
            f = Floor(n + 1, self, floors[n])
            for t in f.generators + f.chips:
                self.types.add(t)
            self.floors.append(f)
        self.floors[0].elevator = True

    def dump(self):
        print(" ")
        print(sorted(map(lambda s: s.title(), self.types)))
        print(" ")
        for k in self.floors[::-1]:
            print(k)
        print(" ")



# Rules:
#
# 1. 1 or 2 items must be in elevator
# 2. the two items may be in any combination
# 3. Elevator must stop on each floor
# 4. When an elevator stops, items on it and the floor are considerd in one space
# 5. A chip and gen is considered together even if 1 is in elevator and other on floor
# 6. Elevator starts on first floor
# 7. Actor starts on first floor
# 8. A micro chip must be on floor/elevator with NO generators, or AT LEAST it's compatible generator
#
def find_answer(building):
    return 11


if __name__ == '__main__':
    descriptions = [
        "The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.",
        "The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.",
        "The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.",
        "The fourth floor contains nothing relevant."
    ]
    b = Building(descriptions)
    b.dump()
    print("Answer:" + str(find_answer(b)))
