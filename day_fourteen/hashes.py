import sys
from _md5 import md5
import re

triple_pattern = re.compile(r'(.)\1{2,}')
penta_pattern = re.compile(r'(.)\1{4,}')


def check_hash(i, salt):
    global triple_pattern, penta_pattern
    hashed = md5((salt + str(i)).encode()).hexdigest()
    mp = penta_pattern.search(hashed)
    if mp: return None, mp.group(0)[:1]
    mt = triple_pattern.search(hashed)
    if mt: return mt.group(0)[:1], None
    return None, None


def run(salt, limit):
    triples = {}; found = []; i = -1; last = 0
    while len(found) < 64 and (limit is None or i < limit):
        i += 1
        triple, penta = check_hash(i, salt)
        if triple: triples.setdefault(triple, []).append(i)
        if penta and penta in triples:
            print("Penta with %s on iteration %d" % (penta, i))
            for triple_i in triples[penta]:
                if (i - triple_i) <= 1000:
                    found.append(triple_i)
                    last = triple_i
                    if len(found) == 64:
                        break
    print("After %d iterations, found %d keys, last one at %d" % (i, len(found), last))
    print(sorted(found))


if __name__ == '__main__':
    if len(sys.argv) < 2: raise Exception("Missing salt")
    else: salt = sys.argv[1]
    if len(sys.argv) >= 3: max_iterations = int(sys.argv[2])
    else: max_iterations = None
    run(salt, max_iterations)

# 126509 too high
# 14833 too low