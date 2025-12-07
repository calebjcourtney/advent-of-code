use crate::y2025::utils;

struct Problem {
    numbers: Vec<i64>,
    operator: String,
}

impl Problem {
    fn solve(&self) -> i64 {
        match self.operator.as_str() {
            "+" => self.numbers.iter().sum(),
            "*" => utils::mult(&self.numbers),
            _ => 0,
        }
    }
}

fn part_one(data: &[String]) -> i64 {
    let mut nums_data: Vec<Vec<i64>> = Vec::new();
    let mut operators: Vec<String> = Vec::new();

    for line in data {
        let nums = utils::get_nums(line);
        if !nums.is_empty() {
            nums_data.push(nums);
        } else {
            operators = line.split_whitespace().map(|s| s.to_string()).collect();
        }
    }

    let rotated_data = utils::rotated(&nums_data);
    let problems: Vec<Problem> = rotated_data
        .iter()
        .zip(operators.iter())
        .map(|(numbers, operator)| Problem {
            numbers: numbers.clone(),
            operator: operator.clone(),
        })
        .collect();

    problems.iter().map(|p| p.solve()).sum()
}

fn part_two(data: &[String]) -> i64 {
    let mut operators: Vec<String> = data
        .last()
        .unwrap()
        .split_whitespace()
        .map(|s| s.to_string())
        .rev()
        .collect();

    let num_rows: Vec<Vec<char>> = data[..data.len() - 1]
        .iter()
        .map(|line| line.chars().collect())
        .collect();

    let mut rotated_data = utils::rotated(&num_rows);
    rotated_data = utils::rotated(&rotated_data);
    rotated_data = utils::rotated(&rotated_data);

    let mut problems = Vec::new();
    let mut current_operator = operators.remove(0);
    let mut group_idx = 0;

    loop {
        let mut group_numbers = Vec::new();

        while group_idx < rotated_data.len() {
            if rotated_data[group_idx].iter().all(|&c| c.is_whitespace()) {
                group_idx += 1;
                break;
            } else {
                let num_str: String = rotated_data[group_idx]
                    .iter()
                    .filter(|&&c| c.is_ascii_digit())
                    .collect();
                if let Ok(num) = num_str.parse::<i64>() {
                    group_numbers.push(num);
                }
                group_idx += 1;
            }
        }

        problems.push(Problem {
            numbers: group_numbers,
            operator: current_operator.clone(),
        });

        if operators.is_empty() {
            break;
        }
        current_operator = operators.remove(0);
    }

    problems.iter().map(|p| p.solve()).sum()
}

pub fn main() {
    let data = utils::get_line_data("06");

    let p1_result = part_one(&data);
    println!("{}", p1_result);

    let p2_result = part_two(&data);
    println!("{}", p2_result);
}
