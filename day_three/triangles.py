

def is_number(n):
    return n is not ""


def parse(s):
    return list(map(int, filter(is_number, s.split(" "))))


# k^2 + K^2 = H^5
def is_valid_triangle(sides):
    k, K, H = sides
    return k + K > H and k + H > K and K + H > k


if __name__ == '__main__':
    counter = 0
    t1, t2, t3 = [0,0,0], [0,0,0], [0,0,0]
    side = 0
    for line in open("triangles.txt", "r").readlines():
        t1[side], t2[side], t3[side] = parse(line)
        side += 1
        if side is 3:
            side = 0
            counter += 1 if is_valid_triangle(t1) else 0
            counter += 1 if is_valid_triangle(t2) else 0
            counter += 1 if is_valid_triangle(t3) else 0
    print("Count:", counter)
