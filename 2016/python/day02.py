from utils import get_line_data
from utils import parse_grid
from utils import timeit
from utils import N, S, E, W


DIRECTION_MAP = {"U": S, "D": N, "R": E, "L": W}

P1_NUM_PAD = parse_grid(["123", "456", "789"])

P2_NUM_PAD = parse_grid("""  1  
 234 
56789
 ABC 
  D  """,
    keep_values = "123456789ABCD")


@timeit
def main(data):
    p1_out = ""
    p2_out = ""
    p1 = [point for point, value in P1_NUM_PAD.items() if value == "5"][0]
    p2 = [point for point, value in P2_NUM_PAD.items() if value == "5"][0]
    for ins in data:
        for code in ins:
            if p1 + DIRECTION_MAP[code] in P1_NUM_PAD:
                p1 += DIRECTION_MAP[code]
            if p2 + DIRECTION_MAP[code] in P2_NUM_PAD:
                p2 += DIRECTION_MAP[code]

        p1_out += P1_NUM_PAD[p1]
        p2_out += P2_NUM_PAD[p2]

    return p1_out, p2_out


if __name__ == '__main__':
    data = get_line_data("02")

    p1, p2 = main(data)
    print(p1)
    print(p2)
