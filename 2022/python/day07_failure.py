from utils import get_data, get_line_data, get_int_data

import json


class File(object):
    def __init__(self, name, parent, is_directory: bool, size: int = None):
        super(File, self).__init__()
        self.name = name
        self.parent = parent
        self.is_directory = is_directory

        self.children = []
        self.size = size

    def get_size(self):
        if self.size is not None:
            return self.size

        self.size = sum(child.get_size() for child in self.children)
        return self.size

    def count_size(self):
        if not self.is_directory:
            return 0

        self.get_size()
        if self.size < 100000:
            return 0

        else:
            return 1 + sum([child.count_size() for child in self.children])

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "parent": None if not self.parent else self.parent.name,
            "is_directory": self.is_directory,
            "children": [str(child) for child in self.children],
            "size": self.size
        })

    def __str__(self):
        return self.to_json()


def part_one(data):
    root = File("/", None, True)
    for line in data:
        tokens = line.split()
        # it's a command
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "/":
                    cur_dir = root
                elif tokens[2] == "..":
                    cur_dir = cur_dir.parent
                else:
                    cur_dir = [child for child in cur_dir.children if child.name == tokens[2]][0]

            elif tokens[1] == "ls":
                pass

            else:
                raise ValueError(tokens)

        # it's a file
        elif tokens[0].isnumeric():
            cur_dir.children.append(File(
                name=tokens[1],
                parent=cur_dir,
                is_directory=False,
                size=int(tokens[0])
            ))
            for child in cur_dir.children:
                if not child.is_directory:
                    print(child)

        # it's a directory
        elif tokens[0] == "dir":
            cur_dir.children.append(File(
                name=tokens[1],
                parent=cur_dir,
                is_directory=True
            ))

    return root.get_size()


def part_two(data):
    for line in data:
        pass


if __name__ == '__main__':
    data = get_line_data("07")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
