from utils import get_line_data, timeit, get_nums
from itertools import count, combinations
from typing import NamedTuple
import re
import z3


class Machine(NamedTuple):
    indicator_light_diagram: list[int]
    button_wiring_schematics: list[list[int]]
    joltage_requirements: list[int]

    def min_button_presses(self) -> int:
        num_lights = len(self.indicator_light_diagram)
        target_state = self.indicator_light_diagram

        return next(
            num_presses
            for num_presses in count(0)
            for pressed_buttons in combinations(self.button_wiring_schematics, num_presses)
            if [
                sum(light_idx in button for button in pressed_buttons) % 2
                for light_idx in range(num_lights)
            ] == target_state
        )

    def min_joltage_presses(self) -> int:
        num_buttons = len(self.button_wiring_schematics)

        press_vars = [z3.Int(f"press{i}") for i in range(num_buttons)]
        solver = z3.Optimize()

        solver.add(z3.And([press_var >= 0 for press_var in press_vars]))

        for counter_idx, target_joltage in enumerate(self.joltage_requirements):
            buttons_affecting_counter = [
                press_vars[button_idx]
                for button_idx, button_counters in enumerate(self.button_wiring_schematics)
                if counter_idx in button_counters
            ]
            solver.add(sum(buttons_affecting_counter) == target_joltage)

        solver.minimize(sum(press_vars))
        solver.check()

        model = solver.model()
        return sum(model[press_var].as_long() for press_var in press_vars)


def parse_data(data):
    pattern = re.compile(r'(\[.*\])\s(\([\d,\)\(\s]+\))\s(\{[\d,]+\})')
    machines = []

    for line in data:
        match = pattern.match(line)
        if not match:
            continue

        pattern_str, buttons_str, joltages_str = match.groups()
        indicator_light_diagram = [int(char == "#") for char in pattern_str if char in "#."]
        button_wiring_schematics = [get_nums(button_str) for button_str in buttons_str.split()]
        joltage_requirements = get_nums(joltages_str)

        machines.append(Machine(
            indicator_light_diagram=indicator_light_diagram,
            button_wiring_schematics=button_wiring_schematics,
            joltage_requirements=joltage_requirements
        ))

    return machines


@timeit
def main():
    data = get_line_data("10")
    machines = parse_data(data)

    p1_result = sum(machine.min_button_presses() for machine in machines)
    print(p1_result)

    p2_result = sum(machine.min_joltage_presses() for machine in machines)
    print(p2_result)
