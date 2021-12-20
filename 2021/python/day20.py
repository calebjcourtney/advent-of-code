from utils import get_data


def get(image, border, x, y):
    if 0 <= x < len(image[0]) and 0 <= y < len(image):
        return image[y][x]
    else:
        return border


def enhance(image, border):
    results = []

    for y in range(-1, len(image) + 1):
        row = []

        for x in range(-1, len(image[0]) + 1):
            i = ""

            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if get(image, border, x + dx, y + dy):
                        i += "1"
                    else:
                        i += "0"

            i = int(i, 2)

            row.append(enhancement_algo[i])

        results.append(row)

    newborder = enhancement_algo[511] if border else enhancement_algo[0]

    return results, newborder


if __name__ == '__main__':
    data = get_data("20")

    enhancement_algo, image = data.split("\n\n")

    enhancement_algo = [c == '#' for c in enhancement_algo]
    image = [[c == '#' for c in i] for i in image.split("\n")]

    image, border = enhance(image, False)
    image, border = enhance(image, border)

    print(f"part one: {len([1 for row in image for cell in row if cell])}")

    # pick up from part 2
    for i in range(48):
        image, border = enhance(image, border)

    print(f"part two: {len([1 for row in image for cell in row if cell])}")
