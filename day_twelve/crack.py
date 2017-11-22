import re


def apply_commands(commands, debug=False):
    container = {"a": 0, "b": 0, "c": 0, "d": 0, "iterations": 0}
    pattern = re.compile("(?P<cmd>\w{3}) (?P<arg1>[\d\w]+)[ ]{0,1}(?P<arg2>[\w\d-]*)")
    parsed = []
    for c in commands:
        m = re.search(pattern, c)
        parsed.append({"cmd": m.group("cmd"), "a1": m.group("arg1"), "a2": m.group("arg2")})

    x = 0
    while x < len(parsed):
        container['iterations'] += 1
        if debug: print(i, container);
        c = parsed[x]['cmd']; a1 = parsed[x]['a1']; a2 = parsed[x]['a2']
        v1 = container[a1] if a1.isalpha() else int(a1)
        if c == "cpy":
            container[a2] = v1
        elif c == "inc":
            container[a1] += 1
        elif c == "dec":
            container[a1] -= 1
        elif c == 'jnz' and v1 != 0:
            x += container[a2] if a2.isalpha() else int(a2)
            continue
        x += 1

    return container


if __name__ == '__main__':
    instructions = [
        # "cpy 1 c", # include for 2nd task
        "cpy 1 a",
        "cpy 1 b",
        "cpy 26 d",
        "jnz c 2",
        "jnz 1 5",
        "cpy 7 c",
        "inc d",
        "dec c",
        "jnz c -2",
        "cpy a c",
        "inc a",
        "dec b",
        "jnz b -2",
        "cpy c b",
        "dec d",
        "jnz d -6",
        "cpy 14 c",
        "cpy 14 d",
        "inc a",
        "dec d",
        "jnz d -2",
        "dec c",
        "jnz c -5"
    ]
    result = apply_commands(instructions, debug=True)
    print(result)
    print("Answer:" + str(result["a"]))
    print("After iterations:" + str(result["iterations"]))
