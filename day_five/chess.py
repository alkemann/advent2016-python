from hashlib import md5


def look_for_hashes(door):
    password = ""
    count = 3231929
    while True:
        hash = md5((door + str(count)).encode('utf-8'))
        count += 1
        string = hash.hexdigest()
        if string[:5] == "00000":
            password += string[5:6]
            if len(password) is 8:
                break
    return password


def look_for_hashes_two(door):
    password = ["#", "#", "#", "#", "#", "#", "#", "#"]
    valid_pos = ["0", "1", "2", "3", "4", "5", "6", "7"]
    count = 3231929
    while True:
        hash = md5((door + str(count)).encode('utf-8'))
        count += 1
        string = hash.hexdigest()
        if string[:5] == "00000":
            pos = string[5:6]
            char = string[6:7]
            if pos not in valid_pos:
                continue
            pos = int(pos)
            if password[pos] == "#":
                password[pos] = char

            if "#" not in password:
                break
    return "".join(password)


if __name__ == '__main__':
    print(look_for_hashes_two("uqwqemis"))
