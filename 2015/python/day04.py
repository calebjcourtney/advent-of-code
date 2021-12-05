import hashlib


def part_one(data):
    num = 0
    while True:
        str2hash = data + str(num)
        result = hashlib.md5(str2hash.encode())
        new = result.hexdigest()

        if new.startswith("0" * 4):
            return num

        num += 1


def part_two(data):
    num = 0
    while True:
        str2hash = data + str(num)
        result = hashlib.md5(str2hash.encode())
        new = result.hexdigest()

        if new.startswith("0" * 6):
            return num

        num += 1


if __name__ == '__main__':
    data = "iwrupvqb"

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
