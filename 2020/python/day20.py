from utils import get_data

from numpy import prod


def encode(edge):
    edge_bin = ["1" if c == "#" else "0" for c in edge]
    a, b = int(''.join(edge_bin), 2), int(''.join(reversed(edge_bin)), 2)
    return tuple(sorted([a, b]))


class Tile:
    def __init__(self, name, lines):
        self.name = int(name.split()[1][:-1])
        self.lines = lines

    def left(self):
        return "".join([line[0] for line in self.lines])

    def left_encode(self):
        return encode(self.left())

    def right(self):
        return "".join([line[-1] for line in self.lines])

    def right_encode(self):
        return encode(self.right())

    def top(self):
        return self.lines[0]

    def top_encode(self):
        return encode(self.top())

    def bottom(self):
        return self.lines[-1]

    def bottom_encode(self):
        return encode(self.bottom())

    def edges_encode(self):
        return (self.top_encode(), self.right_encode(), self.bottom_encode(), self.left_encode())

    def image_lines(self):
        return [line[1:-1] for line in self.lines[1:-1]]

    def rotate_clockwise(self):
        self.lines = [''.join(line) for line in list(zip(*self.lines[::-1]))]

    def mirror_vertical(self):
        self.lines = self.lines[::-1]

    def mirror_horizontal(self):
        self.lines = [line[::-1] for line in self.lines]

    def orient(self, edges, neighbors):
        # match orientation of borders
        if any(isinstance(n, Tile) for n in neighbors):
            count = 0

            if isinstance(neighbors[0], Tile):
                # top neighbor
                neighbor = neighbors[0]

                while self.top_encode() != neighbor.bottom_encode():
                    self.rotate_clockwise()
                    count += 1

                    if count > 3:
                        raise Exception

                if self.top() != neighbor.bottom():
                    self.mirror_horizontal()

            if isinstance(neighbors[1], Tile):
                # left neighbor
                neighbor = neighbors[1]

                while self.right_encode() != neighbor.left_encode():
                    self.rotate_clockwise()
                    count += 1

                    if count > 3:
                        raise Exception

                if self.right() != neighbor.left():
                    self.mirror_vertical()

            if isinstance(neighbors[2], Tile):
                # left neighbor
                neighbor = neighbors[2]

                while self.bottom_encode() != neighbor.top_encode():
                    self.rotate_clockwise()
                    count += 1

                    if count > 3:
                        raise Exception

                if self.bottom() != neighbor.top():
                    self.mirror_horizontal()

            if isinstance(neighbors[3], Tile):
                # right neighbor
                neighbor = neighbors[3]

                while self.left_encode() != neighbor.right_encode():
                    self.rotate_clockwise()
                    count += 1
                    if count > 3:
                        raise Exception

                if self.left() != neighbor.right():
                    self.mirror_vertical()

        elif 0 in neighbors:
            target = tuple((1 if e == 0 else 2 for e in neighbors))
            while tuple(edges[edge] for edge in self.edges_encode()) != target:
                self.rotate_clockwise()

        if neighbors[0] is not None:
            if neighbors[0] == 0:
                assert edges[self.top_encode()] == 1
            else:
                assert self.top() == neighbors[0].bottom()

        if neighbors[3] is not None:
            if neighbors[3] == 0:
                assert edges[self.left_encode()] == 1
            else:
                assert self.left() == neighbors[3].right()

    def __repr__(self):
        return "Tile: " + str(self.name)


def find_edges(tiles):
    edges = dict()
    for tile in tiles:
        for edge in tile.edges_encode():

            if edge in edges:
                edges[edge] += 1

            else:
                edges[edge] = 1

    return edges


# each corner only has two edges
def find_corners(tiles, edges):
    corners = []
    for tile in tiles:
        borders = 0

        for edge in tile.edges_encode():
            if edges[edge] == 1:
                borders += 1

        if borders == 2:
            corners.append(tile)

    return corners


def part_one(tiles, edges):
    result = 1

    for tile in find_corners(tiles, edges):
        result *= tile.name

    return result


# run part one
if __name__ == '__main__':
    data = get_data("20")
    data = data.split("\n\n")

    tiles = [Tile(record.split("\n")[0], record.split("\n")[1:]) for record in data]
    edges = find_edges(tiles)

    print(part_one(tiles, edges))


def find_monsters(image):
    # hopefully no overlapping monsters :-/
    monsters = 0
    for y in range(len(image) - monster_max_y):
        for x in range(len(image[y]) - monster_max_x):
            if all(image[y + dy][x + dx] == "#" for dx, dy in monster):
                monsters += 1

    if monsters > 0:
        roughness = sum(line.count("#") for line in image)

        return roughness - monsters * len(monster)

    return None


def part_two(tiles, edges):
    puzzle_edge = int(len(tiles) ** 0.5)
    puzzle = [[None] * puzzle_edge for _ in range(puzzle_edge)]

    # fill in the puzzle
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            top = puzzle[y - 1][x] if y > 0 else 0
            right = puzzle[y][x + 1] if x < len(puzzle[y]) - 1 else 0
            bottom = puzzle[y + 1][x] if y < len(puzzle) - 1 else 0
            left = puzzle[y][x - 1] if x > 0 else 0

            # place a corner in top-left
            if x == y == 0:
                match = find_corners(tiles, edges)[0]
                match.mirror_horizontal()

            # find piece matching neighbor left
            elif 0 < x < len(puzzle[y]):
                match = [tile for tile in tiles if tile != left and left.right_encode() in tile.edges_encode()][0]

            # find piece matching neighbor top
            elif 0 < y < len(puzzle):
                match = [tile for tile in tiles if tile != top and top.bottom_encode() in tile.edges_encode()][0]

            else:
                print("why?", x, y)

            # place it
            puzzle[y][x] = match

            # orient it
            match.orient(edges, (top, right, bottom, left))

    piece_lines = len(puzzle[0][0].image_lines())
    image_size = puzzle_edge * piece_lines

    image = [''] * image_size

    for line in range(image_size):
        y = line // piece_lines
        for x in range(len(puzzle[0])):
            piece = puzzle[y][x]
            image[line] += piece.image_lines()[line % piece_lines]

    # rotate
    for _ in range(4):
        # print("check")
        result = find_monsters(image)
        if result:
            return result
        # print("check_rev")
        image = [line[::-1] for line in image]
        result = find_monsters(image)
        if result:
            return result
        image = [line[::-1] for line in image]
        image = [''.join(line) for line in list(zip(*image[::-1]))]


# run part two
if __name__ == '__main__':
    data = get_data("20")
    data = data.split("\n\n")

    tiles = [Tile(record.split("\n")[0], record.split("\n")[1:]) for record in data]
    edges = find_edges(tiles)

    monster_img = """\
                  #
#    ##    ##    ###
 #  #  #  #  #  #
""".splitlines()

    monster = list()

    for y, line in enumerate(monster_img):
        for x, c in enumerate(line):
            if c == "#":
                monster.append((x, y))

    monster_max_y = max(y for x, y in monster)
    monster_max_x = max(x for x, y in monster)

    print(part_two(tiles, edges))
