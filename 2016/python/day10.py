import re
from typing import Any
from collections import defaultdict
from collections import deque

from utils import get_line_data
from utils import get_nums
from utils import timeit


GIVE_PATTERN = re.compile(r"bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)")


@timeit
def main(data):
    outputs = defaultdict(list)
    bots = {}
    for line in data:
        match = GIVE_PATTERN.search(line)
        if match:
            give_bot = int(match.group(1))
            type_low = match.group(2)
            index_low = int(match.group(3))
            type_high = match.group(4)
            index_high = int(match.group(5))

            if give_bot not in bots:
                bots[int(give_bot)] = {
                    "low": {
                        "type": type_low,
                        "index": index_low,
                    },
                    "high": {
                        "type": type_high,
                        "index": index_high,
                    },
                    "values": []
                }

            else:
                bots[give_bot]["low"] = {"type": type_low, "index": index_low}
                bots[give_bot]["high"] = {"type": type_high, "index": index_high}

        else:
            val, bot_id = get_nums(line)
            if bot_id not in bots:
                bots[bot_id] = {"values": [val]}
            else:
                bots[bot_id]["values"].append(val)
                assert len(bots[bot_id]["values"]) <= 2

    queue = deque([key for key, value in bots.items() if len(value["values"]) == 2])
    while queue:
        bot_id = queue.popleft()

        values = bots[bot_id]["values"]
        if set(values) == {61, 17}:
            p1 = bot_id

        type_low = bots[bot_id]["low"]["type"]
        index_low = bots[bot_id]["low"]["index"]

        if index_low in queue:
            queue.append(bot_id)
            continue

        type_high = bots[bot_id]["high"]["type"]
        index_high = bots[bot_id]["high"]["index"]

        if index_high in queue:
            queue.append(bot_id)
            continue

        if type_low == "bot" and (bots[index_low]["values"]) == 2:
            queue.append(bot_id)
            continue

        elif type_high == "bot" and (bots[index_high]["values"]) == 2:
            queue.append(bot_id)
            continue

        if type_low == "output":
            outputs[index_low].append(min(bots[bot_id]["values"]))

        elif type_low == "bot":
            bots[index_low]["values"].append(min(values))
            if len(bots[index_low]["values"]) == 2:
                queue.append(index_low)

        if type_high == "output":
            outputs[index_high].append(max(bots[bot_id]["values"]))

        elif type_high == "bot":
            bots[index_high]["values"].append(max(values))
            if len(bots[index_high]["values"]) == 2:
                queue.append(index_high)

        bots[bot_id]["values"] = []

    return p1, outputs[0][0] * outputs[1][0] * outputs[2][0]


if __name__ == '__main__':
    data = get_line_data("10")

    p1, p2 = main(data)
    print(p1)
    print(p2)
