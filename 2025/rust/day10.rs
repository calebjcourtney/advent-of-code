use crate::y2025::utils;
use itertools::Itertools;
use regex::Regex;

struct Machine {
    indicator_light_diagram: Vec<i64>,
    button_wiring_schematics: Vec<Vec<i64>>,
}

impl Machine {
    fn min_button_presses(&self) -> i64 {
        let num_lights = self.indicator_light_diagram.len();
        let target_state = &self.indicator_light_diagram;

        for num_presses in 0..=self.button_wiring_schematics.len() {
            for pressed_buttons in self.button_wiring_schematics.iter().combinations(num_presses) {
                let result_state: Vec<i64> = (0..num_lights)
                    .map(|light_idx| {
                        pressed_buttons
                            .iter()
                            .map(|button| if button.contains(&(light_idx as i64)) { 1 } else { 0 })
                            .sum::<i64>()
                            % 2
                    })
                    .collect();

                if result_state == *target_state {
                    return num_presses as i64;
                }
            }
        }
        0
    }
}

fn parse_data(data: &[String]) -> Vec<Machine> {
    let pattern = Regex::new(r"(\[.*\])\s(\([\d,\)\(\s]+\))\s(\{[\d,]+\})").unwrap();
    let mut machines = Vec::new();

    for line in data {
        if let Some(caps) = pattern.captures(line) {
            let pattern_str = caps.get(1).unwrap().as_str();
            let buttons_str = caps.get(2).unwrap().as_str();

            let indicator_light_diagram: Vec<i64> = pattern_str
                .chars()
                .filter(|&c| c == '#' || c == '.')
                .map(|c| if c == '#' { 1 } else { 0 })
                .collect();

            let button_wiring_schematics: Vec<Vec<i64>> = buttons_str
                .split_whitespace()
                .map(|s| utils::get_nums(s))
                .collect();

            machines.push(Machine {
                indicator_light_diagram,
                button_wiring_schematics,
            });
        }
    }

    machines
}

pub fn main() {
    let data = utils::get_line_data("10");
    let machines = parse_data(&data);

    let p1_result: i64 = machines.iter().map(|m| m.min_button_presses()).sum();
    println!("{}", p1_result);
}
