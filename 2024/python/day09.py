from collections import defaultdict
from collections import deque

from utils import get_data
from utils import timeit


class FileBlock:
    def __init__(self, id: int, files: int, free: int = 0):
        self.id = id
        self.files = files
        self.free = free

    def __eq__(self, other):
        return self.id == other.id


def parse_data(data) -> list[FileBlock]:
    output = []
    for index, (files, free) in enumerate(zip(data[0::2], data[1::2])):
        output.append(FileBlock(index, int(files), int(free)))

    if len(data) % 2 == 1:
        output.append(FileBlock(len(data) // 2, int(data[-1])))

    return output


@timeit
def part_one(data):
    output = 0
    index = 0
    data = deque(data)
    while data:
        record = data.popleft()

        while record.files:
            output += record.id * index
            index += 1
            record.files -= 1

        if record.free and data:
            last_record = data.pop()
        else:
            last_record = None

        while record.free and last_record is not None:
            assert last_record.files > 0
            output += last_record.id * index
            index += 1
            record.free -= 1
            last_record.files -= 1

            if last_record.files == 0 and data:
                last_record = data.pop()
            elif last_record.files == 0 and not data:
                last_record = None

        if last_record is not None and last_record.files:
            data.append(last_record)

    return output


@timeit
def part_two(data):
    empty_spots = defaultdict(list)
    free_indices = defaultdict(list)
    original_index = {}
    index = 0
    for record in data:
        original_index[record.id] = index
        index += record.files
        for _ in range(record.free):
            free_indices[record.id].append(index)
            index += 1

        empty_spots[record.free].append(record.id)

    del empty_spots[0]

    moved_index = {}

    for fb in data[::-1]:
        min_id = min([
            empty_spots[size][0]
            for size in range(1, 10)
            if size in empty_spots and size >= fb.files
        ])

        if min_id >= fb.id:
            continue

        parent = data[min_id]
        new_index = free_indices[parent.id][0]
        moved_index[fb.id] = new_index
        for i in range(fb.files):
            free_indices[parent.id].pop(0)

        empty_spots[parent.free].pop(0)
        parent.free -= fb.files
        assert parent.free >= 0
        if parent.free > 0:
            empty_spots[parent.free].append(parent.id)
            empty_spots[parent.free].sort()

    output = 0

    original_index.update(moved_index)
    for fb in data:
        index = original_index[fb.id]
        for _ in range(fb.files):
            output += fb.id * index
            index += 1

    return output


if __name__ == '__main__':
    data = get_data("09")
    data = parse_data(data)

    p1_result = part_one(data)
    print(p1_result)

    data = get_data("09")
    data = parse_data(data)

    p2_result = part_two(data)
    print(p2_result)
