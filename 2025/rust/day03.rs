use crate::y2025::utils;

fn highest_possible_joltage(line: &str, n: usize) -> u64 {
    let mut digits: Vec<char> = line.chars().take(n).collect();

    for i in n..line.len() {
        digits.push(line.chars().nth(i).unwrap());

        let mut best_number = 0u64;
        let mut best_digits: Option<Vec<char>> = None;

        for j in 0..digits.len() {
            let mut candidate = digits.clone();
            candidate.remove(j);
            let number_str: String = candidate.iter().collect();
            if let Ok(number) = number_str.parse::<u64>() {
                if number > best_number {
                    best_number = number;
                    best_digits = Some(candidate);
                }
            }
        }

        if let Some(best) = best_digits {
            digits = best;
        }
    }

    let result_str: String = digits.iter().collect();
    result_str.parse::<u64>().unwrap_or(0)
}

pub fn main() {
    let data = utils::get_line_data("03");

    let p1: u64 = data.iter().map(|line| highest_possible_joltage(line, 2)).sum();
    let p2: u64 = data.iter().map(|line| highest_possible_joltage(line, 12)).sum();

    println!("{}", p1);
    println!("{}", p2);
}
