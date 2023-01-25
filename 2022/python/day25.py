from utils import get_line_data


MAPPING = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}


def decimalize(val: str):
    return sum(
        (5 ** i) * MAPPING[char]
        for i, char in enumerate(val[::-1])
    )


def snafuize(val: int) -> str:
    output = []
    while val != 0:
        remainder = val % 5
        val = val // 5
        if remainder == 4:
            remainder = -1
            val += 1
        elif remainder == 3:
            remainder = -2
            val += 1
        output.append(remainder)

    output = [str(x) for x in output]
    output = [x.replace("-1", "-").replace("-2", "=") for x in output]
    output = "".join(output[::-1])

    return output


if __name__ == '__main__':
    data = get_line_data("25")
    print(snafuize(sum(map(decimalize, data))))
