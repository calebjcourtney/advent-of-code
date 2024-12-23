from utils import Point, get_line_data

NUM_COORDS = {
    c: Point(x, y)
    for y, row in enumerate(["789", "456", "123", " 0A"])
    for x, c in enumerate(row)
}


def calc_fewest(code, robot_keyboards):
    KEY_COORDS = {
        c: Point(x, y)
        for y, row in enumerate([" ^A", "<v>"])
        for x, c in enumerate(row)
    }
    leg_lengths = {(0, k1, k2): 1 for k1 in KEY_COORDS for k2 in KEY_COORDS}

    def fewest_presses(l, key_string):
        return sum(
            leg_lengths[(l, k1, k2)] for k1, k2 in zip("A" + key_string, key_string)
        )

    for layer in range(1, robot_keyboards + 1):
        if layer == robot_keyboards:
            KEY_COORDS = NUM_COORDS

        for key_i, point_i in KEY_COORDS.items():
            for key_j, point_j in KEY_COORDS.items():
                hor_ks = (">" if point_j.x > point_i.x else "<") * abs(
                    point_j.x - point_i.x
                )
                ver_ks = ("^" if point_j.y < point_i.y else "v") * abs(
                    point_j.y - point_i.y
                )
                fewest_hor_first = (
                    fewest_presses(layer - 1, hor_ks + ver_ks + "A")
                    if (point_j.x, point_i.y) != KEY_COORDS[" "]
                    else float("inf")
                )
                fewest_ver_first = (
                    fewest_presses(layer - 1, ver_ks + hor_ks + "A")
                    if (point_i.x, point_j.y) != KEY_COORDS[" "]
                    else float("inf")
                )
                leg_lengths[(layer, key_i, key_j)] = min(
                    fewest_hor_first, fewest_ver_first
                )

    return fewest_presses(layer, code)


if __name__ == "__main__":
    data = get_line_data("21")
    print(sum(calc_fewest(code, 3) * int(code[:-1]) for code in data))
    print(sum(calc_fewest(code, 26) * int(code[:-1]) for code in data))
