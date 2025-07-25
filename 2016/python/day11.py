from utils import timeit
from utils import get_line_data

import re
from itertools import combinations


def valid(state):
    """Returns whether the current state is valid or not."""
    gens = set(state[::2])
    for i, floor in enumerate(state):
        # Element is a chip if it has an odd index
        if i % 2 == 1:
            # Chip's matching generator is on the same floor
            if state[i - 1] == floor:
                continue

            # There is another generator on the floor
            if floor in gens:
                return False

    return True


def ordered(state):
    """Returns an ordered version of the state (to improve node pruning)."""
    sorted_state = sorted(zip(state[::2], state[1::2]))
    return tuple(item for subl in sorted_state for item in subl)


@timeit
def solve(state, start_floor=0):
    horizon = [(start_floor, state)]
    steps = 0
    seen = set()

    while horizon:
        new_horizon = []

        for floor, state in horizon:
            can_move = [i for i, f in enumerate(state) if f == floor]
            moves = []

            if floor < TOP_FLOOR:
                moves.extend([(2, floor + 1), (1, floor + 1)])

            if floor > 0:
                # Don't move downstairs if the floors below are empty
                if any(f < floor for f in state):
                    moves.extend([(1, floor - 1), (2, floor - 1)])

            moved_two_up = False
            moved_one_down = False

            for n, new_floor in moves:
                # Don't move one item up if you can move two,
                # and don't move two items down if can move one
                if n == 1 and new_floor > floor and moved_two_up:
                    continue
                elif n == 2 and new_floor < floor and moved_one_down:
                    continue

                for move in combinations(can_move, n):
                    next_state = tuple(new_floor if i in move else f for i, f in enumerate(state))

                    # All items are on the top floor, so we're done
                    if all(f == TOP_FLOOR for f in next_state):
                        return steps + 1

                    if valid(next_state) and (new_floor, ordered(next_state)) not in seen:
                        new_horizon.append((new_floor, next_state))
                        seen.add((new_floor, ordered(next_state)))

                        if n == 2 and new_floor > floor:
                            moved_two_up = True
                        if n == 1 and new_floor < floor:
                            moved_one_down = True

        horizon = new_horizon
        steps += 1


TOP_FLOOR = None
generators = {}
microchips = {}

data = get_line_data("11")
print(data)

for i, line in enumerate(data):
    for gen in re.findall(r'(\w+) generator', line):
        generators[gen] = i
    for chip in re.findall(r'(\w+)-compatible microchip', line):
        microchips[chip] = i

    TOP_FLOOR = i


STATE = []

for key in generators:
    STATE.append(generators[key])
    STATE.append(microchips[key])

STATE = tuple(STATE)

print("Minimum number of steps:", solve(STATE))

STATE = tuple(list(STATE) + [0, 0, 0, 0])
print("Including 4 new objects:", solve(STATE))
